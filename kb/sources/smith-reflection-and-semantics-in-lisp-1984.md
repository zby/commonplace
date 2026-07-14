---
source: https://www.ageofsignificance.org/documents/Reflection%20and%20Semantics%20in%20Lisp.pdf
description: "Brian Cantwell Smith's foundational procedural-reflection account: embedded self-theory, bidirectional causal connection, vantage point, and 3-Lisp's reflective tower"
captured: 2026-07-14
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Reflection and Semantics in Lisp

Author: Brian Cantwell Smith
Source: https://www.ageofsignificance.org/documents/Reflection%20and%20Semantics%20in%20Lisp.pdf
Date: 1984

## 1. Introduction

l"or three reasons, bi.';p's self-refi;rential properl.ies have not
led to a general un(h:rst.auding of w h a t it is fro" a cmuputational
system to reason, in s u b s t a n t i a l way~, about its; owe operations
a,ul structures. First., there is more to reasoning t h a n reference;
one also needs a theory, in terms of which to m a k e .,~ense of the
referenced domain. A comln, ter s y s t e m able to reason a b o u t
i t . : ; e l f - w h a t I will call a reflective s y s t e m - - will therefore
need an account of itself embedded within it. Second, there
m o s t he a systematic relationship between t h a t embedded
account and the s y s t e m it describes. W i t h o u t such a connection,
the account would be useless - - as disconnected an the words of
a haple~;s d r u n k who carries on about the evils of inebriation,
without reali~iug t h a t his story applies to himself. Tl'aditional
embeddiugs of IAsp in Lisp are inadequate in j u s t this way; they
provide no m e a n s for the implicit state of the Lisp process to he
reflected, m o m e n t by moment, in t h e explicit t e r m s of the
embecbled account. Tlaird, a reflective s y s t e m n m s t be given a n
appropriate v a n t a g e point at which to stand, far e n o u g h a w a y to
have itself in focus, a n d y e t close enough to see the i m p o r t a n t
details.
This paper presents a general architecture, called
procedurcd refh'ctio,, to support sell'directed reosoning in a
serial p r o g r a m m i n g lmaguage. Tim architecture, illustrated in a
revamped dialect called 3-Lisp, solves all three problems with a
single m e c h a n i s m . The basic idea is to define an infinite tower
of procedural self-nmdels, very m u c h like mctacircular
interpreters [Steele and S u s s m a n 1978b], except connected to
each other in a simple but critical way. In such a n architecture,
any aspect of a procc~s's state t h a t can be described in t e r m s of
One theory can be rendered explicit, in program accessihle
structures. F u r t h e r m o r e , as we will see, this apparently infinite
architecture can be finitely implemented.
The architecture allows the user to define complex
p r o g r a m m i n g constructs {such as escape operators, d e v i a n t
variableqmssing protocols, and d e h u g g i n g primitives), by writing
direct analogues of those metalinguistie semantical expressions
t h a t would normally be used to describe t h e m . As is always
true in semantics, the metatheoretie descriptions m u s t be
phrased in t e r m s of some particular set of concepts; in this case
I have used a theory of Lisp ba:;ed on e n v i r o n m e n t s a n d
continuations. A 3-Lisp program, therefore, at a n y point d u r i n g
a computation, can obtain representations of the e n v i r o n m e n t

and continuation char;wtcrising the s t a t e of the computation at
that pui,~t. T h u s , such constructs as ttmow and C,~TCII, which
m u s t otherwise be providt,d primitively, can in 3-Lisp be easily
defined a:; user procedures (and defined, furthermore, in code
that is ~,!most isomorphic to the ~-calculus. equations one
normally writes, in the metalal'$,3~a!,'c, to describe them). And
all this can be dolte wilhout writing the entire p r o g r a m in a
centinuation-pas:;iz~g :~tyle, o!' the sort illu,;trated in [Steele
197til. T h e point is no!. to decide at the outset w h a t should and
what should not be explicit (in Steele's example, c o n t i n u a t i o n s
m u s t be passed arouml explicitly from the hcgim, ing). Rather,
the retlective architecture provides a method of m a k i n g some
aspects of the computation explicit, right in the midst of a
computation, even if they were implicit a m o m e n t earlier. It
provides a m e c h ' m i s m , in other wo~'ds, of reaching up and
"pulling information out of the sky" when unexpected
circumstances w a r r a n t it, without h a v i n g to worry about it
otherwise.
The overall claim is t h a t retlection is simple to build on a
semantically sound hase, where 'semantically sound' m e a n s
more t h a n t h a t the s e m a n t i c s be earefl~lly formulated. Rather, I
a s s u m e t h r o u g h o u t t h a t computational s t r u c t u r e s have a
semantic significance t h a t t r a n s c e n d s their behavioural import
- - or, to p u t this a n o t h e r way, t h a t c m n p u t a t i n n a l s t r u c t u r e s are
about something, over anti above the effects they have on t h e
s y s t e m s they inhabit.
Lisp's Nft. for example, not only
ev~tluates to itself forever,
but
also (and
somewhat
independently) s t a n d s for Falsehood. A reconstruction of Lisp
semantics, therefore, m u s t deal explicitly with both declarative
and procedural ospects of the overall significance of
computational structures.
This distinction is different from
(though I will coutrast it with) t h e distinction between
operalional and denotational semantics. It is a reconstruction
h a s boca developed within a view t h a t p r o g r a m m i n g l a n g u a g e s
are properly to be understood in the s a m e theoretical t e r m s used
to a n a l y s e not only other computer l a n g u a g e s , but even n a t u r a l
languages.
This approach forces u s to d i s t i n g u i s h between a structure's
wdue and w h a t it returns, and to discriminate entities, like
n u m e r a l s and n u m b e r s , t h a t are isomorphic but not identical
(both instances of t h e general intellectual hygiene of avoiding
u s e / m e n t i o n errors). Lisp's basic notion of evaluation, I will
argue, is confused in this regard, and should be replaced with
independent notions of designation a n d simplification.
The
result is illustrated in a semantically rationalised dialect, called
2-Lisp, based on a simplifying (designation-preserving) term-
reducing processor. The point of defining 2-Lisp is t h a t the
reflective 3-Lisp can be very simply defined on top of it, whereas
defining a reflective version of a non-rationalised dialect would
be more cmnplicated and more difficult to u n d e r s t a n d .
The strategy of p r e s e n t i n g a g e n e r a l architecture by
developing a concrete instance of it was selected on t h e g r o u n d s
t h a t a gemfine theory of reflection (perhaps analogous to t h e
theory of rccursion) would be difficult to m o t i v a t e or defend
without t a k i n g this first, more pragtnatic, step. In section lO,

however, we will sketch a general "recipe" for adding reflective
capabilities to any serial language; 3-Lisp is t h e result of
applying this conversion process to t h e non-reflective 2-Lisp.
It is s o m e t i m e s said t h a t there are only a few con'~truc~.s
fi'om which l a n g u a g e s are a,~sembled, ihcluding for e x a m p l e
predicates, terms, functions, composition, recursion, abstraction,
a branching eulnctor, end quantification. T h o u g h differellt from
Ihe:~e notions (and not definable iJ~ t e r m s of them), reflection is
perhaps best viewed as a preposed addition to t h a t family.
Given this view, it is helpfid to u n d e r s t a n d relleci.ion by
comparing it, ia particular, with L'ecursion - - a construct with
which it s h a r e s m a n y features. Specifically, recursion can s e e m
viciously circldar to the uninitiated, and can lead to confused
i m p l e m e n t a t i o n s if poorly understood. T h e m a t h e m a t i c a l theory
ef recursion, however, underwrites our ability to usa reeursion
in p r o g r a m m i u g l a n g u a g e s without doubting its f u n d a m e n t a l
soundness
(in
thct,
for
many
programmers, without
u n d e r s t a n d i n g m u c h about the formal theory at all). Reflective
systems, similarly, initially seem viciously circular (or at least
infinite), and are difficult to i m p l e m e n t w i t h o u t an a d e q u a t e
understanding. The i n t e n t of this paper, however, is to a r g u e
t h a t reflection is as well-tamed a concept as recursion, a n d
potentially as efficient to use. Tim l o n g . r a n g e goal is not to
force p r o g r a m m e r s to u n d e r s t a n d the intricacies of d e s i g n i n g a
reflective dialect, b u t rather to enable t h e m to use reflection a n d
recursion with equal abandon.

## 2. Motivating Intuitions

Before t a k i n g up technical details, it will help to lay o u t
seme motivations and assumptions. First, by 'reflection' in its
most general sense, I m e a n tire ability of an a g e n t to reason not
only introspectively, about its self and internal t h o u g h t
processes, b u t ~.lso externally, about its behaviour and s i t u a t i o n
in the world. Ordinary reasoning is e x t e r n a l in a simple sense;
the point of reflection is to give a n a g e n t a more sophisticated
stance from which to consider its own presence in t h a t
embedd:,ng world. There is a growing c o n s e n s u s I t h a t reflective
abilities underlie m u c h of t h e plasticity with which we deal with
the world, both in l a n g u a g e (such as when one says Did you
understand uhat I meant?) and in "thought (such as when one
wenders how to deliver bad news compassionately). C o m m o n
sense s u g g e s t s t h a t reflection enables u s to m a s t e r new skills,
cope with incomplete knowledge, define terms, e x a m i n e
assumptions, review and distill our experiences, learn from
unexpected situations, plan, check for consistency, and recover
from mistakes.
In spite of working with reflection in formal l a n g u a g e s ,
most of the driving intuitions about reflection are grounded in
h u m a n rationality a n d language.
Steps towards reflection,
however, can also be found i,l m u c h of c u r r e n t computational
practice.
Debugging systems, trace packages, d y n a m i c code
optimizers,
run-time
compilers,
macros,
metacircular
interpreters, error handlers, type declarations, escape operators,
cerements, and a variety of other p r o g r a m m i n g constructs
involve, in one way or another, s t r u c t u r e s t h a t refer to or deal
with other ourts of a computational s y s t e m . These practices
st~ggest, as a first step towards a more general theory, defining
a limited and r a t h e r intro~,pcctive notion of 'procedural
reflection': self-referential behaviour itJ procedural languages, in
which expressions a r e pr:.marily used iu.,~tructionally, to
engender behaviour, r a t h e r t h a n assertionally, to m a k e claims.
It is the hope t h a t the lessons learned in this s m a l l e r task will
serve well in t h e larger account.
We mentioned at the outset t h a t t h e general task. in
defining a reflective system, is to embed a theory of the s y s t e m
in the system, so as to support smooth shifting b e t w e e n
reasuning directly about the worhl a n d reasoning a b o u t timt
reasoning. Because we are t a l k i n g ef reasoning, not merely of
language, we added a a additional r e q u i r e m e n t on this embedded
theory, beyond its being descriptive aml true: it m u s t also be
what we will call ca,sally conm,ch.d, so t h a t accounts of objects
anti e v e n t s are tied directly to those objects and events. Tim

Figure l : A Serial Medel of Cemputation

|

