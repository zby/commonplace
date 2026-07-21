---
source: https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf
description: "Full-text capture of Weyns's six-wave engineering perspective on self-adaptive systems, including its conceptual model and future challenges."
captured: 2026-07-21
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Software Engineering of Self-Adaptive Systems: An Organised Tour and Future Challenges

Author: Danny Weyns
Source: https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf
Date: 2017 (Handbook of Software Engineering)

Software Engineering of Self-Adaptive Systems:
An Organised Tour and Future Challenges
## Danny Weyns
## Abstract
Modern  software  systems  are  expected  to  operate  under  uncertain
conditions, without interruption. Possible causes of uncertainties include
changes  in  the  operational  environment,  dynamics  in  the  availability  of
resources, and variations of user goals.  The aim of self-adaptation is to
let the system collect additional data about the uncertainties during op-
eration.  The system uses the additional data to resolve uncertainties, to
reason about itself, and based on its goals to reconfigure or adjust itself
to satisfy the changing conditions, or if necessary to degrade gracefully.
In this chapter,  we provide a particular perspective on the evolution of
the field of self-adaptation in six waves.  These waves put complementary
aspects of engineering self-adaptive systems in focus that synergistically
have  contributed  to  the  current  knowledge  in  the  field.   From  the  pre-
sented  perspective  on  the  field,  we  outline  a  number  of  challenges  for
future research in self-adaptation, both in a short and long term.
## 1  Introduction
Back in 1968, at the NATO Software Engineering Conference in Brussels, the
term  “software  crisis”  was  coined,  referring  to  the  manageability  problems
of  software  projects  and  software  that  was  not  delivering  its  objectives  [42].
One  of  the  key  identified  causes  at  that  time  was  the  growing  gap  between
the  rapidly  increasing  power  of  computing  systems  and  the  ability  of  pro-
grammers  to  effectively  exploit  the  capabilities  of  these  systems.    This  cri-
sis triggered the development of novel programming paradigms,  methods and
processes  to  assure  software  quality.    While  today  large  and  complex  soft-
ware  projects  remain  vulnerable  to  unanticipated  problems,  the  causes  that
underlaid  this  first  software  crisis  are  now  relatively  well  under  control  of
project managers and software engineers.
Thirty five years later, in 2003, IBM released a manifesto that referred to
another “looming software complexity crisis” this time caused by the increasing
complexity of installing,  configuring,  tuning,  and maintaining computing sys-
tems [18].  New emerging computing systems at that time went beyond company
boundaries into the Internet,  introducing new levels of complexity that could
hardly be managed, even by the most skilled system administrators.  The com-
## 1

plexity resulted from various internal and external factors, causing uncertainties
that are difficult to anticipate before deployment. Examples are the scale of the
system, inherent distribution of the software system that may span administra-
tive domains, dynamics in the availability of resources and services, system faults
that may be difficult to predict, and changes in user goals during operation.  In
a seminal paper, Kephart and Chess put forward self-management as the only
viable  option  to  tackle  the  problems  that  underlie  this  complexity  crisis  [36].
Self-management refers to computing systems that can adapt autonomously to
achieve their goals based on high-level objectives.  Such computing systems are
usually calledself-adaptive systems.
As already stated by Kephart and Chess, realising the full potential of self-
adaptive system will take “a concerted, longterm, and worldwide effort by re-
searchers in a diversity of fields.”  Over the past two decades, researchers and
engineers  from  different  fields  have  put  extensive  efforts  in  the  realisation  of
self-adaptive systems.  In this chapter, we provide a particular perspective on
the engineering of self-adaptive systems in six waves.  Rather than providing a
set of distinct approaches for engineering self-adaptive systems that have been
developed over time, the waves putcomplementary aspects of engineering self-
adaptive  systemsin focus that synergistically have contributed to the current
body of knowledge in the field.  Each wave highlights a trend of interest in the
research community.  Some of the (earlier) waves have stabilised now and re-
sulted in common knowledge in the community.  Other (more recent) waves are
still very active and subject of debate;  the knowledge of these waves has not
been consolidated yet.
The first wave,Automating Tasks, stresses the role of self-management as a
means to free system administrators and other stakeholders from the details of
installing,  configuring,  tuning,  and maintaining  computing systems that have
to  run  autonomously  24/7.   The  second  wave,Architecture-Based  Adaptation
emphasises the central role of architecture in engineering self-adaptive systems,
in particular the role architecture plays in separating the concerns of the regular
functionality of the system from the concerns that are subject of the adaptation.
The first two waves put the focus on the primary drivers for self-adaptation and
the fundamental principles to engineer self-adaptive systems.
The  third  wave,Runtime  Modelsstresses  the  importance  of  adaptation
mechanisms that leverage software models at runtime to reason about the sys-
tem and its goals.  In particular, the idea is to extend the applicability of mod-
els produced in traditional model-driven engineering approaches to the runtime
context.  The fourth wave,Goal Driven Adaptationput the emphasis on the re-
quirements that need to be solved by the managing system and how they drive
the design of a self-adaptive system and can be exploited at runtime to drive
the self-adaptation process.  These two waves put the focus on key elements for
the concrete realisation of self-adaptive systems.
The fifth wave,Guarantees Under Uncertaintiesstress the fundamental role
of uncertainties as first-class concerns of self-adaptive systems, i.e., the lack of
complete knowledge of the system and its executing conditions before deploy-
ment, and how these uncertainties can be resolved at runtime.  Finally, the sixth
## 2

wave,Control-Based Approaches, emphasizes the solid mathematical foundation
of control theory as a basis to design self-adaptive systems that have to oper-
ate under a wide range of disturbances.  The last two waves put the focus on
uncertainties as key drivers of self-adaptive systems and how to tame them.
The  remainder  of  this  chapter  is  structured  as  follows.   In  Section  2,  we
explain the basic principles and concepts of self-adaptation.  Section 3 presents
the six waves in detail.  Finally,  we discuss a number of future challenges for
self-adaptation in Section 4, both in a short and long term.
2  Concepts and Principles
In  this  section,  we  explain  what  is  a  self-adaptive  system.   To  that  end,
we  define  two  basic  principles  that  determine  the  notion  of  self-adaptation.
These principles allow us to determine the scope of this chapter.  From the two
principles we derive a conceptual model of a self-adaptive system that defines
the basic elements of such a system.  The principles and the conceptual model
provide the basis for the perspective on the engineering of self-adaptive systems
in six waves that we present in the next section.
2.1  Basic Principles of Self-Adaptation
The termself-adaptationis not precisely defined in the literature.  Cheng
et  al.  refer  to  a  self-adaptive  system  as  a  system  that  “is  able  to  adjust  its
behaviour in response to their perception of the environment and the system
itself”  [15].   Brun  et  al.  add  to  that:  “theselfprefix  indicates  that  the  sys-
tem decides autonomously (i.e., without or with minimal interference) how to
adapt or organise to accommodate changes in its context and environment” [10].
Esfahani et al. emphasise uncertainty in the environment or domain in which
the  software  is  deployed  as  a  prevalent  aspect  of  self-adaptive  systems  [26].
These interpretations take the stance of the external observer and look at a self-
adaptive system as one that can handle changing external conditions, resources,
workloads, demands, and failures.
Garlan et al. contrast traditional mechanisms that support self-adaptation,
such as exceptions in programming languages and fault-tolerant protocols, with
mechanisms  that  are  realised  by  means  of  a  closed  feedback  loop  to  achieve
various  goals  by  monitoring  and  adapting  system  behaviour  at  runtime  [29].
Andersson et al. refer in this context to “disciplined split” as a basic principle
of a self-adaptive system, referring to an explicit separation between a part of the
system that deals with the domain concerns and a part that deals the adaptation
concerns [2]. Domain concerns relate to the goals for which the system is built;
adaptation concerns relate to the system itself, i.e., the way the system realises
its goals under changing conditions.  These interpretations take the stance of
## 3

the engineer of the system and look at self-adaptation from the point of view
how the system is conceived.
Hence, we introducetwo basic principlesthat complement one another and
determine what is a self-adaptive system:
1.External principle:  A self-adaptive system is a system that can handle
changes  and  uncertainties  in  its  environment,  the  system  itself  and  its
goals autonomously (i.e., without or with minimal human interference).
2.Internal principle:  A self-adaptive system comprises two distinct parts:
the  first  part  interacts  with  the  environment  and  is  responsible  for  the
domain concerns (i.e., concerns for which the system is built); the second
part interacts with the first part (and monitors its environment) and is
responsible for the adaptation concerns (i.e., concerns about the domain
concerns).
In contrast to self-adaptive systems that comprise of two distinct parts com-
pliant with the internal principle, adaptation can also be realised in other ways.
In self-organising systems, components apply local rules to adapt their interac-
tions in response to changing conditions and cooperatively realise adaptation.
This approach often involves emergent behaviour [22]. Another related approach
is context-awareness [3],  where the emphasis is on handling relevant elements
in the physical environment as a first-class citizen in system design and man-
agement.  Context-aware systems typically have a layered architecture,  where
a  context  manager  or  a  dedicated  middleware  is  responsible  for  sensing  and
dealing with context changes.  While self-organisation or context-awareness can
be applied independently or can be combined with self-adaptation, the primary
scope of this chapter is on self-adaptation as a property of a computing system
that is compliant with the two basic principles of self-adaptation.
Furthermore, self-adaptation can be applied to different levels of the tech-
nology stack of computing systems, from the underlying hardware to low-level
computing infrastructure, from middleware services to the application software.
The challenges of self-adaptation at these different levels are different.  For ex-
ample,  the  design  space  for  the  adaptation  of  higher-level  software  entities  is
often multi-dimensional and software qualities and adaption objectives usually
have a complex interplay [1, 10, 28].  These characteristics are less applicable
to the adaptation of lower-level resources and hardware entities.  The scope of
this chapter is primarily on self-adaptation used to manage higher-level software
elements of computing systems.
Prominent communities that have actively been involved in the research on
self-adaptive systems and the waves presented in this article are the communities
of  Software  Engineering  of  Adaptive  and  Self-Managing  Systems  (SEAMS)
## 1
## ,
Autonomic  Computing  (ICAC)
## 2
,  and  Self-Adaptive  and  Self-Organising  Sys-
tems  (SASO)
## 3
.  Research  results  on  self-adaptation  are  regularly  presented  at
## 1
https://www.hpi.uni-potsdam.de/giese/public/selfadapt/seams/
## 2
http://nsfcac.rutgers.edu/conferences/ac2004/index.html
## 3
http://www.saso-conference.org/
## 4

the  top  software  engineering  conferences,  including  the  International  Confer-
ence on Software Engineering(ICSE)
## 4
and the International Symposium on the
Foundations of Software Engineering (FSE).
## 5
2.2  Conceptual Model of a Self-Adaptive System
We now describe a conceptual model of a self-adaptive system.  The model
describes a set of concepts and the relationship between them. The concepts that
correspond to the basic elements of a self-adaptive system are kept abstract and
general, but they comply with the two basic principles of self-adaptation.  The
conceptual model introduces a basic vocabulary for the field of self-adaptation
and serves as a guidance for organising and focusing the knowledge of the field.
Figure 1 shows the conceptual model of a self-adaptive system.
## Environment
## Adaptation
## Goals
## Managing
## System
## Managed System
effect
adapt
sense
sense
read
Self-Adaptive System
Figure 1:  Conceptual model of a self-adaptive system
The conceptual model comprisesfour basic elements: environment, managed
system, adaptation goals, and managing system.
Environment.The environment refers to the part of the external world
with  which  the  self-adaptive  system  interacts  and  in  which  the  effects  of  the
system will be observed and evaluated [35].  The environment can include both
physical and virtual entities.  For example, the environment of a robotic system
## 4
http://2016.icse.cs.txstate.edu/
## 5
https://www.cs.ucdavis.edu/fse2016/
## 5

includes physical entities like obstacles on the robot’s path and other robots,
as well as external cameras and corresponding software drivers.  The distinction
between  the  environment  and  the  self-adaptive  system  is  made  based  on  the
extent of control.  For instance, in the robotic system, the self-adaptive system
may interface with the mountable camera sensor, but since it does not manage
(adapt) its functionality, the camera is considered to be part of the environment.
The environment can be sensed and effected through sensors and effectors re-
spectively.  However, as the environment is not under the control of the software
engineer of the system, there may be uncertainty in terms of what is sensed by
the sensors or what the outcomes will be of effecting the effectors.
Managed System.The managed system comprises the application code
that realises the system’s domain functionality.  Hence, the concerns of the man-
aged system are concerns over the domain, i.e.  the environment.  For instance,
in the case of robots, navigation of a robot and transporting loads is performed
by the managed system.  To realise its functionality, the managed system senses
and effects the environment.  To support adaptations, the managed system has
to be equipped with sensors to enable monitoring and actuators to execute adap-
tations.  Safely executing adaptations requires that the adaptation actions do
not interfere with the regular system activity for which the system has to be in
a quiescent state [38].  Different terms are used in the literature for the concept
of  managed  system  in  the  context  of  self-adaptation.   For  example,  Kephart
and Chess refer to it as the managed element [36], the Rainbow framework [29]
calls it the system layer,  Salehie and Tahvildari use core function [49],  in the
FORMS  reference  model,  the  managed  system  corresponds  to  the  base-level
subsystem [60], and Filieri et al. refer to it as controllable plant [27].
Adaptation Goals.The adaptation goals are concerns of the managing
system  over  the  managed  system;  they  usually  relate  to  the  software  quali-
ties of the managed system [56].  Four principle types of high-level adaptation
goals can be distinguished:  self-configuration (i.e., systems that configure them-
selves automatically), self-optimisation (systems that continually seek ways to
improve their performance or cost), self-healing (systems that detect, diagnose,
and repair problems resulting from bugs or failures), and self-protection (sys-
tems that defend themselves from malicious attacks or cascading failures) [36].
As  an  example,  a  self-optimisation  goal  of  a  robot  may  be  to  ensure  that  a
particular  number  of  tasks  are  achieved  within  a  certain  time  window  under
changing operation conditions, e.g., dynamic task loads or reduced bandwidth
for communication.  Adaptation goals are often expressed in terms of the un-
certainty they have to deal with.  Example approaches are the specification of
quality of service goals using probabilistic temporal logics [13], the specification
of fuzzy goals, whose satisfaction is represented through fuzzy constraints [5],
and adding flexibility to the specification of goals by specifying the goals declar-
atively,  rather than by enumeration [16].  Adaptation goals can be subject of
change themselves (which is not shown in Figure 1).  Adding new goals or re-
moving goals during operation will require updates of the managing system as
well and may also require updates of probes and effectors.
Managing System:  The managing system manages the managed system.
## 6

