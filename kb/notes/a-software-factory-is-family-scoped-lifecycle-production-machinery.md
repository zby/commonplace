---
description: "Use this synthesis to recover Greenfield's versioned schema-template-factory ontology and distinguish constructing production machinery from acquiring its family specialization."
type: kb/types/note.md
traits:
  - title-as-claim
  - has-comparison
  - has-external-sources
  - synthesis
---

# A software factory is family-scoped lifecycle production machinery

Here, *software factory* means the family-scoped arrangement in Greenfield's
2003 and mature 2007 accounts. In those accounts, human developers use a
specialized development and runtime environment to produce and sustain members
of a declared product family. The family production knowledge is distributed
across a schema, an installable template, processes, tools, and reusable
assets. Product-specific lifecycle artifacts are outputs of this machinery;
they are not the machinery itself.

The vocabulary is versioned. The [available 2004 book
preview](../sources/greenfield-short-software-factories-book-preview.ingest.md)
confirms the book's identity, contributors, and broad integration program, but
its publisher copy and partial contents cannot ground book-wide ontology claims.
The detailed reconstruction is therefore bounded to fuller retained sources.
`G03` says verbatim that “An IDE configured with a software template for a product family
becomes a factory for producing members of the family.” ([Greenfield and Short's
2003 account](../sources/greenfield-short-software-factories-oopsla-2003.ingest.md)).
It supplies the original `software schema`, `software template`, developer roles,
configured-IDE factory, and recursive construction account.
[Greenfield's 2007 account](../sources/greenfield-mass-customizing-software-factories-2007.ingest.md)
(`G07`) supplies the mature schema, template, lifecycle, two-process,
specialization, composition, and feedback-supported revision account. A [later Microsoft patent
execution model](../sources/us20090100406a1-software-factory-specification-execution-model.ingest.md)
(`PAT`) adds precise type/instance relations for views, work products, tasks,
and workstreams. Those relations refine the mature ontology; they are not
definitions retroactively attributed to `G03` or `G07`.

The stable relation across the changing vocabulary is a synthesis rather than
a quotation:

`declared product family and production knowledge -> factory development -> schema plus packaged assets -> configured environment -> creation and sustainment of one family member through lifecycle work products`

Each object in that relation has a different role.

## Versioned ontology

| Object | Family-production role | Product-level boundary |
|---|---|---|
| Product family | `G03` scopes a factory to members sharing modeled commonality and variability. `G07` describes products or solutions that vary in features and operational qualities. The declared scope, common parts, variation points, variants, and constraints delimit the admitted production space. | Family membership is not whatever a generator happens to emit. The retained sources do not supply a formal membership predicate, and ordinary member production does not infer the family boundary. |
| `software schema` (`G03`) | A graph of viewpoints for one family, with associated domain-specific languages, constraints, and transformations. It describes the specifications needed to produce a member. | It is one constituent of the 2003 software template, not an installed factory or one product specification. |
| `software factory schema` (`G07`) | A dynamic, family-specific architecture framework. Its viewpoints relate stakeholder concerns, relevant artifacts, activities acting on those artifacts, and assets supporting those activities. Relationships among viewpoints integrate architecture and lifecycle. | It is a richer, historically related ontology, not merely a new name for the 2003 schema. `Dynamic` does not mean learned or automatically revised. `G07` uses schema modification both when accommodating member variation and when specializing a base factory, so viewpoint change alone does not classify the operation. |
| Software template / software factory template | In `G03`, the schema, the processes for capturing and using its information, and automation tools collectively form a `software template`. In `G07`, a `software factory template` is a structured, installable package of customizable assets. | The schema organizes production knowledge; the template packages machinery for installation and customization. The evidence supports this functional separation, not an exact later containment rule for every asset. |
| Configured or operative factory | `G03` calls an IDE configured with the family template a software factory. `G07` calls it a specialized development and runtime environment supplying integrated special-purpose assets. *Operative factory* is the synthesis term for this installed producer. | It is not its schema, template, any single asset, a product work product, or the resulting family member. Human solution builders use it and it supplies lifecycle guidance, so it is not merely an autonomous code generator. |
| Viewpoint, concern, and view | In `G03`, viewpoints organize family specifications. In `G07`, a viewpoint covers concerns of stakeholder roles and groups relevant artifacts, activities, and assets. `PAT` later declares viewpoint types at schema level. | A concern is what matters to a stakeholder role; a viewpoint is its organizing frame. In `PAT`, a product-specific `view` instantiates a viewpoint type. This last type/instance distinction is later precision, not timeless Greenfield vocabulary. |
| Artifact and work product | `G07` uses `artifact` for items organized under viewpoints and for reusable partial or prototypical content. `PAT` later declares work-product types in the schema. | `PAT` represents product state as work-product instances organized through product views. A reusable prototype may be a factory asset; the product-specific work product created or changed with it is member state. `Artifact`, `work product`, and `asset` overlap but are not universal synonyms. |
| Activity, task, and workstream | `G07` associates activities with the artifacts they act on and the assets that support them. `PAT` later defines task and workstream templates at factory level. | `PAT` instantiates those templates as product-specific tasks and workstreams. Tasks consume or produce declared work-product types. This refines rather than renames `G07`'s activity concept, and the retained account is not a complete execution state machine. |
| Asset | `G03` distinguishes implementation assets from process assets. `G07` includes guidance, processes, content, tools, patterns, samples, templates, libraries, frameworks, models, configuration files, components, and partial lifecycle artifacts. | Assets carry or enact reusable family production knowledge, but they are not autonomous actors and need not be product state. Activities or tasks use them to create or modify member work. |
| Family member | `G03` says product-family member, `G07` often says solution, `PAT` says product, and product-line literature says application. | These names have an analogous role here, not guaranteed identical definitions: one product-specific result built within the family production system. |

## Family knowledge is distributed across the factory

No authorized source puts all production knowledge in one model. It is spread
across:

- the family scope, commonality, variability, variants, and constraints;
- the schema's viewpoints, concerns, relationships, languages, constraints,
  and transformations;
- processes, activities, task and workstream templates, and their expected
  inputs and outputs;
- tools, generators, frameworks, components, patterns, libraries,
  configuration files, and other implementation assets; and
- partial or prototypical requirements, architectures, tests, deployment
  topologies, maintenance plans, migration pathways, and other lifecycle
  content.

A [primary software-product-line account](../sources/framework-for-software-product-line-engineering.ingest.md)
(`SPL`) calls the analogous family-level collection a reusable platform and
includes requirements, reference architecture, components, tests, a
variability model, and traceability. It also separates domain engineering,
which defines the planned family and its platform, from application
engineering, which builds one member. These terms clarify the family/member
boundary; they are not substituted into Greenfield as if he used them.

A [primary generative-programming account](../sources/components-and-generative-programming.ingest.md)
(`GEN`) makes `configuration knowledge` explicit as the mapping from
problem-space requests to solution-space component configurations. Domain
engineering supplies that mapping, the feature model, architecture,
parameterized components, and generator. Application engineering may then use
an algorithm or search to configure a member. Search inside that supplied
space selects a product; it does not acquire or revise the space or mapping.

Model-driven development is one constituent technique, not a synonym for the
whole factory. `G03` defines its synthesis as a model-driven product line:
product-line engineering supplies the scoped family and reusable production
assets, models carry metadata used to automate development, and component-based
techniques realize configurable assemblies. `G07` later names four integrated
contributors: software product lines, model-driven development, guidance
automation, and architecture frameworks. The factory combines these under a
family-specific lifecycle organization; a model or transformation alone is not
the factory.

The schema is therefore the integration structure, the template is the
installable packaging, executable assets realize operations, and the
configured environment makes the arrangement operative. Changing one member's
work product and changing a reusable rule or asset for later members are
different-level changes even when both are called adaptation. Persistence and
reuse scope distinguish the levels; this is an inference from the two-process
division, not a formal rule supplied by the sources.

## Factory development and member development are different paths

The distinction is relative to a fixed reference factory. Product development
changes one of that factory's members; factory development changes that
factory's reusable production machinery. In a meta-factory, the same work may
be product development relative to producer A and factory development relative
to produced factory B. B is A's factory-valued product and a producer for its
own family. Whether B later succeeds some incumbent is a separate operative
relation.

| Aspect | Factory development | Family-member development |
|---|---|---|
| Actors | `G03` product-line developers, `G07` factory developers, and the comparable `SPL` domain-engineering role. | `G03` product developers, `G07` solution developers, the `PAT` development team, and the comparable `SPL` application-engineering role. These are role mappings, not exact terminological identities. |
| Starting inputs | Domain knowledge, intended family scope, commonality and variability, metamodels or languages, process knowledge, platform choices, and production expertise. | Requirements for one member plus an already supplied schema, template, configured environment, variability model, configuration rules, and assets. |
| Work | Define the family and viewpoints; create process, content, implementation, and tool assets; package them in a template; configure the production environment. | Select and bind anticipated variation; choose, parameterize, adapt, configure, complete, assemble, or generate product-specific material. In `PAT`, the environment instantiates product views, work products, tasks, and workstreams, and the work products collectively express product state. |
| Fixed and variable parts | Family scope, viewpoint structure, variability, processes, tools, and reusable assets can all vary while a factory is being developed or revised. | Those family commitments are fixed only relative to an ordinary member-development episode. The member varies within the admitted space. A reusable change for later members crosses back into factory development. |
| Output | A schema, packaged template and assets, and a configured development/runtime environment for a family. | One family member whose evolving product state is expressed through its lifecycle work products. The member may itself be a factory when the reference producer is a meta-factory. |
| Feedback | `G07` routes defects, feature requests, and unanticipated variation from solution developers to factory developers, who revise reusable assets. | Customers report on solutions to solution developers. A member-level discovery can motivate a factory change, but does not itself perform that change. |

The paths remain distinct relative to the same reference factory even when one
work episode has both roles across different factories. In particular, “fixed
during member development” does not mean immutable across factory versions.
Nor does feedback define a learning algorithm: the cited accounts leave people
to interpret reports and decide how reusable machinery changes.

## The product spans the lifecycle

The factory produces more than generated implementation code. It produces and
sustains a family member by creating and modifying the lifecycle work products
that express product state, including executable and deployed realizations
where applicable.

| Lifecycle area | Supplied machinery and resulting work | Evidence limit |
|---|---|---|
| Requirements and specification | Reusable or prototypical requirements, product requirements work, specification viewpoints, languages, constraints, and transformations. `PAT` also places product specification inside its supported environment. | The sources do not show automatic discovery of the right requirements. |
| Architecture and implementation | Logical and technical architectures, guidelines, patterns, samples, templates, libraries, frameworks, models, components, configuration files, editors, transformations, and generators support product architecture and implementation artifacts. | Generation is one possible activity inside the broader production arrangement. |
| Testing | Reusable test suites and domain test assets support tests of a configured member and any member-specific additions. | An inventory of tests does not establish comparative test effectiveness or product quality. |
| Deployment and operation | Deployment topologies, deployment support, runtime facilities, and operational assets extend the factory beyond compilation. | A supported phase or topology is not a complete deployment semantics, and runtime scope does not imply unattended operation. |
| Maintenance and migration | Solution developers maintain individual solutions. Maintenance plans and migration pathways can be reusable assets; `PAT` also includes maintenance in its supported lifecycle. | The sources do not give full change-propagation, compatibility, or versioning rules. A migration pathway is not evidence of an implemented migration engine or an automatic transition between factory versions. |

## Similar operations act at different levels

| Operation | Immediate target and actor | What changes, and what does not |
|---|---|---|
| Product configuration | A product or solution developer configures one member with the operative factory. | Anticipated features, qualities, parameters, selected variants, and product work products vary inside supplied family and configuration rules. The operation does not by itself revise those rules, the family schema, or reusable assets. |
| Product assembly or generation | Developers, tools, or generators materialize one selected configuration from components and other assets. | The concrete member and its lifecycle artifacts change relative to the producing factory. When that family admits factories, the product may itself be a producer; automation alone does not make it a successor. |
| Factory specialization | Factory developers add or remove viewpoints or modify artifacts, activities, and supporting assets in the reusable or base factory. | The reusable family-level production structure, and therefore the space or method of later products, changes. A product-local configured-schema variation remains member development. This is also not automatically identical to MDSoFa's generation of `specific expertise` from generic expertise. |
| Product composition | Portions produced using multiple factories contribute to one deliverable. | The product's make-up changes. The production definitions of the contributing factories do not thereby merge. |
| Factory composition | Viewpoints from constituent factories are combined into a larger production system, including arrangements that support multi-factory supply chains. | The factory's integrated production structure changes. This is not assembly of outputs into one product, and constituent integration may require more than product compatibility. |
| Feedback-supported versioned factory revision | Human factory developers revise reusable machinery in response to defects, requests, new practices or technology, and unanticipated variation. *Factory evolution* is our umbrella term for such change, not a named `G07` operation on the retained evidence. | Schema, template contents, processes, tools, or assets can change across versions. Feedback and version change alone are not learning, and not every revision is specialization or composition. |
| Recursive factory construction | A factory-supporting environment helps developers build another factory, or a computational process produces factory assets. | Relative to a meta-factory, the produced factory is a member; relative to itself, it is a producer with reusable machinery. Factory-valued output says nothing about who supplies its specialization, whether it succeeds an incumbent, or whether learning occurred. |

The sources identify these operations but do not provide a closed algebra of
factory change. The target and reuse scope of a change, not a shared verb such
as *configure*, *adapt*, or *compose*, determine which operation occurred.

## Factory construction is prior art; specialization acquisition is not established

`G03` already makes recursive construction explicit. Its example uses an IDE
to build languages, frameworks, and tools for building factories, packages
them as a template, and loads that template into another IDE to create a
factory-building factory. Its product can itself be another producer, but human
product-line developers still choose the family definition and design the
specialized templates and assets. This is producer-valued product recursion and
tool-assisted bootstrapping, not evidence-responsive acquisition of production
knowledge.

Cook and Kent give the book program's tool-level mechanism. Their language
designer is itself an instance of the generated designer architecture, and
they state verbatim: “This allows the tool factory to bootstrap itself from
one version to the next” ([their Tool Factory proposal](../sources/cook-kent-tool-factory-2003.ingest.md)).
The construction starts from a supplied language-family definition, fragments,
patterns, framework, and mappings into implementation technology. It can
therefore regenerate or bootstrap production tooling without acquiring the
family specialization that the tooling embodies.

MDSoFa makes factory construction more computational. Langlois and Exertier
state verbatim that “a model driven software factory can produce a model-driven factory” in [their MDSoFa account](../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md).
Their implemented process combines supplied metamodels and generic expertise,
selects QVT rules through pattern matching, and applies templates to produce
specific expertise and target assets. Human metamodel designers supply
metamodels, mappings, and aspects; software architects participate in
architectural choices; people also supply expertise, platform, packaging, and
strategy choices. It is therefore useful to understand the computation as
compiling supplied specialization. *Compilation* is a comparison label here,
not MDSoFa's claim that the system learns.

Together the sources establish four progressively automated arrangements:

1. human-designed machinery can help humans construct another factory
   (`G03`);
2. a generated tool chain can bootstrap its own designer class from supplied
   language definitions and implementation mappings (Cook and Kent);
3. a computational process can construct substantial factory assets from
   supplied metamodels and expertise (MDSoFa); and
4. an algorithm or search can configure and materialize a product inside a
   supplied family model (`GEN`).

`G07` and `SPL` also establish feedback between product work and family
engineering. In their accounts, people interpret that feedback and revise the
reusable machinery. None of the retained sources establishes the complete
transition:

`experience from produced members -> computationally determined reusable change -> evidence-governed operative retention -> later production under F_{t+1}`

Explicit candidate generation, reject-capable evaluation, selection, and
promotion are one implementation of that transition. A direct evidence-to-update
path need not expose competing candidates.

In particular, they do not establish computational acquisition or
evidence-responsive revision of a previously human-supplied family scope,
viewpoint decomposition, variability model, configuration knowledge, process,
or asset strategy. Generation, search, recursion, feedback, a dynamic schema,
specialization, and versioning can all occur while those commitments remain
human supplied. The prior-art boundary is therefore the location of acquisition
and revision, not whether computation produces an ordinary member or a
factory-valued member.

## Scope

- The unified ontology is a version-aware synthesis. The retained material
  contains no single canonical ontology spanning `G03`, `G07`, and `PAT`.
- The sources do not provide a formal family-membership predicate, a complete
  executable metamodel with cardinalities, a complete task state machine, or a
  closed algebra of specialization, composition, and versioned revision.
- Classifying a change by persistence and reuse scope is an inference from the
  two development paths. The exact boundary between adapting an asset copy for
  one member and changing a reusable factory asset is not formalized.
- Lifecycle inventories establish scope, reusable content, and partial
  automation. They do not establish end-to-end autonomy or measured gains in
  productivity, quality, predictability, or reuse.
- The feedback accounts are organizational and human-directed. They do not
  specify computational determination and operative retention of reusable
  change. Candidate generation, evaluation, and selection are also unspecified
  where that architecture would be used.
- MDSoFa establishes implemented construction from supplied knowledge, not
  acquisition or revision of that knowledge. Its artifact counts and platform
  coverage do not establish comparative performance or unrestricted
  applicability.
- Cook and Kent establish a proposed generated-designer architecture and
  conditional self-bootstrap, not a tested complete tool chain or acquisition
  of its language-family definition and implementation mappings.
- The negative prior-art finding is bounded to the retained sources. This note
  supplies a foundation and mismatch record; it does not define a closed
  learning loop, successor-factory relation, domain-extensibility, a universal
  factory, or autonomous learning.
