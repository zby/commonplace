---
source: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf
description: Framework unifying Make, Excel, Shake, Bazel, Buck, and Nix as scheduler+rebuilder combinations, formalizing minimality, dynamic dependencies, and early cutoff.
captured: 2026-07-06
capture: pdf-read
genre: scientific-paper
type: ./types/snapshot.md
---

# Build Systems à la Carte

Author: Andrey Mokhov (Newcastle University), Neil Mitchell (Digital Asset), Simon Peyton Jones (Microsoft Research)
Source: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf
Date: September 2018 (Proc. ACM Program. Lang., Vol. 2, No. ICFP, Article 79)

## Abstract

Build systems are awesome, terrifying – and unloved. They are used by every developer around the world, but are rarely the object of study. In this paper we offer a systematic, and executable, framework for developing and comparing build systems, viewing them as related points in landscape rather than isolated phenomena. By teasing apart existing build systems, we can recombine their components, allowing us to prototype new build systems with desired properties.

**CCS Concepts:** Software and its engineering; Mathematics of computing

**Additional Key Words and Phrases:** build systems, functional programming, algorithms

## 1 Introduction

Build systems (such as Make) are big, complicated, and used by every software developer on the planet. But they are a sadly unloved part of the software ecosystem, very much a means to an end, and seldom the focus of attention. For years Make dominated, but more recently the challenges of scale have driven large software firms like Microsoft, Facebook and Google to develop their own build systems, exploring new points in the design space. These complex build systems use subtle algorithms, but they are often hidden away, and not object of study.

In this paper we offer a general framework in which to understand and compare build systems, in a way that is both abstract (omitting incidental detail) and yet precise (implemented as Haskell code). Specifically, we make these contributions:

- Build systems vary on many axes, including: static vs dynamic dependencies; local vs cloud; deterministic vs non-deterministic build tasks; support for early cutoff; self-tracking build systems; and the type of persistent build information. In §2 we identify some key properties, illustrated by four carefully-chosen build systems.
- We describe some simple but novel abstractions that crisply encapsulate what a build system is (§3), allowing us, for example, to speak about what it means for a build system to be correct.
- We identify two key design choices that are typically deeply wired into any build system: *the order in which tasks are built* (§4.1) and *whether or not a task is (re-)built* (§4.2). These choices turn out to be orthogonal, which leads us to a new classification of the design space (§4.4).
- We show that we can instantiate our abstractions to describe the essence of a variety of different real-life build systems, including Make, Shake, Bazel, CloudBuild, Buck, and Nix, each by the composition of the two design choices (§5). Doing this modelling in a single setting allows the differences and similarities between these huge systems to be brought out clearly.
- Moreover, we can readily remix the ingredients to design new build systems with desired properties, for example, to combine the advantages of Shake and Bazel (§5.4).

In short, instead of seeing build systems as unrelated points in space, we now see them as locations in a connected landscape, leading to a better understanding of what they do and how they compare, and suggesting exploration of other (as yet unoccupied) points in the landscape. We discuss engineering aspects in §6 and related work in §7.

## 2 Background

### 2.1 The Venerable Make: Static Dependencies and File Modification Times

Make was developed more than 40 years ago to automatically build software libraries and executable programs from source code. It uses makefiles to describe tasks (often referred to as build rules) and their dependencies in a simple textual form. Example:

```
util.o: util.h util.c
    gcc -c util.c

main.o: util.h main.c
    gcc -c main.c

main.exe: util.o main.o
    gcc util.o main.o -o main.exe
```

The above makefile lists three tasks: (i) compile a utility library comprising files `util.h` and `util.c` into `util.o` by executing the command `gcc -c util.c`, (ii) compile the main source file `main.c` into `main.o`, and (iii) link object files `util.o` and `main.o` into the executable `main.exe`. The makefile contains the complete information about the *task dependency graph*.

If the user runs Make specifying `main.exe` as the desired output, Make will build `util.o` and `main.o` (in any order since these tasks are independent) and then `main.exe`. If the user modifies `util.h` and runs Make again, it will perform a *full rebuild*, because all three tasks transitively depend on `util.h`. On the other hand, if the user modifies `main.c` then a *partial rebuild* is sufficient, since `util.o` does not need to be rebuilt, as its inputs have not changed. Note that if the dependency graph is *acyclic* then each task needs to be executed at most once. Cyclic task dependencies are typically not allowed in build systems but there are rare exceptions, see §6.6.