To  that  end,  the  managing  system  comprises  the  adaptation  logic  that  deals
with one or more adaption goals.  For instance, a robot may be equipped with a
managing system that allows the robot to adapt its navigation strategy to en-
sure that a certain number of tasks are performed within a given time window
under changing operation conditions.  To realise the adaptation goals, the man-
aging system monitors the environment and the managed system and adapts
the  latter  when  necessary.   Conceptually,  the  managing  system  may  consist
of multiple levels where higher-level adaptation subsystems manage underlying
subsystems.   For  instance,  consider  a  robot  that  not  only  has  the  ability  to
adapt its navigation strategy, but also adapt the way such adaptation decisions
are  made,  e.g.,  based  on  the  energy  level  of  the  battery.   Different  terms  are
used in the literature for the concept of managing system.  Examples are:  au-
tonomic manager [36], architecture layer [29], adaptation engine [49], reflective
subsystem [60], and controller [27].
It is important to note that the conceptual model for self-adaptive systems
abstracts away from distribution, i.e., the deployment of the software to hard-
ware.  Whereas a distributed self-adaptive system consists of multiple software
components that are deployed on multiple nodes connected via some network,
from  a  conceptual  point  of  view  such  system  can  be  represented  as  a  man-
aged  system  (that  deals  with  the  domain  concerns)  and  a  managing  system
(that deals with concerns of the managed system represented by the adaptation
goals). The conceptual model also abstracts away from how adaptation decisions
in a self-adaptive system are made and potentially coordinated among different
components.  Such coordination may potentially involve human interventions,
such as in socio-technical and cyber-physical systems.  The conceptual model
is invariant to self-adaptive systems where the adaptation functions are made
by a single centralised entity or by multiple coordinating entities.  Obviously,
the distribution of the components of a self-adaptive system to hardware and
the degree of decentralisation of decision making of adaptation will have a deep
impact on how concrete self-adaptive systems are engineered.
3  An Organised Tour in Six Waves
In the previous section, the focus was onwhatis a self-adaptive system.  We
have explained the basic principles of self-adaptation and outlined a conceptual
model that describes the basic elements of self-adaptive systems compliant with
the  basic  principles.   We  direct  our  focus  now  onhowself-adaptive  systems
are  engineered.   Specifically,  we  provide  a  concise  but  in-depth  introduction
to the engineering of self-adaptive systems.  Instead of presenting distinct and
comprehensive approaches for engineering self-adaptive systems that have been
studied and applied over time, we take a different stance on the field and put
different  aspects  of  engineering  self-adaptive  systems  in  focus.   These  aspects
are structured in six waves that emerged over time, often triggered by insights
derived from other waves as indicated by the arrows in Figure 2.
## 7

## 1. Automating
## Tasks
- Architecture-Based
## Adaptation
- Goal-Driven
## Adaptation
## 3. Runtime
## Models
## 5. Guarantees Under
## Uncertainties
- Control-Based
## Adaptation
systematic engineering
perspective
complexity of
concrete design
theoretical
framework for
self-adaptation
guarantees under
uncertainty
explicit requirements
for feedback loops
adaptation goals as
first-class citizens
uncertainty as
first-class
citizen
link goal models to
feedback loop designs
complexity to
provide assurances
Figure 2:  Six waves of research in self-adaptive systems;  arrows indicate how
waves have triggered new waves
The  waves  have  contributedcomplementary  layers  of  knowledgeon  en-
gineering  self-adaptive  systems  that  synergistically  have  shaped  the  state  of
the  art  in  the  field.Waves  highlighttrends   of   interest   in   the   research
community.  The  knowledge  consolidated  in  each  wave  is  important  for  un-
derstanding  the  concept  of  self-adaptation  and  the  principles  that  under-
lie  the  engineering  of  self-adaptive  systems.  Some  waves  are  stabilised  now
and  have  produced  knowledge  that  is  generally  acknowledged  in  the  com-
munity,  while  other  waves  are  still  very  active  and  the  knowledge  produced
in these waves has not been consolidated yet.
Figure 2 gives a schematic overview of the six waves. The first waveAutomat-
ing  Tasksis concerned with delegating complex and error-prone management
tasks  from  human  operators  to  the  machine.   The  second  waveArchitecture-
based  Adaptationthat  is  triggered  by  the  need  for  a  systematic  engineering
approach (from the first wave) is concerned with applying the principles of ab-
straction and separation of concerns to identify the foundations of engineering
self-adaptive systems.
The third wave,Runtime Modelsthat is triggered by the problem of manag-
ing the complexity of concrete designs of self-adaptive systems (from the second
wave) is concerned with exploiting first-class runtime representations of the key
## 8

elements of a self-adaptive system to support decision making at runtime.  The
fourth wave,Goal-Driven  Adaptationis triggered by the need to consider re-
quirements of self-adaptive systems as first-class citizens (from waves one and
two) and link the goal models to feedback loop designs (from wave three).  The
fourth wave puts the emphasis on the requirements that need to be solved by
the managing system and how they drive its design.
The fifth wave,Guarantees  under  Uncertaintyis triggered by the need to
deal with uncertainty as first-class citizen in engineering self-adaptive systems
(from wave four) and how to mitigate the uncertainty (from wave three).  The
fifth wave is concerned with providing trustworthiness for self-adaptive systems
that need to operate under uncertainty.  Finally, the sixth waveControl-Based
Adaptationis triggered by the complexity to provide assurances (from wave five)
and the need for a theoretical framework for self-adaptation (from wave two).
The sixth wave is concerned with exploiting the mathematical basis of control
theory for analysing and guaranteeing key properties of self-adaptive systems.
Table 1 provides a short summary with the state-of-the-art before each wave
and  a  motivation,  the  topics  that  are  studied  in  the  different  waves,  and  the
contributions that are enabled by each of the waves.  We discuss the waves now
in detail based on a selection of highly relevant work.
## 3.1  Wave I. Automating Tasks
The first wave focusses on the automation of management tasks, from human
administrators to machines.  In the seminal paper [36], Kephart and Chess elab-
orate on the problem that the computing industry experienced from the early
2000s and that underlies the need for self-adaptation:  the difficulty of manag-
ing the complexity of interconnected computing systems. Management problems
include installing, configuring, operating, optimising, and maintaining heteroge-
neous computing systems that typically span multiple administrative domains.
To  deal  with  this  difficult  problem,  the  authors  outline  a  new  vision  on
engineering complex computing system that they coin asautonomic computing.
The principle idea of autonomic computing is to free administrators from system
operation  and  maintenance  by  letting  computing  systems  manage  themselves
given  high-level  objectives  from  the  administrators.   This  idea  is  inspired  by
the autonomic nervous system that seamlessly governs our body temperature,
hearth beat, breathing, etc.  Four essential types of self-management problems
can be distinguished as shown in Table 2.
An  autonomic  computing  system  supports  a  continuous  process,  i.e.,  the
system continuously monitors itself and based on a set of high-level goals adapts
itself to realise the goals.  The primary building block of an autonomic system
is  anautonomic  manager,  which  corresponds  to  the  managing  system  in  the
conceptual model of a self-adaptive system.  Figure 3 shows the basic elements
of  an  autonomic  manager.   The  four  elements:  Monitor,  Analyse,  Plan,  and
Execute realise the basic functions of any self-adaptive system.  These elements
share common Knowledge, hence the model of an autonomic manager is often
referred to as the MAPE-K model.
## 9

Table 1:  Summary of state-of-the-art before each wave with motivation, topic
of the wave, and contributions enabled by each of the waves
WaveSOTA before waveTopic of wave(To be) enabled by wave
W1System management done
by  human  operators  is  a
complex  and  error  prone
process
## Automationof
management tasks
System  manages  itself  au-
tonomously  based  on  high-
level objectives
W2Motivationforself-
adaptation acknowledged,
needforaprincipled
engineering perspective
## Architectureper-
spectiveonself-
adaptation
Separation  between  change
management(dealwith
change)  and  goal  manage-
ment(adaptationobjec-
tives)
W3Architecture  principles  of
self-adaptive  systems  un-
derstood, concrete realisa-
tion is complex
## Model-drivenap-
proach    to    realise
self-adaptivesys-
tems
Runtime  models  as  key  el-
ements    to    engineer    self-
adaptive systems
W4Design  of  feedback  loops
well  understood,  but  re-
quirements  problem  they
intent to solve is implicit
## Requirementsfor
feedback loops
Languages   and   formalisms
to  specify  requirements  for
self-adaptive systems
W5Maturesolutionsfor
engineering   self-adaptive
systems,  but  uncertainty
handled in ad-hoc manner
The    role    of    un-
certaintyinself-
adaptivesystems
and how to tame it
Formal  techniques  to  guar-
antee adaptation goals under
uncertainty
W6Engineering    of    MAPE-
based   self-adaption   well
understood,  but  solutions
are often complex
Applying  principles
from  control-theory
torealiseself-
adaptation
Theoretical   framework   for
(particular   types   of)   self-
adaptive systems
## Managed Element
## Autonomic Manager
## Monitor
## Analyse
## Knowledge
## Plan
## Execute
## Knowledge
Figure 3:  Structure of autonomic manager (based on [36])
TheMonitorelement acquires data from the managed element and its en-
vironment,  and  processes  this  data  to  update  the  content  of  theKnowledge
element  accordingly.   TheAnalyseelement  uses  the  up-to-date  knowledge  to
## 10

Table 2:  Types of self-management
TypeExample ProblemExample Solution
Self-configurationNew  elements  need  to  be  in-
tegrated in a large Internet-of-
Things application.  Installing,
configuring,    and   integrating
heterogeneous elements is time
consuming and error prone.
Automated    integration    and
configuration  of  new  elements
following   high-level   policies.
The rest of the network adapts
automatically and seamlessly.
Self-optimisationA  web  service  infrastructure
wants  to  provide  customers  a
particular  quality  of  service,
but the owner wants to reduce
costs  by  minimising  the  num-
ber of active servers.
The  infrastructure  continually
seeks opportunities to improve
quality  of  service  and  reduce
costs   by   (de-)activating   ser-
vices and change the allocation
of tasks to servers dynamically.
Self-healingA  large-scale  e-health  system
provides   various   remote   ser-
vices to elderly people.  Deter-
mining  problems  in  such  het-
erogeneous system is complex.
The  system  automatically  de-
tects anomalies,  diagnoses the
problem,    and   repairs   local
faults or adapts the configura-
tion to solve the problem.
Self-protectionA   web   e-commerce   applica-
tion  is  vulnerable  to  attacks,
such as illegal communications.
Manually detecting and recov-
ering from such attacks is hard.
The  system  automatically  an-
ticipates  and  defends  against
attacks, anticipating cascading
system failures.
determine whether there is a need for adaptation of the managed element.  To
that end, the analyse element uses representations of the adaptation goals that
are available in the knowledge element.  If adaptation is required, thePlanel-
ement  puts  together  a  plan  that  consists  of  one  or  more  adaptation  actions.
The adaptation plan is then executed by theExecuteelement that adapts the
managed element as needed.  MAPE-K provides a reference model for a manag-
ing system.  MAPE-K’s power is its intuitive structure of the different functions
that are involved in realising the feedback control loop in a self-adaptive system.
While the distinct functions of a managing system are intuitive, the concrete
realisation  of  these  functions  offers  significant  scientific  and  engineering  chal-
lenges.  We illustrate some of these challenges with a Web-based client-server
system, borrowed from the paper that introduces the Rainbow framework [29].
## 6
Figure 4 shows the setup.
The system consists of a set of Web clients that make stateless requests of
content  to  server  groups.   Each  server  group  consists  of  one  or  more  servers.
Clients  connected  to  a  server  group  send  requests  to  the  group’s  shared  re-
quest  queue,  and  servers  that  belong  to  the  group  take  requests  from  the
queue.   The  adaptation  goal  is  to  keep  the  perceived  response  time  of  each
## 6
Besides contributing a concrete and reusable realisation of the MAPE functions, the Rain-
bow framework also contributed a pioneering approach to systematically engineer self-adaptive
systems, which the key focus of the second wave.
## 11

