---
source: https://www.usenix.org/system/files/sec19-torres-arias.pdf
description: USENIX Security '19 paper introducing in-toto, a framework that cryptographically verifies the integrity of each step in a software supply chain from source to deployment via a signed layout and per-step link metadata.
captured: 2026-07-06
capture: pdf-read
type: ./types/snapshot.md
tags: [academic-paper]
---

# in-toto: Providing farm-to-table guarantees for bits and bytes

Author: Santiago Torres-Arias (New York University), Hammad Afzali (New Jersey Institute of Technology), Trishank Karthik Kuppusamy (Datadog), Reza Curtmola (New Jersey Institute of Technology), Justin Cappos (New York University)
Source: https://www.usenix.org/system/files/sec19-torres-arias.pdf
Date: August 2019 (28th USENIX Security Symposium, pp. 1393-1410)

Note: this is a condensed, section-by-section capture of the full 19-page PDF (fetched with `curl` using a browser User-Agent, since `usenix.org` returns 403 to plain fetchers). It preserves the paper's substantive argument, model, and findings but omits most figures, the full grammar listings, and the two-page reference/attack-survey appendix tables. Paraphrase is used for exposition; direct terminology (`layout`, `link`, `functionary`, artifact rules, etc.) is kept verbatim since it is load-bearing.

## Abstract

Software supply chains — check-in, build, test, package, distribute — are chained series of steps run by independent, often mutually distrusting parties. An attacker who compromises any single step can modify the software and harm its users. in-toto is a framework that cryptographically ensures the integrity of the software supply chain as a whole (not just of individual steps), letting the end user verify the chain from a project's inception to its deployment. The paper demonstrates in-toto's effectiveness against 30 real supply-chain compromises and its use in cloud-native, hybrid-cloud, and cloud-agnostic deployments; in-toto is integrated into products used by millions of people daily.

## 1. Introduction / motivation

A software supply chain is a series of *steps*, each an operation that takes *materials* (source, binaries, docs, icons, ...) and produces *products* (libraries, packages, images, installers, ...) — collectively *artifacts*. Steps may run sequentially, in parallel, or by any number of hosts (e.g., to test reproducibility). Steps also emit *byproducts* (stdout/stderr/return value) that indicate success or failure.

Existing supply-chain security is piecemeal: point solutions secure individual steps (commit signing, reproducible builds, package-delivery protections) but there is no mechanism to verify (1) that the correct steps were followed and (2) that no tampering occurred *between* steps. The paper gives real incidents where an attacker altered output between an otherwise-correct step and the next: e.g., a compromised web server let attackers swap a Linux Mint disk image even though every package checksum on the site matched — there was no verification tying the delivered image back to the actual build/release process, enabling a hundred-host botnet in hours.

in-toto ("as a whole," Latin) is presented as the first framework that holistically enforces software-supply-chain integrity by gathering cryptographically verifiable information about the chain itself, rather than only about each step in isolation.

## 2. Definitions and threat model

**Roles.** *Project owner* — defines the supply chain *layout* (which steps, by whom, in what order) and signs it with their private key. *Functionaries* — the parties that perform steps and produce signed *link metadata* recording what they did; can be human or automated (e.g., a build farm). *Client* (end user) — inspects and uses the *delivered product*, using the layout plus the collected links to verify it.

**Security goals:**
- **Supply chain layout integrity** — steps run in the specified order; none added, removed, or reordered.
- **Artifact flow integrity** — artifacts created/transformed/used by steps are not altered in between steps (if step A creates `foo.txt` and step B consumes it, B must use exactly the file A created).
- **Step authentication** — only the intended, explicitly-permitted party may perform a given step.
- **Implementation transparency** — in-toto does not require existing supply chains to change practice; it can represent an existing configuration and reason about it as-is.
- **Graceful degradation of security properties** — a single key compromise should not undermine all security properties; the system should degrade gracefully rather than "lose-one-lose-all."

**Threat model** — the attacker may, in various scenarios: interpose between two existing supply-chain steps to change a step's input; act as a step (e.g., by compromising or coercing the functionary, such as a hacked compiler inserting malicious code); deliver a product for which not all steps were actually performed (including via an honest mistake); include outdated/vulnerable elements; or provide a counterfeit delivered product signed by any keys. Public keys of project owners are assumed known to verifiers and not compromised by the attacker; the paper separately explores degrees of attacker access to functionary/infrastructure keys (Section 5).

## 3. System overview