**Definition 2.1 (Minimality).** A build system is *minimal* if it executes tasks at most once per build and only if they transitively depend on inputs that changed since the previous build.

To achieve minimality Make relies on two main ideas: (i) it uses *file modification times* to detect which files changed, and (ii) it constructs a task dependency graph from the information contained in the makefile and executes tasks in a *topological order*.

### 2.2 Excel: Dynamic Dependencies at the Cost of Minimality

Excel is a build system in disguise. Consider the following simple spreadsheet:

```
A1: 10   B1: A1 + A2
A2: 20
```

There are two input cells A1 and A2, and a single task that computes the sum of their values, producing the result in cell B1. If either of the inputs change, Excel will recompute the result.

Unlike Make, Excel does not need to know all task dependencies upfront. Indeed, some dependencies may change *dynamically* according to computation results. For example:

```
A1: 10   B1: INDIRECT("A" & C1)   C1: 1
A2: 20
```

The formula in B1 uses the `INDIRECT` function, which takes a string and returns the value of the cell with that name. The string evaluates to `"A1"`, so B1 evaluates to 10. However, the dependencies of the formula in B1 are determined by the value of C1, so it is impossible to compute the dependency graph before the build starts.

To support dynamic dependencies, Excel's calc engine is significantly different from Make. Excel arranges the cells into a linear sequence, called the *calc chain*. During the build, Excel processes cells in the calc-chain sequence, but if computing a cell C requires the value of a cell D that has not yet been computed, Excel *aborts* computation of C, moves D before C in the calc chain, and resumes the build starting with D. When a build is complete, the resulting calc chain respects all the dynamic dependencies of the spreadsheet. When an input value (or formula) is changed, Excel uses the final calc chain from the *previous* build as its starting point so that, in the common case where changing an input value does not change dependencies, there are no aborts. Notice that build always succeeds regardless of the initial calc chain (barring truly circular dependencies); the calc chain is just an optimisation.

Dynamic dependencies complicate minimality. In the above example, B1 should only be recomputed if A1 or C1 changes; but not if (say) A2 changes; but these facts are not statically apparent. In practice Excel implements a conservative approximation to minimality: it recomputes a formula if (i) the formula statically mentions a changed cell, or (ii) the formula uses a function like `INDIRECT` whose dependencies are not statically visible, or (iii) the formula itself has changed.

Item (iii) in the above list highlights another distinguishing feature of Excel: it is *self-tracking*. Most build systems only track changes of inputs and intermediate results, but Excel also tracks changes in the tasks themselves — if a formula is modified, Excel will recompute it and propagate the changes. Self-tracking is uncommon in software build systems, where one often needs to manually initiate a full rebuild even if just a single task has changed. We discuss self-tracking further in §6.5.

### 2.3 Shake: Dynamic Dependencies with No Remorse

Shake was developed to solve the issue of dynamic dependencies without sacrificing the minimality requirement. Building on the Make example, add the following files whose dependencies are shown in a figure:

- `LICENSE` is an input text file containing the project license.
- `release.txt` is a text file listing all files that should be in the release. This file is produced by concatenating input files `bins.txt` and `docs.txt`, which list all binary and documentation files of the project.
- `release.tar` is the release archive built by executing the command `tar` on the release files.

The dependencies of `release.tar` are not known statically: they are determined by the content of `release.txt`, which might not even exist before the build. Makefiles cannot express such dependencies, requiring problematic workarounds such as *build phases*. In Shake we can express the rule for `release.tar` as:

```haskell
"release.tar" %> \_ -> do
    need ["release.txt"]
    files <- lines <$> readFile "release.txt"
    need files
    system "tar" ["-cf", "release.tar"] ++ files
```

We first declare the static dependency on `release.txt`, then read its content (a list of files) and depend on each listed file, dynamically. Finally, we specify the command to produce the resulting archive. Crucially, the archive will only be rebuilt if one of the dependencies (static or dynamic) has changed. For example, if we create another documentation file `README` and add it to `docs.txt`, Shake will appropriately rebuild `release.txt` and `release.tar`, discovering the new dependency.