causal relationship, htrtherinore, m u s t go both ways: fi'om e v e n t
to description, a n d from description back to event. (It is as if we
were creating a magic kingdom, where fl'om a cake you could
automatically g e t a recipe, a n d from a recipe you could
automatically g e t a cake.)
In m a t h e m a t i c a l cases of self-
reference, including both self-referential s t a t e m e n t s , a n d models
of s y n t a x and proof theory, there is of course no causation at all,
since there is no temporality or b e h a v i o u r ( m a t h e m a t i c a l
s y s t e m s don't run). Causation, however, is certainly part of a n y
reflective agent. Suppose, for example, t h a t you capsize while
canoeing t h r o u g h dit/icult rapids, and s w i m to the shore to
figure out w h a t you did wrong. You need a description of w h a t
you were doing a t t h e m o m e n t the m i s h a p occurred; merely
h a v i n g a n a m e for yoursell, or even a general description of
yourself, would be u s e l e ~ . Also, your t h i n k i n g m u s t be able to
have some effect; no good will come from your merely
c o n t e m p l a t i n g . a wonderful theory of a n improved you. As well
as stepping back and being able to t h i n k about your behaviour,
in e t h e r words, you m u s t also be able to t a k e a revised t h e o r y .
a n d "dive back in u n d e r it", adjusting your behaviour so as to
satisfy the new account. A n d finally, we m e n t i o n e d t h a t w h e n
you take t h e step backwards, to reflect, you need a place to
~tand with j u s t the r i g h t combination of connection a n d
detachment.
C o m p u t a t i o n a l reflective s y s t e m s , similarly, m u s t provide
both directions of causal connection, a n d an appropriate v a n t a g e
point. Consider, for example, a d e b u g g i n g s y s t e m t h a t accesses
stack
frames
and
other
implementation-dependent
representations of processor state, in order to give the u s e r a n
account of w h a t a p r o g r a m is up to in t h e m i d s t of a
computation. First, slalck-l'rames and i m p l e m e n t a t i o n codes a r e
really j u s t descriptions, in a r a t h e r i n e l e g a n t l a n g u a g e , of the
state of t h e process they describe. Like a n y description, they
m a k e explicit some ef w h a t was implicit in the process itself
(this is one reason they are useful in debugging). F u r t h e r n m r e ,
because of the n a t u r e of i m p l e m e n t a t i o n , they are a l w a y s
available, a n d always true. They h a v e t h e s e properties because
they play a causal role ia..~hever¥ existence el' t h e process t h e y
implement; t h e y therefore a u t o m a t i c a l l y solve t h e "event-to-
description" direction of causal connection. Second, d e b u g g i n g
s y s t e m s m u s t solve t h e "description to reality" problem, by
providing a way of m a k i n g revised descriptions of the process
true of t h a t process.
They carefully provide facilities for
altering the underlying state, based on the user's description of
w h a t t h a t s t a t e should be. W i t h o u t this direction el: causal
connection, t h e d e b u g g i n g s y s t e m , like a n a b s t r a c t nmdel, could
have no effect on the process it was e x a m i n i n g . And finally,
p r o g r a m m e r s who write d e b u g g i n g s y s t e m s wrestle w i t h the
problem of providing a proper v a n t a g e point.
In this case,
practice h a s been particularly atheoretical; it is typical to
arrange, very cautiously, fur the debugger to tiptoe around its
own stack frames, in order to avoid variable clashes a n d other
u n w a n t e d interactions.
As we will see in developing 3-Lisp, all of t h e s e concerns
can be dealt with in a reflective l a n g u a g e in ways t h a t a r e both
simple and implementation-independent. The procedural code in
the metacircular processor serves as the "theory" discussed
above; the causal connection is provided by a m e c h a n i s m
whereby procedures at one level in the reflective tower are r u n
in the process one level above (a clean way, essentially, of
enabling a program to define s u b r e u t i n e s to be rux~ in its own

~ S~l_~act,c Ooma~n S 1

~3F"Semant. i c " Do.._.mmatn D

Figure 2: A Simple Seman.tic lntepretalion Function

m~plemeutation). In one sense it is all straightforward; the
subtlety of 3-Lisp has to do not so much with the power of such
a mechanism, which is evidi~nt, but with how such power can be
finitely provided - - a question we will examine in section 9.
Some final assumptions. I assume a simple serial model of
computation, illustrated in Figure 1, in which a computational
process as a whole is divided into an internal assemblage of
program and data structures collectively called the structural
field, coupled with an internal process that examines and
manipulates these structures. In computer science this inner
process (or 'homunculus') is typically called the intelpreter; in
order to avoid confusion with semantic notions of interpretation,
I will call it the processor. While models of reflection for
concurrent systems could undoubtedly be formulated, I claim
here only that our particular architecture is general for calculi
of this serial (i.e., single processor) sort.
I will use the term 'structure' for elements of the structural
field, all of which are inside the machine, never for abstract
mathematical or other "external" entities like numbers,
functions, or radios.
(Although this terminology may be
confusing for semanticists who think of a structure as a model, I
want to avoid calling them expressions, since the latter term
connotes linguistic or notational entities. The aim is for a
concept covering both
data
structures
and
internal
representations of programs, with which to categorize what we
would in ordinary English call the structure of the overall
process or agent.)
Consequently, I call metastructural any
structure
that
designates another
structure,
reserving
metasyntactic for expressions designating linguistic entities or
expressmns.- Given our interest in internal self-reference, it is
clear that both structural field and processor, as well as
numbers and functions and the like, will be part of the semantic
domain. Note that metastructaral calculi must be distinguished
from those that are higher-order, in which terms and arguments
may designate functions of any degree (2-Lisp and 3-Lisp will
have both properties). 3

•

O

## 3. A Framework for Computational Semantics

We turn, then, to questions of semantics. In the simplest
case, semantics is taken to involve a mapping, possibly
contextually relativized, from a syntactic to semantic domain, as
shown in Figure 2 . . T h e mapping (,1)) is called an interpretation
function (to be distinguished, as noted above, from the standard
comlmter science notion of an interpreter). It is usually specified
inductively, with respect to the compositional structure of the
elements of the syntactic domain, which is typically a set of
syntactic or linguistic sorts of entities. The semantic domain
may be of any type whatsoever, including a domain of
behaviour; in reflective systems it will often include the
syntactic domain as a proper part. We will use a variety of
different terms for different kinds of semantic relationship; in
the general case, we will call s a symbol or sign, and say that s
signifies d, or conversely that d is the significance or
interpretation of s.
In a computational setting, there are several semantic
relationships - - not different ways of characterizing the same
relationship (as operational and denotational semantical
~ c o u n t s are sometimes taken to be), for example, but genuinely
distinct relationships. These different relationships make for a
more complex semantic framework, as do ambiguities in the use
of words like 'program'. In many settings, such as in purely
extensional functional programming languages, such distinctions
are inconsequential.
But when we turn to reflection, self-
reference, and metastructural processors, these otherwise minor
distinctions play a much more important role. Also, since the
semantical thi~ory we adopt will be at least partially embedded

within 3-Lisp, the analysis will aflbct the formal design• Our
approach, therefore, will be start with basic and simple
intuitions, and to identify a finer-grained set of distinctions than
are usually employed. We will consider very brielly the issue of
how current programming language semantics would be
reconstructed in these terms, but the complexities involved in
answering that question adequately would take us beyond the
scope of the present paper.
At the outset, we distinguish three things: a) the objects
and events in the world in which a comlmtational process is
embedded, including both real-world objects like cars and caviar,
and set-theoretic abstractions like numbers and functions (i.e.,
we "ldopt a kind of pan-platonic idealism about mathematics}; b)
the internal elements, structures, or processes inside the
computer, including data structures, l~rogram representations,
execution sequences and so forth {these are all formal objects, in
the sense that computation is formal symbol manipulation}; and
c) notational or communicational expressions, in some externally
observable and eonsensually established medium of interaction,
such as strings of characters, streams of words, or sequences of
display images on a computer terminal. The last set are the
consP.ituent3 of the communication one has with the
computational process; the middle are the ingredients of the
process with which one interacts, and the first (at least
presumptively) are the elements of the world about which that
communication is held. In the h u m a n case, the three domains
correspond to world, mind, and language.
It is a truism that the third domain of objects
communication elements - - are semantic. We claim, however,
that the middle set are semantic as well (i.e., that structures are
bearers of meaning, information, or whatever). Distinguishing
between the semautics of communicative expressions and the
semantics of internal structures will be one of main features of
the framework we adopt. It should be noted, however, that in
spite of our endorsing the reality of internal structures, and the
reality of the embedding world, it is nonetheless true that the
only things that actually happen with computers (at least the
only thing we will consider, since we will ignore sensors and
manipulators} are communicative interactions. If, for example, I
ask my Lisp machine to calculate the square root of 2. w h a t I do
is to type some expression like (SQRr Z.0) at it, and then receive
back some other expression, probably quite like I. 414, by way of
response. '['he interaction is carried out entirely in terms of
expressions; no structures, numbers, or functions are part of the
• interactional event. The participation or relevance of any of
these more abstract objects, therefore, must be inferred from,
and mediated through, the communicative act.
We will begin to analyse this complex of relationships
using the terminology suggested in Figure 3. By O, very simply,
we refer to the relationship between external notational
expressions and internal structures; by ,1, to the processes and
behaviours those structural tield elements engender (thus I, is
inherently temporal), and by ,1, to the entities in the world that
they designate. The relations 4, and t, are named, for mnemonic
convenience, by analogy with philosophy and psychology,
respectively, since a study of ,I, is a study of the relationship
between structures and the world, whereas a study of ,1, is a
study of the relationships among symbols, all of which, in
contrast, are "within the head" (of person or machine).
Computation is inherently temporal; our semantic analysis,
therefore, will have to deal explicitly with relationships across
the passage of time. In Figure 4, therefore, we have unfolded
the diagram of Figure 3 across a unit of time, so as to get at a
full configuration of these relationships. The expressions n I and
n2 are intended to be linguistic or communicative entities, as
described above; Sl and s2 are internal structures over which
the internal processing is defined. The relationship o, which we
will call internalisation, relates these two kinds of object, as
appropriate for the device or process in question (we will say, in
addition, that nl ,otates sl)• For example, in first-order logic nl
and n2 would be expressions, perhaps written with letters and
spaces and '3" signs; st and s2. t~ '~he extent they can even be
said to exist, would be something like abstract derivation tree

7J

Figure 3: Sem~lntic Relationships in a Computollonal Process