Two fundamental limitations of the pre-in-toto landscape: (1) point solutions securing individual steps cannot guarantee the security of the entire chain; (2) even when testing/analysis tools are used, information about what tools ran or what they found is rarely surfaced to clients making trust decisions. in-toto addresses both by gathering and verifying metadata about every stage, from first commit to delivered package, in a cryptographically verifiable fashion.

Three components carry the framework:

**3.1 The supply chain layout.** A signed recipe (JSON) listing named *steps* and (optionally) *inspections*, each with: `expected_materials` / `expected_products` (as artifact rules — see below), `expected_command`, `pubkeys` (which functionary key(s) may sign this step's link), and `threshold` (minimum number of independently signed, matching links required — supports requiring k-of-n redundant functionaries, e.g. for reproducible-build attestation). The layout carries an expiration date and a human-readable README field. *Inspections* are extra verification-time actions the client runs against the delivered product itself (e.g., unzip an archive and check every contained file was created by the right party) — useful when in-toto's step/artifact-rule vocabulary alone can't express a supply chain's domain-specific semantics.

**3.2 Link metadata.** Each executed step produces a *link*: `_type: "link"`, `name` (matches the step definition), `command` run, `materials` and `products` (paths with cryptographic hashes), `byproducts` (stdout/stderr/return-value), and a `signature` from the functionary's key. Links are the chain's actual evidence: they tie each step's real inputs/outputs together and let a verifier reconstruct what happened and confirm it matches the layout's requirements.

**3.3 Artifact rules.** These are the mechanism that ties artifact flow between steps (they behave like firewall rules over artifact paths, matched by regex pattern): `CREATE`, `DELETE`, `MODIFY`, `ALLOW`, `DISALLOW` govern whether an artifact may be produced/consumed within one step; `MATCH` (with optional `IN <prefix>` clauses on both sides) requires that an artifact used at one step be byte-identical (same hash) to a named artifact created at another named step — this is literally how in-toto prevents "an attacker interposes between two steps and swaps the file." The paper's example: project owner Diana defines a three-step layout (`tag` -> `build` -> `package`), each with a distinct functionary (Alice, Bob, Clara); `foo.c` produced by `tag` must `MATCH` the material consumed by `build`, etc.

**3.4 Verification (`VERIFY_FINAL_PRODUCT`).** The client, holding the layout, all collected links, and the project owner's public key, runs: (1) verify the layout's signature and that it has not expired; (2) load the functionary public keys from the layout; (3) for each step, collect signed links and drop any with invalid signatures, then check the surviving count meets the step's threshold (fail with "link metadata is missing" otherwise); (4) apply all artifact rules across the collected links/steps, building an artifact-flow graph; (5) run any inspections and re-apply artifact rules including inspection-produced artifacts; (6) if all checks pass, verification succeeds. This is the mechanism giving the end user assurance that the delivered artifact's *history* — not just its present bytes — met every declared requirement, without the user re-executing the pipeline.

## 4. Layout and key management

A layout can be revoked by revoking the signing key, or (more commonly) superseded by a newer layout — used e.g. to rotate out a misbehaving functionary's key (any of that functionary's metadata is then automatically no longer trusted once the layout no longer lists their key). Because the layout key is the root of trust, it should be used rarely and, ideally, kept offline.

## 5. Security analysis

**5.1 No key compromise.** Given the design (layout and links are signed, and the threat model assumes project-owner and functionary keys are uncompromised), the paper argues the three relevant goals hold: artifact-flow integrity (an attacker cannot interpose between two steps — the product hash of one link won't match the material hash of the next, and a counterfeit whole product won't match any link), supply-chain layout integrity (missing/reordered steps are detectable because required links are absent or out of order), and step authentication (an attacker lacking a listed key cannot produce accepted link metadata for a step).