Shake's implementation is different from both Make and Excel in two aspects. First, it uses the dependency graph from the previous build to decide which files need to be rebuilt. This idea has a long history, going back to *incremental*, *adaptive*, and *self-adjusting computations*. Second, instead of aborting or deferring the execution of tasks whose newly discovered dependencies have not yet been built (as Excel does), Shake *suspends* their execution until the dependencies are brought up to date. We refer to this task scheduling algorithm as *suspending*.

Shake also supports the *early cutoff* optimisation. When it executes a task and the result is unchanged from the previous build, it is unnecessary to execute the dependent tasks, and hence Shake can stop a build earlier. Not all build systems support early cutoff: Make and Excel do not, whereas Shake and Bazel (introduced below) do.

### 2.4 Bazel: A Cloud Build System

When build systems are used by large teams, different team members often end up executing exactly the same tasks on their local machines. A *cloud build system* can speed up builds dramatically by sharing build results among team members. Furthermore, cloud build systems can support *shallow builds* that materialise only end build products locally, leaving all intermediates in the cloud.

Consider an example: the user starts by downloading the sources, whose hashes are (for simplicity) 1, 2 and 3, and requests to build `main.exe`. By looking up the global history of all previous builds, the build system finds that someone has already compiled these exact sources before and the resulting files `util.o` and `main.o` had hashes 4 and 5, respectively. Similarly, the build system finds that the hash of the resulting `main.exe` was 6 and downloads the actual binary from the cloud storage — it must be the end build product.

If the user modifies the source file `util.c`, thereby changing its hash from 1 to 7, the cloud lookup of the new combination `{util.c, util.h}` fails, which means that nobody has ever compiled it. The build system must therefore build `util.o`, materialising it with the new hash 8. Since the combination of hashes of `util.o` and `main.o` has not been encountered before either, the build system first downloads `main.o` from the cloud and then builds `main.exe` by linking the two object files. When the build is complete, the results can be uploaded to the cloud for future reuse by other team members.

Bazel is one of the first openly-available cloud build systems. As of writing, it is not possible to express dynamic dependencies in user-defined build rules; however some of the pre-defined build rules require dynamic dependencies and the internal build engine can cope with them by using a *restarting* task scheduler, which is similar to that of Excel but does not use the calc chain. Bazel is not minimal in the sense that it may restart a task multiple times as new dependencies are discovered and rebuilt, but it supports the early cutoff optimisation.

To support cloud builds, Bazel maintains (i) a *content-addressable cache* that can be used to download a previously built file given the hash of its content, and (ii) the history of all executed build commands annotated with observed file hashes. The latter allows the build engine to bypass the execution of a task, by predicting the hash of the result from the hashes of its dependencies, and subsequently downloading the result from the cache.

### 2.5 Summary

Table 1 summarises differences between four discussed build systems: Make, Excel, Shake, Bazel — differing in persistent build information, scheduler, dependencies, minimality, cutoff, and cloud support:

| Build system | Persistent build information | Scheduler | Dependencies | Minimal | Cutoff | Cloud |
|---|---|---|---|---|---|---|
| Make | File modification times | Topological | Static | Yes | No | No |
| Excel | Dirty cells, calc chain | Restarting | Dynamic | No | No | No |
| Shake | Previous dependency graph | Suspending | Dynamic | Yes | Yes | No |
| Bazel | Cloud cache, command history | Restarting | Dynamic(*) | No | Yes | Yes |

(*) At present, user-defined build rules cannot have dynamic dependencies.

- Make stores file modification times, or rather, it relies on the file system to do that.
- Excel stores one dirty bit per cell and the calc chain from the previous build.
- Shake stores the dependency graph discovered in the previous build, annotated with file content hashes for efficient checking of file changes.
- Bazel stores the content-addressable cache and the history of all previous build commands annotated with file hashes. This information is shared among all users of the build system.

In this paper the authors elucidate which build system properties are consequences of specific implementation choices (stored metadata and task scheduling algorithm), and how one can obtain new build systems with desired properties by recombining parts of existing implementations. As a compelling example, in §5.4 they demonstrate how to combine the advantages of Shake and Bazel.

## 3 Build Systems, Abstractly