Client-Server System
## Architecture Layer
## Plan
## Execute
## Adaptation
## Engine
## Adaptation
## Executor
## Constraint
## Evaluator
## Model
## Manager
## Strategy
## Operators
## Properties
## Rules
Client1Client2Client3
Client4Client5
ServerGrp1
ServerGrp2
EffectorsProbes
Figure 4:  Web-based client-server system (based on [29])
client (self.responseTime) below a predefined maximum (maxResponseTime).
The managing system (Architecture Layer) connects to the managing sys-
tem  (Client-Server  System)  through  probes  and  effectors.   The  Model  Man-
ager  (Monitor)  uses  probes  to  maintain  an  up-to-date  architectural  model  of
the executing system,  i.e.,  a graph of interacting components with properties
(i.e., clients and servers).  Server load (ServerT.load) and available bandwidth
(ServerT.bandwidth) are two properties that affect the response time (response-
Time).  The Constraint Evaluator (Analyse) checks the model periodically and
triggers the Adaptation Engine (Plan) if the maximum response time is violated.
If the adaptation goal is violated, the managing system executes an adaptation
strategy (responseTimeStrategy).  This strategy works in two steps:  if the load
of  the  current  server  group  exceeds  a  predefined  threshold,  it  adds  a  server
to the group decreasing the response time; if the available bandwidth between
the client and the current server group drops too low, the client is moved to a
group with higher available bandwidth lowering the response time.  Finally, the
Adaptation  Executor  (Execute)  uses  the  operator  ServerGroupT.addServer()
to add a ServerT to a ServerGroupT to increase the capacity, and the operator
ClientT.move(from, toGroup) reconnects ClientT to another group (toGroup).
In  the  Rainbow  paper  [29],  Garlan  and  his  colleagues  state  that  external
control  mechanisms  that  from  a  closed  control  loop  provide  a  more  effective
engineering solution than internal mechanisms.  The statement is based on the
observation that external mechanisms localise the concerns of problem detection
and resolution in separate modules that can be analysed, modified, extended,
## 12

and reused across different systems.  However, it took 10 years before the first
empirical evidence was produced that supports the statement [59].
Table 3 summarises the key insights derived from Wave I.
Table 3:  Key insights of Wave I: Automating Tasks
•Automating tasks is a key driver for self-adaptation.  This driver originates from
the difficulty of managing the complexity of interconnected computing systems.
•The four essential types of self-management problems are self-configuration, self-
optimisation, self-healing, and self-protection.
•Monitor,  Analyse,  Plan,  Execute  +  Knowledge,  MAPE-K  in  short,  provides  a
reference model for an managing system.
•The  MAPE-K  functions  are  intuitive,  however,  their  concrete  realisation  offers
significant scientific and engineering challenges.
3.2  Wave II. Architecture-Based Adaptation
The second wave directs the focus from the basic motivation for self-adaption
to the foundational principles to engineer self-adaptive systems.  The pioneering
approaches described in the first wave specify solutions at a higher level of ab-
straction, for example, the MAPE-K model.  However, these approaches do not
provide an integrated perspective on how to engineer self-adaptive systems.  In
the second wave, researchers apply basic design principles, in particular abstrac-
tion and separation of concerns, to identify the key concerns of self-adaptation.
Understanding these concerns is essential for designers to manage the complex-
ity of engineering self-adaptive systems and consolidate knowledge that can be
applied to future designs.
Already in 1998, Oreizy et al. [44] stressed the need for a systematic, princi-
pled approach to support runtime change.  These authors argued thatsoftware
architecturecan provide a foundation to deal with runtime change in a system-
atic way.  Software architecture in this context has a twofold meaning.  On the
one hand, it refers to the high-level layered structure of a self-adaptive software
system that separates domain concerns from adaptation concerns.  On the other
hand, software architecture refers to an explicit up-to-date architecture model
of the managed system that is used at runtime by a feedback control mechanism
to reason about adaptation.
In their FOSE’07 paper [37], Kramer and Magee argue for an architecture-
based approach to engineer self-adaptive software systems.  Such an approach
offers  various  benefits,  including:generalityof  concepts  and  principles  that
apply to a wide range of domains, an appropriatelevel of abstractionto describe
dynamic change of a system, thepotential for scalabilityas architecture supports
composition and hiding techniques,leverage on existing workof languages and
notations  that  provide  a  rigorous  basis  to  support  reasoning  at  runtime,  and
thepotential  for  an  integrated  approachas  specifications  at  the  architecture
level typically support configuration, deployment and reconfiguration.  Inspired
## 13

by  the  flexibility  and  responsiveness  of  sense-plan-act  types  of  architectures
used in robotics, Kramer and Magee propose a simple yet powerful three-layer
architecture model for self-adaptation, as shown in Figure 5.
## Goal
## Management
Plan request
## G
## G’G’’
Change plans
## Change
## Management
## Component
## Control
Change actions
## C1
## C2
## C3
## P1
## P2
## Status
Figure 5:  Three-layer architecture model for self-adapation (based on [37])
The bottom layer,Component Control, consists of the interconnected com-
ponents that provide the functionalities of the system.  Hence,  this layer cor-
responds  to  the  managed  system  as  described  in  the  conceptual  model  of  a
self-adaptive system (see Figure1).  This layer may contain internal mechanisms
to adjust the system behaviour.  However, to realise self-adaptation, component
control needs to be instrumented with mechanisms to report the current sta-
tus  of  the  system  to  higher  layers  as  well  as  mechanisms  to  support  runtime
modification, such as component addition, deletion, and reconnection.
The middle layer,Change Management, consist of a set of pre-specified plans.
The middle layer reacts to status changes of bottom layer by executing plans
with  change  actions  that  adapt  the  component  configuration  of  the  bottom
layer. The middle layer is also responsible for effecting changes to the underlying
managed system in response to new objectives introduced from the layer above.
Change management can adjust operation parameters of components, remove
failed components, add new components, and change interconnections between
components.  If a condition is reported that cannot be handled by the available
plans, the middle layer invokes the services of the top layer.
The  top  layer,Goal  Management,  comprises  a  specification  of  high-level
goals.  This layer produces change management plans in response to requests
for plans from the layer beneath.  Such a request will trigger goal management
to identify alternative goals based on the current status of the system and gen-
erate plans to achieve these alternative goals.  The new plans are then delegated
to the change management layer.  Goal management can also be triggered by
stakeholders that introduce new goals.  Representing high-level goals and auto-
## 14

matically synthesising change management plans is a complex and often time
consuming task.
The  pioneering  models  shown  in  Figures  3,  4  and  5  capture  foundational
facets of self-adaptation.  However, these models lack precision to reason about
key architectural characteristics of self-adaptive systems, such as the responsi-
bilities allocated to different parts of a self-adaptive system, the processes that
realise adaptation together with the models they operate on,  and the coordi-
nation between feedback loops in a distributed setting.  A precise vocabulary
for such characteristics is essential to compare and evaluate design alternatives.
Furthermore, these models take a particular stance but lack an encompassing
perspective of the different concerns on self-adaption.  FORMS (FOrmal Refer-
ence Model for Self-adaptation) provides a reference model that targets these
issues [60].  FORMS defines the essential primitives that enable software engi-
neers to rigorously describe and reason about the architectural characteristics
of distributed self-adaptive systems.  The reference model builds on established
principles of self-adaptation.  In particular, FORMS unifies three perspectives
that represent three common but different aspects of self-adaptive systems:  re-
flective computation, distributed coordination, and MAPE-K.
Figure 6 shows the reflection perspective in UML notation.  For the formal
representation of the three perspectives in Z notation we refer to [60].  To illus-
trate the FORMS model, we use a robotics application [25] shown in Figure 7.
This application comprises a base station and a robot follower that follows a
leader.  Self-adaption in this system is used to deal with failures and to support
dynamic updates.
## Computation
Base-Level
## Computation
## Reflective
## Computation
## Model
## Reflection
## Model
## Domain
## Model
## Environment
Self-Adaptive
## System
## Subsystem
## Reflective
## Subsystem
Base-Level
## Subsystem
triggers >
## 1..*
## 1..*
## 1..*
reasons about
and acts upon >
## 1..*1..*
## 1..*
## *
## *
## 1
< is situated in
perceives and
effects v
perceives v
monitors and
adapts >
## *
## *
## 1..*
## 1..*
## 0..1
## *
## 0..1
## Representation
## 1
## 1..*
## 0..1
## KEY
## Generalization
## Association
## Containment
FORMS Element
Figure 6:  FORMS primitives for the reflection perspective [60]
## 15

IR Cliff
## Sensor
## Status
## Collector
## Failure
## Collector
## Version
## Collector
## Status
## Analyzer
## Failure
## Analyzer
## Version
## Analyzer
## Robot
## Admin
## Updater
## Line
## Follower
## Motor
## Actuator
## Camera
## Driver
## Object
## Follower
## Motor
## Actuator
## Robot Leader
## Robot Follower
## Base Station
## Robot Behavior
## Robot Behavior
## Failure Manager
## Failure Manager
## Version Manager
## Version Manager
HostInteracts
## KEY
## Subsystem Component
Figure 7:  Robotics architecture presented [25]
As shown in Figure 6, a self-adaptive system is situated in an environment
and comprises one or more base-level and reflective subsystems.  The environ-
ment in the robotic application includes the area where the robots can move with
lines that mark the paths the robots have to follow, the location of obstacles,
and external sensors and cameras with the corresponding software drivers.
A  base-level  subsystem  (i.e.,  managed  system)  provides  the  system’s  do-
main functionality; it comprises a set of domain models and a set of base-level
computations, inline with principles of computational reflection.
A  domain  model  represents  a  domain  of  interest  for  the  application  logic
(i.e., system’s main functionality).  A base-level computation perceives the en-
vironment, reasons about and acts upon a domain model, and effects the envi-
ronment.
The base-level subsystem of the robots consists of two parts corresponding
to the behaviours that realise the mission of the robots.  The domain models
incorporate a variety of information:  a map of the terrain, locations of obsta-
cles and the other robot, etc.  The base-level computation of the robot leader
decides how to move the vehicle along a line, avoiding obstacles.  The base-level
subsystem of the follower moves the vehicle by tracking and following the leader.
A reflective subsystem (i.e., a managing system) manages another subsys-
tem,  which  can  be  either  a  base-level  or  a  reflective  subsystem.   A  reflective
subsystem  consists  of  reflection  models  and  reflective  computations.   Reflec-
tion models represent the relevant elements that are needed for reasoning about
adaptation, such as subsystems, connections, environment attributes, and goals.
The reflection models are typically architectural models.  A reflective computa-
tion reasons about and acts upon reflection models.  A reflective computation
## 16

also monitors the environment to determine when/if adaptations are necessary.
However, unlike the base-level computation, a reflective computation does not
have the ability to effect changes on the environment directly.  The rationale is
separation of concerns:  reflective computations are concerned with a base-level
subsystem, base-level computations are concerned with a domain.
The robot application comprises a reflective subsystem to deal with failures
of the robot follower.  This subsystem consists of failure managers deployed on
the  two  robots  that,  based  on  the  collected  data,  detect  and  resolve  failures
of the robotic behaviour of the follower.  Reflection models include a runtime
system architecture of the robot behaviour, adaptation policies, and plans (the
models are not shown in Figure 7).  Examples of reflective computations are the
failure collector that monitors the camera driver and reports failures to failure
analyzer that in turn determines the best replacement component for the camera
based on adaptation policies.  The failure manager layer is subject to additional
version manager layer, which replaces the failure collector components on robot
follower nodes whenever new versions are available.
For the integration of the distributed coordination and MAPE-K perspective
with the reflection perspective,  and several examples that show how FORMS
supports  reasoning  on  the  architecture  of  self-adaptive  systems,  we  refer  the
interested reader to [60].
Table 4 summarises the key insights derived from Wave II.
Table 4:  Key insights of Wave II: Architecture-Based Adaptation
•Architecture provides a foundation to support systematic runtime change and man-
age the complexity of engineering self-adaptive systems.
•An architecture perspective on self-adaptation provides:  generality of concepts and
principles, an appropriate level of abstraction, scalability, leverage on existing work,
and an integrated approach.
•Two fundamental architectural concerns of self-adaptive systems are change man-
agement (i.e., manage adaptation using plans) and goal management (generate plans
based on high-level goals).
•Three primary but interrelated aspects of self-adaptive systems are:  reflective com-
putation, MAPE-K, and distributed coordination.
3.3  Wave III. Models at Runtime
The second wave clarified the architecture principles that underlie self-adaptive
systems.  However, the concrete realisation of self-adaptation is complex.  The
third wave puts the concrete realisation of runtime adaptation mechanisms in
focus.   In  an  influential  article,  Blair  et  al.  elaborate  on  the  role  of  software
models at runtime as an extension of model driven engineering techniques to
the runtime context [7].  A model at runtime is defined as “a causally connected
self-representation of the associated system that emphasises the structure, be-
haviour, or goals of the system from a problem space perspective.”
## 17

