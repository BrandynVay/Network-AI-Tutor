# Network+ (N10-009) — 90-Day Outline

Written 2026-09-10, after the diagnostic quiz (see `STUDENT_PROFILE.md` §
Diagnostic quiz). This is a plan, not a contract — see "Adapting this
outline" at the bottom, and `CLAUDE.md` § Adapting the plan / Falling
behind, which govern how and when this changes.

## How this was built

- **Domain day-count is weighted by the real exam blueprint, not by
  self-reported weak areas.** The diagnostic came back 0/20 uniformly
  across all 5 domains — there's no genuine weak/strong signal to weight
  toward yet, so day allocation instead mirrors what the actual exam
  rewards: Concepts 23%, Implementation 20%, Operations 19%, Security
  14%, Troubleshooting 24% (see `STUDENT_PROFILE.md` § Exam facts). As
  real signal appears (mastery-gate holds, practice exam results), this
  allocation is exactly what gets adjusted — see "Adapting this outline."
- **Domain order follows the standard dependency chain**: Concepts →
  Implementation → Operations → Security → Troubleshooting. This isn't
  arbitrary — Troubleshooting in particular leans on everything taught
  before it (you can't reason about *why* a config is broken without
  knowing what "working" looks like), so it's deliberately last and
  gets extra scenario-practice days as a result.
- **Fixed special days**: practice exams at day 30 (⅓), day 60 (⅔), and
  day 80 (~90%); taper (no new material) days 84–90. Everything else is
  a content day. 80 content days ÷ blueprint weighting → 18 / 16 / 15 /
  11 / 20 days for Concepts / Implementation / Operations / Security /
  Troubleshooting respectively.
- **Every day also carries a review component** — this isn't written out
  per-day below (that would be 90 near-identical lines); it's a standing
  formula, stated once:

  > **Review formula**: on any day N (beyond roughly day 14), lightly
  > revisit N-1, N-3, N-7, N-14, and N-30's material (whichever exist) —
  > a handful of flashcards or quiz questions, not a full re-teach. On
  > every 10th day (10, 20, 30, 40...), replace that fixed-offset review
  > with a rotating cross-domain pass instead: touch *every* domain
  > covered so far, a little each, so nothing goes more than ~10 days
  > without some contact once it's more than 30 days old. See `CLAUDE.md`
  > § Spaced repetition for why both parts exist.

- **🔧 marks a day with a hands-on lab step** on the student's confirmed
  gear (managed switch(es), a router/firewall appliance, wireless AP(s)
  — see `STUDENT_PROFILE.md` § Interview). Where marked, that day's
  session should include an actual on-gear config step, not just a
  diagram — see `CLAUDE.md` § Hands-on lab practice.
- **Diagnostic call-outs** — a few days are flagged where they directly
  address a specific gap from the diagnostic (e.g. "direct fix for Q17")
  so the connection back to round-1 results stays visible.

## Domain 1 — Networking Concepts (Days 1–18)

| Day | Topic | Notes |
|---|---|---|
| 1 | OSI model & encapsulation | Day 1 — teach the 7 layers, encapsulation/decapsulation, PDU names |
| 2 | TCP/IP model | Map onto OSI from Day 1 |
| 3 | Network appliances & their functions | Hub/switch/router/firewall/LB/AP/WLC/proxy/IDS/IPS |
| 4 | Ports & protocols, part 1 | TCP vs UDP, well-known ports (FTP–NTP) |
| 5 | Ports & protocols, part 2 | Remaining ports, heavy drilling — this table is the single most-tested list in the domain |
| 6 | Network topologies & architectures | Star/mesh/hybrid, three-tier, spine-leaf, SDN/SD-WAN |
| 7 | Cabling — copper | Cat5e/6/6a/7/8, 100m limit |
| 8 🔧 | Cabling — fiber & connectors | SMF/MMF, RJ45/LC/SC/ST, SFP — direct fix for diagnostic Q3 |
| 9 | Wireless standards | 802.11 a/b/g/n/ac/ax, 2.4/5/6GHz tradeoffs |
| 10 | IPv4 fundamentals | Classes, default masks, RFC 1918 private ranges |
| 11 | Subnetting, part 1 | The method — host bits, block size, boundaries |
| 12 | Subnetting, part 2 | Practice problems — direct fix for diagnostic Q6 |
| 13 | Subnetting, part 3 | Harder problems, intro to splitting into N subnets — direct fix for diagnostic Q8-style question |
| 14 | IPv6 basics, part 1 | Format, shorthand rules |
| 15 | IPv6 basics, part 2 | Address types — unicast/multicast/anycast/link-local |
| 16 🔧 | Concepts integration | Scenario questions tying OSI + ports + topologies + addressing together; basic connectivity lab |
| 17 | Concepts review | Remediation buffer — actual content depends on how days 1-16 went |
| 18 | **Concepts mastery check** | Informal mini-quiz — mastery gate must clear before Day 19 (see `CLAUDE.md` § Mastery gate) |