The paper's purely functional abstractions express all the intricacies of build systems in §2, and are used to design complex build systems from simple primitives: the `Task` and `Build` abstractions (§3.2, §3.3 respectively). Sections 4 and 5 scrutinise the abstractions further and provide concrete implementations for several build systems.

### 3.1 Common Vocabulary for Build Systems

*Keys, values, and the store.* The goal of any build system is to bring up to date a *store* that implements a mapping from *keys* to *values*. In software build systems the store is the file system, the keys are filenames, and the values are file contents. In Excel, the store is the worksheets, the keys are cell names (such as `A1`), and the values are numbers, strings, etc., displayed as the cell contents. Many build systems use *hashes* of values as compact summaries with a fast equality check.

*Input, output, and intermediate values.* Some values must be provided by the user as input. For example, `main.c` can be edited by the user who relies on the build system to compile it into `main.o` and subsequently `main.exe`. End build products, such as `main.exe`, are *output* values. All other values (in this case `main.o`) are *intermediate*; they are not interesting for the user but are produced in the process of turning inputs into outputs.

*Persistent build information.* As well as the key/value mapping, the store also contains information maintained by the build system itself, from one invocation of the build system to the next – its "memory".

*Task description.* Any build system requires the user to specify how to compute the new value for one key, using the (up to date) values of its dependencies. We call this specification the *task description*. For example, in Excel, the formulae of the spreadsheet constitute the task description; in Make the rules in the makefile are the task description.

*Build system.* A build system takes a task description, a target key, and a store, and returns a new store in which the target key and all its dependencies have an up to date value.

### 3.2 The Task Abstraction

```haskell
newtype Task c k v = Task { run :: forall f. c f => (k -> f v) -> f v }
type    Tasks c k v = k -> Maybe (Task c k v)
```

Here `c` stands for constraint, such as `Applicative` (§3.4). A `Task` describes a single build task, while `Tasks` associates a `Task` to every non-input key; input keys are associated with `Nothing`. The highly-abstracted type `Task` describes how to build a value when given a way to build its dependencies, and is best explained by an example. Consider this Excel spreadsheet:

```
A1: 10   B1: A1 + A2
A2: 20   B2: B1 * 2
```

Here cell A1 contains the value 10, cell B1 contains the formula A1 + A2, etc. This can be represented with the following task description:

```haskell
sprsh1 :: Tasks Applicative String Integer
sprsh1 "B1" = Just $ Task $ \fetch -> ((+) <$> fetch "A1" <*> fetch "A2")
sprsh1 "B2" = Just $ Task $ \fetch -> ((*2) <$> fetch "B1")
sprsh1 _    = Nothing
```

We instantiate keys `k` with `String`, and values `v` with `Integer`. The task description `sprsh1` embodies all the *formulae* of the spreadsheet, but not the input values. It pattern-matches on the key to see if it has a task description (in the Excel case, a formula) for it. If not, it returns `Nothing`, indicating that the key is an input. If there is a formula in the cell, it returns the `Task` to compute the value of the formula. Every `Task` is given a callback `fetch` to find the value of any keys on which it depends.

### 3.3 The Build Abstraction

```haskell
type Build c i k v = Tasks c k v -> k -> Store i k v -> Store i k v
```

The signature is straightforward. Given a task description, a target key, and a store, the build system returns a new store in which the value of the target key is up to date. Here is a simple build system, `busy`, that terminates with a correct result but is not a *minimal* build system (Definition 2.1) — since it has no memory, it cannot keep track of keys it has already built and will busily recompute the same keys again and again if they have multiple dependents. Much more efficient build systems are developed in §5.

### 3.6 Correctness of a Build System

The paper formalises correctness: when the build system completes, the target key, and all its dependencies, should be up to date, meaning that if we recompute the value of a key in a given store (using the task description and the final store), we should get exactly the same value as in the final store. A build system is *correct* if it produces a correct result for any given tasks, key, and store — this is stated precisely via `getValue k result == getValue k store` for input keys, and `getValue k result == compute task result` for non-input keys.

## 4 Build Systems à la Carte

The scheduler (which decides which tasks to execute and in what order) can be cleanly separated from the rebuilder (which decides whether a key needs to be rebuilt). §4.1 explores three task schedulers — *topological*, *restarting*, *suspending* — and §4.2 explores four rebuilding strategies — *dirty bit*, *verifying traces*, *constructive traces*, *deep constructive traces*.