The basic underlying motivation for runtime models is the need for managing
the complexity that arises from the large amounts of information that can be
associated  with  runtime  phenomena.   Compared  to  traditional  computational
reflection,  runtime  models  of  adaptive  systems  are  typically  at  a  higher  level
of  abstraction  and  the  models  are  causally  connected  to  the  problem  space
(in  contrast  to  the  computation  space  in  reflection).   The  causal  connection
is bidirectional:  (1) runtime models provide up-to-date information about the
system to drive adaptations (sensing part),  and (2) adaptations can be made
at  the  model  level  rather  than  at  the  system  level  (effecting  part).   Runtime
models provide abstractions of the system and its goals serving as a driver and
enabler for automatic reasoning about system adaptations during operation.
Models at runtime can be classified along four key dimensions as shown in
## Table 5.
Table 5:  Dimensions of models at runtime (based on [7])
TypeExample Problem
Structural versus behaviouralStructural models represent how the system or parts
of  it  are  organised,  composed,  or  arranged  together;
behaviour models represent facets of the execution of
the system, or observable activities of the system such
as the response to internal or external stimuli.
Procedural versus declarativeProcedural models emphasis thehow, i.e., they reflect
the  actual  organisation  or  execution  of  the  system;
declarative  models  emphasis  thewhat,  i.e.,  they  re-
flect  the  purpose  of  adaptation,  e.g.,  in  the  form  or
explicitly represented requirements or goals.
Functional versus non-functionalFunctional models reflect functions of the underlying
system; non-functional models reflect quality proper-
ties of the system related to some functionality; e.g.,
a model keeps track of the reliability of a service.
Formal versus non-formalFormal models specify the system or parts of it using
a mathematical language, supporting automated rea-
soning; informal models reflect the system using e.g.,
a programming or domain modelling language.
Building upon the notion of models at runtime, Morin et al. define a self-
adaptive  system  as  a  set  of  configurations  that  are  determined  by  a  space  of
variation points [41]. Depending on changing conditions (changes in the context,
errors,  etc.),  the  system  dynamically  chooses  suitable  variants  to  realise  the
variation points, changing it from one configuration to another.
Consider as an example a dynamic customer relationship management sys-
tem that provides accurate client-related information depending on the context.
When a user is working in his or her office, the system can notify him or her
by e-mail via a rich Web-based client.  When the user is driving a car to visit a
client, messages received by a mobile or smart phone should notify only client-
related or critical issues.  If the user is using a mobile phone, he or she can be
## 18

notified via the short message service or audio/voice.  In the case the user uses
a smart phone the system can use a lightweight Web client.
As these examples illustrate, the variants may provide better quality of ser-
vice,  offer  new  services  that  were  not  relevant  under  previous  conditions,  or
discard  services  that  are  no  longer  useful.   It  is  essential  that  transitions  be-
tween configurations follow a safe migration path.  Figure 8 shows the primary
elements of a model-oriented architecture that realises this perspective.
## Business Application
## Online Model Space
Goal-Based
## Reasoner
## Event
## Processor
## Model
## Weaver
## Configuration
## Manager
feature
model
## Sensors
## Factories
feature
model
context
model
architecture
model
runtime events
factory services
architecture
model
## Configuration
## Checker
## Causal Connection
## Configuration
## Checker
reasoning
model
Figure 8:  Model-oriented architecture for self-adaptive systems (based on [41])
The model-oriented architecture that corresponds with the managing system
of the conceptual model of a self-adaptive systems consists of three layers.  The
top layerOnline Model Spaceis a platform-independent layer that only manipu-
lates models.  The middle layerCausal Connectionis platform-specific and links
the model space to the runtime space.  Finally, the bottom layerBusiness Ap-
plicationcontains the application logic and is equipped with sensors that track
runtime events from the application and its environment, and factories that can
instantiate new component instances.
The five components of the model-oriented architecture interact by exchang-
ing four types of runtime models.  Thefeature  modeldescribes the variability
of the system, including mandatory, optional, and alternative, and constraints
among features (requires, excludes).  Features refer to architectural fragments
that  realise  the  features  using  a  particular  naming  convention.   Thecontext
## 19

modelspecifies relevant variables of the environment in which the system exe-
cutes.  Context variables are kept up to date at runtime based on sensor data.
Thereasoning  modelassociates sets of features with particular context.  One
possible  instantiation  of  a  reasoning  model  is  a  set  of  event-condition-action
rules.  An event specifies a signal that triggers the invocation of a rule, e.g. a
particular service fails.  The condition part provides a logical expression to test
whether  the  rule  applies  or  not,  e.g.  the  functionality  of  the  failed  service  is
required  in  the  current  context.   The  action  part  consists  of  update  actions
that are invoked if the rule applies,  e.g. unbind the failed service and bind a
new alternative service.  Finally, thearchitecture modelspecifies the component
composition of the application.  The architecture model refines each leaf feature
of the feature model into a concrete architectural fragment.
TheEvent Processorobserves runtime events from the system and its context
to update a context model of the system.  Complex event processing entities can
be used to aggregate data, remove noise, etc.  When theGoal-Based  Reasoner
receives  an  updated  context  model,  it  uses  the  feature  model  and  reasoning
model to derive a specific feature model with mandatory features and selected
optional  features  aligned  with  the  current  context.   TheModel  Weaveruses
the  specific  feature  model  to  compose  an  updated  architecture  model  of  the
system  configuration.   TheConfiguration  Checkerchecks  the  consistency  of
the configuration at runtime, which includes checking generic and user-defined
application-specific invariants.  If the configuration is valid,  the model weaver
sends it to theConfiguration Managerthat will reconfigure the architecture of
the business application accordingly.  Such a configuration includes deducing a
safe sequence of reconfiguration actions such as removing, adding and binding
components.
The  model-oriented  architecture  for  self-adaptive  systems  emphasises  the
central role of runtime models in the realisation of a self-adaptive systems.  The
modularity  provided  by  the  models  at  runtime  allows  to  manage  potentially
large design spaces in an efficient manner.
Table 6 summarises the key insights derived from Wave III.
Table 6:  Key insights of Wave III: Models at Runtime
•A  model  at  runtime  is  a  causally  connected  self-representation  of  the  structure,
behaviour, or goals of the associated system.
•Runtime models enable managing the complexity that arises from the large amounts
of information that can be associated with runtime phenomena.
•Making goals first class citizens at runtime enables analysis of the behaviour of the
system during operation, supporting the decision making for self-adaptation.
•Four key dimensions of runtime models are; structural versus behavioural, procedu-
ral versus declarative, functional versus non-functional, and formal versus non-formal.
•From a runtime model viewpoint,  a self-adaptive system can be defined as a set
of configurations that are determined by a space of variation points.  Self-adaptation
then boils down to choosing suitable variants to realise the variation points, providing
better quality of service for the changing context.
## 20

3.4  Wave IV. Goal Driven Adaptation
The fourth wave turns the focus of research from the design of the managing
system to therequirementsfor self-adaptive systems.  When designing feedback
loops, it is essential to understand to requirements problem they intent to solve.
A pioneering approach for the specification of requirements for self-adaptive sys-
tems is RELAX [62].  RELAX is a language that includes explicit constructs for
specifying and dealing with uncertainties.  In particular, the RELAX vocabulary
includes operators that define constraints on how a requirement may be relaxed
at runtime.  The grammar provides clauses such as “AS CLOSE AS POSSIBLE
TO”  and  “AS  FEW  AS  POSSIBLE.”  As  an  example,  the  requirement  “The
system  SHALL  ensure  a  minimum  of  liquid  intake”  can  be  relaxed  to  “The
system SHALL ensure AS CLOSE AS POSSIBLE TO a minimum of liquid in-
take; the system SHALL ensure minimum liquid intake EVENTUALLY.” The
relaxed requirement tolerates the system temporarily not to monitor a person’s
intake  of  liquid,  but  makes  sure  that  it  is  eventually  satisfied  not  to  jeopar-
dise  the  person’s  health.   A  related  approach  is  FLAGS  [4]  that  is  based  on
KAOS [54], a goal-oriented approach for modelling requirements.  FLAGS dis-
tinguishes between crisp goals, whose satisfaction is boolean, and fuzzy goals,
whose satisfaction is represented through fuzzy constraints.
Cheng et al. unite the RELAX language with goal-based modelling, explicitly
targeting environmental uncertainty factors that may impact the requirements
of  a  self-adaptive  system  [16].   Figure  9  shows  excerpts  that  illustrates  two
mechanisms to mitigate uncertainties.
## Refinement
## Agent
## Goal
## Obstacle
... affects
## KEY
## Maintain
[Health]
## Maintain
[Is	
  Hydrated]
## Maintain
[LiquidIntake	
  AS	
  CLOSE
AS	
  POSSIBLE	
  TO	
  ideal]
## Fridge
## Mary
## Become
unhealthy
## Become
dehydrated
## Inadequate
liquid	
  intake
## Forgets
to	
  drink
## Achieve
[LiquidDrunk]
## Maintain
[SupplyOf
FreshWater]
## Requirement
Responsible for
Assigned to
## (1)
## Achieve
[ReminderTo
DrinkIssued]
mitigates
## Maintain
[Health]
## Maintain
[Is	
  Hydrated]
## Maintain
[Adequate
LiquidIntake]
## Fridge
## Mary
## Become
unhealthy
## Become
dehydrated
## Inadequate
liquid	
  intake
## Forgets
to	
  drink
## Achieve
[LiquidDrunk]
## Maintain
[SupplyOf
FreshWater]
## (2)
## Achieve
[Prompted
ToDrink]
mitigates
## AAL
Figure 9:  Left:  original goal model.  Right:  goal model with two types of un-
certainty mitigations:  (1) relaxing a goal; (2); adding a subgoal (based on [16])
## 21

The first mechanism to mitigate uncertainty is relaxing a goal.  For example,
if the goal Maintain[AdequateLiquidIntake] cannot be guaranteed in all circum-
stances, e.g. based on uncertainties of Mary’s behaviour, this uncertainty may
be tolerated.  To that end, RELAX is applied to the original goal resulting in
Maintain[LiquidIntake AS CLOSE AS POSSIBLE TO ideal].  The arc pointing
to the obstacle “Inadequate liquid intake” indicates a partial mitigation.
The second mechanism to mitigate uncertainty factors is adding a subgoal.
The uncertainty whether Mary will drink enough is mitigated by adding the new
sub-goal Achieve[ReminderToDrinkIssued].  This new goal is combined with the
expectation that Mary drinks and that the fridge supplies fresh water.  The re-
minders to drink are realised by an AAL system that is responsible for prompting
Mary to drink based, i.e.  requirement Achieve[PromptedToDrink].
Another mechanism to mitigate uncertainties is adding a new high-level goal
for  the  target  system.   The  interested  reader  is  referred  to  [16]  for  a  detailed
discussion of this mitigation mechanism.
The main contributions of approaches such as RELAX and FLAGS are nota-
tions to specify the goals for self-adaptive systems.  Other researchers approach
the problem ofrequirementsfor self-adaptive systems from a different angle and
look at requirements as drivers for the design of the managing system.  Souza
et al. phrase it as “if feedback loops constitute an (architectural) solution for
self-adaption,  what  is  the  requirements  problem  this  solution  is  intended  to
solve?”  [52].   The  conclusion  is  that  requirements  to  be  addressed  with  feed-
back loops (i.e.  the concerns of the managing system) are requirements about
the runtime success/failure/quality-of-service of other requirements (i.e.  the re-
quirements of the managed system).  These requirements are calledawareness
requirements.   Table  7  shows  different  types  of  awareness  requirements.   The
illustrative examples are from an ambulance dispatching system.
Table 7:  Types of awareness requirements (based on [52])
TypeIllustrative example
RegularAR1:  Input emergency information should never fail.
AggregateAR2:  Search call database should have a 95% success rate over one
week periods.
TrendAR3: The success rate of the number of unnecessary extra ambulances
for a month should not decrease, compared to the previous month, two
times consecutively.
DeltaAR4:  Update  arrival  at  site  should  be  successfully  executed  within
10 minutes of the successful execution of Inform driver, for the same
emergency call.
MetaAR5:  AR2 should have 75% success rate over one month periods.
A regular awareness requirement refers to another requirement that should
never fail.  An aggregate awareness requirement refers to another requirement
and  imposes  constraints  on  their  success/failure  rate.   AR3  is  a  trend  aware-
ness requirement that compares the success rates over a number of periods.  A
## 22

delta  awareness  requirement  specifies  acceptable  thresholds  for  the  fulfilment
of  requirements,  such  as  achievement  time.   Finally,  meta  awareness  require-
ments make statements about other awareness requirements.  The constraints
awareness requirements place are on instances of other requirements.
Awareness requirements can be graphically represented as illustrated in Fig-
ure  10.   The  figures  shows  an  excerpt  of  a  goal  model  for  an  ambulance  dis-
patching system with awareness requirements AR1, AR2, and AR5.
## Communication
networks working
Mark as
duplicate of
recent call
## Display
similar calls
Mark as
unique or
duplicate
Send to
dispatchers
## Input
emergency
information
Search call
database
## Determine
uniqueness
of call
and
or
SuccessRate (95%, 7d)
SuccessRate (75%, 30d)
NeverFail
Awareness requirement
## Task
## Goal
## Constraint
## KEY
Figure 10:  Graphical representation of awareness requirements (based on [52])
In order to reason about awareness requirements they need to be rigorously
specified and become first class citizens that can be referred to.  The following
excerpt shows how example requirement AR2 in Table 7 can be specified in the
Object  Constraint  Language  (OCL
## 7
)  extended  with  temporal  operators  and
other constructs such as scopes and timeouts:
context Goal-SearchCallDataBase
def: all : Goal-SearchCallDataBase.allInstances()
def: week: all -> select(...)
def: success : week -> select(...)
inv AR2: always(success -> size() / week -> size() >= 0.95)
The   first   line   states   that   for   AR2,   all   instances   of   the   goal   Goal-
SearchCallDataBase are collected in a set.  The next two lines use theselect()
operator to separate the subset of instances per week and the subset of these
instances that succeeded.  Finally, the sizes of these two sets are compared to
assert that 95% of the instances are successful at all times (always).
## 7
ISO/IEC 19507:2012(en):  Information Technology – Object Management Group Object
Constraint Language (OCL) – https://www.iso.org/obp/ui
## 23