## Domain 2 — Networking Implementation (Days 19–29, 31–35)

| Day | Topic | Notes |
|---|---|---|
| 19 | Routing fundamentals | Static vs dynamic, routing tables, default route |
| 20 | Routing protocols (conceptual) | RIP, OSPF, BGP — what problem each solves, not deep config |
| 21 🔧 | Switching — VLANs | Why segment; create VLANs on the student's managed switch |
| 22 🔧 | Switching — trunking | 802.1Q tagging — direct fix for diagnostic Q7's missing half; trunk config on gear |
| 23 🔧 | Switching — STP & port security | Loop prevention; port security config |
| 24 🔧 | NAT/PAT in depth | How it actually rewrites packets — direct fix for diagnostic Q5; config if gear supports it |
| 25 | Subnetting → VLSM, part 1 | Builds on Concepts Days 11-13 |
| 26 | Subnetting → VLSM, part 2 | Harder VLSM problems |
| 27 | WAN types, part 1 | MPLS, broadband, cellular |
| 28 | WAN types, part 2 | DIA and connection technologies, continued |
| 29 | Cloud concepts | IaaS/PaaS/SaaS, cloud connectivity models — no real analog on home gear, discuss conceptually |
| *(30)* | *Practice exam 1 — see "Practice exams" below* | |
| 31 | Implementation integration | Routing + switching scenario questions |
| 32 🔧 | Implementation lab day | Combined lab: VLANs + trunk + routing between networks |
| 33 | Implementation review | Remediation buffer |
| 34 | Implementation review | Remediation buffer / deeper VLSM practice |
| 35 | **Implementation mastery check** | Gate must clear before Day 36 |

## Domain 3 — Networking Operations (Days 36–50)

| Day | Topic | Notes |
|---|---|---|
| 36 | Monitoring — SNMP | Versions, traps — direct fix for diagnostic Q9 |
| 37 | Monitoring — syslog & flow data | Log aggregation |
| 38 | Documentation types | Diagrams, wiring docs, IPAM, SOPs |
| 39 | Baselines | Why they matter, how to establish one |
| 40 | Business continuity — RPO/RTO | Direct fix for diagnostic Q10 |
| 41 | Business continuity — site types | Hot/warm/cold — direct fix for diagnostic Q12 |
| 42 | Business continuity — backups | Full/incremental/differential, snapshots |
| 43 | High availability, part 1 | Redundancy, failover |
| 44 | High availability, part 2 | Load balancing, NIC teaming, clustering |
| 45 | Change management | Maintenance windows, rollback plans |
| 46 | Operations integration | Monitoring + DR scenario questions |
| 47 🔧 | Operations lab day | Check what monitoring/logging the student's gear actually supports |
| 48 | Operations review | Remediation buffer |
| 49 | Operations review | Remediation buffer |
| 50 | **Operations mastery check** | Gate must clear before Day 51 |

## Domain 4 — Network Security (Days 51–59, 61–62)

| Day | Topic | Notes |
|---|---|---|
| 51 | Core security concepts | CIA triad, least privilege — direct fix for diagnostic Q13; defense in depth, zero trust |
| 52 | AAA in depth | Direct fix for diagnostic Q14's missing "accounting" piece; RADIUS/TACACS+/802.1X |
| 53 | Common threats, part 1 | On-path/MITM — direct fix for diagnostic Q15; DNS poisoning |
| 54 | Common threats, part 2 | Phishing, DoS/DDoS (contrast with MITM), rogue DHCP/AP, VLAN hopping |
| 55 🔧 | Wireless security | WPA2/WPA3, EAP — configure WPA on the student's AP |
| 56 🔧 | Firewalls in depth | Stateful vs stateless — direct fix for diagnostic Q16; ACLs, NGFW, zones/DMZ; ACL on gear |
| 57 🔧 | Physical/logical controls | Locks, badges, cameras vs. port security/NAC — config on gear |
| 58 | VPNs | Site-to-site vs client, IPsec vs SSL VPN |
| 59 | Security integration | Threat-scenario questions |
| *(60)* | *Practice exam 2 — book the real exam after this one, see "Practice exams"* | |
| 61 | Security review | Remediation buffer |
| 62 | **Security mastery check** | Gate must clear before Day 63 |