**5.2 Under key compromise.** in-toto is explicitly *not* "lose-one-lose-all" — it degrades gracefully depending on which key is compromised and what artifact rules apply. The paper categorizes possible attacks by an attacker holding a compromised functionary key: **fake-check** (forge evidence a step ran when its expected products were never produced, e.g. faking a passing test-suite result); **product modification** (supply a tampered artifact as a step's product, e.g. a backdoored build output); **unintended retention** (fail to destroy artifacts a step was supposed to delete, e.g. leaving exploitable files behind after a "clean" step); **arbitrary supply chain control** (a full project-owner key compromise, which can redefine the whole layout). Table 1 in the paper maps rule combinations (e.g., presence of `DELETE`/`ALLOW`/`MATCH`/`CREATE`/`MODIFY`) to which of these attacks becomes possible, showing that raising a step's threshold (requiring multiple independent signers) and layering more steps/inspections both shrink the attack surface a single compromised key can exploit. A compromise of the *project owner* key is catastrophic (attacker can redefine the layout entirely) — mitigated operationally by higher signing thresholds and keeping the layout key offline.

## 6. Deployment (three case studies)

- **Debian rebuilder constellation** — reproducible-builds infrastructure where independent rebuilder organizations independently rebuild Debian packages and produce in-toto links attesting to the result; a client can cryptographically require that k-of-n rebuilders agree via the threshold mechanism, defending against a single compromised buildfarm or backdoored compiler (a direct operationalization of the Reflections-on-Trusting-Trust threat).
- **Cloud-native builds with Jenkins/Kubernetes (Control Plane / kubesec)** — a Jenkins plugin and a Kubernetes admission controller track container-image builds and gate promotion to production on in-toto verification of the full pipeline (build, test, package) before a container is admitted.
- **Datadog: end-to-end verification of Python packages** — a three-step pipeline (`tag`, `wheels-builder`, `wheels-signer`, plus one inspection) where the tag step is signed with a hardware key (Yubikey) and CI uses online keys; `MATCH` rules and an inspection ensure a wheel's contents are byte-identical to the tagged source, closing the gap left by TUF (The Update Framework) alone — TUF gives compromise-resilient *distribution* (secure the transport/rotation of keys and metadata) while in-toto gives end-to-end *pipeline* verification; the two are complementary and combined in this deployment.

## 7. Evaluation

**Overhead.** Measured against Datadog's public integrations repository (111+ packages): in-toto metadata adds roughly 19% storage overhead relative to total repository size (link metadata dominates over the layout, which is 3-6x smaller than the links); verification adds under 0.6 seconds per package, dominated by signature verification and bounded by the number of links times the threshold.

**Effectiveness against real attacks.** The authors surveyed 30 major supply-chain compromises (2010-2019, e.g., CCleaner, NotPetya, RedHat breach, KingSlayer, Operation Red). 23 of 30 did not involve any key compromise at all — all three in-toto deployment types (Datadog, Cloud Native, reproducible builds) would have caught these via basic step/artifact verification. Of the 7 that did involve a key compromise, the reproducible-builds deployment would have prevented 90%, cloud-native 83%, and the TUF+in-toto (Datadog) combination 100% — because integrating a compromise-resilient key-distribution/update system on top of in-toto's pipeline verification closes the remaining gap (protecting the keys used to verify in-toto metadata itself).

## 8. Related work (brief)

Distinguishes in-toto from: prior automated supply-chain administration research (focused on resource allocation, not security); Google's Grafeas (a centralized store for supply-chain metadata, but without in-toto's verification/signature/step-topology model); reproducible builds and diverse double-compiling (DDC, Wheeler) as point techniques for mitigating Trusting-Trust-style compiler attacks, which in-toto's threshold links can subsume/verify but does not itself define; proof-carrying code and compiler/kernel verification (different target — proving properties of a single artifact/step, not chain-wide provenance); package-manager security work (Cappos et al., TUF) as complementary "last mile" distribution security that in-toto's pipeline-integrity guarantees compose with (as in the Datadog case study).

## 9. Conclusions and future work

The paper argues it has shown that protecting the entirety of the software supply chain — not just individual steps — is possible and can be done automatically via in-toto, and that in a number of practical deployments in-toto is an effective solution against contemporary supply-chain compromises. Open work includes reducing storage cost and further integration with the broader ecosystem (as of writing, in-toto had ~a dozen production integrations).

## Publication details

- **Booktitle:** 28th USENIX Security Symposium (USENIX Security 19)
- **Pages:** 1393-1410
- **ISBN:** 978-1-939133-06-9
- **Publisher:** USENIX Association
- **Landing page:** https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias
- **Presentation video:** https://www.youtube.com/watch?v=gLVmWA7LBjA

## BibTeX

```
@inproceedings {236322,
	author = {Santiago Torres-Arias and Hammad Afzali and Trishank Karthik Kuppusamy and Reza Curtmola and Justin Cappos},
	title = {in-toto: Providing farm-to-table guarantees for bits and bytes},
	booktitle = {28th USENIX Security Symposium (USENIX Security 19)},
	year = {2019},
	isbn = {978-1-939133-06-9},
	address = {Santa Clara, CA},
	pages = {1393--1410},
	url = {https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias},
	publisher = {USENIX Association},
	month = aug
}
```