Souza  et  al.  [52]  demonstrate  how  awareness  requirements  can  be  moni-
tored at runtime using a monitoring framework.  Monitoring of awareness re-
quirements  enables  analysis  of  the  behaviour  of  the  system  during  operation,
supporting the decision making for adaptation at runtime.  In complementary
work [53], the authors introduce the notion of evolution requirements that are
modeled as condition-action rules, where the actions involve changing (strength-
ening, weakening, abandoning, ...)  other requirements.
Table 8 summarises the key insights derived from Wave IV.
Table 8:  Key insights of Wave IV: Goal Driven Adaptation
•Goal  driven  adaptation  has  two  sides:  (i)  how  to  specify  the  requirements  of  a
system that is exposed to uncertainties, and (2) if feedback loops constitute a solution
for adaptation, what are the requirements this solution is intended to solve?
•Specifying  goals  of  self-adaptive  systems  requires  taking  into  account  the  uncer-
tainties to which the system is exposed to.
•Defining constraints on how requirements may be relaxed at runtime enables han-
dling uncertainties.
•Requirements to be addressed by feedback loops (i.e.  the concerns of the managing
system) are requirements about the runtime success/failure/quality-of-service of other
requirements (i.e.  the requirements of the managed system).
## 3.5  Wave V. Guarantees Under Uncertainties
In  the  fourth  wave,  uncertainty  emerged  as  an  important  concern  that  self-
adaptive systems need to deal with.  The fifth wave puts the emphasis on taming
uncertainty, i.e., providingguaranteesfor the compliance of the adaption goals
of self-adaptive systems that operate under uncertainty.  As such, the fifth wave
introduces  a  shift  in  the  motivation  for  self-adaptation:  uncertainty  becomes
the central driver for self-adaptation.
Researchers and engineers observe that modern software systems are increas-
ingly embedded in an open world that is constantly evolving, because of changes
in the surrounding environment, the behaviour of users, and the requirements.
As these changes are difficult to anticipate at development time, the applications
themselves need to change during operation [4].  Consequently, in self-adaptive
systems,  change activities are shifted from development time to runtime,  and
the responsibility for these activities is shifted from software engineers or system
administrators to the system itself.  Multiple researchers have pointed out that
the primary underlying cause for this shift stems from uncertainty [26, 47, 57].
Different  sources  of  uncertainty  in  self-adaptive  systems  have  been  identi-
fied [40], as shown in Table 9.  This table classifies the sources of uncertainty in
four groups:  uncertainty related to the system itself, uncertainty related to the
system goals, uncertainty in the execution context, and uncertainty related to
human aspects.
Exposing self-adaptive systems – in particular systems with strict goals – to
uncertainty introduces a paradoxical challenge:  how can one provide guarantees
## 24

Table 9:  Sources of uncertainty (based on [40])
GroupSource of uncertaintyExplanation
## System
Simplifying assumptionsRefers to modelling abstractions that intro-
duce some degree of uncertainty.
Model driftMisalignment  between  elements  of  the  sys-
tem and their representations.
IncompletenessSome  parts  of  the  system  or  its  model  are
missing that may be added at runtime.
Future parameters valueUncertainty of values in the future that are
relevant for decision making.
Automatic learningLearning with imperfect and limited data, or
randomness in the model and analysis.
Adaptation functionsImperfect monitoring, decision making, and
executing functions for realising adaption.
DecentralisationLack of accurate knowledge of the entire sys-
tem state by distributed parts of it.
## Goals
Requirements elicitationElicitation  of  requirements  is  known  to  be
problematic in practice.
Specification of goalsDifficulty  to  accurately  specify  the  prefer-
ences of stakeholders.
Future goal changesChanges   in   goals   due   to   new   customers
needs, new regulations or new market rules.
## Context
Execution contextContext model based on monitoring mecha-
nisms  that  might  not  be  able  to  accurately
determine the context and its evolution.
Noise in sensingSensors/probes are not ideal devices and they
can provide (slightly) inaccurate data.
Different sources of information   Inaccuracy  due  composing  and  integrating
data originating from different sources.
## Humans
Human in the loopHuman  behaviour  is  intrinsically  uncertain;
it can diverge from the expected behaviour.
Multiple ownershipThe exact nature and behaviour of parts of
the system provided by different stakeholders
may be partly unknown when composed.
for the goals of a system that is exposed to continuous uncertainty?
A  pioneering  approach  that  deals  with  this  challenge  is  Runtime  Quanti-
tative Verification (RQV). Quantitative verification is a mathematically based
technique that can be used for analysing quality properties (such as performance
and reliability) of systems that exhibit stochastic behaviour.  RQV applies quan-
titative verification at runtime.  Calinescu et al. apply RQV in the context of
managing the quality of service in service-based systems [13].
Figure  11  shows  the  architecture  of  the  approach  that  is  called  QoSMOS
(Quality of Service Management and Optimisation of Service-based systems).
The service based system offers clients remote access to a composition of Web-
services through a workflow engine.  To that end, the workflow engine executes
services in a workflow.  The functionality of each service may be provided by
multiple service instances but with different qualities, e.g. reliability, response
## 25

time, cost, etc.  The aim of the system is to provide users the functionality of
the composite service with particular qualities.  The tele-assistance application
is available as an artifact for experimentation [58].
## Executor
## Planner
## Analyzer
## Monitor
## Operational
## Model
QoS
## Requirements
## Abstract
## Workflow
## Resource
## Allocation
## Concrete
## Workflow
## Model
## Checker
sensors
effectors
## Workflow
## Engine
## Resources
Service-Based System
## Internet
## Autonomic Manager
## Users
Figure 11:  QoSMOS architecture (based on [13])
The adaptation problem is to select concrete services that compose a QoS-
MOS service and allocate resources to concrete services such that the required
qualities are guaranteed.  Given that the system is subject to several uncertain-
ties, such as fluctuations in the availability of concrete services, changes in the
quality properties of services,  etc., the requirements are necessarily expressed
with  probabilities.   An  example  isR
## 0
:“the  probability  that  an  alarm  failure
ever occurs during the lifetime of the system is less than P = 0.13.”
The  core  of  the  QoSMOS  architecture  is  anAutonomic  Managerthat  in-
teracts with the service-based system throughsensorsandeffectors.  The auto-
nomic manager comprises of a classic MAPE loop that exploits a set of runtime
models to make adaptation decisions.
TheMonitortracks: (1) quality properties, such as the performance (e.g. re-
sponse  time)  and  reliability  (e.g.  failure  rate)  of  the  services,  and  (2)  the  re-
sources allocated to the individual services (CPU, memory, etc.)  together with
their workload.  This information is used to update theoperational model.  The
types of operational models supported by QoSMOS are different types of Marko-
vian  models.   Figure  12  shows  an  excerpt  of  a  Discrete  Time  Markov  Chain
(DTMC) model for a tele-assistance application.  In particular, the model shows
a  part  the  workflow  of  actions  with  probabilities  assigned  to  branches.   The
initial  estimates  of  these  probability  values  are  based  on  input  from  domain
experts.  The monitor updates the values at runtime, based on observations of
the  real  behaviour.   Failure  probabilities  to  service  invocations  (e.g.,cin  the
## 26

model) are modelled as variables because these values depend on the concrete
service selected by the MAPE loop.
## 3
vitalParamMsg
## 7
analyseData
## 11
results
## 14
failedAnalysis
alarm
## 6
## 0.3
## 1
## 1-c
c
changeDrug
## 9
changeDose
## 0.12
## 0.45
## 0.43
## 6
Figure 12:  Excerpt of DTMC model for Tele-assistance system (based on [13])
TheAnalyzercomponent employs the parameterised operational model to
identify  the  service  configurations  that  satisfy  the  quality  of  service  require-
ments.  To that end, the analyser employs amodel checker.
## 8
The model checker
requires that the stakeholder requirements are translated from a format in high-
level  natural  language  to  a  formal  expression  in  the  language  supported  by
the  model  checker  (QoS  requirements).   For  example,  for  a  DTMC  model  as
shown in Figure 12, requirements can be expressed in Probabilistic Computa-
tion Tree Logic (PCTL). The example requirement given above would translate
to:R
## 0
## :P
## ≤0.13
[♦“f ailedAlarm”].   PRISM  [39]  is  a  model  checker  that  sup-
ports the analysis of DTMC models for goals expressed in PCTL expressions.
The analyser automatically carries out the analysis of a range of possible con-
figurations of the service based system by instantiating the parameters of the
operational model.  The result of the analysis is a ranking of the configurations
based on the required QoS requirements.
ThePlanneruses the analysis results to build a plan for adapting the con-
figuration of the service-based system.  The plan consists of adaptation actions
that can be a mapping of one (or multiple) concrete services with suitable qual-
ity properties to an abstract service.  Finally, theExecutorreplaces the concrete
workflow used by the workflow engine with the new concrete workflow realising
the functionality of the QoSMOS service with the required quality of service.
The focus of runtime quantitative verification as applied in [13] is on pro-
viding guarantees for the adaptation goals (see Figure 1).  Guaranteeing that
the managing system realises its objectives also requires functional correctness
of the adaptation components themselves, i.e., the components that realise the
MAPE functions.  For example,  important properties of a self-healing system
may  be:   does  the  analysis  component  correctly  identify  errors  based  on  the
## 8
Model  checking  refers  to  the  following  problem:   Given  a  model  of  a  system,  exhaus-
tively  and  automatically  check  whether  this  model  meets  a  given  specification,  see  e.g.,
https://en.wikipedia.org/wiki/Modelchecking
## 27

monitored data,  or does the execute component execute the actions to repair
the managed system in the correct order?  Lack of such guarantees may ruin
the adaptation capabilities.  Such guarantees are typically provided by means
of design-time modelling and verification of the managing system, before it is
implemented.  ActivFORMS [34] (Active FORmal Models for Self-adaptation)
is  an  alternative  approach  to  provide  functional  correctness  of  the  managing
system that is based on executable formal models.  Figure 13 shows the basic
architecture of ActivFORMS.
## Model
## Checker
ExecutorPlannerAnalyzer
## Monitor
## Probes
## Knowledge Repository
## Effectors
## Managed System
## Change Management
## Goal Management
## Managing System
## Virtual Machine
Figure 13:  ActivFORMS architecture (based on [34])
The   architecture   conforms   to   the   three-layer   model   of   Kramer   and
Magee [37].  A virtual machine enables direct execution of the verified MAPE
loop models to realise adaptation at runtime.  The approach relies on formally
specified templates that can be used to design and verify executable formal mod-
els of MAPE loops [30].  ActivFORMS eliminates the need to generate controller
code and provides additional assurances for it.  Furthermore, the approach sup-
ports  on-the-fly  changes  of  the  running  models  using  the  Goal  Management
interface, which is crucial to support dynamic changes of adaptation goals.
Table 10 summarises the key insights derived from Wave V.
3.6  Wave VI. Control-Based Approaches
Engineering self-adaptive systems is often a complex endeavour.  In particular,
ensuring compliance with the adaptation goals of systems that operate under
## 28

Table 10:  Key insights of Wave V: Guarantees Under Uncertainties
•Uncertainty is a key driver for self-adaptation.
•Four sources of uncertainties are: uncertainty related to the system itself, the system
goals, the execution context, and uncertainty related to human aspects.
•Guarantees  for  a  managing  system  includes  guarantees  for  the  adaptation  goals
(qualities) and the functional correctness of the adaptation components themselves.
•Runtime  quantitative  verification  tackles  the  paradoxical  challenge  of  providing
guarantees for the goals of a system that is exposed to continuous uncertainty.
•Executable formal models of feedback loops eliminate the need to generate controller
code and to provide assurances for it;  this approach supports on-the-fly changes of
the deployed models, which is crucial for changing adaptation goals during operation.
uncertainty is challenging.  In the sixth wave, researchers explore the application
of control theory as a principle approach to realise runtime adaptation.  Control
theory is a mathematically-founded discipline that provides techniques and tools
to design and formally analyse systems.  Pioneering work on the application of
control theory to computing systems is documented in [23, 33].  Figure 14 shows
a typical control-based feedback loop.

## Controller
## Disturbances

## Target
## System
## Control
## Signal
## Control
## Error
## Measured
## Output
## Setpoint
## +
## -
Figure 14:  A typical control-based feedback loop
A  control-based  computing  system  consists  of  two  parts:  a  target  system
(or  plant)  that  is  subject  to  adaptation  and  a  controller  that  implements  a
particular control algorithm or strategy to adapt the target system. The setpoint
is the desired or target value for an adaptation goal; it represents a stakeholder
requirement expressed as a value to be achieved by the adaptive system.  The
target system (managed system) produces an output that serves as a source of
feedback for the controller.  The controller adapts the target system by applying
a  control  signal  that  is  based  on  the  difference  between  the  previous  system
output and the setpoint. The task of the controller is to ensure that the output of
the system corresponds to the setpoint while reducing the effects of uncertainty
that  appear  as  disturbances,  or  as  noise  in  variables  or  imperfections  in  the
models of the system or environment used to design the controller.
Different types of controllers exist that can be applied for self-adaptation; the
most commonly used type in practice (in general) is the Proportional-Integral-
Derivative (PID) controller.  Particularly interesting for controlling computing
## 29