types of the corresponding first-order formulae, hi Lisp, as we
will see, n I and n 2 would be the input and output expressions,
written with letters and parent.hoses, or perhaps with boxes and
arrows; sl and s2 would be the cons-cells in the s-expre,q.qion
heap.
In contrast, dl and d 2 are elements oz" fragments of the
embedding world, and 4, is the relationship that internal
structures bear to them. q~, in other words, is the interpretation
function t h s t makes explicit what we will call the designation of
intern,d structures (not the designation of linguistic terms,
which would be described by ~,oO). The relationship between my
mental token for T. S. Eliot, for example, and the poet himself,
would be formulated as part of ~, whereas the relationship
between the public name ~I'. S. Eliot" and the poet would be
expressed as 4~(O("T.S.EI.IOT')) • T.S.I.:I.IOT. Similarly, 4, would
relate an internal "numeral" structure (say, the numeral 3) to
the corresponding number. As mentioned at the outset, our
focus on ,1, is evidence of our permeating semantical assumption
that all structures have designations - - or, to put it another
way, that the structures are all symbols. 4
The ~1, relation, in contrast to O and ~, always (and
necessarily, b e c a u ~ it dosen't hove access to anything else)
relates some internal structures to others, or a t least to
behaviours over them. To the extent that it would make sense
to talk of a '¢ in logic, it would approximately be the formally
computed derivability relationship (i.e., I-); in a natural
deduction or resolution ~ h e m e e , ,I, would be a subset of the
derivability relationship, picking out the particular inference
procedures those regimens adopt. In a computational setting,
however, ,l, would be the function computed by the processor
(i.e., * is evaluation in Lisp).
The relationships O, ,I,, and q have differeat relative
importances in different linguistic disciplines, and different
relationships among them have been given different names. For
example, O is usually ignored in logic, and there is little
tendency to view the study of ~', called proof theory, as
semantical, although it is always related to semantics, as in
proving soundness and completsner~ (which, incidentally, can be
expressed as the equation ~,(Sl,S 2) m [ dl ~ d2 ]. if one takes ,If
to be a relation, and <, to be an inverse satisfaction relationship
between sentences and possible worlds that satisfy them). In
addition, there are a variety of "independence" claims that have
arisen in different fields. That ,I, does not uniquely determine 4,,
for example, is the "psychology narrowly construed" and
col~comitant methodological solipsism of Putnam, Fodor, and
others [Fodor 19801.
That O is usually specifiable
compositionally and independently of 4, or • is essentially a
statement of the autonomy thesis for language. Similarly, when
0 cannot be ~pecified indepently of ,I,, computer science will say
that a programming language "cannot be parsed except at
runtime" (Teco and the first versions of Smalltalk were of this
character).
A thorough analysis of these semantic relationships,
however, and of the relationships among them, is the subject of
a different paper. For present purposes we need not take a
stand on which of O, q', or • has a prior claim on being
semantics, but we do need a little terminology to make sense of
it all. For discussion, we will refer to the "~" of a structure as
its declaratit~e import, and to its "q," as its procedural

J

Figure 4: A Fra mework for Computational Semantics

consequence. It is also convenient to identify some of the
situations when two of the six entities (nt, n2, sl, s2, all, and
do) are identical. In particular, we will say that sl is self-
referential if dl • sl, that ,I, de-references s! if s2 ffi dr, and that
• is designatioa.preser~iag (at st) when d t • d 2 (as it always is,
for example, in the ~,-calculus, where t, - - a- and #-reduction
do not a l t e r the interpretation in the standard model).
It is natural to ask what a program is, what programndng
language semantics gives an account of, and how (this is a
related question) • and ,Z, relate in the programming language
case. An adequate answer to this, however, introduces a maze
of complexity that will be considered in future work.
To
appreciate some of the difficulties, note that there are two
different ways in which we can conceive of a program,
suggesting different semantical analyses. On the one hand, a
program can be viewed as a linguistic object that de~riboa or
signifies a computational process consisting of the data
structures and activities that result from (or arise during) its
execution.
In this sense a program is primarily a
communicative object, not so much playing a role within a
computational process as existing outside the process and
representing it. Putting aside for a m o m e n t the question of
whom it is m e a n t to communicate to, we would simply say that
a program is in the domain of O, and, roughly, that ~oO of such
an expression would be the computation described. The same
characterization would of course apply to a specification; indeed,
the only salient difference might be t h a t a specification would
avoid using non-effective concepts in describing behaviour. One
would expect specifications to be stated in a declarative
language (in the sense defined in footnote 4), since specifications
aren't themselves to be executed or run, even though they speak
about behaviours or computations.
Thus, for program or
specification b describing computational process c, we would
have (for the relevant language) something like ~ ( O ( b ) l - c. If
b were a program, there would be an additional constraint that
the program somehow play a causal role in engendering the
computational process c t h a t it is taken to describe.
There is, however, an alternative conception, that places
the program inside the machine as a causal participant in the
bchsviour that results. This view is closer to the one implicitly
adopted in Figure 1, and it is closer (we claim) to the way in
which a Lisp program must be semantically analysed, especially
if we are to understand Lisp's emergent reflective properties. In
some ways this different view has a yon N e u m a n character, in
the sense of equating program and data. On this view, the more
appropriate equation would seem to be ¢/(O(b)) --e, since one
would expect t h e .processing of the program to yield the
appropriate behaviour. One would seem to have to reconcile
this equation with t h a t in the previous paragraph; something it
is not clear it is possible to do.
But this will require further work. What we can say here
is that programming language semantics seems to focus on
what, in our terminology, would be a n amalgam of q' and @.
For our purposes we need only note that we will have to keep q,
and • strictly separate, while recognising (because of the context
relativity and nonlocal effects) that the two parts cannot be told
independently.
Formally, one needs to specify a general
significance function Z, that recursively specifies • and
together. In particular, given any structure Sl, and any state of

the processor a n d the rest of the field (encoded, say, in a n
environment, continuation, and perhaps a store), ~ will specify
the structure, configuration, and state t h a t would result (i.e., it
will specify the use of st), and also the relationship to the world
t h a t Sl signifies. For example, given a I,isp s t r u c t u r e o£ t h e
form (÷ I (PRO~ (SZTQ A 2) A)), X would specify t h a t the whole
structure designated t h e n u m b e r three, t h a t it would r e t u r n the
n u m e r a l 3, and t h a t the m a c h i u e would be left in a state in
which the binding of the variable A was changed to the n u m e r a l

z.

Before leaving s e m a n t i c s completely, it is instructive to
apply our various distinctions to traditional Lisp. We said
above t h a t all interaction with computational processes is
mediated by cmnmunication; this can be stated in this
terminology by noting t h a t O a n d O "t (we will call the latter
e.rternalisation) are a part of any interaction. T h u s Lisp's "read-
eval-print" loop is mirrored in our a n a l y s i s as an iterated
version of O'1o*oO (i.e., if nj is a n expression you type at Lisp,
then n 2 is o ' l ( * ( O ( n l l ) ) ) .
The Lisp s t r u c t u r a l field, as it
happens, h a s an extremely simple compositional structure, based
on a binary directed g r a p h of atomic e l e m e n t s called cons-cells,
extended with atoms, n u m e r a l s , and so forth. The linguistic or
communicative expressions t h a t we use to r e p r e s e n t Lisp
programs - - the formal l a n g u a g e objects t h a t we edit with our
editors and print in books and on t e r m i n a l screens - - is a
separate lexicai (or s o m e t i m e s graphical) object, with its own
s y n t a x (of parentheses and identifiers in the lexical case; or
boxes and arrows in the graphical).
There is in Lisp a relatively close correspondence between
expressions and structures; it is one-to-one in the graphical case,
but the s t a n d a r d lexical notation is both a m b i g u o u s (because of
shared tails) and incomplete (because of its inability to
represent cyclical structures).
The correspondence need n o t
have been as close as it is; t h e process of converting from
external s y n t a x or notation to internal structure could involve
arbitrary a m o u n t s of computation, as evidenced by read macros
and other syntactic or notational devices. But the i m p o r t a n t
point is t h a t it is s t r u c t u r a l field elements, not notations, over
which most Lisp operations are defined.
If you type
(RPLACA '(A e I 'el, for example, the processor will c h a n g e t h e
CAR of a field structure; it will not back up your t e r m i n a l a n d
erase t h e eleventh character of your im~ut exvreseion.
Similarly, Lisp a t o m s are field element% not to be confused with
their lexical representations (called P.names). Again, quoted
forms like (QUOTE AOC) designate s t r u c t u r a l field e l e m e n t s , not
input strings.
T h e form (QUOrE ...), in other words, is a
structural quotation operator; notational quotation is different,
usually notated with string quotes ('ABe'). 5

.

Considered

## 4. Evaluation Considered Harmful

The claim t h a t all three relationships (O, ~, a n d ,v) figure
crucially in :m account of Lisp is not a formal one. It m a k e s a n
empirical claim on the m i n d s of p r o g r a m m e r s , a n d c a n n o t be
settled by pointing to any c u r r e n t them'ies or i m p l e m e n t a t i o n s .
Nonetheless, it is u n a r g u a b l e t h a t l,isp's n u m e r a l s designate
n u m b e r s , a n d t h a t t h e a t o m s T and NIL (at least in predicative
contexts) designate t r u t h a n d falsity - - no one could l e a r n Lisp

"lhrce

x

Tmthl

"l~ree

a

Falsityl

th

nction

Figure 5: L I S P Evaluation vs. Designation: Some Examples

,b

¢,1,

Intctnal Structures

~

... cdgc of the machinc

,:

External World

Figure 6: LISP's "De-reference I f You Call" Evalunlion Protocol

without learning Lhis fact.
Similarly, (EQ 'A '8) d e s i g n a t e s
falsity. Furthermore, the s t r u c t u r e (CAR '(A . n i l d e s i g n a t e s
the atom A; this is manifested by the fact t h a t people, in
describing Lisp, use expressions such as "i£ the C^lt of t h e list is
I At~nOA, tl~cn it's a procedure", where t h e t e r m "the CAR of the
list" is used as an English referring expression, not as a quoted
f r a g m e n t of Lisp (and English, or n a t u r a l l a n g u a g e generally, is
by definition the locus of what designation is). (ouorE A), or 'A,
is a n o t h e r way of designating the atom A; t h a t ' s j u s t w h a t
quotation is. Finally, we can take a t o m s like CAR a n d ÷ to
designate the obvious functions.
What, then, is the relationship h e t w e e n the declarative
import (,I,) of Lisp s t r u c t u r e s and their procedural consequence
(,v)? Inspection of the data given in Figure 5 shows t h a t Lisp
obeys the following constraint (more m u s t be said about * in
those cases for which ~ ( * ( s ) ) = ,P(s), since the identity function
would satisfy this equation):

VS E ,S'[ i f [~P(SlC S ] then [¢/(S) = 4b(S) ]
else ['~(¢/(S)) = 4)(S)I]

(1)

All Lisps, including Scheme [Steele a n d S u s s m a n 1978a], in
other words, dereference a n y s t r u c t u r e whose designation is
a n o t h e r structure, b u t will r e t u r n a co-designating s t r u c t u r e for
any whose designation is outside of the m a c h i n e (Figure 6).
W h e r e a s evaluation is often t h o u g h t to correspond to t h e
semantic interpretation function q,, in other words, a n d
therefore to have type EXeRESSIONS -~ VALUES, evaluation in Lisp
is often a designation-preserving operation. In fact no c o m p u t e r
can evaluate a s t r u c t u r e like (~ 2 3), if t h a t m e a n s r e t u r n i n g
the designation, a n y more t h a n it can e v a l u a t e the n a m e
Ilesperus or peanut b,tter.
Obeying equation (t) is highly anomolous. It m e a n s t h a t
even if one knows w h a t Y is, and k n o w s X e v a l u a t e s to Y, one
still doesn't know what X designates. It licences such s e m a n t i c
anomalies as (÷ I 'z), which will e v a l u a t e to 3 in all e x t a n t
Lisps. Informally, we will s a y t h a t Lisp's e v a l u a t e r crosses
semantical levels, and therefore o h ~ u r e s the difference between
simplification a n d designation. Given t h a t processors cannot
always de-reference (since the co-domain is limited to t h e
structural field), it serous they should a l w a y s simplify, a n d
therefore obey t h e following constraint ( d i a g r a m m e d in Figure
7):

VS E S [ , b ( * ( s ) )

: ,P(S) A NOIINAL-FORM(~P(S))]

(2)

The content of this equation clearly depends entirely on t h e
content of the predicale'NonHAL-rOaN (if ~ORH^L-rOnN were kx. true
then * could be the identity function). In the k-calculus, t h e

~

/

normal form

Figure 7: A Normalisation Protocol

Reduction

[ vo: valut~ Dos l~l.li

Application

Figure 8: Appliceaion vs. Reduction

notion of n o r m a l - f o r m e d n e s s is defined in t e r m s of t h e
processing protocols (~- and p-reduction), b u t we cannot use t h a t
definition here, on t h r e a t of circularity. Instead, we s a y t h a t a
s t r u c t u r e is in n o r m a l iorm if and only if it satisfies t h e
following three independent conditions:
1. It is context-independent, in t h e sense of h a v i n g t h e s a m e
declarative (,I,) and procedural (,1,) import independent of
the context of use;
2. It is side-effect-free, implying t h a t the processing of the
s t r u c t u r e will h a v e no effect on the s t r u c t u r a l field,
processor state, or external world; and
3. It is stable, m e a n i n g t h a t it m u s t normalise to itself in all
contexts, so t h a t * will be idempotent.
We would t h e n have to prove, given a l a n g u a g e specification,
t h a t equation (2) is satisfied.
Two notes. First, I won't use the t e r m s 'evaluate' or
'value' for expressions or structures, referring instead to
normalisation for *, and designrttion for ¢. I will s o m e t i m e s call
the result of normulising a s t r u c t u r e its result or what it
retur~ts. There is also a problem with the t e r m s 'apply' a n d
'application'; in s t a n d a r d Lisps, APPLY is a function from
s t r u c t u r e s and a r g u m e n t s onto values, b u t its use, like
"evaluate', is rife with u s e / m e n t i o n confusions. As illustrated in
Figure 8, we will use 'apply' for m a t h e m a t i c a l function
application - - i.e., to refer to a relationship between a function,
some a r g u m e n t s , and the value of the function applied to those
a r g u m e n t s --- and the t e r m 'reduce' to relate t h e three
expressions t h a t designate functions, a r g u m e n t s , and values,
respectively.
Note t h a t I still use the t e r m 'value' (as for
example in the previous sentence), b u t only to n a m e t h a t entity
onto which a function m a p s its a r g u m e n t s .
Second, t h e idea of a n o r m a l i s i n g processor depends on t h e
idea t h a t symbolic s t r u c t u r e s have a s e m a n t i c significance prior
to. and independent at: the way in which they are treated by
the processor. Witlmut this a s s u m p t i o n we could not even a s k
about t h e semantic character of the Lisp (or a n y other)
processor, let alone s u g g e s t a cleaner version. W i t h o u t such a n
assumption, more generally, one cannot say t h a t a given
processor is correct, or coherent, or incoherent; it is merely w h a t
it is.
Given one account of w h a t it does (like a n
implementation), one c~n compare t h a t to a n o t h e r account (like
a specification).
One can also prove t h a t it h a s certain
properties, such as t h a t it always t e r m i n a t e s , or uses resources
in certain ways. One can prove properties of p r o g r a m s written
in the l a n g u a g e it r u n s (from a specification of the ALGOL
processor, for example, one m i g h t prove t h a t a particular
t)rogram sorted its input). However none of these q u e s t i o n s deal
with the f u n d a m e n t a l question about t h e s e m a n t i c a l n a t u r e of
the processor itself. We are not looking for a way in which to
say t h a t the s e m a n t i c s of (CA~ ' ( a . s ) ) is A because t h a t is how
the language is defined; rather, we w a n t to s a y t h a t the
l a n g u a g e was defined t h a t way because A is w h a t (CAR ' ( ^ . 8))
designates. Semantics, in other words, can be a tool with which
to judge s y s t e m s , not merely a method of describing them.

## 5. 2-Lisp: A Semantically Rationalised Dialect

Since we lmve torn a p a r t the notion of e w d u a t i o n into two
constituent notions, we m u s t s t a r t at the b e g i n n i n g a n d build
Lisp over again. 2-Lisp is a proposed result. Some s u m m a r y
c o m m e n t s can be made. First, I h a v e reconstructed w h a t I call
the category structure of Lisp, requiring t h a t the categories into
which Lisp s t r u c t u r e s are sorted, for various purposes, line up
(giving the dialect a property called category alignment). More
specifically, Lisp expressions are sorted into categories by
notation, by s t r u c t u r e (atoms, cons pairs, n u m e r a l s ) , by
procedural t r e a t m e n t (the "dispatch" inside EVAL), a n d by
declarative s e m a n t i c s (the type of object designated).
Traditionally, as illustrated in Figure 9, these categories are not
aligned; lists, a derived structure type, include some of the pairs
and one atom (Nzt); t h e procedural r e g i m e n treats some pairs
(those with LAMSDA in the CAR) in one way, most a t o m s (except T
and ~It) in another, and so forth. In 2-Lisp we require t h e
notational, structural, procedural, a n d semantic categories to
correspond one-to-one, as shown in Figure l0 (this is a bit of a n
oversimplification, since a t o m s and pairs - - r e p r e s e n t i n g
arbitrary variables a n d arbitrary function application s t r u c t u r e s
or redexes - - can d e s i g n a t e entities of a n y s e m a n t i c type).
A s u m m a r y of 2-Lisp is given in Figure 11, b u t some
c o m m e n t s can be m a d e here. Like most m a t h e m a t i c a l a n d
logical l a n g u a g e s , 2-Lisp is almost entirely declaratively
extensional.
T h u s (+ 1 z), which is a n abbreviation for
(+ . [t 2]), d e s i g n a t e s the value of t h e application of t h e
function designated by the atom + to the sequence of n u m b e r s
designated by t h e rail f l 2]. In other words (+ I z) d e s i g n a t e s
the n u m b e r three, of whici~ the n u m e r a l 3 is t h e normal-form
designator; (÷ 1 2) therefore normelises to the n u m e r a l 3, as
expected. 2-Lisp is also u s u a l l y call-by-value (what one c a n
t h i n k of as "procedurally extensional"), in t h e s e n s e t h a t
procedures by a n d large normalise t h e i r a r g u m e n t s .
Thus,
(+ ! (BLOCK (PnZNT "hello')Z) will n o r m a l i s e to 3, p r i n t i n g
'hello ° in the process.
Many properties of Lisp t h a t m u s t normally be posited in
an ad hoc way fall o u t directly from our analysis. For example,
one m u s t normally s t a t e explicitly t h a t some atoms, such as v
and NZL and t h e n u m e r a l s , a r e self-evaluating; in 2-Lisp, t h e fact
t h a t the boolean c o n s t a n t s a r e self-normalising follows directly
from t h e fact t h a t they are n o r m a l form designators. Similarly,
closures are a n a t u r a l category, a n d d i s t i n g u i s h a b l e from t h e
functions they d e s i g n a t e (there is ambiguity, in Scheme, as to
w h e t h e r t h e value of + is a function or a closure). Finally,
because of the category alignment, if x d e s i g n a t e s a sequence of
the first three n u m b e r s (i.e., it is bound to t h e rail [z 3]), t h e n
(+ . x) will designate five a n d n o r m a l i s e to 5; no metatbeoretic
m.'zchinery is needed for this " u n c u r r y i n g " operation (in r e g u l a r
Lisp one m u s t use (APPLY '+ X); in Scheme, (aPPLY ÷ X)).
'['here are n u m e r o u s properties of 2-Lisp t h a t we will
ignore in this paper. T h e dialect is defined (in [Smith 82]) to
izmlude side-effects, inte||sional procedures ( t h a t do not
uot~nalise their a r g u m e n t s ) , and a variety of other sometimes-
s h u n n e d properties, in part to show t h a t our s e m a n t i c
reconstruction is compatible with t h e full g a m u t of features
found in real p r o g r a m m i n g l a n g u a g e s . Reeursion is handled
with explicit fixed-point operators.
2-Lisp is a n e m i n e n t l y '
usable dialect (it s u b s u m e s Scheme b u t is nmre powerful, in
part because of the m e t ^ s t r u c t u r a l access to closures), a l t h o u g h
it is ruthlessly semantically strict.

## 6. Self-Reference in 2-Lisp

We t u r n now to m a t t e r s of ~elf-reference.
Traditional I,isps provide n a m e s U=V^L and APPLY) for t h e
primitive proce&~or procedures; the 2-Lisp a n a l o g u e s a r e
UORHALZSF a n d n[DUCE. Ignoring for a m o m e n t context a r g u m e n t ~
such as e n v i r o n m e n t s and continuations, (I~OR~ALISE '(÷ Z 3) )
designates the normal-form s t r u c t u r e to which" (÷ z 3)
normaliscs, and therefore r e t u r n s the handle '5. Similarly,

I)cr. Str.

Lexical

Proccdural

Declarative

. A I" or NIL

H

T.Values

,,o.r.,s

[ Labels

~

Atoms

loot tea P.

~..-~(quote : . ) ~
Sexprs-
N~. L i s t s
,~Se~uence,
'1
Appl'ns "

LiStS

Jl

"~"

I "L!st"

Figure 9: The Categol:y Structure o f LISP 1.5

We begin with the objects.
Ignoring i n p u t / o u t p u t
categories such as characters, strings, a n d s t r e a m s , t h e r e are
seven 2-Lisp s t r u c t u r e types, as illustrated in Table 1. T h e
numerals (notated as usual) a n d t h e two boolean c o n s t a n t s
(notated 'ST' and '$f') are u n i q u e (i.e., canonical), atomic,
normal-form designators of n u m b e r s
and
truth-values,
respectively. Rails (notated '[A~ Az ... AA]') d e s i g n a t e sequences;
they resemble s t a n d a r d Lisp lists, b u t we d i s t i n g u i s h t h e m from
pairs in order to avoid category confusion, and give t h e m their
own name, in order to avoid confusion with sequences (or
vectors or tuples), which are normally t a k e n to be platonic
ideals.
All atoms are used as variables (i.e., as context-
dependent names); as a consequence, no a t o m is normal-form,
and no atom will ever be r e t u r n e d as the r e s u l t of processing a
structure (although a designator of it m a y be).
Pairs
(sometimes also called redexes, and notated '(A~ . Az)') d e s i g n a t e
the value of t h e function designated by the CAR applied to the
a r g u m e n t s designated by the CDR. By t a k i n g t h e notational
form '{A~ Az ... A~)' to abbreviate '(A 1 . I:A z Aa ... Akl)' i n s t e a d of
'(A~ . (Az . ( ... (A~ .NIL)...)))', we preserve the s t a n d a r d look
of Lisp programs, without sacrificing category a l i g n m e n t . (Note
t h a t in 2-Lisp there is no d i s t i n g u i s h e d a t o m NIL, a n d *()' is a
notational error ~ corresponding to no s t r u c t u r a l field element.)
Closures (notated '(CLOSURE: ... }') are normal-form function
designators, but they are not canonical, since it is not generally
decidable whether two structures designate the same function.
Finally, handles are unique normal-form designators of all
structures; they are notated with a leading single quote m a r k
(thus "'A' notates the handle of the atom notated 'A', "(A . St'
notates the handle of the pair notated '(A . s)', etc.). Because
designation and simplification are orthogonal, quotation is a
structural primitive, not a special procedure (although a QUOTE
procedure is easy to define in 3-Lisp).
W e turn next to the functions (and use '~' to m e a n
'normalises to'). There are the usual arithmetic primitives (+, -,
• . and /). Identity (signified with =) is computable over the fall
semantic domain except functions; thus (- 3 (+ I z)) =* ST, but
(= + (LAMOOA [X] (+ X X)))will generate a processing error, even
though it designates truth. The traditionally unmotivated
difference between E0 and EOUAL turns out to be an expected
difference in granularity between the identity of mathematical
sequences and their syntactic designators; thus:
(= I t 2 3] [-1 z 3 ] )
= , Sr

(= ' [ I Z 3] '[1 2 3])
(= (z z 3] ' [ I z 3 ] )

=~
=~

$F
$F

(In the last case one s t r u c t u r e d e s i g n a t e s a sequence a n d one a
rail.) IST and REST are the CAR/CDR a n a l o g u e s on sequences and
rails; thus, ( t a t It0 20 30]) ~ t0; (REST El0 20 30~]) ~ r20 30].
CAR and CaR are defined over pairs; t h u s (CAR ' ( a . S)) ~ 'A
(because it designates A), and (COR '(+ 1 2)) = '[1 z]. T h e pair
constructor is called PC0NS (thus (PCONS 'A 'a) ~ ' (A . a)); the
corresponding constructors for atoms, rails, and closures are
called AEONS, aeONS, and CC0NS. There are 11 primitive
characteristic predicates, 7 for the internal s t r u c t u r a l types

I)cclarative

I.exical

Structural

Ih'ocedural

Numbers I
lruth Values I
Funct ions I

.

.

.

Sequences [

....
:~

flails
Eorm
tom s

J'

Structures [

~ o r , . a l

L~mcric

s ~s._J~-~____A_A

I ( ^1 .-^z )' [--t___pal~_~__J

I

Pairs

Figure I0: The Category Structure of 2-LISP a n d 3-LISP

Figure I 1: A n Overview of 2-Li~p

(AlOM, PAll|, RAIl., i;OOLEAN, NUMERAL, CLOSURE, a n d IIAFJDLE) and 4 fo~
the external types (NUMBER, TRurtI-VALUE, SEOUENCE, a n d FuNcrIo~J).

Thus:
(NUMOER 3)

~ $T
=~ ST
~ Sf

(NUMERAL '3)
(NUMBER '3)

(FUNCTION +l
==> ST
(FUBCTION '*) =-~ Sf
Procedurally intensional IF and CONO are defined as usual; BLOCK
(as in Scheme) is like standard Lisp's PROGN. BODY, PATTERN, a n d
fNVta0NMENT are the three selector functions on closures.
Finally, functions are u s u a l l y "defined" (i.e., conveniently
designated in a contextually relative way) with s t r u c t u r e s of the
tbrm (LAM8OA SIMPLE AReS BOOY) (the keyword SIMPLE will be
explained presently); t h u s (LAMBDA SIMPLe IX] (+ X Xll r e t u r n s a
closure t h a t d e s i g n a t e s a function t h a t doubles n u m b e r s ;
((LAblBflA SIMPLE IX] (+ X X)) 4) ~ 8,
2-Lisp is h i g h e r order, and therefore lexically seeped, like
the X-calculus a n d Scheme. However, as mentioned earlier and;
illustrated with the h a n d l e s in t h e previous paragraph, it is also
m e t a s t r u c t u r a l , providing a n explicit ability to n a m e internal
structures.
Two primitive procedures, called uP a n d DOWN
(usually notated with the arrows %' a n d "C) help to mediate t h i s
m e t a s t r u c t u r a l h i e r a r c h y (there is otherwise no way to add or
remove quotes; ~z will normalise to "2 forever, never TO z).
Specifically, tSTAVC d e s i g n a t e s the normal~form designator of t h e
designation of SrRUC; i.e., tSreUC d e s i g n a t e s w h a t STRUC
normalises to (therefore t(+ z 3 ) ~
's).
Thus:
(LAMBDA SIMPLE IX] X) designates a function,
' (LAMaDA S I MPLE [ X ] X) d e s i g n a t e s a pair or redex, a n d
t(LAMODA SIMPLE [xJ x) designates a closure.
(Note t h a t ' t ' is call-by-value b u t not declaratively extensional.)
Similarly, ~sTeuc designates the designation of the designation
of STROC, providing the designation of STRUC is in normal-form
(therefore *'2 ==* z). ~,*STRUC is always equivalent to SrRoc, in
terms of both designation a n d result; so is t~.srRvC when it is
defined. T h u s if 00URLE is bound to (the result of normalising)
(I^MBO^ IX] (* x x)), then (BODY OOURLE) generates an error,
since BODY is extensional and DOUBLE d e s i g n a t e s a function, b u t
(RODe tDOUrJLE) will designate the pair (+ x x).

Type

Designq/ion

Norm,d Canonical

Notation

Numerals
Booleans
Handles
Closures
Rails
Atoms
Pairs

Numbers
Truth-Values
Structures
Functions
Sequences
(,~ of Binding)
(ValueofApp.)

Yes
Yes
Yes
Yes
Some
No
No

digits
ST or SF
' STRUC
(closure}
[STRUC... srRv~
alphamerics
(STRUC. STRUC

Yes
Yes
Yes
No
No
--
--

--
--
--
CC0NS
RC0NS
AC0NS
PCONS

Table 1: The 2-LISP(and 3-LISP) Categories

===~

~

..o

Figure 12: Meta-Circtdar Processors

.!

(NORgAL[SE '(CAR ' ( A . B ) ) )
(NORNALISE (PCONS '= ' [ 2 3 ] ) )
(REDUCE 'IST '[~10 20 3 0 ] )

~
=~
=*,

''A
'$1 r
'10.
More generally, the basic idea is t h a t ~(NOIIMALISE) • ~, tO be

contrasted with o(~,), which is approximately o, except t h a t
because ,t is a partial function we have @(~, o NORHALISE) = ~.
Given these equations, t h e behaviour illustrated in t h e
foregoing
examples
is
forced
by
general
semantical
considerations.
In a n y computational formalism able to model its own
syntox a n d ~structures, 6 it is possible to construct w h a t a r e
commonly k n o w n as metacircular interpreters, which we call
,lelacireular processors (or MCPs) ~ " m e t a " because t h e y
operate on (and therefore t e r m s within t h e m designate) other
formal structures, ~nd "circular" because they do not constitute
a definition of t h e processor. They are circular for two reasons.
First, they have to he r u n by t h a t processor in order to yield
a n y sort of behaviour (since they are programs, not processors,
strictly). Second, t h e behaviour they would thereby e n g e n d e r
can be known only if one knows beforehand w h a t the processor
does. (Standard techniques of fixed points, f u r t h e r m o r e , are of
no help in discharging this circularity, because this kind of
modelling is a kind of ~ l f - m e n t i o n , w h e r e a s reeursive
definitions are more ~ l f - u s e . ) Nonetheless, such processors are
pedagogically illuminating, and play a critical role in t h e
development of procedural reflection.
T h e role of MCPs is illustrated in Figure 12, s h o w i n g how,
if we ever replace P in Figure 1 with a process t h a t results from
P processing t h e metacircular processor MCP, it would ~till
correctly e n g e n d e r the behaviour of a n y overall program.
T a k i n g processes to be functions from s t r u c t u r e s onto b e h a v i o u r
(whatever behaviour is - - ['unctions from initial to final states,
say), a n d calling the primitive processor P, we should be able to
prove that. P(MCP) = P, where by '=" we m e a n behaviourally
equivalent in some appropriate sense. T h e equivalence is, of
course, a global equivalence; by and large t h e primitive
processor a n d t h e processor r e s u l t i n g from t h e explicit r u n n i n g
of the MCP c a n n o t be arbitrarily mixed. If a variable is bound
by the underlying processor P, it will not be able to be looked up
by t h e metacircular code, for example,
Similarly, if t h e
metacircular processor encounters :: control-structure primitive,
such a s a Till'tOW or a 0nil, it wid not cause the m e t a c i r c u l a r
processor itself to exit p r e m a t u r e l y , o t t o t e r m i n a t e . T h e point,
rather, is t h a t if a n entire computation is run by the process
t h a t r e s u l t s from t h e explicit prece.~qing of the MCP by P, t h e
results will be tbe s a m e (modulo time) as i f t h a t entire
computation had been carried out directly by P. MCPs a r e not
causally connected with the s y s t e m s they model.
The reason t h a t we cannot mix code for the u n d e r l y i n g
processor and cede for the MCI ) and the r e a ~ a t h a t we ignored
context a r g u m e n t s in the definitions above both h a v e to do with
the s t a t e of the processor P, In very simple s y s t e m s (unordered
rewrite rule systems, for example, and h a r d w a r e architectures
).hat p u t even t h e p r o g r a m counter into a m e m o r y location), the
processor h a s no internal state, in the sense t h a t it is in a n
identical configuration at every "click point" d u r i n g the r u n n i n g
of a program (i.e., all information is recorded explicitly in t h e

structural field). B u t in more complex circumstances, there is
always a certain a m o u n t of s t a t e t~) the processor t h a t affects its
behaviour with respect to a n y particular embedded f r a g m e n t of
code. In w r i t i n g an MCP one m u s t demonstrate, more or less
explicitly, how the proce.~qor s t a t e affects the processing of
object-level structures. By "more or less explicitly" we m e a n
t h a t the designer of the MCP h a s options: the state can be
represented in explicit s t r u c t u r e s t h a t are passed around as
a r g u m e n t s within the processor, or it can be absorbed into the
state of the processor r u n n i n g the MCP. (I will say t h a t a
property or feature of an object l a n g u a g e is obsorbed in a
m e t a l a n g u a g e or theory ju:;t in case t h e m c t a t b e o r y u s e s t h e
very s a m e property to explain or describe the property of t h e
object language.
T h u s conjunction is absorbed in s t a n d a r d
model theories of first-order logics, because the s e m a n t i c s of
p A 0 is explained simply by conjoining t h e explanation of P and
0 - - specifically, in such a fornmla as: 'P A 0' is true j u s t in
case 'P' is true a n d '0' is true.)
The state of a processor for a recursively-embedded
functional language, of which Lisp is a n example, is typically
represented in a n e n v i r o n m e n t a n d a continuation, both in
MCPs and in the s t a n d a r d metatheoretic accounts. (Note t h a t
these are notions t h a t arise in the theory of Lisp, net in Lisp
itself; except in self-referential or self-modelling dialects, user
programs don't traffic in s u c h entities.) Most MCPs m a k e the
e n v i r o n m e n t explicit. T h e control port of the state, Imwever,
encoded in a continuation, m u s t also be m a d e explicit in order
to explain non-standard control operations, b u t in m a n y MCPs
(such as in [McCarthy 1965] and Steele a n d S u s s m a n ' s versions
for Scheme (see for example [ S u s s m a n a n d Steele 1978b}), it is
absorbed. Two versions of the 2-Lisp metacircular processor, one
absorbing and one m a k i n g explicit the c o n t i n u a t i o n structure,
are presented in Figures 13 a n d 14. Note, however, t h a t in both
cases the u n d e r l y i n g agency or a # i m a is not reified; it r e m a i n s
entirely absorbed by t h e processor of t h e MCP. We h a v e no
m e c h a n i s m to designate a process (as opposed to structures),
and no method of obtaining causal access to an i n d e p e n d e n t
locus of active agency (the reason, of course, being t h a t we have
no theory of w h a t a process is).

## 7. Procedural Reflection and 3-Lisp

Given the met~tcircular processors defined above, 3-I,isp can
be non-cffectively defined in a series of steps. First, i m a g i n e a
dialect of 2-[,isp, called 2-l,isp/1, where u s e r progr'xms were not
r u n directly by the primitive processor, b u t by t h a t p r o c e s ~ r
r u n n i n g a copy of an MCP. Next, imagine 2-Lisp/2, in which the
MCP in t u r n was not r u n by t h e primitive processor, b u t w a s
r u n by the primitive processor r u n n i n g a n o t h e r copy of the MCP.
Etc. 3-Lisp is essentially 2-Lisp/Do, except t h a t the MCP is
changed in a critical way in order to provide the proper
connection between levels. 3-Li..,p. in e t h e r words, is w h a t we
call a reflective lower, defined ad an infinite n u m b e r of Ct)l)ies of
a n MCP-like program, r u n at t h e "top" by a n (infinitely fleet)
processor. The claim t h a t 3-Lisp is well-founded is the claim
t h a t the limit exists, as n-.oo, of 2-Lisp/n.
We will look a t the revised MCP presently, b u t some
general properties of this tower architecture c a n he pointed out
first. A rough idea of the levels of processing is given in F i g u r e
15: at each level the processor code is processed by a n active
process t h a t interacts with it (locally and serially, as usual), b u t
each processor is in t u r n composed of a s t r u c t u r a l field f r a g m e n t
in t u r n processed by a reflective processor on top of it. T h e
implied infinite regress is not problematic, a n d t h e architecture
can be efficiently realised, since only a finite a m o u n t of
information is encoded in all b u t a finite n u m b e r of the bottom
levels,
There are two ways to t h i n k about reflection. On the one
hand, one can t h i n k of there being a primitive a n d noticeable
reflective act, which causes the i)rocessor to shilZ levels r a t h e r
markedly (this is the explanation t h a t best coheres with some of
our pre-theoretic intuitions about reflective t h i n k i n g in the
sense of contemplation). On the other hand, t h e explanation

(define READ-NORHALISE-PRINT
(lambda simple [env stream]
(block (prompt&reply (normalise (prompt&road stream) env)
stream)
(road-normalise-prlnt one stream))))
(define NORMALISE
(lambda simple [str'uc e.v]
(rend [(normal struc) struc]
[(atom sLruc) (binding sLruc env)]
[ ( r a i l struc) (normaltse-rail struc env)]
[ ( p a i r struc) (reduce ( c a r s t r u c ) ( c d r s t r u c ) e n v ) ] ) ) )
define REOUCE
(lambda slmple [proc args env]
( l e t [[proc! (normalise proc env)]]
(selectq (procedure-type procl)
[simple ( l e t [[args! (eormaltse args env)]]
( i f (primitive procl)
(reduce-primitive-simple
proc! argsl env)
(expand-closure procl a r g s l ) ) ) ]
[intensional ( i f (primitive proc!)
(reduce-primtttve-lntenslonal
proc! targs any)
(expand-closure procl targs))]
[macro (normalise (expand-closure procl targs)
env))]))))
(define NORMALISE°RAIL
(lambda simple [ r a i l env]
( I f (empty r a i l )
(rears)
(prep (normalise ( l s t r a i l ) env)
(normaiise-ratl (rest r a i l ) onv)))))
define EXPAND-CLOSURE
(lambda simple [proc! argsl]
(normalise (body, procl)
(bind (pattern procl)
argsi
(environment p r o c l ) ) ) )

Figure 13:ANon-C(mtinuation-Passblg 2-LISPMCP

given in the previous paragraph leads one to think of an infinite
number of levels of reflective processors, each implementing the
one below. 7 On such a view it is not coherent either to ask at
which level the tower is running, or to ask how many retlective
levels are running: in some sense they are all r u n n i n g at once.
Exactly the same situation obtains when you use an editor
implement, ed in APL. It is not as if the editor and the APL
interpreter are both running together, either side-by-side or
independently; rather, the one, being interior to the other,
SUl)plies the anima or agency of /.he outer one. To put this
another way, when you implement one process in another
process, you might w a n t to say t h a t you have two different
processes, but you don't have concurrency; it is more a
part/whole kind of relation. It is just this sense in which the
higher levels in our rcllective hierarchy are always running:
each of them is in some sense within the processor at the level
below, so that it can thereby engender it. We will not take a
principled view on which account - - a single locus of agency
stepping between levels, or an infinite hierarchy of
simultaneous processors - - is correct, since they t u r n out to be
behaviourally equivalent. (The simultaneous infinite tower of
levels is often the better way to understand processes, whereas
a shi|!,ing-level viewpoint is sometimes the better way to
understand programs.)
3-Lisp, as we said, is an infinite reflective tower based on
2-Lisp. The cede at each level is like; the continuation-passing 2-
Lisp MCP of Figure 14, but extended to provide a mechanism
whereby the user's program can gain access to fully articulated
descriptions of that program's operations and structures (thus
extended, and located in a reflective tower, we call this code the
3-Lisp reflective processor). One gains this access by using what
are called reflective prncedures ~
procedures that, when
invoked, arc run not at the level at which the invocation
occurred, but one level higher, at the level of the reflective
processor r u n n i n g the program, given as a r g u m e n t s those
structures being passed around in the reflective processor.

define READ-NORNALISE-PRINT
(lambda simple lone stream]
(normailse (prompt&read stream) oily
(lambda simple [ r e s u l t ]
(block (prompt&reply result stream)
(read-normalise-print env stream))))))
(define NORHALISE
(lambda simple [strc one cent]
(rend [(normal struc) (cent s t r c ) ]
[(atom sire) (cent (binding strc env))]
[ ( r a i l strc) (normaltse-rail strut env cont)]
[ ( p a i r strc)(reduce ( c a r s t r c ) ( c d c s t r c ) e n v c o n t ) ] ) }
(define REDUCE
(lambda simple [proc args env coat]
(normalise proc env
(lambda slmpte [proc!]
(selectq (procedure-type procl)
[simple
(normaltse args any
(lambda simple [args!]
( i f (primitive procl)
(redece-primtttve-stmple
pratt args! env cent)
(expand-closure proc! args! c o s t ) ) ) ) ]
[intensional
( i f (primitive procl)
(reduce-primitive-intenslonal
proc! targs env cent)
(expand-closure procl ~args cont))]
[macro (expand-closure pros! targs
(lambda simple [ r e s u l t ]
(normallse result any c o n t ) ) ) ] ) ) ) ) ) )
(define NORMALISE-RAIL
(lambda simple [ r a i l env cent]
( i f (empty r a i l )
(cent (rcons))
(normalise ( l s t r a i l ) env
(lambda simple [ f t r s t l ]
(normalise-rall (rest rat1) env
(iambda simple [ r e s t ! ]
(cent (prep f i r s t ! r e s t ! ) ) ) ) ) ) ) ) )
define EXPAND-CLOSURE
(lambda simple [proc! ergs! cent]
(normalise (body procl)
(bind (pattern proc!) args! (one procI))
cent)))

Figure 14: A Continaation-Passing 2-LISP MCP

Reflective procedures are essentially analogues of subroutines b
be run "in tile implementation", except that they are in the
same dialect as that being implemented, and can use all the
power o(' the implemented language in carrying out their
function (e.g., reflective procedures can themselves use reflective
procedures, without limit). There is not a tower of different
languages - - there is a single dialect (3-Lisp) all the way up.

L ve,,co
l''l . J

Figure 15: The 3-LISP Reflective Tower

Rather, there is a tower of processors, necessary because there
is different processor state at each reflective level.
Some simple examples will illustrate.
Reflective
procedures are "defined" (in the sense we described earlier)

using the form (LAMBOA REFLECT ARGS BODY), where ARG$
typically the rail fAnGS ENV coNr] - - is a pattern that should

match a 3-element designator of, respectively, the argument
structure at the point of call, the enviromnent, and the
continuation.
Some simple examples are given in the
"Programming in 3-Lisp" overview in Figure 16, including a
working definition of Scheme's CATCH. Though simple, these
definitions would be impossible in a traditional language, since
they make crucial access to the full processor state at point of
call. Note also that although Tlm0w and CMC, deal explicitly
with continuations, the code that uses them need k n o w nothing
about such subtleties. More complex routines, such as utilities
to abort or redefine calls already in process, are almost ns
simple. In addition, the reflection mechanism is so powerful
that m a n y traditional primitives can be defined; C^MBOA, IF, and
QUOTE are all non-primitive (user) definitions in 3-Lisp, again
illustrated in the insert. There is also a simplistic break
package, to illustrate the use of the reflective machinery for
debugging purposes.
It is noteworthy that no reflective
procedures need be primitive; even LAHBDA can bc built up from
scratch.
The importance of these examples comes from the fact that
they are causally connected in the right way, and will therefore

For illustration, we will look at a handful of simple 3-Lisp
programs. The first merely coils thc Continuation with the
numeral 3; thus it is semantically identical to the simple
numeral:

(define THREE
(lambda reflect [[1 env cent]
(cent '3)))

Thus (three) ~ 3; (+ It (three)) ~ 14. The next example is a n
intensional predicate, true if and only if its a r g u m e n t (which
must be a variable) is hound in the current context:

(define BOUND
(lambda rerlect [ [ v a r ] one cent]
( t f (bound-in-env ear one)
(cent 'ST)
(cent 'Of))))

or equivalently

(define SOUND
(lambda reflect [[var] env cent]
(cent t(bound-in-env vat envl}))
Thus (LET [[X 31] (BOUND X)) ~ St, whereas (Donne x) ~ SF in

the global context. The following quits the computation, by
discarding the continuation and simply "returning":

(define QUIT
(lambda r e f l e c t [ [ ] env cont]
'QUIT!))

There are a variety of ways to implement a TtlROW/CATCH p a i r ;
the following defines the version used in Scheme:

(define SCHEME-CATCH
(lambda r e f l e c t [[tag body] catch-ear catch-cent]
(normalise body
(bind tag
t(lambda r e f l e c t [[answer] throw-env throw-cent]
(normal tso answer throw-ear catch-cent))
catch-earl
catch-cent)))
For example:
( l e t [ix 111
(+ 2 (scheme-catch punt
(* 3 ( / 4 ( i f ( : x I)
(punt 15)
(- x l ) ) ) ) ) ) )

would designate seventeen and return the numeral 17.
In addition, the reflection mechanism is so powerful that
many traditional primitives can be defined; LN4BDA, If, and QUOTE

run in the system in which they defined, rather than being
models of another system. And, since reflective procedures are
fully integrated into the system design (their n a m e s are not
treated as special keywords), they can he passed around in the
normal higher-order way. There is also a sense in which 3-Lisp
is simpler than 2-I,isp, as well as being more powerful; there
are fewer primitives, and 3-[,isp provides much more compact
ways of dealing with a variety of intensional issues (like
macros).

## 8. The 3-Lisp Reflective Processor

3-Lisp can be understood only with a close inspection of the
3-l,isp reflective processor (Figure 17). the promised modification
of the continuation-passing 2-Lisp met~lcircular processor
mentioned above.
NOnMALISE (line 7) takes an structure,
cnviromnent, and c o n t i n u a t i o n , returning the structure
unchanged (i.e., sending it to the continuation) if it is in normal
lbrm, looking up the binding if it in an atom, normalising the
elements i f it is a rail (NORMALISE-RAIL is 3-I,isp's tail-recursive
continuation-passing analogue of Lisp 1.5's EVilS). and otherwise
reducing the CAR (procedure) with the CDIt (arguments). REOUCE
(line 13) first aormalises the procedure, with a continuation (C-
I'ROC!) that checks to see whether it is reflective (by convention,
we use exclamation point suffixes on atom n a m e s used as
variables to designate normal form structures). If it is not
rellcctive, C.PltOC~ normalises the arguments,
with a
continuation that either expands the closure (lines 23-25) if the

Figure 16: Programming in 3-Lisp:

are all non-primitive (user) definitions in 3-Lisp, with the
following definitions:

(define LNdBDA
(lambda r e f l e c t [[kind pattern body] env cent]
(cent (coons kind tony pattern body))))
(define I f
(lambda rerlect [[promise then else] env cent]
(normal tse premise env
(lambda stmple [preml:ol]
(normalise (or 4premtse! then else) env c e n t ) l ) ) )
(define QUOTE
(lambda r e f l e c t [[arg] nay cent] (cent targ)))
Some comments. First., the definition of tA..OA just given is of

course circular; a non-circular but effective version is given in
Smith and des Rivi&res [1984]; the one given in the text, if
executed in 3-Lisp, would leave the definition unchanged, except
that it is an innocent lie; in real 3-Lisp kind is a procedure t h a t
is called with the arguments and environment, allowing the
definition of (lambda macro . . . ), etc.
COONS is a closure
constructor that uses SIMPLE and nEFLECT to tag the closures for
recognition by the reflective processor described in section 6. ZF
is an extensional conditional, t h a t normalises all of its
arguments: the definition of IF defines the standard intensional
version that normalises only one of the second two, depending
on the result of normalising the first. Finally, the definition of
QUOTE will yield (QUOTE A) ~ 'A.
Finally, we have a trivial break package, with ENV and
C0Nr bound in the break environment for the user to see, and
nFivnn bound to a procedure that will normalise its a r g u m e n t
and pass that out as the result of the call to SNEAK:

(define BREAK
(lambda r e f l e c t [ [ a r g ] env cent]
Iblock (print arg primary-stream)
(read-normallse-prlnt ">>"
(bind' ['env tenv]
['cent t r e n t ]
[ ' r e t u r n t(lambda r e f l e c t [ [ a 2 ] 02 c2]
(normaltse a2 e2 cent))]
env)

pr Imary-stream) ) ) )
If viewed 'as models of control constructs in a language being
iinplemented, these definitions will look innocuous; what is
important to remember is that they work in the very language
in which they are defined.

i

l

..... ( d e f i n e

READ-NOnMALISE-PRINT

2 ........... (lambda simple [ l e v e l say stream]
3 ................. ( n o ~ m i i s e (prompt&read level stream) env
4 ....................... (lambda simple [ r e s u l t ]
;ContinuationCRElq,Y
5 ............................ (block (prompt&reply r e s u l t level stream)
6 ...............................................
( r e a d - n o r m a l t s e - p r t n t l e v e l env s ~ r e a m ) ) ) ) ) )

7 ..... ( d e f i n e NORMALISE
8 ........... (lambda simple [ s t r u c env coat]

9 ................. (cond [(normal struc) (cent s t r u c ) ]
IO ............................ [(atom s t r u c ) (cent (binding struc e n v ) ) ]
II ............................ [ ( r a i l s t r u c ) ( n o r m a l i s e - r s l l struc env c o n t ) ]
12 ............................ [ ( p a i r s t r u c ) (reduce (car s t r u t ) (cdr s t r u c ) env c e n t ) i ) ) )
13 ..... ( d e f i n e REDUCE

14 ........... (lambda s i m p l e [ p r o c args e a r c o a t ]
15 ................. ( n o r m s l l s e proc env

26 ..... ( d e f i n e NORMALISE-RAIL
27 ........... (lambda stmple t r a i l env coat]
28 ................. ( t f (empty r a i l )
29 ..........................
(COOt (teens))
30 ..........................
(normeltso ( l e t rat1) env
31 ................................ (lsmbds simple [ f l r s t l ]

;ContinuatlonC-FIRST!
32 ....................................... (normsltso-rail ( r e s t r a i l ) e a r
33 .............................................. (lambde simple [ r e s t ] ]
;Continuation C-RESTI
34 .................................................... (cent (prep f i r s t ] r e s t l ) ) ) ) ) ) ) ) )

Figure 17: The 3-Lisp Refleclive Processor:

procedure is non-primit, ve, or else directly executing it if it is
primitive (line 22).
Consider (REOUCE '+ ' i x 3] ENV IO), for example, where x is
be, end to t h e n u m e r a l z and + to the primitive addition closure
in [NV. A t t h e point of line 22, PaOC! will d e s i g n a t e t h a t
primitive closure, and ARG$! will designate t h e normal-form rail
[z 3]. Since addition is primitive, we m u s t simply do the

ARGS!) won't

PROC! a n d

AflGSl

addition.

(Peoc!.

work,

because

are a t the wrong level; they designate structures, not functions
or a r g u m e n t s . So, for a brief m o m e n t , we de-reference t h e m
(with ~), do the addition, and t h e n r e g a i n our m e t a - s t r u c t u r a l
viewpoint with t h e ,.8 If the procedure is reflective, however, it
is (as s h o w n in line 18 of Figure 17) called directly, not
processed, and given the obvious t h r e e a r g u m e n t s (AnGS, [W,
and CONI) t h a t are being passed around.
T h e ¢(o[-nrFLECT
PROC:) is merely a m e c h a n i s m to purify the reflective procedure
so t h a t it doesn't reflect again, a n d to de-reference it to be a t
the r i g h t level (we w a n t to use, not mention, the procedure t h a t
is designated by PROCO. Note t h a t line 18 is the only place t h a t
reflective procedures c a n ever be called; this is why they m u s t
always be prepared to accept exactly those three a r g u m e n t s .
Line 18 is t h e essence of 3-Lisp; it alone engenders t h e full
reflective tower, for it says t h a t some parts of t h e object
language - - the code processed by this p r o g r a m - - are called
d~rectly in this program. It is as if a n object level f r a g m e n t
were included directly in the meta language, which raises t h e
question of who is processing the m e t a language. T h e 3-Lisp
claim is t h a t a n exactly equivalent reflective processor can be
processing this code, w i t h o u t vicious t h r e a t of infinite ascent.

A reflective procedurc,.in s u m , arrives in the middle of t h e
processor context. It is handed e n v i r o n m e n t a n d continuation
structure t h a t designat~ t h e processing of t h e code below it, b u t
it is r u n in a different context, with its own (implicit)
e n v i r o n m e n t and continuation, which in t u r n is represented in
s t r u c t u r e s passed around by t h e processor one level above it.
Thu~ it is given causal access to the s t a t e of t h e process t h a t
was in progress (answering one of our initial requirements), a n d
it can of course cause a n y effect it wants, since it h a s complete

16 ........................ (lsmbda simple [ p r o c l ]
;ContinuationC-PROC!
[7 .............................. ( t r ( r e f l e c t i v e procl)
18 ....................................... (4(de-reflect procl) ar~s env cont~
19 ...................................... (normaltse args e n v
20 .............................................. (lambde simple [ a r g s l ]
;Continuation C-ARGS!
21 ................................................. ( I f (prhntttvo proci)
22 .......................................................... (cent *lCprocl . $argsl)}
23 .......................................................... (normsltse Ibody procl)
24 .................................................................................. (bind (pattern proc!) args! (environment proc!)
2S .................................................................................. c o a t ) ) ) ) ) ) ) ) )

access to all future processing ot t h a t code. F u r t h e r m o r e , it h a s
a safe place to stand, where it will not conflict with the code
being r u n below it.
These various protocols illustrate a general point.
As
mentioned at the outset, part of d e s i g n i n g an a d e q u a t e
reflective architecture involves a trade-off between being so
connected t h a t one steps all over oneself (as in traditional
i m p l e m e n t a t i o n s of d e b u g g i n g utilities), and so disconnected (as
with metacircular processors) t h a t one h a s no effective access to
what is going on. T h e 3-Lisp tower, we are suggesting, provides
j u s t the r i g h t balance between these two extremes, solving t h e
problem of v a n t a g e point as well as of causal connection.
The 3-Lisp reflective processor unifies three traditionally
independent capabilities in Lisp: t h e explicit availability of EVAL
and APPLY, the ability to support metacircular processors, a n d
explicit operations (like Maclisp's RETFUN ~nd Interlisp's FRETURN)
for debugging purposes. It is striking t h a t the latter facilities
are required in traditional dialects, in spite of t h e presence of
the former, especially since they depend crucially on
implementation details, violating portability and other n a t u r a l
aesthetics. In 3-Lisp, in contrast, all information a b o u t t h e
state of the processor is fully available within the l a n g u a g e .

## 9. The Threat of Infinity, and a Finite Implementation

The a r g u m e n t as to why 3-Lisp is finite is complex in
detail, b u t simple in outline and in substance. Basically, one
shows t h a t t h e reflective processor is fully tail-recursive, in two
senses: a) it r u n s p r o g r a m s tail-recursively, in t h a t it does not
build up records of s t a t e for programs across procedure calls
(only on a r g u m e n t passing), and b) it itself is fully tail-
recursive, in t h e sense t h a t all recursive calls within it (except
for u n i m p o r t a n t subroutines) occur in tail-recursive position.
The reflective processor, can be executed by a simple finite s t a t e
machine. In particular, it can r u n itself without u s i n g a n y s t a t e
at all. Once t h e limiting behaviour of a n infinite tower of
copies of this processor is determined, therefore, t h a t entire
chain of processors can be simulated by a n o t h e r s t a t e m a c h i n e ,
of complexity only moderately greater t h a n t h a t of the reflective
processor itself. (It is an interesting open research question

whether that "implementing" processor can be algorithmically
derived from the reflective processor code.) A full copy of such
an implementing processor - - about 50 lines of 2-Lisp - - is
provided in {Smith and des Rivi~res 1984J" a more substantive
discussion of tractability will appear in [Smith forthcoming].

## 10. Conclusions and Morals

Fundamentally, the use of Lisp as a language in which to
explore semantics and reflection is of no great consequence; the
ideas shouhi hold in any similar circumstance. We chose Lisp
because it is familiar, because it has rudimentary self-
referential capabilities, and because there is a standard
procedural
self-theory
(continuation-passing
metacircular
"interpreters").
Work h a s begun, however, on designing
reflective dialects of a side-effect-free Lisp and of Prolog, and on
studying a reflective version of the X-calculus (the last being an
obvious candidate for a mathematical study of reflection).
Furthermore, the technique we used in defining 3-Lisp can
be generalised r a t h e r directly to these other languages. In
order to construct a reflective dialect one needs a) to formulate
a theory of the language analogous to the metacircular
processor descriptions we have examined, b) to embed this
theory within the language, and c ) t o connect the theory with
the underlying language in a causally connected way, as we did
in line 18 of the reflective processor, by providing reflective
procedures invoeable in the object language but run in the
processor. It remains, of course, to implement the resulting
infinite tower; a discussion of general techniques is presented in
[desRivi~res, forthcoming].
It is partly a consequence of using Lisp that we have used
non-data-abstracted
representations
of
functions
and
environments; this facilitates side-effects to processor structures
without introducing unfamiliar machinery.
It is clear t h a t
enviromnenta could be readily abstracted, although it would
remain open to decide w h a t modifying operations would be
supported (changing bindings is one, but one m i g h t wish to
excise bindings completely, splice new ones in, etc.).
In
standard X-calculus-based metatheory there are no side effects
(and no notion of processing); environment designators m u s t
therefore be passed around ("threaded") in order to model
environment side effects. It should be simple to define a side-
effect-free version of 3-Lisp with an environment-threading
reflective processor, and then to define s~rQ and other such
routines as reflective procedures. Similarly, we assume in 3-
Lisp t h a t the main structural field is simply visible from all
code; one could define an alternative dialect in which the field,
too, was threaded through the processor as an explicit
argument, as in standard metatheory.
The representation of procedures as closm'es is troublesome
(indeed, closures are failures, in the sense that they encode far
more information than would be required to identify a function
in intension; the problem being t h a t we don't yet know w h a t a
function in intension might be.). 3-Lisp unarguably provides far
too fine-grained (i.e., metastructural) access to function
designators, including continuations, and the like. Given a n
abstract notion of procedure, it would be n a t u r a l to define a
reflective dialect t h a t used abstract structures to encode
procedures, and then to define reflective access in such terms.
We did not follow this direction here only to avoid taking on
another very difficult problem, b u t we will move in this
direction in future work.
These considerations all illustrate a general point: in
designing a reflective processor, one can choose to bring into
v i e w more or less of the state of the underlying process. It is
all a question of what you w a n t to make explicit, and w h a t you
want to absorb.
3-Lisp, as currently defined, reifies the
environment and continuation, m a k i n g explicit w h a t was
implicit one level below. It absorbs the structural field (and
lmrtly absorbs the global enviromnent); as mentioned earlier, it
completely absorbs the animating agency of the whole
computation. If one defines a reflective procSssor based on a
metacircular processor that al.~o absorbs the representation of

control (i.e., like the MCP in Figure 13, which uses the control
structure of the processor to encode the control structure of the
code being processed), then reflective procedures couhl not affect
the control structure, In any real application, it would need to
be determined j u s t w h a t parts of the underlying dialect required
reification. One could perhaps provide a dialect in which a
reflective procedure could specify, with respect to a very general
theory, what aspects it wanted to get explicit access to. Then
operations, for example, that needed only environment access,
like 9ouNo, could avoid having to traffic in continuations.
A final point. I have talked throughout about semantics,
but have presented no mathematical semantical accounts of any
of these dialects.
To do so for 2-Lisp is relatively
straightforward (see Smith [forthcoming J), but I have not yet
worked out the appropriate semantical equations to describe 3-
Lisp.
It would be simple to model such equations on the
implementation mentioned in section 9, b u t to do so would be a
failure: rather, one should instead take the definition of 3-Lisp
in terms of the infinite virtual tower (i.e., take the limit of 2-
Lisp/n), and then prove that the implementation strategies of
section 9 are correct. This awaits further work. In addition, I
want to explore what it would be to deal explicitly, in the
semantical account, with the a n i m a or agency, and with the
questions of causal connection, that are so crucial to the success
of any reflective architecture. These various tasks will require
an even more radical reformulation of semantics t h a n h a s been
considered here.

## Acknowledgements

I have benefited greatly from the collaboration of J i m des
Rivi~res on these questions, particularly with regard to issues of
effective implementation. The research was conducted in the
Cognitive and Instructional Sciences Group at Xerox PARC, as
part of the Situated Language Program of Stanford's Center for
the Study of Language and Information.

## Notes

1. See ]Doyle 1980], ]Wcyrauch 1980], [Genesereth and Lenat 1980], and
{Batali 1983].
2. In the dialects we consider, the metastructural capability must be provided
by primitive quotation mechanisms, as opposed to merely by being able to
model or designate syntax - - something virtually any calculus can do,
using Godel numbering, for exomple - - for reasons of causal connection.
3. Most programming languages, such as Fortran and Algol 60, are neither
higher-order nor metastructura]; the ~,-calculus is the first but not the
second, whereas Lisp 1.5 is the second but not the first (dynamic .seeping is
n contextual protocol that, coupled with the mete-structural facilities,
partially allows Lisp 1.5 to compensate for the fact that it is only first-
order). At least soma incarnations of Scheme, on the other hand, are beth
(although Scheme's metastructural imwers are limited). As we will see, 2-
Lisp and 3-Lisp are very definitely both metastructural and higher-order.
4. For what we might call declarative languages, there is n natural account of
the relationship between linguistic expressions and in.the-world designations
that need not make crucial.reference to issues of processing (to which we
wiU turn in a moment). It is for such languages, in particular, that the
composition ~PoO, which we might call ep,, would be formulated. And this,
for obvious reasons, is what is typically studied in mathematical model
theory and logic, since those fields do not deal in any crucial way with the
active use of the languages they ~tudy. Thus, for example, 4J' in logic
would be the interpretation function of standard model theory. In what we
will call cnmpototionol languages, on the other hand, questions of
processing do arise.
5. The string '10tmTE Ae¢]' notates a structure that designates another
structure that in turn could be notated with the string "ABe'. The string
'"ABC"', on the other hand, notates a structure that designates the string
'ABe' directly.
6. Virtually any language, of course, has the requisite power to do this kind
of modelling. In a language with mete-structural ahilities, the mete-
circular processor can represent programs for the MCP as themsolsee - -
this is always done in Lisp MCPs - - but we need not define that to be an
essential property. The term 'metocircular processor" is by no means
strictly defined, and there arc various constraints that one might or might
not put on it. My general approach has been to view as metacircular any
non.causally connected model of a calculus within itself; thus the 3-Lisp
reflective processor is nut mete-circular, because it does have the requisite

caused connl,ction~,
and therelbrc an essential Imrt of the 3-Lisp
architecture.
7. Curiously, there are also intuition~ about conlemplative thinking, where
one is both detoched and yet directly present, that fit more with this view.
8. One way to undcr~tand thi~ is tn realize that the reflective processor simply
asks its processor to do any primiHves that it encounters. I.e., it passes
responsibility up to the processor running it.
In other words, each time
one level uses a primitive, its proceg~or runs around setting everything up,
finally re~whing the point at which it must simply do the primitive action,
whereup~n it asks its own processor for help. Bul of course the processor
runnin~ that processor will else come racing towards the edge of the same
cliff, and will similarly duck responsibility, handing the primitive up yet
anolher level. In fact every primitive ever ex,~cutcd is handed all the way
to the tap of the tower. There is a magic moment, when the thing actually
happ~ms, and then the answer filters all the way back down to the level
that stortt.d tile whole procedure. It is as if tile deus ex mrwhina, living at
the tap of the tower, sends a lightning bolt down to some level or other,
once every intervening level gets appropria~x~ly lined up (rather like the
sun, at the stonehenge and pyramids, reaching down through a long tunnel
at just one particular moment during the year). Except, of course, that
nothing ever h[Ippens, ultimately, except primitives. In other words tile
enabling agency, which must flow down from the top of the tower, consists
of an infinitely dense series of these lightning bolts, with something like
10% of the ones that reach each level being allowed through to the level
below.
All infinitely fast.

## References

Batali, J., "Computational Introspection",
Laboratory Memo AIM-TI{-701 (1983).

M.I.T.

Artificial

lntenigeneo

dt, sll.ivi~,r~,s, J. '"l'he Implenl~ntotlon of Procedurally Reflective Languages",
(forthcoming).
Doyk,, J., A Model [or I)elihr,rali~m, Action, and Introspection, M.I.T. Artificial
Intelligence L~boratory Memo AIMJI'R-581 (1980).
Fodor, J. "MethodologicM Solipsism Considered as a Research Stralegy in
Cognitive Psychology", The Beh~wiour~d end Brian Sciences, 3:1 (1980) pp.
63-73; reprinted in Fodor, J., Iteprcsent~ttlons, Cambridge: Bradford (1981).
Gmresereth, M., and l,cnat, D. I:|., "Self-Description end -Modification in a
Knowledge Representation I,anguage", |leuristic Programming Project
Report IIPI'-B0-10, Stanford University CS Dept., (1980),
McCarthy, J. at el,, Lh~P 1.5 Progrummcr'$ Munuul, Cambridge, Mass.: The
MIT PRess (1965).
Smith, B., Reflection and ,~emaltlics in a Prueetlural Language, M.I.T.
latboratory for Computer Science Report MIT-TR-272 (1982).
Smith, B. and desRivi~'res, J. "Interim 3-LISP Reference Manual ~, Xerox
PARC Report CIS-nn, Pale Alto (1984. forthcoming).
Steele, G., "I,AMI|DA: q'i~e Ultimate Declaralive", M.I.T. Artificial Intelligence
Laboratory Memo AIM.a79 (1976).
Steele, G., and Sussman, G. "The Revised Report an SCHEME, a Dialect of
IJSI >'', M.I.'I ~. Artificial Intelligence Imboratory Memo AIM-452, (1978a).
Steele, G., and Sussman, G. "The Art of the Interpreter, or, The Modularity
Complex (Parts Zero, One, and Two)", M.I.T. Artificial Intelligence
Imboratory Memo AIM-.153, (1978b).
Wcyhrauch, R. W., "Prolegomena to a Theory of Mechanized Formal
Reasoning", Artificial I~:lrlligem'e 13:1,2 (1980) pp. 133-170.
