---
source: https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf
description: "Full-text capture of the Parasuraman-Sheridan-Wickens framework for allocating automation across four function types and graded levels of human interaction."
captured: 2026-07-21
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# A Model for Types and Levels of Human Interaction with Automation

Authors: Raja Parasuraman, Thomas B. Sheridan, and Christopher D. Wickens
Source: https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf
Date: 2000 (IEEE Transactions on Systems, Man, and Cybernetics—Part A, 30(3), 286–297)

286IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
A Model for Types and Levels of Human Interaction
with Automation
Raja Parasuraman, Thomas B. Sheridan, Fellow, IEEE, and Christopher D. Wickens
Abstract—Technical developments in computer hardware and
software now make it possible to introduce automation into virtu-
ally all aspects of human-machine systems. Given these technical
capabilities, which system functions should be automated and to
what extent? We outline a model for types and levels of automa-
tion that provides a framework and an objective basis for making
such choices. Appropriate selection is important because automa-
tion does not merely supplant but changes human activity and can
impose new coordination demands on the human operator. We pro-
pose that automation can be applied to four broad classes of func-
tions: 1) information  acquisition; 2) information analysis; 3) de-
cision and action selection; and 4) action implementation. Within
each of these types, automation can be applied across a continuum
of levels from low to high, i.e., from fully manual to fully automatic.
A particular system can involve automation of all four types at dif-
ferent levels. The human performance consequences of particular
types and levels of automation constitute primary evaluative cri-
teria for automation design using our model. Secondary evaluative
criteria include automation reliability and the costs of decision/ac-
tion consequences, among others. Examples of recommended types
and levels of automation are provided to illustrate the application
of the model to automation design.
Index Terms—Automation, cognitive engineering, function allo-
cation, human-computer interaction, human factors, human-ma-
chine systems, interface design.
## I.  INTRODUCTION
## C
ONSIDER the following design problem. A human op-
erator of a complex system provided with a large number
of dynamic information sources must reach a decision relevant
to  achieving  a  system  goal  efficiently  and  safely.  Examples
include an anesthesiologist given various vital signs who must
decide  whether  to  increase  the  dosage  of  a  drug  to  a  patient
undergoing  surgery;  an  air  defense  operator  given  various
sensor  readings  who  has  to  decide  whether  to  shoot  down  a
potentially hostile enemy aircraft; or a securities analyst given
various financial data who must judge whether to buy a large
block of stocks. Technical developments in computer hardware
and software make it possible toautomatemany aspects of the
system, i.e., to have a computer carry out certain functions that
the human operator would normally perform. The automation
Manuscript received January 26, 1999; revised February 7, 2000. This work
was supported by grants from NASA Ames Research Center, Moffett Field, CA
(NAG-2-1096) and NASA Goddard Space Research Center, MD (NAG 5-8761)
to R.P., and from NASA Ames Research Center to T.B.S. (NAG-2-729). This
paper was recommended by Associate Editor R. Rada.
R. Parasuraman is with the Cognitive Science Laboratory, The Catholic Uni-
versity of America, Washington, DC 20064 USA.
T. B. Sheridan is with the Massachusetts Institute of Technology, Cambridge,
## MA 02165 USA.
C. D. Wickens is with the University of Illinois, Champaign, IL 61820 USA.
## Publisher Item Identifier S 1083-4427(00)03579-7.
can differ in type and complexity, from simply organizing the
information  sources,  to  integrating  them  in  some  summary
fashion,  to  suggesting  decision  options  that  best  match  the
incoming information, or even to carry out the necessary action.
The system design issue is this: given these technical capabil-
ities, which system functions should be automated and to what
extent? These fundamental questions increasingly drive the de-
sign of many new systems. In this paper we outline a model of
human interaction with automation that provides a framework
for answers to these questions. The human performance con-
sequences of specific types and levels of automation constitute
the primary evaluative criteria for automation design using the
model. Secondary evaluative criteria include automation relia-
bility and the costs of action consequences. (Both these sets of
criteria are described more fully later in this paper). Such a com-
bined approach—distinguishing types and levels of automation
and applying evaluative criteria—can allow the designer to de-
termine what should be automated in a particular system. Be-
cause the impact of the evaluative criteria may differ between
systems, the appropriate types and levels of automation for dif-
ferent systems can vary widely. Our model does not therefore
prescribewhat should and should not be automated in a partic-
ular system. Nevertheless, application of the model provides a
more complete and objective basis for automation design than
do approaches based purely on technological capability or eco-
nomic considerations.
## II.  A
## UTOMATION
Machines, especially computers, are now capable of carrying
out many functions that at one time could only be performed
by humans. Machine execution of such functions—or automa-
tion—has also been extended to functions that humans do not
wish to perform, or cannot perform as accurately or reliably as
machines. Technical issues—how particular functions are au-
tomated, and the characteristics of the associated sensors, con-
trols, and software—are major concerns in the development of
automated systems. This is perhaps not surprising given the so-
phistication and ingenuity of design of many such systems (e.g.,
the  automatic  landing  of  a  jumbo  jet,  or  the  docking  of  two
spacecraft). The economic benefits that automation can provide,
or are perceived to offer, also tend to focus public attention on
the technical capabilities of automation.
In contrast to the voluminous technical literature on automa-
tion, there is a small but growing research base examining the
humancapabilities involved  in work with automated  systems
[1]–[8]. This work has shown clearly that automation does not
simply supplant human activity but rather changes it, often in
## 1083-4427/00$10.00 © 2000 IEEE

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION287
ways unintended and unanticipated by the designers of automa-
tion [8],  and  as a  result  poses  new  coordination  demands on
the human operator [7]. Until recently, however, these findings
have not had much visibility or impact in engineering and de-
sign circles. Examination of human performance issues is es-
pecially important because modern technical capabilities now
force system designers to consider some hard choices regarding
what to automate and to what extent, given that there is little that
cannot be automated. In the present paper we propose a model
for types and levels of automation that provides a framework
and an objective basis for making such choices. Our approach
was guided by the concept of “human-centered automation” [9]
and by a previous analysis of automation in air traffic control
## (ATC) [10].
## 1
Let us begin by defining automation, because the term has
been used many different ways. The Oxford English Dictionary
(1989) defines automation as
1)  Automatic  control  of  the  manufacture  of  a  product
through a number of successive stages;
2)  the application of automatic control to any branch of in-
dustry or science;
3)  by extension, the use of electronic or mechanical devices
to replace human labor.
The original use of the term implies automatic control (auto-
matichaving many alternative definitions suggesting reflexive
action, spontaneity, and independence of outside sources). Au-
tomatic control can be open loop as well as closed loop, and
can refer to electronic as well as mechanical action. Automation
does not simply refer to modernization or technological innova-
tion. For example, updating a computer with a more powerful
system does not necessarily constitute automation, nor does the
replacement of electrical cables with fiber optics. The present
paper is concerned with human performance in automated sys-
tems. We therefore use a definition that emphasizes human-ma-
chine comparison and define automation as a device or system
that accomplishes (partially or fully) a function that was previ-
ously, or conceivably could be, carried out (partially or fully) by
a human operator [8].
## III.  A M
## ODEL FORTYPES ANDLEVELS OFAUTOMATION
In our definition, automation refers to the full or partial re-
placement of a  function previously  carried out by the human
operator. This implies  that automation  is not all or none,  but
can vary across a continuum of levels, from the lowest level of
fully manual performance to the highest level of full automation.
Several levels between these two extremes have been proposed
[11], [12]. Table I shows a 10-point scale, with higher levels rep-
resenting increased autonomy of computer over human action
[10], based on a previously proposed scale [11]. For example, at
a low level 2, several options are provided to the human, but the
system has no further say in which decision is chosen. At level
4, the computer suggests one decision alternative, but the human
## 1
In principle, our approach does not exclude the possibility of full automation,
without any human operator involvement. This might suggest that our model is
not needed if total automation is technically feasible. As we discuss later, how-
ever, full automation does not necessarily eliminate a human role in automated
systems [8].
## TABLE   I
## L
## EVELS  OFAUTOMATION  OFDECISION
## AND
## ACTIONSELECTION
Fig. 1.    Simple four-stage model of human information processing.
retains authority for executing that alternative or choosing an-
other one. At a higher level 6, the system gives the human only
a limited time for a veto before carrying out the decision choice.
Automated systems can operate at specific levels within this
continuum.  For  example,  a  conflict  detection  and  resolution
system  that  notifies  an  air  traffic  controller  of  a  conflict  in
the  flight  paths  of  two  aircraft  and  suggests  a  resolution
would qualify as level 4 automation. Under level 6 or higher,
the  system  would  automatically  execute  its  own  resolution
advisory, unless the controller intervened.
In the proposed model we extend Table I to cover automa-
tion of different types of functions in a human-machine system.
The scale in Table I refers mainly to automation of decision and
action selection, oroutputfunctions of a system. However, au-
tomation may also be applied toinputfunctions, i.e., to func-
tions that precede decision making and action. In the expansion
of the model, we adopt a simple four-stage view of human in-
formation processing (see Fig. 1).
The  first  stage  refers to  the  acquisition  and  registration  of
multiple sources of information. This stage includes the posi-
tioning and orienting of sensory receptors, sensory processing,
initial pre-processing of data prior to  full perception, and se-
lective attention. The second stage involves conscious percep-
tion, and manipulation of processed and retrieved information
in working memory [13]. This stage also includes cognitive op-
erations such as rehearsal, integration and inference, but these
operations occurprior to the point of decision. The third stage is
where decisions are reached based on such cognitive processing.
The fourth and final stage involves the implementation of a re-
sponse or action consistent with the decision choice.
This four-stage model is almost certainly a gross simplifica-
tion of the many components of human information processing
as discovered by information processing and cognitive psychol-
ogists [14]. The performance of most tasks involves inter-de-
pendent stages that overlap temporally in their processing oper-
ations [15]. The stages can also be considered to be coordinated

288IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
Fig.  2.    Levels  of  automation  for  independent  functions  of  information
acquisition,informationanalysis,decisionselection,andaction
implementation.  Examples  of  systems  with  different  levels  of  automation
across functional dimensions are also shown.
together in “perception-action” cycles [16] rather than in a strict
serial sequence from stimulus to response. Our goal is not to de-
bate the theoretical structure of the human cognitive system but
to propose a structure that is useful in practice. In this respect,
the conceptualization shown in Fig. 1 provides a simple starting
point with surprisingly far-reaching implications for automation
design. Similar conceptual models have been found to be useful
in deriving human factors recommendations for designing sys-
tems in general [17].
The four-stage model of human information processing has
its equivalent in system functions that can be automated. Ac-
cordingly, we propose that automation can be applied to four
classes of functions (see also [18] and related proposals in [9]
and [19]):
1)  information acquisition;
2)  information analysis;
3)  decision and action selection;
4)  action implementation.
Each  of  these  functions  can  be  automated  to  differing  de-
grees,  or  many  levels.  The  multiple  levels  of  automation  of
decision  making  as  shown  in  Table  I  can  be  applied,  with
some modification, to the information acquisition, information
analysis,  and  action  implementation  stages  as  well,  although
the  number  of  levels  will  differ  between  the  stages.  Fig.  2
provides  a  schematic  of  our  model  of  types  and  levels  of
automation.  As  a  convenient  shorthand,  we  refer  to  the  four
types asacquisition,analysis,decision, andactionautomation.
We also occasionally refer jointly  to  acquisition and analysis
automation asinformationautomation.
A particular system can involve automation of all four dimen-
sions at different levels. Thus, for example, a given system (A)
could be designed to have moderate to high acquisition automa-
tion, low analysis automation, low decision automation, and low
action automation. Another system (B), on the other hand, might
have high levels of automation across all four dimensions.
## A.  Acquisition Automation
Automation of information acquisition applies to the sensing
and registration of input data. These operations are equivalent to
the first human information processing stage, supporting human
sensory  processes.  At the  lowest  level,  such  automation  may
consist of strategies for mechanically moving sensors in order to
scan and observe. For example, the radars used in commercial
ATC acquire information on aircraft by scanning the sky in a
fixed pattern, but in military ATC the radars may “lock on” as a
function of detected targets. Artificial visual and haptic sensors
could also be used with an industrial robot to allow it to find and
grasp an object, thereby providing information about that object.
Moderate levels of automation at this stage may involve organi-
zation of incoming information according to some criteria, e.g.,
a priority list, and highlighting of some part of the information.
For example “electronic flight strips” for air traffic controllers
could list aircraft in terms of priority for handling; and the elec-
tronic data block showing aircraft on the controller’s radar dis-
play (which itself represents an earlier form of acquisition au-
tomation) could be highlighted to indicate a potential problem
with a particular aircraft. Note that both organization and high-
lighting preserve the visibility of the original information (“raw”
data). This is not necessarily the case with a more complex op-
eration at this stage of automation, filtering,  in which certain
items of information are exclusively selected and brought to the
operator’s attention. Highlighting and filtering can lead to dif-
fering human performance consequences, as described in a later
section in a discussion of automation reliability.
## B.  Analysis Automation
Automation of information analysis involves cognitive func-
tions such as working memory and inferential processes. At a
low level, algorithms can be applied to incoming data to allow
for  their  extrapolation  over  time,  orprediction.  For  example,
predictor displays have been developed for the cockpit that show
the projected future course of another aircraft in the neighboring
airspace [20], [21]. Trend displays have also been developed for
use in process control (e.g., nuclear power plants), in which a
model of the process is developed and used to show both the cur-
rent and the anticipated future state of the plant [22]. A higher
level of automation at this stage involvesintegration, in which
several input variables are combined into a single value. One
example is to use a display with anemergent perceptual fea-
turesuch as a polygon against a background of lines [23]. An-
other example of information analysis automation in ATC is the
converging runway display aid (CRDA), which eliminates the
need  for  the controller  to  mentally  project  the approach  path
of  one  aircraft  onto  that  of  another  landing  on  a  converging
runway [24]. In both these  examples, information  integration
serves the purpose  of augmenting human operator perception
and cognition. More complex forms of analysis automation in-
clude “information managers” that provide context-dependent
summaries of data to the user [45].
## C.  Decision Automation
The third  stage, decision  and action  selection, involves  se-
lection from  among decision  alternatives. Automation  of this

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION289
stage involves varying levels of augmentation or replacement
of human selection of decision options with machine decision
making,  as  described  previously  in  Table  I.  For  example  ex-
pert systems are designed with conditional logic (i.e., produc-
tion rules) to prescribe a specific decision choice if particular
conditions exist [25]. Examples can be found in medicine [26],
military command and control [27], and in route planning for
pilots  to  avoid  bad  weather  [28].  As  with  the  analogous  de-
cision-making stage in human performance, such systems de-
part from those involved in inference (analysis automation) be-
cause they must make explicit or implicit assumptions about the
costs and values of different possible outcomes of the decision
process, and the nature of these outcomes is uncertain in a prob-
abilistic world. The different levels of automation at this stage
are best defined by the original taxonomy proposed by Sheridan
[11] and shown in Table I, which defines a continuum that pro-
gresses from systems that recommend courses of action, to those
that execute those courses. For example, in comparing proposed
and existing  designs for decision  automation in  avoiding  air-
craft–ground collisions, the current ground proximity warning
system (GPWS) is positioned at level 4, in which a single ma-
neuver is recommended, but the pilot can chose to ignore it. But
a proposed automatic ground collision avoidance (auto GCAS)
system for combat aircraft is defined at level 7, in which automa-
tion will automatically take control if the pilot does not [29].
## D.  Action Automation
The  final  stage  of  action  implementation  refers  to  the  ac-
tual  execution  of the  action  choice. Automation  of this  stage
involves different levels of machine execution of the choice of
action, and typically replaces the hand or voice of the human.
Different levels of action automation may be defined by the rel-
ative amount of manual versus automatic activity in executing
the response. For example, in a photocopier, manual sorting, au-
tomatic sorting, automatic collation, and automatic stapling rep-
resent different levels of action automation that can be chosen
by the user. A somewhat more complex example from ATC is
the automated “handoff,” in which transfer of control of an air-
craft from one airspace sector to another is carried out automat-
ically via a single key press, once the decision has been made
by  the  controller. On  the  flight  deck,  systems  are also  being
considered in  which a  flight plan,  uplinked from the ground,
can be “autoloaded” into the plane’s flight management com-
puter by a single keypress, rather than through more time-con-
suming manual data entry [30]–[32]. Finally, action automation
includes “agents” that track user interaction with a computer and
execute certain sub-tasks automatically in a contextually-appro-
priate manner [45].
## E.  Adaptive Automation
Levels  of  automation  across  any  of  these  functional  types
need not be fixed at the system design stage. Instead, the level
(and perhaps even the type) of automation could be designed to
vary depending on situational demands during operational use.
Context-dependent automation is known as adaptive automation
[33]–[35]. Two examples will illustrate the concept. In an air de-
fense system, the beginning of a “pop-up” weapon delivery se-
quence could lead to the automation at a high level of all aircraft
defensive measures [36]. The automation is adaptive because if
this critical event does not occur, the automation is not invoked
or is set at a low level. In another example, the decision to con-
tinue or abort an aircraft takeoff following an engine malfunc-
tion might be automated at either a low or a high level depending
upon the time criticality of the situation (e.g., how close the air-
craft is to the critical speed V1 for takeoff) [37]. Considerable
empirical research on adaptive automation has been reported in
recent years [38]–[44]. However, we do not describe this work
because it raises several complex ancillary issues, the discussion
of which would take us far afield from the primary purpose of
this paper.
## IV.  A F
## RAMEWORK FORAUTOMATIONDESIGN
The model we have outlined provides a framework for exam-
ining automation design issues for specific systems. How can
the framework be used? We propose a series of steps and an iter-
ative procedure that can be captured in a flow chart (see Fig. 3).
The first step is to realize that automation is not all-or-none but
can vary by type. One can ask whether automation should be
applied to information acquisition, information analysis, deci-
sion selection, or to action implementation. Automation of one
class of function (e.g., information analysis), of different com-
binations of functions, or of all four functional domains, can be
entertained.
At a subsequent stage of design, one can ask what level of
automation should be applied within each functional domain.
There is probably no simple answer to this question, and trade-
offs between anticipated benefits and costs are likely. However,
the four-dimensional  model we  have  proposed  can provide  a
guiding framework. As shown in Fig. 3, multiple levels of au-
tomation can be  considered for  each  type of automation. We
propose that any particular level of automation should be eval-
uated by examining its associated human performance conse-
quences. These constitute primary evaluative criteria for levels
of automation. However, human performance is not the only im-
portant factor. Secondary evaluative criteria include automation
reliability and the costs of decision/action consequences
## 2
## . These
should also be applied to evaluate the feasibility and appropri-
ateness of particular levels of automation. We envisage the ap-
plication of these criteria and their evaluation as constituting a
recursive process (see Fig. 3) that could be made part of an iter-
ative design procedure. We emphasize, however, that the model
should not be treated as a static formula or as a prescription that
decreesa particular type or level of automation. Rather, when
considered in combination with the primary and secondary eval-
uative criteria we have described, the model can provide princi-
pled guidelines for automation design.
We provide examples where, following consideration of these
evaluative criteria, particular  levels of automation are recom-
mended for each of the four types or stages of automation. Such
recommendations refer to the appropriateupper boundon the
level of automation, i.e., the maximum, but not necessarily the
required level. In other words, we recommend that automation
## 2
This is not an exhaustive list of criteria. Others that are important include
ease of system integration, efficiency/safety tradeoffs, manufacturing and oper-
ating costs, and liability issues.

290IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
Fig. 3.Flow chart showing application of the model of types and levels of
automation. For each type of automation (acquisition, analysis, decision, and
action), a level of automation between low (manual) and high (full automation)
is chosen. This level is then evaluated by applying the primary evaluative criteria
of human performance consequence, and adjusted if necessary, in an iterative
manner as shown. Secondary evaluative criteria are then also iteratively applied
to adjust the level of automation. The process is then repeated for all four types
of automation.
could be designed to go as high as that particular level, but no
further. But the designer could choose a level lower than this
maximum if necessary, particularly after considering evaluative
criteria other than the ones we discuss (e.g., ease of system in-
tegration, or cost). Thelower boundon the level of automation
can also be determined by applying the same evaluative criteria.
Acceptable system performance may require a certain minimal
level of automation.
## A.  Human Performance Consequences: Primary Evaluative
Criteria for Automation Design
An important  consideration in  deciding  upon  the  type and
level of automation in any system design is the evaluation of the
consequences for human operator performance in theresulting
system (i.e., after automation has been implemented). As shown
in Fig. 3, particular types and levels of automation are evalu-
ated by examining their associated human performance conse-
quences. To take a hypothetical example, suppose prior research
has shown (or modeling predicts) that compared to manual op-
eration, both human and system performance are enhanced by
level 4 automation but degraded by automation above level 6.
Application of our framework would determine the lower and
upper bounds of automation to be 4 and 6, respectively. This
initial specification would then be evaluated again with respect
to the secondary evaluative criteria, in an iterative manner, and a
final choice of level within this range could be made (see Fig. 3).
Over  the  past  two  decades,  researchers  have  examined  a
number  of  different  aspects  of  human  interaction  with  auto-
mated systems. This research, which has  included theoretical
analyzes,  laboratory  experiments,  simulation  and  modeling,
field  studies,  and  analyzes  of  real-world  incidents  and  acci-
dents, has found that automation can have both beneficial and
negative effects on human performance [1]–[10], [45]–[48]. We
briefly  discuss  four  human  performance  areas:  mental  work-
load, situation awareness, complacency, and skill degradation.
1)  Mental  Workload:The  evidence suggests  that  well-de-
signed  information  automation  can  change  human  operator
mental workload to  a level  that is appropriate  for  the system
tasks to be performed. At the simplest level, organizing infor-
mation sources, e.g., in a priority list, will help the operator in
picking the information relevant to a decision. Data summaries
can also help by eliminating  time-consuming search  or com-
munication operations. As mentioned previously, the electronic
data block on the air traffic controller’s radar display replaces
the  need  for  the  controller  to  communicate  with  pilots  to
determine the aircraft position and altitude. Other information
automation operations that are beneficial include highlighting,
and  integration,  in  which  different  information  sources  are
collated and presented together [10]. Cockpit predictor displays
have  also  shown  that  pilot  workload  decreases  and  hazard
detection performance improves with the addition of predictive
information concerning the flight path of neighboring aircraft
[21].  Data  transformation,  for  example  graphic  presentation
of  information,  can  also  be  beneficial.  Transformation  and
integration  of  raw  data  into  a  form  (graphical  or  otherwise)
that matches the operator’s representation of system operations
has  been  found to  be  a  useful  design  principle  [49]. A  good
example  is  the  horizontal  situation  indicator  in  the  cockpit,
which provides the pilot with a graphic display of the projected
flight plan and the current position of the aircraft. This, more
than  any  other  automated  system  in  the  cockpit,  has  been
credited with reducing the workload of the pilot [50].
These results should not be construed to mean that automa-
tion always results in balanced operator workload. Instances of
automationincreasingworkload have also been found [8], [50].
These mostly involve systems in which the automation is diffi-
cult to initiate and engage, thus increasing both cognitive work-
load [51] and if extensive data entry is required, the physical
workload of the operator. Such systems have been referred to
as implementing “clumsy” automation [50]. In general, the ef-
fect of automation on mental workload has been mirrored by
the similarly mixed record of automation in improving human
productivity and efficiency [52].
In addition to unbalanced mental workload, other human per-
formance costs have been linked to particular forms of automa-
tion. We briefly consider three such costs.
2)  SituationAwareness:First,automationofdeci-
sion-making  functions  may  reduce  the  operator’s  awareness

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION291
of  the  system  and  of  certain  dynamic  features  of  the  work
environment. Humans tend to be less aware of changes in en-
vironmental or system states when those changes are under the
control of another agent (whether that agent is automation or
another human) than when they make the changes themselves
[53]–[56]. Also, if a decision aid, expert system, or other type
of decision automation consistently and repeatedly selects and
executes decision choices in a dynamic environment, the human
operator  may  not  be  able  to  sustain  a  good  “picture”  of  the
information sources in the environment because he or she is not
actively engaged in evaluating the information sources leading
to a decision. This might occur in systems where operators act
as passive decision-makers monitoring a process to determine
when to intervene so as to prevent errors or incidents [53]. Note
that  such a  cost may occur  even  as the use  of automation of
information  analysis,  e.g.,  data  integration,  may  improve  the
operator’s situation awareness.
3)  Complacency:Second,  if  automation  is  highly  but  not
perfectly reliable in executing decision choices, then the oper-
ator may not monitor the automation and its information sources
and hence fail to detect the occasional times when the automa-
tion fails [57], [58]. This effect of over-trust or “complacency” is
greatest when the operator is engaged in multiple tasks and less
apparent when monitoring the automated system is the only task
that the operator has to perform [58]. The complacency effect in
monitoring has recently been modeled using a connectionist ar-
chitecture [59]: the analysis suggested that complacency reflects
differential learning mechanisms for monitoring under manual
control and automation.
Automation of information analysis can also lead to compla-
cency if the algorithms underlying filtering, prediction, or in-
tegration operations are reliable but not perfectly so. A recent
study of a simulated air-ground targeting task [60] found that a
cue that incorrectly directed attention away from the target led to
poorer detection performance even though pilots were informed
that the cue was not perfectly reliable. Automated cueing (at-
tention guidance) can lead operators to pay less attention to un-
cued areas of a display than is appropriate [61]. Thus compla-
cency-like effects can also be obtained even if automation is ap-
plied to information acquisition and analysis and not just to de-
cision-making. It is not known, however, whether such effects
of unreliable automation apply equally strongly to all stages of
information processing. There is some evidence to indicate that
although complacency can occur with both information automa-
tion  and  decision  automation,  its  effects  on  performance  are
greater with the latter. In a study of decision aiding, both forms
of automation benefited performance equally when the automa-
tion was perfectly reliable [62]. When the automation was un-
reliable, however, performance suffered much more when un-
reliable recommendations were given  by decision automation
than when only incorrect status information was provided by
information automation. This study, however, is the only one to
date that has directly compared the effects of automation unre-
liability at different stages of automation. The issue of whether
automation unreliability has similar negative effects for all four
stages of automation in our model needs further examination.
4)  Skill degradation:Third, if the decision-making function
is consistently performed by automation, there will come a time
when the human operator will not be as skilled in performing
that  function.  There  is  a  large  body  of  research  in  cognitive
psychology documenting that forgetting and skill decay occur
with disuse [63]. Degradation of cognitive skills may be partic-
ularly important following automation failure. A recent simula-
tion study of human control of a telerobotic arm used for move-
ment of hazardous materials found that following automation
malfunction,  performance  was  superior  with  an  intermediate
level of decision automation compared to higher levels [53].
These  potential  costs—reduced  situation  awareness,  com-
placency,   and   skill   degradation—collectively   demonstrate
that  high-level  automation  can  lead  to  operators  exhibiting
“out-of-the-loop”   unfamiliarity   [47].   All   three   sources   of
vulnerability may pose a threat to safety in the event of system
failure. Automation must therefore be designed to ensure that
such potential human performance costs do not occur. Human
performance  costs  other  than  the  areas  we  have  discussed
should  also  be  examined.  Automation  that  does  not  lead  to
unbalanced  mental  workload,  reduced  situation  awareness,
complacency, or skill loss may nevertheless be associated with
other  human  performance  problems  that  ultimately  impact
on  system  performance,  including  mode  confusion  and  low
operator trust in automation [1]–[10], [45]–[48].
By considering these human performance consequences, the
relative merits of a specific level of automation can be deter-
mined. However, full application of our model also requires con-
sideration of other  criteria. We consider two  other  secondary
criteria here, automation reliability and the cost of decision and
action outcomes.
## B.  Secondary Evaluative Criteria
1)  Automation  Reliability:The  benefits  of  automation  on
operator mental workload and situation awareness noted previ-
ously are unlikely to hold if the automation is unreliable. Hence
ensuring high reliability is a critical evaluative criterion in ap-
plying automation. Several procedures for estimating reliability
have been proposed, including fault and event tree analysis [64]
and various methods for software reliability analysis [65]. The
use of these techniques can be helpful, so long as their results
are interpreted cautiously. In particular, what appear to be “hard
numbers,” such as a reliability of .997, or a mean time to failure
of 100 000 hours, must be viewed with some skepticism because
such values represents an estimate of a mean, whereas what is
required is the variance around the mean, which can be consid-
erable. The complexity and size of software in many automated
systems may also preclude comprehensive testing for all pos-
sible faults, particularly those that arise from interaction with
the existing system in which the automated sub-system is placed
[10]. Furthermore, automation reliability cannot always simply
be defined in  probabilistic terms. Failures may occur not  be-
cause of a predictable (in a statistical sense) malfunction in soft-
ware or hardware, but because the assumptions that are modeled
in the automation by the designer are not met in a given opera-
tional situation [8].
Automation reliability is an important determinant of human
use of automated systems because  of its influence on human
trust [66] [67]. Unreliability lowers operator trust and can there-
fore  undermine  potential  system  performance  benefits  of  the

292IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
automation. Automated systems may be  underutilized or dis-
abled because of mistrust, as in the case of alarm systems that
frequently give false alerts [8]. Signal detection analysis [68]
can be used  to determine  the alerting threshold that balances
the competing requirements of timely detection (to allow for ef-
fective  action), a  near-zero missed  detection  rate  (because  of
potentially catastrophic consequences—e.g., a collision), and a
low false alert rate [69]. To ensure alert reliability, the proba-
bility that an alarm reflects a true hazardous event must also be
maximized to the extent possible: this can be examined by com-
bining signal detection theory and Bayesian statistics [70].
If information automation can be made  extremely reliable,
then pursuing very high levels of information automation can
be justified. Of course, high reliability cannot be guaranteed in
many cases. As mentioned previously, the inherent uncertain na-
ture of information sources, either due to sensor imprecision or
to changes in operator priorities, means that there will always
exist conditions in which the algorithms used by the automation
are inappropriate for those conditions. Nevertheless, informa-
tion acquisition and analysis automation may still be retained at
a relatively high level,
as long asthe operator has access to the
raw data (e.g., highlighting, but not filtering), and the operator is
aware of (calibrated to) the level of unreliability, such that some
attention will be allocated to the original information [60], [71].
Although many examples of highly reliable information au-
tomation exist, more sophisticated forms of such automation are
being developed in which complex algorithms are applied to the
raw data in order to predict future events. For example, traffic
displays in the cockpit, and conflict prediction tools for the air
traffic controller both attempt to project the future flight paths
of aircraft. Projecting the future is inherently less than perfectly
reliable, particularly if carried out far enough out in time (e.g.,
20 min. for ATC conflict prediction). Further work needs to be
done to evaluate not only the reliability of the algorithms un-
derlying these predictor systems, but also their susceptibility to
noise in the raw data, and the consequences for human perfor-
mance of information automation unreliability. Some emerging
research is beginning to define the conditions under which unre-
liability does or does not influence human performance. For ex-
ample, two recent studies found that when feedback is provided
as to the occasional errors made by information automation, ap-
propriate calibration of the operator’s  trust in the automation
can take place fairly rapidly, and the benefits of information au-
tomation can still be realized [60], [71]. This suggests that the
negative effects of over-trust, noted earlier for decision automa-
tion, may be less apparent for information automation.  How-
ever, as discussed previously, only one study has directly com-
pared information and decision automation [62]. Thus the issue
of whether automation unreliability has greater negative effects
for later stages of automation requires further examination.
2)  Costs of Decision/Action Outcomes:Our analysis so far
indicates that high levels of automation may be associated with
potential  costs  of  reduced  situation  awareness,  complacency,
and skill degradation. This is not to say that high levels of au-
tomation should not be considered for decision and action au-
tomation. However, assessing the appropriate level of automa-
tion for decision automation requires additional consideration
of the costs associated with decision and action outcomes.
The decisions and associated actions that humans and auto-
mated systems take in most systems vary in the costs that occur
if the actions are incorrect or inappropriate. Many routine ac-
tions have predictable consequences that involve little or no cost
if the actions do not go as planned. Theriskassociated with a
decision outcome can be defined as the cost of a error multi-
plied by the probability of that error. For decisions involving
relatively little risk, therefore, out-of-the-loop problems are un-
likely to have much impact, even if there is a complete automa-
tion failure. Such decisions are strong candidates for high-level
automation. In fact, if human operators had to be continually in-
volved in making each of these relatively simple decisions, they
could be so overloaded  as to prevent them from carrying out
other more important functions.
Note that high-level automation of decision selection and ac-
tion may also be justified  in highly time-critical situations  in
which there is insufficient time for a human operator to respond
and take appropriate action. For example, if certain serious prob-
lems are detected in the reactor of a nuclear power plant, control
rods are automatically lowered into the core to turn off the re-
actor, without any human operator intervention. Bypassing the
human  operator  is  justified  in  this  case  because  the  operator
cannot reliably respond in time to avoid an accident. As pre-
viously discussed, automating the decision to abort or continue
the takeoff of an aircraft when an engine malfunction occurs too
near in time to the critical V1 speed for appropriate pilot action
would represent another qualifying example [37], as would the
decision to take control of the aircraft if a fighter aircraft is about
to run into the ground [29].
It  is also appropriate to consider high-level  automation for
decisions involving high risk in situations in which human op-
erators have time to respond. In this case, the cost of adverse
consequences define major evaluative criteria for determining
appropriate  levels  of automation.  The  examples  in  anesthesi-
ology, air defense, and the stock market with which we began
this paper qualify as involving high-cost decisions. System de-
signers can certainlyconsiderimplementing decision automa-
tion  above  low  to  moderate  levels  for  such  systems,  e.g.,  at
levels at  or above  level 6 in  Table I,  in which  computer sys-
tems are given autonomy over decision making. This would be
appropriate if the human operator is not required to intervene or
manage the system in the event of automation failure. In fact,
in this case even full automation (Level 10) could be justified
## 3
## .
However, if the human operator is ever expected under abnormal
circumstances to take over control, then our analysis suggests
that high levels of decision automation may not be suitable be-
cause of the documented human performance costs associated
with such automation. The burden of proof should then be on
the designer to show that their design will not lead to the prob-
lems of loss of situation awareness, complacency, and skill loss
that we have discussed.
## 3
Full automation requires highly reliable error handling capabilities and the
ability to deal effectively and quickly with a potentially large number of anoma-
lous situations. In addition to requiring the technical capability to deal with all
types of known errors, full automation without human monitoring also assumes
the ability to handle unforeseen faults and events. This requirement currently
strains the ability of most intelligent fault-management systems.

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION293
A system  designer may object  to  the recommendation  that
decision  automation  should  not  exceed  a  moderate  level  for
high-risk situations on the grounds that if information automa-
tion  can  be  made  highly  reliable,  then  decision  automation
can also be, so why not implement high-level automation for
this function too? The answer is that although decision-aiding
systems  can  be  engineered  to  be  highly  reliable  for  many
known  conditions,  the  “noisiness”  of  the  real  world,  with
unplanned   variations   in   operating   conditions,   unexpected
or  erratic  behavior  of  other  system  components  or  human
operators,  system  malfunctions,  etc.,  as  well  as  the  inherent
unreliability of predicting the future, will mean that there will
always  be  a  set  of  conditions  under  which  the  automation
will  reach  an  incorrect  decision.  If  under  such  conditions  of
system failure the human operator is required to intervene and
salvage the situation, the problem of out-the-loop unfamiliarity
may prevent the operator from intervening successfully or in a
timely manner [8], [47], [55].
Finally, the inter-dependence of the decision automation and
action  automation  dimensions  for  high-risk  functions  should
be noted. A system could be designed to have high-level deci-
sion automation, in which decision choices are selected without
human involvement or veto power. For example, currently an
air traffic controller issues a verbal clearance to a pilot, who ac-
knowledges and then executes a flight maneuver consistent with
the clearance. With the development of two-way electronic data
link communications between aircraft and ATC, however, the
clearance (which itself may be a computer choice) could be up-
linked and  loaded in  the aircraft’s flight management  system
(FMS) automatically. The aircraft could then carry out the ma-
neuver,  without  pilot  intervention.  If  the  consequences  of  an
incorrect or inappropriate decision are great, however,  then it
would be prudent to require that the action automation level be
sufficiently low so that the (automated) decision choice is exe-
cuted by the pilot (i.e., by actively pressing a button that “loads”
the proposed flight plan into the FMS). Giving the pilot the op-
portunity to review the decision choice and forcing a conscious
overt action, provides an “error-trapping” mechanism that can
guard against mindless acquiescence in computer-generated so-
lutions that are not contextually appropriate. Note that we are
not implying that some degree of human action is
alwaysneeded
for the purposes of error trapping. The need only arises at the last
action implementation stage if the previous decision selection
stage has been highly automated. In this situation having some
human involvement at the action stage provides a “last chance
opportunity” to trap errors.
Recent studies have examined the relative effects of low and
high levels of action automation on use of the FMS [30], [31].
Use of a lower level of automation of action selection—in en-
tering data-linked flight information into the flight management
computer—allowed for more errors of decision making automa-
tion to be caught, than a higher level, in which data entry was ac-
complished by pressing a single “accept” button. Of course this
advantage for error trapping must be balanced against the added
workload, and possible error source of less automated (manual)
data entry [32]. Certainly cumbersome and clumsy data entry
remains a viable candidate for automation. But to reiterate the
linkage  between  decision  and  action  automation,  if  high  au-
tomation is selected for the latter, then designers should resist
the temptation for high automation levels of decision making.
## C.  Application Example
Our multi-stage model of human-automation interaction can
be applied to specific systems in conjunction with a considera-
tion of evaluative criteria, of which we have discussed three in
this paper—human performance consequences, automation re-
liability, and the costs of decision/action consequences. To fur-
ther illustrate application of the model, we briefly consider its
use in the design of future ATC systems, based on analyses pre-
viously presented in [10].
ATC systems are being redesigned because the volume of air
traffic is likely to double over the next two decades, posing a
significant threat to handling capacity [72]. One alternative is
Free Flight [73], which would allow user-preferred routing and
free maneuvering, among other changes aimed at minimizing
ATC restrictions [74]. Another approach is to supplement the
current system of ground-based ATC with additional automa-
tion to support air traffic controllers in the management of an
increasingly dense airspace [10]. Elements of both alternatives
are likely to be implemented, but the increasing complexity of
future airspace will require automation tools to support both air
traffic controllers and pilots. Automation tools will be needed
for planning, traffic management, conflict detection and resolu-
tion, etc.
Application of our model suggests the following recommen-
dations for future ATC automation. (We again emphasize that
each recommendation represents an upper bound or maximum
level of automation, not a required level.) High levels of infor-
mation acquisition and analysis automation can be pursued and
implemented if the resulting system can be shown to be reliable.
This recommendation is represented by the arrows on the left
part of the scales in Fig. 4. Several examples of such automation
(such as CRDA) already exist and others are being developed.
For decision and action automation, however, high levels should
be implemented only for low-risk situations (indicated by the
upper arrow in the middle scale in Fig. 4). For all other situ-
ations, the level of decision automation should not exceed the
level of the computer suggesting (but not executing) a preferred
alternative to the controller (indicated by the lower arrow). For
example, in risky situations, as when a climb clearance has to
be issued to resolve a crossing conflict in dense airspace, con-
flict resolution automation can provide alternatives to the con-
troller but should not select one of them without controller in-
volvement. If relatively high-level  decision automation is im-
plemented in risky situations, however, then we recommend that
some degree of human action be retained by having a moderate
level of action automation. As discussed previously, this allows
for last-stage error trapping. This recommendation is indicated
by the right-most arrow in Fig. 4.
## V.  A
## LTERNATIVES,LIMITATIONS,ANDEXTENSIONS
Before  concluding, we  briefly consider two  alternative  ap-
proaches to the implementation of automation, and discuss some
limitations and extensions of our framework. One alternative to
our approach is to automate everything that one can. This can be

294IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
Fig. 4.Recommended  types and  levels  for future  ATC  systems,  consistent
with  three  evaluative  criteria-human  performance  consequences,  automation
reliability, and costs of actions.
a viable option and to some extent has been the default strategy
used in most systems that have been automated to date, often be-
cause increasing efficiency or reducing costs are major driving
forces for automation. However, a problem with this strategy is
that the human operator is left with functions that the designer
finds hard, expensive, or impossible to automate (until a clev-
erer designer comes around). This approach therefore defines
the human operator’s roles and responsibilities in terms of the
automation [8]. Designers automate every subsystem that leads
to an economic benefit for that subsystem and leave the operator
to manage the rest. Technical capability or low cost are valid
reasons for automation, given that there is no detrimental im-
pact on human performance in theresulting wholesystem, but
this is not always the case. The sum of subsystem optimizations
does not typically lead to whole system optimization. A second
alternative is to use task allocation methods to match human and
machine capabilities, as in the Fitts list approach [75]. That is,
tasks that are putatively performed better by machines should
be automated, whereas those that humans do better should not.
Unfortunately, although function allocation methods are useful
in principle, it has proved difficult in practice to use procedures
such as the Fitts List to determine which functions should be
automated in a system [76].
Some limitations of our model for types and levels of automa-
tion should also be noted. First, while we used Sheridan’s 10
levels of automation [11] for decision automation, we did not
explicitly specify the number of levels for the other types of au-
tomation, e.g., information automation. One reason is that while
there is extensive research pointing to the benefits of informa-
tion automation vs. no automation (e.g., as in predictor displays
for CDTI, see [20], [21]), there is as yet little empirical work
explicitly comparing the effects on human performance ofdif-
ferent levelsof automation for information acquisition and anal-
ysis. Another reason is that any proposed taxonomy is likely to
be superceded by technological developments in methods for
information integration and presentation, so that new levels will
need to be specified.
Second,   in   proposing   human   performance   benefits   and
costs  as  evaluative  criteria  for  determining  appropriate  types
and levels of automation, we did not discuss how the relative
benefits  and  costs should  be weighed.  Should the  benefit  (of
a  particular  automation  level)  of  balanced  mental  workload
be  outweighed by the  cost of  reduced  situation awareness or
increased  likelihood  of  complacency?  What  is  the  relative
weighting  of  the  human  performance  costs  we  discussed  in
this  paper,  as  well  as  of  those  we  did  not?  Similarly,  which
is  the  most  important  of  the  several  secondary  evaluative
criteria we have listed, such as automation reliability, costs of
action outcomes, ease of system integration,  efficiency/safety
tradeoffs,  manufacturing  and  operating  costs,  and  liability?
These are difficult issues to which there are no simple answers.
Of  course,  as  a  qualitative  model  our  approach  is  meant  to
provide  a  framework  for  design,  not  a  set  of  quantitative
methods. Nevertheless, one way forward might be to examine
the  possibility  of  formalizing  the  model.  More  generally,  it
would  be  desirable  to  have  quantitative  models  that  could
inform  automation  design  for  human-machine  systems  [77].
Several  computational  models  of  human-automation  interac-
tion  have  been  put  forward  very  recently,  including  models
based on expected value statistics [37], [78], task-load models
[79],  cognitive-system  models  [80],  and  a  model  based  on
state-transition  networks  [81]  (for  a  recent  review  of  these
models, see [82]). As these and related models mature and are
validated,  it  may  be  possible  to  improve  automation  design
by supplementing the qualitative analysis presented here with
quantitative modeling.
## VI.  C
## ONCLUSIONS
Automation  design  is  not  an  exact  science.  However,  nei-
ther does it belong in the realm of the creative arts, with suc-
cessful design dependent upon the vision and brilliance of indi-
vidual creative designers. (Although such qualities can certainly
help  the  “look  and  feel”  and  marketability  of  the  automated
system—see [83]). Rather, automation design can be guided by
the four-stage model of human-automation interaction we have
proposed, along with the consideration of several evaluative cri-
teria. We do not claim that our model offers comprehensive de-
sign principles but a simple guide. The model can be used as a
starting point for considering what types and levels of automa-
tion should be implemented in a particular system. The model
also provides a framework within which important issues rel-
evant to  automation design  may be  profitably explored.  Ulti-
mately, successful automation design will depend upon the sat-
isfactory resolution of these and other issues.
## A
## CKNOWLEDGMENT
The authors thank the members of the Panel on Human Fac-
tors in Air Traffic Control Automation of the National Research
Council (Anne Mavor, Study Director) for their contributions to
this work. They also thank P. Hancock, D. Kaber, N. Moray, U.
Metzger, and M. Scerbo for useful comments on this work.
## R
## EFERENCES
[1]   E. L. Wiener and R. E. Curry, “Flight-deck automation: Promises and
problems,”Ergonomics, vol. 23, pp. 995–1011, 1980.
[2]   L.  Bainbridge,  “Ironies  of  automation,”Automatica,  vol.  19,  pp.
## 775–779, 1983.

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION295
[3]  N. Chambers and D. C.  Nagel, “Pilots of the future: Human or com-
puter?,”Commun. ACM, vol. 28, pp. 1187–1199, 1985.
[4]  R. Parasuraman, “Human-computer monitoring,”Human Factors, vol.
29, pp. 695–706, 1987.
[5]  T.   B.   Sheridan,Telerobotics,   Automation,   and   Supervisory   Con-
trol.    Cambridge, MA: MIT Press, 1992.
[6]  R. Parasuraman and M. Mouloua,Automation and Human Performance:
Theory and Applications.    Mahwah, NJ: Erlbaum, 1996.
[7]  D.  D.  Woods,  “Decomposing  automation:  Apparent  simplicity,  real
complexity,”  inAutomation  and  Human  Performance:  Theory  and
Applications,  R.  Parasuraman  and  M.  Mouloua,  Eds.    Mahwah,  NJ:
Erlbaum, 1996, pp. 1–16.
[8]  R. Parasuraman and V. A. Riley, “Humans and automation: Use, misuse,
disuse, abuse,”Human Factors, vol. 39, pp. 230–253.
[9]  C. E. Billings,Aviation Automation: The Search for a Human-Centered
Approach.    Mahwah, NJ: Erlbaum, 1997.
[10]  C. D. Wickens, A. Mavor, R. Parasuraman, and J. McGee,The Future of
Air Traffic Control: Human Operators and Automation.Washington,
DC: National Academy Press, 1998.
[11]  T.  B.  Sheridan  and  W.  L.  Verplank,  “Human  and  Computer  Control
of  Undersea  Teleoperators,” MIT  Man-Machine  Systems Laboratory,
Cambridge, MA, Tech. Rep., 1978.
[12]  V.  Riley,  “A  general  model  of  mixed-initiative  human-machine  sys-
tems,”  inProc.  33rd  Annual  Human  Factors  Society  Conf..  Santa
Monica, CA, 1989, pp. 124–128.
[13]  A. D. Baddeley,Working Memory.    Oxford, U.K.: Clarendon, 1996.
[14]  D.  E.  Broadbent,Perception  and  Communication.    London,  U.K.:
## Pergamon, 1958.
[15]  C.  D. Wickens and J. Hollands,Engineering Psychology and Human
Performance, 3rd ed.    Englewood Cliffs, NJ: Prentice-Hall, 1999.
[16]  J. J. Gibson,The Ecological Approach to Visual Perception.    Boston,
MA: Houghton-Mifflin, 1979.
[17]  C.  D. Wickens, S. E. Gordon, and Y. Liu,An Introduction to Human
Factors Engineering.New York: Longman, 1998.
[18]  T. B. Sheridan, “Rumination on automation,” inProc. JFAC-MMS Conf..
## Kyoto, Japan, 1998.
[19]  J. D. Lee and T. F. Sanquist,Maritime automation in “Automation and
Human Performance:  Theory and Applications”, R. Parasuraman and
M. Mouloua, Eds.    Mahwah, NJ: Erlbaum, 1996, pp. 365–384.
[20]  S. G. Hart and T. E. Wempe, “Cockpit Display of Traffic Information:
Airline Pilots Opinions about Content, Symbology, and Format.,” NASA
Ames Research Center, Moffett Field, CA, NASA Tech. Memo. 78 601,
## 1979.
[21]  M. E. Morphew and C. D. Wickens, “Pilot performance and workload
using  traffic  displays  to  support  Free  Flight,”  inProc.  42nd  Annual
Human  Factors  and  Ergonomics  Society  Conf..  Santa  Monica,  CA,
1998, pp. 52–56.
[22]  N. Moray, “Human factors in process control,” inHandbook of Human
Actors  and  Ergonomics,  2nd  ed.  ed,  G.  Salvendy,  Ed.New  York:
Wiley, 1997, pp. 1944–1971.
[23]  K. Bennett and J. M. Flach, “Graphical displays: Implications for di-
vided attention, focused attention, and problem solving,”Human Fac-
tors, vol. 34, pp. 513–533, 1992.
[24]  A. Mundra, “A New Automation Aid to Air Traffic Controllers for Im-
proving Airport Capacity,” The Mitre Corporation, McLean, VA, Tech-
nical Report MP-89W00034, 1989.
[25]  A. Madni, “The role of human factors in expert systems design and ac-
ceptance,”Human Factors, vol. 30, pp. 395–414, 1988.
[26]  E.H.Shortliffe,Computer-BasedMedicalConsultation:
MYCIN.    Amsterdam, The Netherlands: Elsevier, 1976.
[27]  L. L. Schlabach, C. C. Hayes, and D. E. Goldberg, “FOX-GA: A genetic
algorithm for generating and analyzing battlefield courses of action,”J.
Evol. Comput., vol. 7, no. Spring, pp. 45–68, 1999.
[28]  C.  Layton,  P.  J.  Smith,  and  C.  E.  McCoy,  “Design  of  a  cooperative
problem-solving system for en-route flight planning: An empirical eval-
uation,”Human Factors, vol. 36, pp. 94–119, 1994.
[29]  W. B. Scott, “Automatic GCAS: You can’t fly any lower,”Aviation Week
and Space Technology, pp. 76–79, February 1, 1999.
[30]  W. Olson  and N. B. Sarter, “Supporting informed consent  in human-
machine collaboration: The role of conflict type, time pressure, display
design, and trust,” inProc. Human Factors and Ergonomics Society 43rd
Annual Meeting. Santa Monica, CA, 1999, pp. 189–193.
[31]  E.  W. Logdson,  S.  E. Infield,  S.  Lozito,  A.  McGann,  M. Macintosh,
and  A.  Possolo,  “Cockpit  data  link technology  and flight  crew  com-
munications procedures,” inProc. 8th Int. Symp. Aviation Psychology.
Columbus, OH, 1995, pp. 324–239.
[32]  E. E. Hahn and J. Hansman, “Experimental Studies on the Effect of Au-
tomation on Pilot Situational Awareness in the Datalink ATC Environ-
ment,” SAE International, PA, Tech. Paper 922 922, 1992.
[33]  P. A. Hancock, M. H. Chignell, and A. Lowenthal, “An adaptive human-
machine system,” inProc. 15th Annual IEEE Conf. Syst., Man, Cybern..
Washington, DC, 1985, pp. 627–629.
[34]  R. Parasuramanet al., “Theory and Design of Adaptive Automation in
Aviation Systems,” Naval  Air Warfare Center, Warminster, PA, Tech.
Rep. NAWCADWAR-92 033-60, 1992.
[35]  W. B. Rouse, “Adaptive aiding for human/computer control,”Human
Factors, vol. 30, pp. 431–438, 1988.
[36]  M. Barnes and J. Grossman, “The Intelligent Assistant Concept for Elec-
tronic Warfare Systems,” Naval Warfare Center, China Lake, CA, Tech.
Rep. NWC TP 5585, 1985.
[37]  T. Inagaki, “Situation-adaptive autonomy: Trading control of authority
in  human-machine  systems,”  inAutomation  Technology  and  Human
Performance: Current Research and Trends.Mahwah, NJ: Erlbaum,
1999, pp. 154–158.
[38]  E. A. Byrne and R. Parasuraman, “Psychophysiology and adaptive au-
tomation,”Biol. Psychol., vol. 42, pp. 249–268, 1996.
[39]  B. Hilburn, P. G. Jorna, E. A. Byrne, E. A. Byrne, and R. Parasuraman,
“The effect of adaptive air traffic control (ATC) decision aiding on con-
troller mental workload,” inHuman-Automation Interaction: Research
and Practice, M. Mouloua and J. Koonce, Eds.Mahwah, NJ: Erlbaum,
1997, pp. 84–91.
[40]  D. B. Kaber and J. M. Riley, “Adaptive automation of a dynamic con-
trol task based on workload assessment through a secondary monitoring
task,” inAutomation Technology and Human Performance: Current Re-
search and Trends, M. W. Scerbo and M. Mouloua, Eds.    Mahwah, NJ:
Erlbaum, 1999, pp. 129–133.
[41]  N. Moray, T. Inagaki, and M. Itoh, “Adaptive automation, trust, and self-
confidence in fault management of time-critical tasks,”J. Exper. Psych.:
Appl., vol. 6, pp. 44–58.
[42]  R. Parasuraman, M. Mouloua, and R. Molloy, “Effects of adaptive task
allocation on monitoring of automated systems,”Human Factors, vol.
38, pp. 665–679, 1996.
[43]  S. Scallen, P. A. Hancock, and J. A. Duley, “Pilot performance and pref-
erence for short cycles of automation in adaptive function allocation,”
Appl. Ergon., vol. 26, pp. 397–403, 1995.
[44]  M   Scerbo,  “Theoretical  perspectives   on   adaptive  automation,”  in
Automation  and  Human  Performance:  Theory  and  Applications,R.
Parasuraman  and  M.  Mouloua,  Eds.    Mahwah,  NJ:  Erlbaum,  1996,
pp. 37–63.
[45]  M. Lewis, “Designing for human-agent interaction,”Artif. Intell. Mag.,
vol. Summer, pp. 67–78, 1998.
[46]    “Automation surprises,” N. Sarter, D. D. Woods, and C. E. Billings,
inHandbook of Human Factors and Ergonomics, 2nd ed., G. Salvendy,
Ed.New York: Wiley, 1997, pp. 1926–1943.
[47]  C.   D.  Wickens,  “Designing  for  situation   awareness  and   trust   in
automation,”  inProc.  IFAC  Conf.  Integrated  Systems  Engineering.
Baden-Baden, Germany, 1994.
[48]  D. D. Woods and N. Sarter, “Evaluating the impact of new technology on
human-machine cooperation,” inVerification and Validation of Complex
Systems, J. A. Wise, V. D. Hopkin, and P. Stager, Eds.    Berlin: Springer-
Verlag, 1993, pp. 133–158.
[49]  K.J. Vicente and J. Rasmussen, “Ecological interface design: Theoretical
foundation,”IEEE Trans. Syst.,  Man,  Cybern.,  vol. 22,  pp.  489–506,
## 1992.
[50]  E. L. Wiener, “Cockpit automation,” inHuman Factors in Aviation,E.
L.  Wiener  and  D.  C.  Nagel,  Eds.    New  York:  Academic,  1988,  pp.
## 433–461.
[51]  A. Kirlik, “Modeling strategic behavior in human-automation interac-
tion: Why "aid" can (and should) go unused,”Human Factors, vol. 35,
pp. 221–242, 1993.
[52]  T. K. Landauer,The Trouble with Computers.    Cambridge, MA: MIT
## Press, 1995.
[53]  D. B. Kaber, E. Omal, and M. R. Endsley, “Level of automation effects
on telerobot performance and human operator situation awareness and
subjective  workload,”  inAutomation  Technology and  Human  Perfor-
mance: Current Research and Trends.Mahwah, NJ: Erlbaum, 1999,
pp. 165–170.
[54]  M. Endsley, “Automation and situation awareness,” inAutomation and
Human Performance: Theory and Applications, R. Parasuraman and M.
Mouloua, Eds.    Mahwah, NJ: Erlbaum, 1996, pp. 163–181.
[55]  M. Endsley and E. O. Kiris, “The out-of-the-loop performance problem
and  level  of  control  in  automation,”Human  Factors,  vol.  37,  pp.
## 381–394, 1995.

296IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART A: SYSTEMS AND HUMANS, VOL. 30, NO. 3, MAY 2000
[56]  N. Sarter and D. D. Woods, “’Strong, silent, and out-of-the-loop’: Prop-
erties of advanced (cockpit) automation and their impact on human-au-
tomation interaction,” Cognitive Systems Engineering Laboratory, Ohio
State  University,  Columbus,  OH,  Technical  Report  CSEL  95-TR-01,
## 1995.
[57]  E. L. Wiener, “Complacency: Is the term useful for air safety?,” inProc.
26th Corporate Aviation Safety Seminar. Denver, CO, 1981.
[58]  R. Parasuraman, R. Molloy, and I. L. Singh, “Performance consequences
of automation-induced ’complacency’,”Int. J. Aviation Psychology, vol.
3, pp. 1–23, 1993.
[59]  S. Farrell and S. Lewandowsky, “A connectionist model of complacency
and adaptive recovery under automation,”J.  Exper.  Psychol.: Learn.,
Memory, Cogn., vol. 26, pp. 395–410.
[60]  C.  D.  Wickens,  R.  Conejo,  and  K.  Gempler,  “Unreliable  automated
attention  cueing  for  air-ground  targeting  and  traffic  maneuvering,”
inProc. 34th  Annual Human Factors and Ergonomics Society Conf..
Santa Monica, CA, 1999.
[61]  M. Yeh, C. D. Wickens, and F. J. Seagull, “Target cueing in visual search:
The effects  of conformality and display  location on  the allocation of
visual attention,”Human Factors, vol. 41, 1999.
[62]  W. M. Crocoll and B. G. Coury, “Status or recommendation: Selecting
the type of information for decision aiding,” inProc. 34th Annu. Human
Factors and Ergonomics Society Conf.. Santa Monica, CA, 1990, pp.
## 1524–1528.
[63]  A.  M.  Rose,  “Acquisition  and  retention  of  skills,”  inApplication  of
Human Performance Models to System Design, G. McMillan, Ed.    New
## York: Plenum, 1989.
[64]  A. Swain, “Human reliability analysis: Needs, status, trends, and limi-
tations,”Reliab. Eng. Syst. Saf., vol. 29, pp. 301–313, 1990.
[65]  D. L. Parnas, A. J. van Schouwen, and S. P. Kwan, “Evaluation of safety-
critical software,”Commun. ACM, vol. 33, pp. 636–648, 1990.
[66]  J. D. Lee and N. Moray, “Trust, control strategies, and allocation of func-
tion in human-machine systems,”Ergonomics, vol. 35, pp. 1243–1270,
## 1992.
[67]  A. J. Masalonis and R. Parasuraman, “Trust as a construct for evalua-
tion of automated aids: Past and present theory and research,” inProc.
Human Factors and Ergonomics Society 43rd Annual Meeting. Santa
Monica, 1999, pp. 184–188.
[68]  J.  A.  Swets  and  R.  M.  Pickett,Evaluation  of  Diagnostic  Systems:
Methods from Signal Detection Theory.    New York: Academic, 1982.
[69]  J. Kuchar, “Methodology for alerting-system performance evaluation,”
J. Guidance, Control, and Dyanmics, vol. 19, pp. 438–444, 1996.
[70]  R. Parasuraman, P. A. Hancock, and O. Olofinboba, “Alarm effective-
ness in driver-centered collision-warning systems,”Ergonomics, vol. 39,
pp. 390–399, 1997.
[71]  J. L. Merlo, C. D. Wickens, and M. Yeh, “Effects of reliability on cue
effectiveness and display signalling,” University of Illinois Aviation Re-
search Lab, Savoy, IL, Technical report ARL-99-4/Fedlab-99-3, 1999.
[72]    “Aviation Week and Space Technology,”Answers to the Gridlock, pp.
## 42–62, February 2, 1998.
[73]  “Report of the RTCA Board  of Director’s Select Committee on Free
Flight,” RTCA, Washington, DC, 1995.
[74]  R. van Gent, J.  M. Hoekstra,  and R. C.  J. Ruigrok, “Free flight with
airborne separation assurance,” inProc. Int. Conf. Human Computer In-
teraction in Aeronautics. Montreal, , Canada, 1998, pp. 63–69.
[75]  P.  M. Fitts,Human Engineering  for  an  Effective  Air  Navigation and
Traffic Control System.Washington, DC: National Research Council,
## 1951.
[76]  T. B. Sheridan,  “Allocating functions rationally between humans and
machines,”Ergonomics in Design, vol. 6, no. 3, pp. 20–25, 1998.
[77]  R.  W.  Pew  and  A.  S.  Mavor,Modeling  Human  and  Organizational
Behavior:  Application   to   Military  Simulations.Washington,   DC:
## National Academy Press, 1998.
[78]  T.  B.  Sheridan  and  R.  Parasuraman,  “Human  vs.  automation  in  re-
sponding to failures: An expected-value analysis,” Human Factors, to
be published.
[79]  Z. Wei, A. P. Macwan, and P. A. Wieringa, “A quantitative measure for
degree of automation and its relation to system performance,”Human
Factors, vol. 40, pp. 277–295, 1998.
[80]  K. Corker, G. Pisanich, and M. Bunzo, “Empirical and analytic studies
of human/automation dynamics in airspace management for free flight,”
inProc. 10th Int. CEAS Conf. Free Flight. Amsterdam, The Netherlands,
## 1997.
[81]   A. Degani, M. Shafto, and A. Kirlik, “Models in human-machine sys-
tems: Constructs, representation, and classification,”Int. J. Aviation Psy-
chology, vol. 9, pp. 125–138, 1999.
[82]   R.  Parasuraman,  “Designing  automation  for  human  use:  Empirical
studies and quantitative models,” Ergonomics, to be published.
[83]   D. A. Norman,The Invisible Computer, 1998.
Raja Parasuramanreceived the B.Sc. degree (first
class honors) in electrical engineering from Imperial
College, University of London, U.K. in 1972, and the
M.Sc. and Ph.D. degrees in applied psychology from
the University of Aston, Birmingham, U.K in 1973
and 1976, respectively.
From  1978  to  1982,  he  was  a  Research  Fellow
at  the  University  of  California,  Los  Angeles.  In
1982, he joined the Catholic University of America,
Washington,  D.C.  as  Associate  Professor  and  was
promoted to Full Professor in 1986. He is currently
Director  of  the  Cognitive  Science  Laboratory  and  also  holds  a  visiting
appointment at the Laboratory of Brain and Cognition at the National Institute
of  Mental  Health,  Bethesda,  MD.  His  research  interests  are  in  the  areas  of
attention,  automation,  aviation  and  air  traffic  control,  event-related  brain
potentials, functional brain imaging, signal detection, vigilance, and workload.
Dr. Parasuraman is a Fellow of the American Association for the Advance-
ment of Science (1994), the Human Factors and Ergonomics Society (1994),
and the American Psychological Society (1991). He is also currently serving on
the National Research Council Panel on Human Factors.
Thomas  B.  Sheridan(M’60–SM’82–F’83–LF’96)
received  the  B.S.  degree  from  Purdue  University,
West Lafayette, IN, the MS degree from University
of  California,  Los  Angeles,  the  Sc.D.  degree  from
the  Massachusetts  Institute  of  Technology  (MIT),
Cambridge,   and   the   Dr.   (honorary)   from   Delft
University of Technology, The Netherlands.
For most of his professional career he has remained
at MIT, where he is currently Ford Professor of Engi-
neering and Applied Psychology Emeritus in the De-
partment of Mechanical Engineering and Department
of Aeronautics and Astronautics, continuing to teach and serve as Director of
the Human-Machine Systems Laboratory. He has also served as a visiting pro-
fessor at University of California, Berkeley, Stanford, Delft University , Kassel
University, Germany, and Ben Gurion University, Israel. His research interests
are in experimentation, modeling, and design of human-machine systems in air,
highway and rail transportation, space and undersea robotics, process control,
arms control, telemedicine, and virtual reality. He has published over 200 tech-
nical papers in these areas. He is co-author ofMan-Machine Systems(Cam-
bridge, MA: MIT Press, 1974, 1981; USSR, 1981), coeditor ofMonitoring Be-
havior and Supervisory Control(New York: Plenum, 1976), author ofTeler-
obotics, Automation, and Human Supervisory Control(Cambridge, MA: MIT
Press, 1992), and co-editor ofPerspectives on the Human Controller(Mahwah,
NJ: Erlbaum, 1997). He is  currently Senior Editor of the MIT  Press journal
Presence: Teleoperators and Virtual Environmentsand serves on several edito-
rial boards. He chaired the National Research Council’s Committee on Human
Factors, and has served on numerous government and industrial advisory com-
mittees. He is principal of Thomas B. Sheridan and Associates, a consulting
firm.
Dr. Sheridan was President of the IEEE Systems, Man, and Cybernetics So-
ciety,  Editor  of  IEEE  T
RANSACTIONS  ONMAN-MACHINESYSTEMS,  received
their  Norbert  Wiener and  Joseph  Wohl  awards,  the  IEEE  Centennial  Medal
and Third Millenium Medal. He is also a Fellow of the Human Factors and Er-
gonomics Society, recipient of their Paul M. Fitts Award, and was President of
HFES. He received the 1997 National Engineering Award of the Amer.ican As-
sociation of Engineering Societies and the 1997 Oldenburger Medal of ASME.
He is a member of the National Academy of Engineering.