systems is adaptive control that adds an additional control loop for adjusting the
controller itself, typically to cope with slowly occurring changes of the controlled
system [10].  For example, the main feedback loop, which controls a web server
farm, reacts rapidly to bursts of Internet load to manage quality of service (e.g.,
dynamically upscaling).  A second slow-reacting feedback loop may adjust the
controller algorithm to accommodate or take advantage of changes emerging over
time (e.g., increase resource provision to anticipate periods of high activity).
Besides the specific structure of the feedback loop, a key feature of control-
based adaptation is the way the target system is modelled, e.g., with difference
equations (discrete time) or differential equations (continuous time).  Such mod-
els allow to mathematically analyse and verify a number of key properties of
computing systems.  These properties are illustrated in Figure 15.
## Overshoot
Steady-state error
Setting time
## Setpoint
Controlled variable
TimeTransient stateSteady state
Figure 15:  Properties of control-based adaptation
Overshootis  the  maximum  value  by  which  the  system  output  surpasses
the setpoint during the transient phase.Settling  timeis the time required to
converge the controlled variable to the setpoint.  The amplitude of oscillations of
the system output around the setpoint during steady state is called thesteady-
state error.  In addition,stabilityrefers to the ability of the system to converge
to the setpoint, whilerobustnessrefers to the amount of disturbance the system
can withstand while remaining in a stable state.  These control properties can
be mapped to software qualities.  For example, overshoot or settling time may
influence the performance or availability of the application.
Historically, the application of control to computing systems has primarily
targeted  the  adaptation  of  lower  level  elements  of  computing  systems,  such
as  the  number  of  CPU  cores,  network  bandwidth,  and  the  number  of  virtual
machines [46].  The sixth wave manifested itself through an increasing focus on
the  application  of  control  theory  to  design  self-adaptivesoftwaresystems.   A
prominent example is the Push-Button Methodology (PBM) [27].  PBM works
in two phases as illustrated in Figure 16.
In themodel  building  phase,  a linear model of the software is constructed
automatically.  The model is identified by running on-the-fly experiments on the
software.  In particular, the system tests a set of sampled values of the control
variable and measures the effects on specified non-functional requirement.  The
## 30


## Controlling
## Disturbances

## Target
## System
## Output
## Setpoint
## +
## -

## Model
## Building
Figure 16:  Two phases of PBM (based on [27])
result  is  a  mapping  of  variable  settings  to  measured  feedback.   For  example,
model  building  measures  response  time  for  different  number  of  servers  of  a
Web-based  system.   In  thecontroller  synthesis  phasea  PI-controller  uses  the
synthesised  model  to  adapt  the  software  automatically.   For  example,  in  the
Web-based system, the controller selects the number of servers that need to be
allocated to process the load while guaranteeing the response time goal.
To deal with possible errors of the model, the model parameters are updated
at runtime according to the system behaviour.  For example, if one of the servers
in the Web-based system starts to slow down the system response due to over-
heating, an additional server will be allocated.  In case of radical changes, such
a failure of a number of servers, a rebuilding of the model is triggered.
A major benefit of a control-theoretic approach such as PBM is that it can
provide  formal  guarantees  for  system  stability,  absence  of  overshoot,  settling
time, and robustness.  Guarantees for settling time and robustness depend on
the so called controller pole (a parameter of the controller that can be set by
the designer).  Higher pole values improve robustness but lead to higher settling
times,  while  smaller  pole  values  reduce  robustness  but  improve  settling  time.
In other words, the pole allows trading-off the responsiveness of the system to
change with the ability to withstand disturbances of high amplitude.
PBM is a foundational approach that realises self-adaptation based on prin-
ciples of control theory.  However, basic PBM only works for a single setpoint
goal.  Examples of follow-up research that can deal with multiple requirements
are AMOCS [28] and SimCA [51].  For a recent survey on control-adaptation of
software systems, we refer the interested reader to [50].
Table 11 summarises the key insights derived from Wave VI.
## 4  Future Challenges
Now, we peak into the future of the field and propose a number of research
challenges for the next five to ten years to come.  But before zooming into these
challenges, we first analyse how the field has matured over time.
## 31

Table 11:  Key insights of Wave V: Control-Based Approaches
•Control  theory  offers  a  mathematical  foundation  to  design  and  formally  analyse
self-adaptive systems.
•Adaptive controllers that are able to adjust the controller strategy at runtime are
particularly interesting to control computing systems.
•Control theory allows providing analytical guarantees for stability of self-adaptive
systems, absence of overshoot, settling time, and robustness.
•Linear models combined with online updating mechanisms have demonstrated to
be very useful for a variety of control-based self-adaptive systems.
4.1  Analysis of the Maturity of the Field
According to a study of Redwine and Riddle [48] it typical takes 15 to 20 years
for  a  technology  to  mature  and  get  widely  used.   Six  common  phases  can  be
distinguished as shown in Figure 17.  In the first phase,basic research, the basic
## Basic Research
## Concept Formulation
Development/Extension
External Enhancement/Exploration
## Popularisation
quiescence, runtime architecture model, MAPE-K, adaptation
strategies and tactics, component models, workshops
Foundations: dynamic architectures, feedback loops, reasoning with uncertainty, control theory
feedback control mechanisms, modeling dimensions,
models at runtime, goal-driven design, community
symposia, dedicated volumes
patterns, engineering processes, control
theoretic solutions, publications in top
conferences and journals, exemplars, books
meta-requirements, runtime probabilistic models, quality
metrics, formal analysis at runtime, special issues
Industry efforts e.g; IBM Autonomic
Toolkit, IBM/Google Large- Scale
Internet Computing initiative
## Time
## 1990s....
## 2006
## 2016
Autonomic Computing IBM, N1 Sun,
Adaptive Enterprise HP, Dynamic
Systems Microsoft, etc.
Internal Enhancement/Exploration
Figure 17:  Maturation of the field of self-adaptation.  Grey shades indicate the
degree the field has reached maturity in that phase (phases based on [48])
ideas  and  principles  of  the  technology  are  developed.   Research  in  the  ICAC
community
## 9
has made significant contributions to the development of the basic
## 9
http://nsfcac.rutgers.edu/conferences/ac2004/index.html
## 32

ideas  and  principles  of  self-adaptation.   Particularly  relevant  in  this  develop-
ment were also the two editions of the Workshop on Self-Healing Systems.
## 10
## In
the second phase,concept formulation, a community is formed around a set of
compatible concepts ideas and solutions are formulated on specific subproblems.
The SEAMS symposium
## 11
and in particular, the series of Dagstuhl seminars
## 12
on engineering self-adaptive systems have significantly contributed to the matu-
ration in this phase. In the third phase,development and extension, the concepts
and principles are further developed and the technology is applied to various
applications leading to a generalisation of the approach. Phase four,internal en-
hancement and exploration, the technology is applied to concrete real problems,
and training is established.  The establishment of exemplars
## 13
is currently play-
ing an important role to the further maturation of the field.  Phase five,external
enhancement and exploration, involving a broader community to show evidence
of value and applicability of the technology, is still in its early stage.  Various
prominent ICT companies have invested significantly in the study and applica-
tion of self-adaptation [9], example initiatives are IBM’s Autonomic Comput-
ing, Sun?s N1, HP’s Adaptive Enterprise, and Microsoft’s Dynamic Systems.  A
number of recent R&D efforts have explored the application of self-adaptation
beyond mere resource and infrastructure management.  For example, [14] ap-
plies self-adaptation to an industrial middleware to monitor and manage highly
populated  networks  of  devices,  while  [19]  applies  self-adaptive  techniques  to
role-based access control for business processes.  Nevertheless, the effect of self-
adaptation in practice so far remains relatively low [56].  Finally, the last phase,
popularisation, where production-quality technology is developed and commer-
cialised is in a very early stage for self-adaptation.  Examples of self-adaption
techniques that have found their way to industrial applications are automated
server management, cloud elasticity, and automated data centre management.
In conclusion, after a relatively slow start, research in the field of self-adaptation
has taken up significantly from 2006 onwards and is now following the regular
path of maturation.  The field is currently in the phases of internal and external
enhancement and exploration.  The application of self-adaptation to practical
applications will be of critical importance for the field to reach full maturity.
## 4.2  Challenges
After  the  brief  maturity  analysis  of  the  field,  we  look  now  at  challenges  that
may be worth focusing at in the years to come.
Predicting the future is obviously a difficult and risky task.  The community
has produced several roadmap papers in the past years, in particular [15], [21],
and  [20].  These roadmap papers provide a wealth of research challenges struc-
tured along different aspects of engineering self-adaptive systems.  Here we take
a different stance and present open research challenges by speculating how the
## 10
http://dblp2.uni-trier.de/db/conf/woss/
## 11
www.hpi.uni-potsdam.de/giese/public/selfadapt/seams/
## 12
www.hpi.uni-potsdam.de/giese/public/selfadapt/dagstuhl-seminars/
## 13
www.hpi.uni-potsdam.de/giese/public/selfadapt/exemplars/
## 33

field may evolve in the future based on the six waves the field went through in
the past.  We start with a number of short term challenges within current waves.
Then we look at challenges in a long term that go beyond the current waves.
4.2.1    Challenges Within the Current Waves
Adaptation in decentralised settings. A principal insight of the first wave is
that MAPE represents the essential functions of any self-adaptive system.  Con-
ceptually,  MAPE  takes  a  centralised  perspective  on  realising  self-adaptation.
When systems are large and complex, a single centralised MAPE loop may not
be sufficient for managing all adaptation in a system.  A number or researchers
have investigated decentralisation of the adaptation functions; recent examples
are [61] where the authors describe a set of patterns in which the functions from
multiple MAPE loops are coordinated in different ways, and [12] that presents
a formal approach where MAPE loops coordinate with one another to provide
guarantees for the adaptation decisions they make.  A challenge for future re-
search is to study principled solutions to decentralised self-adaptation.  Crucial
aspects to this challenge are coordination mechanisms and interaction protocols
that MAPE loops require to realise different types of adaptation goals.
Deal  with  changing  goals.   One  of  the  key  insights  of  the  second  wave  is
that  the  two  basic  aspects  of  self-adaptive  systems  are  change  management
(i.e., manage adaptation) and goal management (manage high-level goals).  The
focus of research so far has primarily been on change management.  Goal man-
agement  is  basically  limited  to  runtime  representations  of  goals  that  support
the decision making of adaptation under uncertainty.  A typical example is [6],
where goal realisation strategies are associated with decision alternatives and
reasoning about partial satisfaction of goals is supported using probabilities.  A
challenge for future research is to support changing goals at runtime, including
removing and adding goals.  Changing goals is particularly challenging.  First, a
solution to this challenge requires goal models that provide first class support
for change.  Current goal modelling approaches (wave four) take into account
uncertainty, but these approaches are not particularly open for changing goals
dynamically.   Second,  a  solution  requires  automatic  support  for  synthesising
new plans that comply with the changing goals.  An example approach in this
direction is ActivFORMS that supports on-the-fly updates of goals and the cor-
responding MAPE functions [34].  However, this approach requires the engineer
to  design  and  verify  the  updated  models  before  they  are  deployed.   The  full
power of dealing with changing goals would be a solution that enables the sys-
tem itself to synthesize and verify new models.
Domain  specific  modelling  languages.   Wave  three  has  made  clear  that
(runtime) models play a central role in the realisation of self-adaptive systems.
A number of modelling languages have been proposed that support the design
of self-adaptive systems, but often these languages have a specific focus.  An ex-
ample is Stitch, a language for representing repair strategies within the context
of architecture-based self-adaptation [17].  However, current research primarily
## 34