## Domain 5 — Network Troubleshooting (Days 63–79, 81–83)

| Day | Topic | Notes |
|---|---|---|
| 63 | Troubleshooting methodology | The ordered CompTIA steps, why order matters — direct fix for diagnostic Q17 |
| 64 | CLI tools — ping & traceroute | Ties into diagnostic Q19's traceroute-reasoning gap |
| 65 | CLI tools — nslookup/dig, ipconfig | Direct fix for diagnostic Q18's DNS gap |
| 66 | CLI tools — netstat, arp | |
| 67 🔧 | Physical layer troubleshooting | Test a real cable/link on gear |
| 68 🔧 | Link lights & port status | Direct fix for diagnostic Q20; observe real port LEDs |
| 69 | Common wired issues, part 1 | Switching loops, duplicate IPs, DHCP exhaustion |
| 70 🔧 | Common wired issues, part 2 | Wrong VLAN, cabling issues — reproduce on gear |
| 71 | Common wireless issues | Channel overlap/interference, weak signal, AP placement |
| 72 | Scenario practice — Concepts-flavored | OSI-layer identification drills |
| 73 | Scenario practice — Implementation-flavored | Routing/switching problems |
| 74 | Scenario practice — Operations-flavored | Monitoring/DR-flavored scenarios |
| 75 | Scenario practice — Security-flavored | Threat identification |
| 76 | Mixed-domain scenario drills, part 1 | |
| 77 | Mixed-domain scenario drills, part 2 | |
| 78 | Troubleshooting integration | |
| 79 | Troubleshooting review | Remediation buffer |
| *(80)* | *Practice exam 3 — see "Practice exams"* | |
| 81 | Troubleshooting review | Post-exam-3 remediation buffer |
| 82 | Cumulative review, part 1 | All 5 domains, weighted by practice-exam-3 weak spots |
| 83 | **Troubleshooting mastery check** | Cumulative review, part 2 — final gate before the taper |

## Final review / taper (Days 84–90)

No new material, by rule — see `CLAUDE.md` § Final review (taper).

| Day | Focus |
|---|---|
| 84 | Full review — Concepts + Implementation |
| 85 | Full review — Operations + Security |
| 86 | Full review — Troubleshooting + weakest domain from practice exam 3 |
| 87 | **Practice exam 4** — final full-length exam, a few days out, not exam-eve |
| 88 | Targeted light review of whatever exam 4 showed was still shaky |
| 89 | Light confidence-building review + test-day logistics (PBQ flag-and-skip, process of elimination, revisiting flagged questions) |
| 90 | Rest. Very light review only — no new drilling. |

## Practice exams

Full-length, 90 questions / 90 minutes, blueprint-weighted domain mix —
see `CLAUDE.md` § Practice exams for format rules.

- **Day 30** — baseline benchmark. Only Concepts and part of Implementation
  have been taught yet; expect a rough score on Operations/Security/
  Troubleshooting questions. The point here is format/pacing familiarity
  and an early data point, not a mastery check.
- **Day 60** — after this one, prompt the student to book the real exam
  (see `CLAUDE.md` § Exam logistics) and do the version-currency check.
- **Day 80** — after Troubleshooting is fully covered; this score is the
  first genuinely meaningful readiness signal.
- **Day 87** — final exam, during the taper. Log all four in
  `STUDENT_PROFILE.md` § Practice exam results as they happen.

## Adapting this outline

This is Day 1's starting plan, not a fixed schedule. Concretely:

- A failed mastery gate (see `CLAUDE.md` § Mastery gate) inserts a
  remediation day and pushes everything after it back by one — don't
  renumber, just note the deviation in `STUDENT_PROFILE.md`.
- Once practice exam results start actually differentiating domains
  (unlike the diagnostic), it's fair to pull days from a domain that's
  clearly solid into one that's clearly still weak — log the reasoning.
- If real-world pace falls behind a booked exam date, see `CLAUDE.md` §
  Falling behind for the compression-first policy.