### Table 2: Build systems à la carte

|  | Topological | Restarting | Suspending |
|---|---|---|---|
| Dirty bit | Make | Excel | – |
| Verifying traces | Ninja | – | Shake |
| Constructive traces | CloudBuild | Bazel | – |
| Deep constructive traces | Buck | – | Nix |

With this classification, the paper tabulates 12 possible build systems (scheduler × rebuilder), 8 of which are inhabited by existing build systems. Of the remaining 4 spots, all result in workable build systems. The most interesting unfilled spot is *suspending constructive traces*, which would provide many benefits, and which the authors title Cloud Shake and explore further in §5.4.

## 5 Build Systems, Concretely

The paper makes the abstract distinction concrete by implementing a number of build systems as a composition of a scheduler and a rebuilder:

```haskell
type Scheduler c i ir k v = Rebuilder c ir k v -> Build c i k v
type Rebuilder c   ir k v = k -> v -> Task c k v -> Task (MonadState ir) k v
```

A `Scheduler` is a function that takes a `Rebuilder` and uses it to construct a `Build` system, by choosing which keys to rebuild in which order. A `Rebuilder` takes three arguments: a key, its current value, and a `Task` that can (re)compute the value of the key if necessary. It uses the persistent build information `ir` to decide whether rebuilding is unnecessary. If doing so is unnecessary, it returns the current value; otherwise it runs the supplied `Task` to rebuild it.

These two abstractions are the key to modularity: *we can combine any scheduler with any rebuilder, and obtain a correct build system.* §5.1–5.4 write a scheduler for each column of Table 2, and a rebuilder for each row, then combine them to obtain the build systems in the table's body — Make (§5.1), Excel (§5.2), Shake (§5.3), and Bazel/CloudBuild/CloudShake/Buck/Nix (§5.4).

## 6 Engineering Aspects

Discusses corners the model abstracts away: partial stores and exceptions (modelling missing values/errors via `Maybe`/`Either`); parallelism (each scheduler — topological, restarting, suspending — can be parallelised); impure computations (untracked dependencies, non-determinism, volatility, e.g. Excel's `RANDBETWEEN`); cloud implementation concerns (communication, offloading, eviction, shallow builds — illustrated via a "Frankenbuild" example combining deep constructive traces with non-determinism to produce an inconsistent result); self-tracking (Excel and Ninja can recompute a task if either its dependencies or the task itself changes); iterative computations (LaTeX-style fixed-point rebuilding, distinct from cyclic dependencies); and polymorphism (richer key/value types, as used by Shake).

## 7 Related Work

### 7.1 Other Build Systems

Notable examples discussed: Dune (uses arrows rather than monads), Ninja (topological scheduler + verifying traces, limited polymorphism), Nix (coarse-grained dependencies, content-addressed storage, not primarily a build system), Pluto (Shake-like, allows cyclic build rules with resolution strategies), Redo, Tup (refined dirty-bit implementation using file-system watching). Fabricate is identified as the one build system that cannot be modelled in this framework, since instead of a mapping from outputs to tasks it supplies a list of statements in order without declaring what each line produces.

### 7.2 Self-adjusting Computation

Self-adjusting computations are closely related — automatically adjusting to external changes to their inputs (e.g. self-adjusting sorting algorithms) — but are mostly used for in-memory computation and rely on the ability to dynamically allocate new keys in the store, a feature rarely seen in build systems (Shake's oracles can model this to a limited degree).

### 7.3 Memoization

Memoization — storing values of a function instead of recomputing them each time it is called — is a classic optimisation technique. Minimal build systems perform memoization, and memoization can be reduced to a minimal build system, but not vice versa, since minimal build systems solve a more complex optimisation problem (illustrated via a Levenshtein edit-distance example expressed in the `Tasks` abstraction).

## 8 Conclusions

The authors have investigated multiple build systems, showing how their properties are consequences of two implementation choices: what order you build in and how you decide whether to rebuild. By first decomposing the pieces, they show how to recompose the pieces to find new points in the design space. In particular, a simple recombination leads to a design for a monadic suspending cloud build system. Armed with that blueprint they hope to actually implement such a system as future work.