relies on general purpose modelling paradigms.  A challenge for future research
is to define domain specific modelling languages that provide first-class support
for  engineering  self-adaptive  systems  effectively.   Contrary  to  traditional  sys-
tems, where models are primarily design-time artifacts, in self-adaptive systems
models are runtime artifacts.  Hence, it will be crucial for modelling languages
that they seamlessly integrate design time modelling (human-driven) with run-
time  use  of  models  (machine-driven).   An  example  approach  in  this  direction
is EUREMA that supports the explicit design of feedback loops, with runtime
execution and adaptation [55].
Deal with complex types of uncertainties.  Wave five has made clear that
handling  uncertainty  is  one  of  the  “raisons  d’ˆetre”  for  self-adaptation.   The
focus of research in self-adaptation so far has primarily been on parametric un-
certainties, i.e., the uncertainties related to the values of model elements that
are  unknown.   A  typical  example  is  a  Markov  model  in  which  uncertainties
are  expressed  as  probabilities  of  transitions  between  states  (Figure  12  shows
an example).  A challenge for future research is to support self-adaptation for
complex  types  of  uncertainties.   One  example  is  structural  uncertainties,  i.e.
uncertainties related to the inability to accurately model real-life phenomena.
Structural uncertainties may manifest themselves as model inadequacy, model
bias,  model  discrepancy,  etc.  To  tackle  this  problem,  techniques  from  other
fields may provide a starting point.  E.g., in health economics, techniques such
as  model  averaging  and  discrepancy  modelling  have  been  used  to  deal  with
structural uncertainties [8].
Empirical evidence for the value of self-adaptation.  Self-adaptation is
widely  considered  as  one  of  the  key  approaches  to  deal  with  the  challenging
problem  of  uncertainty.   However,  as  pointed  out  in  a  survey  of  a  few  years
ago, the validation of research contributions is often limited to simple example
applications [56].  An important challenge that crosscuts the different waves will
be to develop robust approaches and demonstrate their applicability and value
in practice.  Essential to that will be the gathering of empirical evidence based
on rigorous methods, in particular controlled experiments and case studies.  Ini-
tially, such studies can be set up with advanced master students (one of the few
examples is [59]).  However, to demonstrate the true value of self-adaptation, it
will be essential to involve industry practitioners in such validation efforts.
Align with emerging technologies.  A variety of new technologies are emerg-
ing that will have a deep impact on the field self-adaptation.  Among these are
the Internet of Things, Cyber Physical Systems, 5G and Big Data.  On the one
hand,  these technologies can serve as enablers for progress in self-adaptation;
e.g., 5G has the promise of offering extremely low latency.  On the other hand,
they can serve as new areas of self-adaptation,  e.g.,  adaptation in support of
auto-configuration in large-scale Internet of Things applications.  A challenge for
future research is to align self-adaptation with emerging technologies.  Such an
alignment will be crucial to demonstrate practical value for future applications.
An initial effort in this direction is [45] where the authors explore the use of run-
## 35

time variability in feature models to address the problem of dynamic changes
in (families of) sensor networks.  [11] outlines an interesting set of challenges for
self-adaption in the domain of Cyber Physical Systems.
4.2.2    Challenges Beyond the Current Waves
To conclude, we speculate on a number of challenges in the long term that may
trigger new waves of research in the field of self-adaptation.
Exploiting  artificial  intelligence.   Artificial  intelligence  (AI)  provides  the
ability for systems to learn,  improve,  and make decisions in order to perform
complex tasks [31].  The field of AI is broad and ranges from expert systems
and decision-support systems, to multi-agent systems, computer vision, natural
language processing, speech recognition, machine learning, neural networks and
deep learning, and cognitive computation, among others.  Some areas in which
AI techniques have proved to be useful in software engineering in general are
probabilistic reasoning, learning and prediction, and computational search [32].
A number of AI techniques have been turned into mainstream technology, such
as machine learning and data analytics.  Other techniques are still in a develop-
ment phase, examples are natural language processing and online reasoning. The
application of AI techniques to self-adaptation has the potential to disruptively
propelling  the  capabilities  of  such  systems.   AI  techniques  can  play  a  central
role  in  virtually  every  stage  of  adaptation,  from  processing  large  amounts  of
data, performing smart analysis and machine-man co-decision making, to coor-
dinating adaptations in large-scale decentralised systems.  Realising this vision
poses  a  variety  of  challenges,  including  advancing  AI  techniques,  making  the
techniques  secure  and  trustworthy,  and  providing  solutions  for  controlling  or
predicting the behaviour of systems that are subject to continuous change.  An
import remark of P. Norvig in this context is that AI programs are different.
One of the key differences is that AI techniques are fundamentally dealing with
uncertainty,  while  traditional  software  are  essentially  hiding  uncertainty  [43].
This stresses the potential of AI techniques for self-adaptive systems.
Dealing with unanticipated change.  Software is (so far) a product of hu-
man efforts.  Ultimately, a computing machine will only be able to execute what
humans have designed for and programmed.  Nevertheless, recent advances have
demonstrated that machines equipped with software can be incredible capable
of making decisions for complex problems, examples are machines participating
in complex strategic games such as chess and self-driving cars.  Such examples
raise the intriguing question to what extent we can develop software that can
handle conditions that were not anticipated at the time when the software was
developed.  From the point of view of self-adaptation,  an interesting research
problem is how to deal with unanticipated change.  One possible perspective on
tackling this problem is to seamlessly integrate adaptation (i.e., the continuous
machine-driven process of self-adaptation to deal with known unknowns) with
evolution (i.e., the continuous human-driven process of updating the system to
deal with unknown unknowns).  This idea goes back to the pioneering work of
## 36

Oreizy et al. on integrating adaptation and evolution [44].  Realising this idea
will require bridging the fields of self-adaptation and software evolution.
Control theory as a scientific foundation for self-adaptation.  Although
researchers in the field of self-adaptation have established solid principles, such
as  quiescence,  MAPE,  meta-requirements,  and  runtime  models,  there  is  cur-
rently no comprehensive theory that underpins self-adaptation.  An interesting
research challenge is to investigate whether control theory can provide such a
theoretical  foundation  for  self-adaptation.   Control  theory  comes  with  a  solid
mathematical basis and (similarly to self-adaptation) deals with the behaviour
of  dynamical  systems  and  how  their  behaviour  is  modified  through  feedback.
Nevertheless,  there  are  various  hurdles  that  need  to  be  tackled  to  turn  con-
trol theory into the foundation of self-adaptation of software systems.  One of
the hurdles is the difference in paradigms.  Software engineers have systematic
methods for the design, development, implementation, testing and maintenance
of software.  Engineering based on control theory on the other hand offers an-
other  paradigm  where  mathematical  principles  play  a  central  role,  principles
that may not be easily accessible to typical software engineers.  Another more
concrete hurdle is the discrepancy between the types of adaptation goals that
self-adaptive software systems deal with (i.e., software qualities such as reliabil-
ity and performance), and the types of goals that controllers deal with (i.e., typ-
ically setpoint centred).  Another hurdle is the discrepancy between the types
of  guarantees  that  self-adaptive  software  systems  require  (i.e.,  guarantees  on
software qualities) and the types of guarantees that controller provide (settling
time, overshoot, stability, etc.).  These and other hurdles need to be overcome
to turn control theory into a scientific foundation for self-adaptation.
Multi-disciplinarity.  Every day, we observe an increasing integration of com-
puting  systems  and  applications  that  are  shaping  a  world-wide  ecosystem  of
software-intensive systems, humans, and things.  An example is the progressing
integration of different IoT platforms and applications that surround us, forming
smart cities.  Such integrations have the potential to generate dramatic syner-
gies; for a discussion see for example [24].  However, the evolution towards this
world-wide ecosystem comes with enormous challenges.  These challenges are of
a technical nature (e.g., how to ensure security in an open world, how to ensure
stability in a decentralised ecosystem that is subject to continuous change), but
also business-oriented (e.g., what are suitable business models for partners that
operate  in  settings  where  uncertainty  is  the  rule),  social  (e.g.,  what  are  suit-
able methods for establishing trust) and legal (e.g., what legal frameworks are
needed for systems that continuously change).  Clearly, the only way forward to
tackle these challenges is to join forces between disciplines and sectors.
## 5  Conclusions
In a world where computing systems rapidly converge into large open ecosys-
tems,  uncertainty  is  becoming  the  de-facto  reality  of  most  systems  we  build
## 37

today, and it will be a dominating element of any system we will build in the
future.   The  challenges  software  engineers  face  to  tame  uncertainty  are  huge.
Self-adaptation has an enormous potential to tackle many of these challenges.
The field has gone a long way and a substantial body of knowledge has been
developed over the past two decades.  Building upon established foundations,
addressing key challenges now requires consolidating the knowledge and turn-
ing  results  into  robust  and  reusable  solutions  to  move  the  field  forward  and
propagate the technology throughout a broad community of users in practice.
Tackling these challenges is not without risk as it requires researchers to leave
their comfort zone and expose the research results to the complexity of practical
systems.  However, taking this risk will propel research, open new opportunities,
and pave the way towards reaching full maturity as a discipline.
## Acknowledgements
I am grateful to Sungdeok Cha, Kenji Tei, Nelly Bencomo, Vitor Souza, Usman
Iftikhar, Stepan Shevtsov, and Dimitri Van Landuyt for the invaluable feedback
they provided on earlier versions of this chapter.  I thank the editors of the book
to which this chapter belongs for their support.  Finally, I thank Springer.
## References
[1]  J.  Andersson,  R.  De  Lemos,  S.  Malek,  and  D.  Weyns.    Modelling  Di-
mensions of Self-adaptive Software Systems.  InSoftware  Engineering  for
Self-Adaptive Systems, volume 5525 ofLecture Notes in Computer Science.
## Springer, 2009.
[2]  J. Andersson, R. de Lemos, S. Malek, and D. Weyns.  Reflecting on Self-
adaptive Software Systems. InSoftware Engineering for Adaptive and Self-
Managing Systems, SEAMS ’09. IEEE Computer Society, 2009.
[3]  M. Baldauf,  S. Dustdar,  and F. Rosenberg.  A Survey on Context-aware
Systems.International  Journal  on  Ad  Hoc  and  Ubiquitous  Computing,
## 2(4):263–277, June 2007.
[4]  L.   Baresi   and   C.   Ghezzi.The   Disappearing   Boundary   Between
Development-time and Run-time.  InWorkshop on Future of Software En-
gineering Research, FoSER ’10. ACM, 2010.
[5]  L. Baresi,  L. Pasquale,  and P. Spoletini.  Fuzzy Goals for Requirements-
Driven Adaptation. InInternational Requirements Engineering Conference,
RE ’10. IEEE Computer Society, 2010.
[6]  N.  Bencomo  and  A.  Belaggoun.Supporting  decision-making  for  self-
adaptive  systems:   From  goal  models  to  dynamic  decision  networks.   In
International Working Conference on Requirements Engineering:  Founda-
tion for Software Quality, REFSQ ’13. Springer Berlin Heidelberg, 2013.
## 38

