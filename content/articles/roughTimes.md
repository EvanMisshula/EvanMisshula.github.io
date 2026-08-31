title: Rough Times
date: 2026-08-30
author: emisshula
category: grit
tags: ambition, persitence
slug: rough

<p><img src="../../images/safetyObs.jpeg" width="600px" alt="emerson" title="safety"></p>


<a id="orgf35a5db"></a>

# A Rough 18 Months on the Flight Deck: Using the experience of Linux Kernel maintainers to build HRO's in the Age of AI

An aircraft-carrier flight deck is an improbable place to look for
reassurance.Aircraft land on a moving ship. Jet engines, fuel,
ordnance, people, vehicles, and heavy machinery share a cramped,
pitching surface. The tempo is relentless, information is incomplete,
and a minor lapse can cascade into catastrophe within seconds. The
crews are highly trained, yet they remain human: they fatigue,
miscommunicate, overlook signals, and err.And yet carrier aviation
learned to conduct these operations day after day with extraordinary
reliability.That puzzle helped launch the study of High Reliability
Organizations (HROs). In a foundational 1987 paper, Gene Rochlin, Todd
La Porte, and Karlene Roberts examined aircraft-carrier flight
operations as a setting in which ordinary trial-and-error learning
could prove catastrophically expensive.
<https://digital-commons.usnwc.edu/nwc-review/vol40/iss4/7/>