PARASURAMANet al.: TYPES AND LEVELS OF HUMAN INTERACTION WITH AUTOMATION297
Christopher D.  Wickensreceived the A.B. degree
from Harvard College, Cambridge, MA, in 1967 and
the Ph.D. degree  from the University  of Michigan,
Ann Arbor, in 1974.
He served as a commissioned officer in the U.S.
Navy from 1969 to 1972. He is currently a Professor
of Experimental  Psychology,  Head  of  the Aviation
Research Laboratory, and Associate Director of the
Institute of Aviation at the University of Illinois at
Urbana-Champaign. He also holds an appointment in
the Department of Mechanical and Industrial Engi-
neering and the Beckman Institute of Science and Technology. His research in-
terests involve the application of the principles of human attention, perception
and cognition to modeling operator performance in complex environments, par-
ticularly aviation, air traffic control and data visualizations.
Dr. Wickens is a member and Fellow of the Human Factors Society and re-
ceived the Society’s Jerome H. Ely Award in 1981 for the best article in the
Human Factors Journal, and the Paul M. Fitts Award in 1985 for outstanding
contributions  to  the  education  and  training  of  human  factors  specialists.  He
was elected to the Society of Experimental Psychologists, elected Fellow of the
American Psychological Association, and in 1993 received the Franklin Taylor
Award for Outstanding Contributions to Engineering Psychology from Division
21 of that association.