[7]  G.  Blair,  N.  Bencomo,  and  R.  B.  France.   Models@run.time.Computer,
## 42(10):22–27, 2009.
[8]  L. Bojke, K. Claxton, M. Sculpher, and Palmer S.  Characterizing Struc-
tural Uncertainty in Decision Analytic Models:  A Review and Application
of Methods.Value Health, 12(5):739–749, 2009.
[9]  Y. Brun.  Improving Impact of Self-adaptation and Self-management Re-
search  Through  Evaluation  Methodology.    InSoftware  Engineering  for
Adaptive and Self-Managing Systems, SEAMS ’10. ACM, 2010.
## [10]  Y. Brun, G. Marzo Serugendo, C. Gacek, H. Giese, H. Kienle, M. Litoiu,
H. M ̈uller, M. Pezz`e, and M. Shaw. Software Engineering for Self-Adaptive
Systems.   chapter  Engineering  Self-Adaptive  Systems  Through  Feedback
Loops, pages 48–70. Springer-Verlag, 2009.
## [11]  T. Bures, D. Weyns, C. Berger, S. Biffl, M. Daun, T. Gabor, D. Garlan,
I. Gerostathopoulos, C. Julien, F. Krikava, R. Mordinyi, and N. Pronios.
Software Engineering for Smart Cyber-Physical Systems – Towards a Re-
search Agenda.SIGSOFT Software Engineering Notes, 40(6):28–32, 2015.
[12]  R.  Calinescu,  S.  Gerasimou,  and  A.  Banks.   Self-adaptive  software  with
decentralised control loops.  InInternational  Conference  on  Fundamental
Approaches to Software Engineering, FASE ’15. Springer, 2015.
[13]  R. Calinescu, L. Grunske, M. Kwiatkowska, R. Mirandola, and G. Tambur-
relli.  Dynamic QoS Management and Optimization in Service-Based Sys-
tems.IEEE Transactions on Software Engineering, 37(3):387–409, 2011.
[14]  Javier  C ́amara,  Pedro  Correia,  Rog ́erio  De  Lemos,  David  Garlan,  Pedro
Gomes,  Bradley  Schmerl,  and  Rafael  Ventura.   Evolving  an  adaptive  in-
dustrial software system to use architecture-based self-adaptation.  InPro-
ceedings  of  the  8th  International  Symposium  on  Software  Engineering  for
Adaptive  and  Self-Managing  Systems,  SEAMS  ’13,  pages  13–22,  Piscat-
away, NJ, USA, 2013. IEEE Press.
[15]  B. Cheng,  R. de Lemos,  H. Giese,  P. Inverardi,  J. Magee,  J. Andersson,
## B.  Becker,  N.  Bencomo,  Y.  Brun,  B.  Cukic,  G.  Di  Marzo  Serugendo,
S.  Dustdar,  A.  Finkelstein,  C.  Gacek,  K.  Geihs,  V.  Grassi,  G.  Karsai,
H.  Kienle,  J.  Kramer,  M.  Litoiu,  S.  Malek,  R.  Mirandola,  H.  M ̈uller,
S. Park, M. Shaw, M. Tichy, M. Tivoli, D. Weyns, and J. Whittle.Software
Engineering  for  Self-Adaptive  Systems:   A  Research  Roadmap.   Springer
Berlin Heidelberg, Lecture Notes in Computer Science vol. 5525, 2009.
[16]  B. Cheng,  P. Sawyer,  N. Bencomo,  and J. Whittle.  A Goal-Based Mod-
elling Approach to Develop Requirements of an Adaptive System with En-
vironmental  Uncertainty.   InInternational  Conference  on  Model  Driven
Engineering Languages and Systems, MODELS ’09. Springer-Verlag, 2009.
## 39

[17]  S. Cheng and D. Garlan.  Stitch:  A language for architecture-based self-
adaptation.Journal of Systems and Software, 85(12):2860–2875, 2012.
[18]  IBM Corporation.  An Architectural Blueprint for Autonomic Computing.
IBM  White  Paper,  2003.    http://www-03.ibm.com/autonomic/pdfs/AC
Blueprint White Paper V7.pdf (last accessed:  1/2017).
[19]  Carlos Eduardo da Silva, Jos ́e Diego Saraiva da Silva, Colin Paterson, and
Radu Calinescu.  Self-adaptive role-based access control for business pro-
cesses.   InProceedings  of  the  12th  International  Symposium  on  Software
Engineering  for  Adaptive  and  Self-Managing  Systems, SEAMS ’17, pages
193–203, Piscataway, NJ, USA, 2017. IEEE Press.
[20]  R.  de  Lemos,  D.  Garlan,  C.  Ghezzi,  H.  Giese,  J.  Andersson,  M.  Litoiu,
## B. Schmerl, D. Weyns, L. Baresi, N. Bencomo, Y. Brun, J. Camara, R. Ca-
linescu,  M.  Chohen,  A.  Gorla,  V.  Grassi,  L.  Grunske,  P.  Inverardi,  JM.
## Jezequel, S. Malek, R. Mirandola, M. Mori, H. M ̈uller, R. Rouvoy, C. Ru-
bira, E. Rutten, M. Shaw, Tamburrelli, G. Tamura, N. Villegas, T. Vogel,
and F. Zambonelli.Software  Engineering  for  Self-adaptive  Systems:  Re-
search Challenges in the Provision of Assurances.  Springer Berlin Heidel-
berg, Lecture Notes in Computer Science vol. 9640, 2017.
[21]  R.  de  Lemos,  H.  Giese,  H.  M ̈uller,  M.  Shaw,  J.  Andersson,  M.  Litoiu,
## B.  Schmerl,  G.  Tamura,  N.  Villegas,  T.  Vogel,  D.  Weyns,  L.  Baresi,
## B.  Becker,  N.  Bencomo,  Y.  Brun,  B.  Cukic,  R.  Desmarais,  S.  Dustdar,
## G. Engels, K. Geihs, K. G ̈oschka, A. Gorla, V. Grassi, P. Inverardi, G. Kar-
sai,  J. Kramer,  A. Lopes,  J. Magee,  S. Malek,  S. Mankovskii,  R. Miran-
dola,  J.  Mylopoulos,  O.  Nierstrasz,  M.  Pezz`e,  C.  Prehofer,  W.  Sch ̈afer,
R. Schlichting, D. Smith, J. Sousa, L. Tahvildari, K. Wong, and J. Wut-
tke.Software  Engineering  for  Self-Adaptive  Systems:  A  Second  Research
Roadmap.  Springer Heidelberg Berlin, Lecture Notes in Computer Science
vol. 7475, 2013.
[22]  T. De Wolf and T. Holvoet. Emergence Versus Self-Organisation: Different
Concepts but Promising When Combined.  InEngineering Self-Organising
Systems:  Methodologies and Applications, pages 1–15. Springer Berlin Hei-
delberg, 2005.
[23]  Pedro C. Diniz and Martin C. Rinard.  Dynamic Feedback:  An Effective
Technique for Adaptive Computing.  InConference on Programming Lan-
guage Design and Implementation, PLDI ’97. ACM, 1997.
[24]  S. Dustdar, S. Nastic, and O. Scekic. A novel vision of cyber-human smart
city.  In2016 Fourth IEEE Workshop on Hot Topics in Web Systems and
Technologies (HotWeb), pages 42–47, Oct 2016.
[25]  G.   Edwards,   J.   Garcia,   H.   Tajalli,   D.   Popescu,   N.   Medvidovic,
G. Sukhatme, and B. Petrus. Architecture-driven Self-adaptation and Self-
management in Robotics Systems.  InSoftware  Engineering  for  Adaptive
and Self-Managing Systems, SEAMS ’09. IEEE, 2009.
## 40

[26]  N. Esfahani and S. Malek. Uncertainty in self-adaptive software systems. In
Software Engineering for Self-Adaptive Systems II, pages 214–238. Springer
## Berlin Heidelberg, 2013.
[27]  A. Filieri, H. Hoffmann, and M. Maggio. Automated Design of Self-adaptive
Software  with  Control-theoretical  Formal  Guarantees.    InInternational
Conference on Software Engineering, ICSE ’14. ACM, 2014.
[28]  A. Filieri, H. Hoffmann, and M. Maggio.  Automated Multi-objective Con-
trol for Self-adaptive Software Design. InJoint Meeting on Foundations of
Software Engineering, ESEC/FSE ’15. ACM, 2015.
[29]  D. Garlan, S. Cheng, A. Huang, B. Schmerl, and P. Steenkiste.  Rainbow:
Architecture-Based  Self-Adaptation  with  Reusable  Infrastructure.Com-
puter, 37(10):46–54, 2004.
[30]  D. Gil and D. Weyns.  MAPE-K Formal Templates to Rigorously Design
Behaviors for Self-Adaptive Systems.ACM  Transactions  on  Autonomous
and Adaptive Systems, 10(3):15:1–15:31, 2015.
[31]  Anne Hakansson.  Artificial intelligence in smart sustainable societies.
[32]  Mark  Harman.  The  role  of  artificial  intelligence  in  software  engineering.
InRealizing AI Synergies in Software Engineering, RAISE ’12, Piscataway,
NJ, USA, 2012. IEEE Press.
[33]  J.  Hellerstein,  Y.  Diao,  S.  Parekh,  and  D.  Tilbury.Feedback  Control  of
## Computing Systems.  John Wiley & Sons, 2004.
[34]  U. Iftikhar and D. Weyns.  ActivFORMS: Active Formal Models for Self-
adaptation.  InSoftware Engineering for Adaptive and Self-Managing Sys-
tems, SEAMS ’14. ACM, 2014.
[35]  M. Jackson.  The Meaning of Requirements.Annals of Software Engineer-
ing, 3:5–21, 1997.
[36]  J. Kephart and D. Chess. The Vision of Autonomic Computing.Computer,
## 36(1):41–50, 2003.
[37]  J. Kramer and J. Magee.  Self-Managed Systems:  An Architectural Chal-
lenge.  InFuture of Software Engineering, FOSE ’07. IEEE Computer So-
ciety, 2007.
[38]  Jeff  Kramer  and  Jeff  Magee.   The  Evolving  Philosophers  Problem:  Dy-
namic Change Management.IEEE Transactions on Software Engineering,
## 16(11):1293–1306, 1990.
[39]  M. Kwiatkowska, G. Norman, and D. Parker. Probabilistic symbolic model
checking  with  prism:   A  hybrid  approach.   InTools  and  Algorithms  for
the  Construction  and  Analysis  of  Systems,  TACAS  ’02.  Springer  Berlin
## Heidelberg, 2002.
## 41

[40]  S. Mahdavi-Hezavehi, P. Avgeriou, and D. Weyns. A Classification of Cur-
rent Architecture-based Approaches Tackling Uncertainty in Self-Adaptive
Systems with Multiple Requirements. InManaging Trade-offs in Adaptable
## Software Architectures. Elsevier, 2016.
[41]  B. Morin, O. Barais, J.M. Jezequel, F. Fleurey, and A. Solberg.  Models at
Runtime to Support Dynamic Adaptation.IEEE Computer, 42(10):44–51,
## 2009.
[42]  P.  Naur  and  B.  Randell.   Software  Engineering:  Report  of  a  Conference
Sponsored by the NATO Science Committee.Brussels,  Scientific  Affairs
Division, NATO, 1968.
[43]  Peter Norvig.Artificial  intelligence  in  the  software  engineering  workflow.
Google,  2017.   See:  https://www.youtube.com/watch?v=mJHvE2JLN3Q
and https://www.youtube.com/watch?v=FmHLpraT-XY.
[44]  P.  Oreizy,  N.  Medvidovic,  and  R.  Taylor.   Architecture-based  Runtime
Software Evolution.  InInternational Conference on Software Engineering,
ICSE ’98. IEEE Computer Society, 1998.
## [45]
## ́
O. Ortiz, A. B. Garc ́ıa, R. Capilla, J. Bosch, and M. Hinchey. Runtime Vari-
ability for Dynamic Reconfiguration in Wireless Sensor Network Product
## Lines.  In16th  International  Software  Product  Line  Conference  -  Volume
## 2. ACM, 2012.
[46]  T. Patikirikorala, A. Colman, J. Han, and Liuping W. A Systematic Survey
on the Design of Self-adaptive Software Systems using Control Engineer-
ing Approaches.  InSoftware Engineering for Adaptive and Self-Managing
Systems, SEAMS ’12, 2012.
[47]  D. Perez-Palacin and R. Mirandola. Uncertainties in the Modelling of Self-
adaptive Systems: A Taxonomy and an Example of Availability Evaluation.
InInternational Conference on Performance Engineering, ICPE ’14, 2014.
[48]  S.  Redwine  and  W.  Riddle.   Software  Technology  Maturation.   InInter-
national  Conference  on  Software  Engineering, ICSE ’85. IEEE Computer
## Society Press, 1985.
[49]  M. Salehie and L. Tahvildari.  Self-adaptive Software:  Landscape and Re-
search  Challenges.Transactions  on  Autonomous  and  Adaptive  Systems,
## 4:14:1–14:42, 2009.
[50]  S. Shevtsov, M. Berekmeri, D. Weyns, and M. Maggio. Control-theoretical
software adaptation:  A systematic literature review.IEEE  Transactions
on Software Engineering, PP(99):1–1, 2017.
[51]  S. Shevtsov and D. Weyns.  Keep it SIMPLEX: Satisfying Multiple Goals
with Guarantees in Control-Based Self-Adaptive Systems. InInternational
Symposium on the Foundations of Software Engineering, FSE ’16, 2016.
## 42

[52]  V. Silva Souza, A. Lapouchnian, W.. Robinson, and J. Mylopoulos. Aware-
ness  Requirements  for  Adaptive  Systems.    InSoftware  Engineering  for
Adaptive and Self-Managing Systems, SEAMS ’11. ACM, 2011.
[53]  V.  Silva  Souza,  A.  Lapouchnian,  K.  Angelopoulos,  and  J.  Mylopoulos.
Requirements-driven software evolution.Computer Science - Research and
## Development, 28(4):311–329, 2013.
[54]  A.  van  Lamsweerde,  R.  Darimont,  and  E.  Letier.   Managing  conflicts  in
goal-driven requirements engineering.IEEE Transactions on Software En-
gineering, 24(11):908–926, Nov 1998.
[55]  T. Vogel and H. Giese. Model-Driven Engineering of Self-Adaptive Software
with EUREMA.ACM Transactions on Autonomous and Adaptive Systems,
## 8(4):18:1–18:33, 2014.
[56]  D.  Weyns  and  T.  Ahmad.Claims  and  Evidence  for  Architecture-Based
Self-adaptation:  A Systematic Literature Review, pages 249–265.  Springer
## Berlin Heidelberg, Berlin, Heidelberg, 2013.
[57]  D.  Weyns,  N.  Bencomo,  R.  Calinescu,  J.  C ́amara,  C.  Ghezzi,  V.  Grassi,
L. Grunske, P. Inverardi, J.M. Jezequel, S. Malek, R. Mirandola, M. Mori,
and G. Tamburrelli.  Perpetual Assurances in Self-Adaptive Systems.  In
Software  Engineering  for  Self-Adaptive  Systems,  volume  9640  ofLecture
Notes in Computer Science. Springer, 2016.
[58]  D. Weyns and R. Calinescu.  Tele assistance:  A self-adaptive service-based
system examplar.  InProceedings  of  the  10th  International  Symposium  on
Software  Engineering  for  Adaptive  and  Self-Managing  Systems,  SEAMS
’15, pages 88–92, Piscataway, NJ, USA, 2015. IEEE Press.
[59]  D.  Weyns,  U.  Iftikhar,  and  J.  S ̈oderlund.   Do  External  Feedback  Loops
Improve the Design of Self-Adaptive Systems?  A Controlled Experiment.
InInternational Symposium on Software Engineering of Self-Managing and
Adaptive Systems, SEAMS ’13, 2013.
[60]  D. Weyns, S. Malek, and J. Andersson. FORMS: Unifying Reference Model
for Formal Specification of Distributed Self-adaptive Systems.ACM Trans-
actions on Autonomous and Adaptive Systems, 7(1):8:1–8:61, 2012.
[61]  D.  Weyns,  B.  Schmerl,  V.  Grassi,  S.  Malek,  R.  Mirandola,  C.  Prehofer,
J. Wuttke, J. Andersson, H. Giese, and K. G ̈oschka.  On patterns for de-
centralized  control  in  self-adaptive  systems.   InSoftware  Engineering  for
Self-Adaptive Systems II, pages 76–107. Springer, 2013.
[62]  J. Whittle, P. Sawyer, N. Bencomo, B. Cheng, and J.M. Bruel. RELAX: In-
corporating Uncertainty into the Specification of Self-Adaptive Systems. In
IEEE  International  Requirements  Engineering  Conference, RE ’09. IEEE
## Computer Society, 2009.
## 43