Later, Karl Weick and Roberts described reliable flight-deck
performance in terms of a  \`\`collective mind'': reliability emerged not
because any individual became incapable of error, but because people
attended carefully to one another and continually fitted their
actions into a larger, living system.
<https://www.jstor.org/stable/2393372>  

That picture was on my mind while listening to Linux kernel
maintainer Greg Kroah-Hartman talk about what large language models
are doing to software security.

Kroah-Hartman is not principally asking what a sufficiently advanced
AI might do someday. He is describing what AI-assisted vulnerability
discovery is doing to a real security workflow now. His warning is
memorable:

> "It's going to be a rough 18 months &#x2026;"

I do not mean that Kroah-Hartman is making an HRO argument. The
comparison is mine. But I think Linux is giving us an unusually
concrete example of a problem many organizations are facing:

> How do we scale verification as we scale intelligence?


<a id="org27abd6d"></a>

# Weak signals become cheap

Kroah-Hartman's description of LLMs is deliberately reductive. He
calls them pattern matchers. Code is full of patterns, and security
bugs often have patterns too. Give a model examples of old
vulnerabilities and an enormous body of source code and it can search
for related mistakes at a scale that would have been economically
impossible with human attention alone.

The operational capability matters more here than the philosophical
argument about whether a model "reasons." I disagree but we can fight
that out in your favorite pub or coffee shop in person some other
time.

A human security researcher has limited time. A tiny defect may not
justify hours of investigation. Machine search changes that
calculation. It can inspect far more code and look for ways that
individually unimpressive defects can be combined:

    small defect + small defect + small defect -> consequential attack path

Kroah-Hartman says the kernel security workload is already
accelerating. In the talk, he describes a security-patch tempo that
has gone from roughly one fix every thirty minutes to roughly one
every twenty minutes. He explicitly calls it "not a huge increase."
But for a system already processing security fixes publicly, in high
volume and 24-hours a day, it is not trivial.

There is a flip side to the story. The very systems that cheaply
generate useful weak signals also an overflow of false ones.

Kroah-Hartman estimates that even the best models he is seeing are
wrong something like a quarter to a third of the time in this
setting. I would take that as his operational estimate, not as a
benchmark result. But it points to what I think is the central
organizational problem:

> LLMs are both the world's greatest detectors of weak
> signals yet also the world's greatest generators of false weak signals.

When detection becomes nearly free, verification becomes the scarce
resource. Organizations are inundated with warnings while their
capacity to separate genuine danger from plausible noise remains
tightly constrained.This is exactly the environment high-reliability
organizing was built for: one in which serious failures often first
appear as weak signals, yet treating every signal as urgent would
quickly exhaust the system's capacity to respond.


<a id="orga9a474c"></a>

# Reliability is a property of the system

High Reliability Organization research began with a puzzle: some
organizations operate complex technologies where mistakes can kill
people and catastrophic failure is always possible, yet they sustain
remarkably reliable performance. The original Berkeley researchers
studied U.S. Navy aircraft carriers, nuclear power operations, and
air-traffic control. Aircraft-carrier flight operations became one of
the foundational cases. [Rochlin, La Porte & Roberts (1987)](https://digital-commons.usnwc.edu/nwc-review/vol40/iss4/7/).

The idea extends well beyond the flight deck. Organizations and
industries commonly examined through the high-reliability lens
include:

-   aircraft-carrier flight operations;
-   air-traffic control;
-   nuclear power generation;
-   commercial aviation; and
-   increasingly, health-care systems attempting to adopt HRO practices.

Commercial aviation provides a striking example of what sustained
improvement can look like. In the 1970s, there were roughly one fatal
accident for every 165,000 flights. Recent figures are on the order of
one fatal accident per several million flights. [Historical
aviation-safety data](https://ourworldindata.org/data-insights/commercial-flights-have-become-significantly-safer-in-recent-decades). The important fact is not that aviation
eliminated human error. It did not. Reliability improved while humans
remained fallible.

The familiar five-part HRO vocabulary came later. Weick, Kathleen
Sutcliffe, and their collaborators synthesized the research tradition
around:

-   preoccupation with failure;
-   reluctance to simplify;
-   sensitivity to operations;
-   commitment to resilience; and
-   deference to expertise.

[Weick & Sutcliffe, *Managing the Unexpected*](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119175834)

Those labels should not be projected backward onto the original
carrier researchers. They are a later synthesis of what the HRO
tradition learned about organizations that repeatedly do dangerous
things without allowing ordinary errors to become catastrophes.

My shorthand for the underlying lesson is:

> The systems layer should do work, the system should be more reliable than the
> least reliable individual in it.

My shorthand for the underlying lesson is:

> The systems layer should do work. A reliable organization should be
> more reliable than any individual it depends on.

That is my formulation, not a quotation from the HRO literature. But
it captures the organizational problem Weick and Roberts were trying
to explain with "heedful interrelating." High reliability does not
come from eliminating human error. It comes from arranging fallible
people, procedures, checks, and lines of communication so that one
person's mistake does not automatically become the system's mistake.

Who notices? Who communicates? Who has the relevant expertise? Who can
stop the process? What gets checked independently? What happens when
something almost goes wrong? And when one layer fails, what prevents
that failure from propagating?

In other words, the organization itself has to contribute to
reliability.

That is what makes the Linux response to LLM-generated vulnerability
reports so interesting.

The objective cannot be to make every model right. It cannot even be
to make every human reporter right.

The objective is to build a process that remains reliable when they
are wrong.


<a id="org99dd19f"></a>

# "Give me a patch"

One of Kroah-Hartman's most practical observations is almost comically simple.

When someone submits an AI-generated security report, don't just ask
for the vulnerability. Ask the reporter to submit a patch.

> "Give me a patch."

Kroah-Hartman says this eliminates roughly a third of the reports. A
model may confidently describe a vulnerability and produce a
persuasive explanation, yet fail when asked to specify the change that
would actually fix it.

That simple requirement changes the economics of the process.

A bug report is a claim. A patch is a proposed intervention based on
that claim. Requiring both forces the reporter and the model to carry
the argument one step further: **if this is really the problem, what
exactly should change?**

This does not make the model trustworthy. It makes a cheap claim more
expensive to act upon. The surrounding process is doing work.

And a patch is still not proof. Linux subjects patches to layered
testing, subsystem review, expert judgment, and integration. A change
can compile, pass local tests, and still be wrong in the larger
system.

> "Give me a patch" is a filter, not a proof system.

That is the cannonical idea of high-reliability. Do not search for one
perfect defense. Build layers of partially independent defenses so
that when one layer fails, the failure still has somewhere else to be
caught.


<a id="org808ce40"></a>

# Near misses are information

HROs are often described as having a **preoccupation with
failure**. That does not mean buying into the "doom marketing" of the
frontier AI labs. Be an optimist. Build things. Expect them to
work. But recognize that **failure is where the information lives**.

Small failures, anomalies, close calls, and weak signals tell us where
our picture of the system is incomplete. A near miss is especially
valuable because it exposes a path toward failure while there is still
time to learn from it.

Suppose a model reports a vulnerability and proposes a patch. Testing
or expert review catches the patch because, while fixing the reported
problem, it would introduce another one.

It is tempting to record that as: **the process worked.**

It did. But the more useful questions are:

-   What did we just learn about how the process could fail?
-   Which layer caught the problem?
-   Which earlier layers missed it, and why?
-   Would another subsystem or reviewer have caught it?
-   Was the problem obvious to an expert but invisible to the automated tests?
-   What happens when the next model produces a more convincing wrong answer?

The point is not to celebrate failure or become paralyzed by its
possibility. It is to extract information from failure while the
consequences are still cheap.

A near miss is therefore more than a successful interception. It is
evidence about the structure of the system: where its defenses are
strong, where they overlap, and where a failure might still pass
through.

Applying that framing to AI-generated patches is my extension of the
HRO idea. As machine-generated work increases, we should not throw
away intercepted failures.

> Near misses are training data for the organization.


<a id="org1ad0d9f"></a>

# Defer to expertise

There is another striking correspondence between Linux practice and
HRO thinking.

The Linux kernel security team does not pretend to contain the world's
deepest expert on every subsystem. Kroah-Hartman's description of the
security process is explicit: when a problem requires expertise the
security team does not have, they bring in the maintainers who do.

That resembles the HRO principle of **deference to expertise**.

In a high-reliability organization, authority cannot always follow the
org chart. When something unusual happens, the critical question is
not **who outranks whom?** It is **who understands this problem best?**
The organization must be able to find that person, get the relevant
information to them, and give their expertise influence over the
decision while it can still matter.

That is a more demanding idea than simply hiring brilliant people.

It also has implications for how we build institutions around
AI. Frontier labs and the agencies charged with regulating AI safety
certainly need extraordinary computer scientists, mathematicians, and
engineers. But the problems created by increasingly capable AI systems
will not all be computer-science problems.

They will also be problems of organizations, incentives, human
behavior, security, law, institutions, communication, adversarial
behavior, and failure under partial information. A lab or regulator
filled exclusively with CS prodigies can therefore be extraordinarily
intelligent and still possess dangerous blind spots.

That is why these institutions would do well to hire trained social
scientists and experts of many stripes alongside their technical
talent: organizational sociologists who study institutional failure;
psychologists who understand human judgment; criminologists who study
deterrence, rule-breaking, and oversight; security practitioners who
think adversarially; lawyers who understand how rules behave in
institutions; and people from high-reliability domains who have spent
careers managing systems where mistakes have consequences.

The point is not diversity of expertise as an ornament. It is
diversity of expertise as a safety mechanism.

> Deference to expertise only works if the expertise you will eventually need is somewhere in the room.

Linux does not make every security-team member an expert on every
kernel subsystem. It has built a system capable of reaching the
relevant expertise when a problem demands it. AI labs and regulators
should aspire to the same thing.


<a id="org5d8ff46"></a>

# A strange signal from the security list

The most provocative part of Kroah-Hartman's talk concerns duplicate
reports.

He says the kernel security team sees duplicate bug reports every day
and warns that information sent to an external model should be treated
as public. In the talk, he interprets at least some of that
duplication as evidence of leakage or models sharing information.

The underlying observation is stronger than a single anecdote.

Linux's security documentation now instructs researchers that if AI
assistance was used to identify a bug, they should treat the finding
as public. The stated reason is operational experience: AI-assisted
discoveries repeatedly surface across multiple researchers, often on
the same day.

Linus Torvalds has separately complained about the \`\`enormous
duplication'' created when different people find the same issues with
the same tools.

So the duplicates are real.

The causal mechanism is not established.

Duplicate discoveries do not prove that a model provider took one
researcher's private vulnerability and exposed it to another
user. Given the volume of overlap, the observation cannot be summarily
dismissed either.

This is a false choice. We need not either dismiss the signal or
pretend its cause has been proven.

Linux has observed a recurring pattern, recognized that the loss of
vulnerability secrecy can be serious, and adopted a conservative rule:
if you use external AI assistance, act as though the discovery may no
longer be secret.

That is a concrete example of HRO epistemology:

> High reliability does not require certainty before taking a weak
> signal seriously. It requires taking the signal seriously without
> pretending that uncertainty has disappeared.


<a id="org8138ff3"></a>

# Run it locally — and understand its limits

Kroah-Hartman's practical recommendation for security-sensitive work
is to run models locally.

That advice is sound, but it is worth being precise about **why**.

    DATA BOUNDARY
    Does sensitive information leave my controlled environment?
    
    MODEL BOUNDARY
    What am I trusting about the model, its weights, provenance, training,
    and behavior?

Local inference directly addresses the first. When the surrounding
system is configured correctly, unpublished vulnerabilities and
proprietary code need not leave the organization's perimeter for an
external inference service.

Open-weight models can also improve control over the second. A team
can pin a specific revision, archive it, hash the files, test it,
inspect it, and decide when (or whether) to replace it, rather than
silently tracking a remote provider's changing default.

These are real advantages. They are capabilities, not guarantees.

A hash confirms that the file is the one you expected; it does not
certify that the policy encoded in that file is
benign. Reproducibility requires capturing the surrounding inference
stack, not merely the weights. Local execution protects
confidentiality only if the rest of the application and host are
actually configured to keep the data local.

Most importantly:

> Local does not mean trusted.


<a id="org717e9a9"></a>

# leeper agents and the model boundary

The **Sleeper Agents** experiments by Evan Hubinger and colleagues make
the distinction concrete.

The researchers deliberately trained language models with conditional
backdoors. In one code-generation setting, a model was trained to emit
secure code under one year/context cue and vulnerable code under
another. That conditional behavior persisted through several of the
subsequent safety-training procedures they tested.

The result should not be overstated.

The researchers **constructed** the sleeper agents. They did not
discover that any particular production open-weight model already
contains such a backdoor. The experiment demonstrates technical
feasibility, not prevalence in the wild.

Feasibility is enough for the narrow point at hand: physical
possession of a model does not certify the policy encoded in its
weights.

Running locally can protect the confidentiality of what is sent to the
model. Open weights can increase an organization's ability to freeze,
inspect, test, and audit the artifact. Neither fact removes the need
to ask what the model will do under conditions that have not yet been
anticipated.

This is not an argument against open weights. It is closer to the
opposite. Local and open models supply valuable tools for controlling
the data boundary and investigating the model boundary.

The HRO lesson is that those tools still have to sit inside a reliable
process.


<a id="org8cbb72a"></a>

# Intelligence is getting cheaper. Verification is not.

For years, much of the AI-safety discussion has focused,
understandably, on the properties of models. Can we make them more
truthful? More aligned? More robust?

Those questions matter.

But a second problem grows more urgent as intelligent systems
proliferate:

> How do we scale verification as we scale intelligence?

Suppose machine intelligence becomes cheap enough that we can place an
intelligent agent against every codebase, log stream, transaction,
sensor feed, filing, and organizational decision.

We will receive more genuine signals.  We will also receive more false
ones.

The bottleneck moves.

The scarce resource becomes the capacity to decide which claims
deserve attention, which interventions may proceed, which experts must
be involved, what evidence is sufficient, and what the organization
should learn when a defense nearly fails.

That is why I keep returning to the flight deck.

The sailors on a carrier did not solve their problem by eliminating
human fallibility.

Neither Linux nor any other complex organization will solve its
problem by eliminating fallibility from every maintainer, contributor,
security researcher, or model.

AI safety cannot rest entirely on the hope of building models that
never err, never deceive, and never encounter conditions their
designers failed to anticipate.

> Trust individuals and tools where justified. Build the organization
> for the moments when that trust fails.

**Do the work**

Kroah-Hartman's warning is that we may be in for a rough 18 months.

Whether that number proves exact matters less than the operational
problem he is naming.

Machine intelligence is making useful signals cheaper to discover and
false signals cheaper to generate. It hands us extraordinary new tools
while forcing us to redesign the institutions through which those
tools reach consequential systems.

**The response should not be panic.**

It is better filters, stronger evidence, layered verification,
attention to near misses, deference to expertise, clear boundaries
around sensitive information, processes that can recover when one
defense fails, and organizations capable of learning.

Aircraft-carrier crews learned to do this while launching and
recovering aircraft from moving ships. Linux maintainers are adapting
the same basic organizational problem to a world in which machines can
search, report, and write code at enormous scale.

The HRO connection is mine, not Kroah-Hartman’s. But I think his
advice remains the right place to end:

> Just do the work.


<a id="org23565df"></a>

# A brief note on where this goes next

The same institutional question arises wherever consequential
decisions are made under incomplete information: how much safety
should rest on the virtue or competence of any single actor, and how
much should be designed into the organization surrounding that actor?

I believe the HRO lens has important implications beyond software
security which include AI control and criminal justice. Those
arguments deserve posts of their own. For now, Linux offers a concrete
place to begin.


<a id="org855dbb7"></a>

# References

-   ****Rochlin, G. I., La Porte, T. R., & Roberts, K. H. (1987).**** "The Self-Designing High-Reliability Organization: Aircraft Carrier Flight Operations at Sea." **Naval War College Review**, 40(4), Article 7, pp. 76–90. [[Naval War College Repository](<https://digital-commons.usnwc.edu/nwc-review/vol40/iss4/7/>)]
-   ****Weick, K. E., & Roberts, K. H. (1993).**** "Collective Mind in Organizations: Heedful Interrelating on Flight Decks." **Administrative Science Quarterly**, 38(3), pp. 357–381. [[DOI: 10.2307/2393372](<https://doi.org/10.2307/2393372>)]
-   ****Weick, K. E., & Sutcliffe, K. M. (2015).**** **Managing the Unexpected: Sustained Performance in a Complex World** (3rd ed.). Jossey-Bass / Wiley. [[Publisher Link](<https://onlinelibrary.wiley.com/doi/book/10.1002/9781119175834>)]
-   Greg Kroah-Hartman, "Linux kernel security work," January 2, 2026. [[[<https://www.kroah.com/log/blog/2026/01/02/linux-kernel-security-work/>](<https://www.kroah.com/log/blog/2026/01/02/linux-kernel-security-work/>)][GKH's site]]
-   ****The Linux Kernel Organization.**** "Security Bugs." **Linux Kernel Documentation**. [[docs.kernel.org](<https://docs.kernel.org/process/security-bugs.html>)]
-   ****The Linux Kernel Organization.**** "AI Coding Assistants." **Linux Kernel Documentation**. [[docs.kernel.org](<https://docs.kernel.org/process/coding-assistants.html>)]
-   ****Torvalds, L. (2026, May 17).**** "Linux 7.1-rc4." **Linux Kernel Mailing List (LKML)**. [[LKML Archive](<https://lkml.iu.edu/hypermail/linux/kernel/2605.2/01597.html>)]
-   ****The Linux Kernel Organization.**** "Linux Kernel Patch Submission Checklist." **Linux Kernel Documentation**. [[docs.kernel.org](<https://docs.kernel.org/process/submit-checklist.html>)]
-   ****Hubinger, E. et al. (2024).**** "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training." **arXiv preprint arXiv:2401.05566**. [[arXiv Link](<https://arxiv.org/abs/2401.05566>)]

