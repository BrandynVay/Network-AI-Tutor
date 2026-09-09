# Domain 1 — Networking Concepts (23% of N10-009)

Standing reference chapter. This is meant to actually teach the material —
read it top to bottom the first time, then use it later as a lookup. See
`CLAUDE.md` for how this file is maintained.

## Contents

1. The OSI model & encapsulation
2. TCP/IP model
3. Network appliances & their functions
4. Ports and protocols
5. Network topologies & architectures
6. Cabling and connectors
7. Wireless standards
8. IPv4 addressing fundamentals (+ a worked subnetting example)
9. IPv6 basics

---

## 1. The OSI model & encapsulation

The OSI (Open Systems Interconnection) model is a 7-layer conceptual
framework for how data moves across a network. You will be tested on it
directly (name the layer, name what happens at a layer) *and* indirectly
(every troubleshooting question is implicitly "which layer is this
problem at?").

| # | Layer | What it actually does | Example units / things |
|---|---|---|---|
| 7 | Application | The protocol the user-facing app speaks | HTTP, FTP, SMTP, DNS |
| 6 | Presentation | Formats, encrypts/decrypts, compresses data | TLS, JPEG, ASCII/Unicode |
| 5 | Session | Opens, manages, and closes a conversation between two hosts | SMB session, RPC |
| 4 | Transport | End-to-end delivery, ports, reliability | TCP, UDP — segments/datagrams |
| 3 | Network | Logical addressing and routing between networks | IP, ICMP — packets |
| 2 | Data Link | Framing and addressing on the *local* link (same network) | MAC addresses, switches — frames |
| 1 | Physical | The actual bits on the wire/air | Cabling, radio, hubs — bits |

**Mnemonic** (top to bottom, 7→1): "**A**ll **P**eople **S**eem **T**o
**N**eed **D**ata **P**rocessing." Bottom to top (1→7): "**P**lease **D**o
**N**ot **T**hrow **S**ausage **P**izza **A**way."

**Why layer 3 vs layer 2 keeps showing up on the exam:** Layer 2 only
knows about devices on the *same* local network segment (it uses MAC
addresses, which don't route). Layer 3 is what lets traffic leave your
network and reach a different one (it uses IP addresses, which do route).
A switch operates at Layer 2; a router operates at Layer 3. This single
fact answers a surprising number of "why can't these two devices talk"
questions.

**Encapsulation** is the process of wrapping data in headers as it goes
*down* the stack to be sent, and **decapsulation** is unwrapping it as it
goes *up* the stack on the receiving end. Concretely, sending an HTTP
request:

1. App layer: your browser generates an HTTP request (the raw data).
2. Transport: TCP wraps it in a **segment** — adds source/destination
   *ports* (e.g., destination port 443) and sequencing info.
3. Network: IP wraps that in a **packet** — adds source/destination *IP
   addresses*.
4. Data Link: Ethernet wraps that in a **frame** — adds source/
   destination *MAC addresses*.
5. Physical: the frame becomes **bits** — electrical signal, light pulse,
   or radio wave.

The receiving host reverses this exactly, one header removed per layer,
until the browser on the other end gets the original HTTP request.
**Know the PDU (protocol data unit) name at each layer** — segment
(transport), packet (network), frame (data link), bits (physical). This
gets asked directly.

## 2. TCP/IP model

The practical, 4-layer model the real internet actually runs on. The exam
expects you to map it onto OSI:

| TCP/IP layer | Maps to OSI layers |
|---|---|
| Application | 7, 6, 5 (Application, Presentation, Session) |
| Transport | 4 (Transport) |
| Internet | 3 (Network) |
| Network Access (Link) | 2, 1 (Data Link, Physical) |

Same reality, coarser buckets. When a question says "TCP/IP model," don't
panic — translate it back to OSI in your head if that's what you know
better.

## 3. Network appliances & their functions

| Device | Layer | Function |
|---|---|---|
| Hub | 1 | Repeats bits to every port — no addressing awareness, one shared collision domain. Legacy; know it exists, don't expect to use one. |
| Switch | 2 | Forwards frames based on MAC address table; each port is its own collision domain. The default choice for wiring a LAN. |
| Router | 3 | Forwards packets between different networks based on IP; makes routing decisions using a routing table. |
| Firewall | mainly 3/4 (some are "next-gen" and inspect up to 7) | Permits/denies traffic based on rules (IP, port, sometimes application). |
| Load balancer | 4/7 | Distributes client requests across multiple backend servers. |
| Access point (AP) | 1/2 | Bridges wireless clients onto the wired network. |
| Wireless LAN controller (WLC) | — | Centrally manages many APs (channels, power, roaming, SSIDs). |
| Proxy server | 7 | Sits between clients and the internet; forward proxy = client-side (filtering/caching outbound), reverse proxy = server-side (protects/distributes inbound). |
| IDS | — | **Detects** suspicious traffic and alerts — passive, doesn't block. |
| IPS | — | **Detects and blocks** suspicious traffic inline — active. |

Common exam trap: **IDS vs IPS** — remember "**P**revention" implies it
can act (block); "**D**etection" implies it only watches and alerts.

## 4. Ports and protocols

TCP is connection-oriented (three-way handshake: SYN, SYN-ACK, ACK —
guarantees delivery, retransmits lost data, more overhead). UDP is
connectionless (fire-and-forget — faster, lower overhead, no delivery
guarantee). Rule of thumb: if losing a packet would be *annoying but
survivable* (a dropped video frame), it's UDP; if losing a packet would
*break correctness* (half a file transferred), it's TCP.

Memorize this table — it is tested constantly, often as "which port would
you allow through the firewall for X":

| Port | Protocol | Transport | What it's for |
|---|---|---|---|
| 20/21 | FTP | TCP | File transfer (20 = data, 21 = control) |
| 22 | SSH | TCP | Encrypted remote shell / secure file copy (SCP/SFTP ride on this) |
| 23 | Telnet | TCP | Unencrypted remote shell — legacy, avoid in practice |
| 25 | SMTP | TCP | Sending email (server to server / client to server) |
| 53 | DNS | TCP/UDP | Name resolution (UDP for lookups, TCP for zone transfers / large responses) |
| 67/68 | DHCP | UDP | Automatic IP address assignment (67 = server, 68 = client) |
| 69 | TFTP | UDP | Trivial file transfer — no auth, used for device configs/firmware |
| 80 | HTTP | TCP | Unencrypted web traffic |
| 110 | POP3 | TCP | Retrieve email (downloads and typically removes from server) |
| 123 | NTP | UDP | Time synchronization |
| 143 | IMAP | TCP | Retrieve email (keeps mail synced on the server) |
| 161/162 | SNMP | UDP | Network device monitoring (162 = traps, unsolicited alerts) |
| 389 | LDAP | TCP | Directory services lookups (e.g., Active Directory) |
| 443 | HTTPS | TCP | Encrypted web traffic (HTTP over TLS) |
| 445 | SMB | TCP | Windows file/printer sharing |
| 3389 | RDP | TCP | Windows Remote Desktop |

**Memory hooks:** SSH "grew up" from Telnet and simply took the next
number's neighbor spot in your memory — 22 vs 23. HTTP → HTTPS is 80 →
443 (not 80 → 8080, that's a common alt-port, not the standard). DNS uses
*both* transports: UDP 53 for the fast, small everyday lookups; TCP 53
only when a response is too big for one UDP packet, or for zone
transfers.

## 5. Network topologies & architectures

- **Star** — every device connects to a central switch. Standard for
  modern LANs. Failure of one link only drops one device; failure of the
  central switch drops everyone.
- **Mesh** — every device connects to every other device (full mesh) or
  many others (partial mesh). High redundancy, expensive to cable/scale.
  Common conceptually for WAN links between sites, or wireless mesh Wi-Fi
  systems.
- **Hybrid** — a mix, e.g., star topologies at each site joined by a mesh
  of WAN links between sites.
- **Three-tier architecture** (core / distribution / access) — the
  traditional enterprise design: access switches (where devices plug in)
  → distribution switches (aggregate access, apply policy) → core switches
  (high-speed backbone). Built for north-south (client-to-server) traffic.
- **Spine-leaf** — every leaf switch connects to every spine switch, no
  leaf-to-leaf or spine-to-spine links. Built for data centers, where
  east-west (server-to-server) traffic dominates. Consistent latency
  between any two leaves (always exactly 2 hops: leaf→spine→leaf).
- **SDN (Software-Defined Networking)** — separates the *control plane*
  (decides where traffic should go) from the *data plane* (actually
  forwards it), managed centrally instead of configuring each device by
  hand.
- **SD-WAN** — applies that same idea to WAN links across sites: a
  central controller picks the best path (MPLS, broadband, LTE) per
  application, dynamically.

## 6. Cabling and connectors

**Copper (twisted pair):**

| Category | Max speed | Max distance (100 Ω, typical) | Notes |
|---|---|---|---|
| Cat5e | 1 Gbps | 100 m | Still common, minimum for gigabit |
| Cat6 | 1 Gbps (10 Gbps up to 55 m) | 100 m / ~55 m at 10G | Tighter twist, less crosstalk |
| Cat6a | 10 Gbps | 100 m | Full 10G at full 100m distance |
| Cat7 / Cat8 | 10–40 Gbps | shorter, data-center focused | Less common on the exam beyond "know it exists and is faster/shielded" |

**Fiber:**

- **Single-mode fiber (SMF)** — thin core, laser light travels a single
  straight path. Long distance (kilometers), higher cost. Yellow jacket
  by convention.
- **Multimode fiber (MMF)** — larger core, light bounces at multiple
  angles. Shorter distance (hundreds of meters), cheaper transceivers.
  Orange or aqua jacket by convention.
- Common connectors: **LC** (small, common on modern SFPs), **SC**
  (push-pull, older), **ST** (twist-lock, older). **SFP/SFP+** are the
  hot-swappable transceiver modules that plug into a switch port to give
  it a fiber (or copper) interface.

**Copper connector:** **RJ45** for Ethernet (8 pins). Don't confuse with
RJ11 (4/6 pins — telephone).

**The 150 m outdoor cable question from your diagnostic** is really
asking: copper Ethernet is capped at 100 m — beyond that, signal
degrades past reliable use without a repeater. Fiber (especially
single-mode) easily covers 150 m and is also immune to the electrical
interference that outdoor/inter-building runs are exposed to (lightning,
EMI from power lines). That's the reasoning to reproduce on the exam, not
just the answer "fiber."

## 7. Wireless standards

| Standard | Marketing name | Frequency | Rough max speed |
|---|---|---|---|
| 802.11a | — | 5 GHz | 54 Mbps |
| 802.11b | — | 2.4 GHz | 11 Mbps |
| 802.11g | — | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 & 5 GHz | 600 Mbps |
| 802.11ac | Wi-Fi 5 | 5 GHz | ~3.5 Gbps |
| 802.11ax | Wi-Fi 6 / 6E | 2.4, 5, (6E: 6 GHz) | ~9.6 Gbps |

**2.4 GHz** — longer range, better wall penetration, only 3 non-overlapping
channels (1, 6, 11) in most regions, more prone to interference
(microwaves, Bluetooth, cordless phones). **5 GHz** — shorter range, more
non-overlapping channels, less interference, faster. **6 GHz** (Wi-Fi 6E)
— even more clean spectrum, shortest range. Security for wireless
(WPA2/WPA3) lives in Domain 4 — Network Security; this chapter is just the
radio-layer facts.

## 8. IPv4 addressing fundamentals

An IPv4 address is 32 bits, written as 4 decimal octets (0–255) separated
by dots — e.g., `192.168.10.50`. A **subnet mask** marks which bits are
*network* bits (shared by every host on that subnet) vs *host* bits
(unique to each device). **CIDR notation** (`/26`) is shorthand for "the
first 26 bits are the network portion."

| Class | Range (first octet) | Default mask | Default CIDR |
|---|---|---|---|
| A | 1–126 | 255.0.0.0 | /8 |
| B | 128–191 | 255.255.0.0 | /16 |
| C | 192–223 | 255.255.255.0 | /24 |

(127 is reserved for loopback — `127.0.0.1` is always "this machine.")
Class-based addressing is legacy thinking — real networks use CIDR to
subnet however finely they need — but the exam still expects you to know
the class ranges and default masks cold.

**Private (non-routable) ranges** (RFC 1918) — you'll see these constantly
since they're what's behind NAT on every home and office network:

- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

**Worked subnetting example** — this is the skill, more than any single
fact, that separates a pass from a fail. Walk through it slowly:

> Given `192.168.10.50/26`, find the network address and broadcast
> address.

1. `/26` means 26 network bits, so 32 − 26 = **6 host bits** remain.
2. 6 host bits → 2⁶ = 64 total addresses per subnet (block size 64).
3. The last octet is what varies (since /26 falls inside the 4th octet).
   Subnets in the last octet step in multiples of the block size: `0, 64,
   128, 192`.
4. `50` falls between `0` and `64` → this address belongs to the subnet
   starting at **`192.168.10.0`** — that's the **network address**.
5. The next subnet starts at `192.168.10.64`, so the last usable address
   in *this* subnet is one below that: `192.168.10.63` — that's the
   **broadcast address**.
6. Usable host range: `192.168.10.1` – `192.168.10.62` (network and
   broadcast addresses are never assignable to a host) — **62 usable
   hosts** (64 total − 2).

**General method, reusable for any mask:** host bits = 32 − CIDR → block
size = 2^(host bits) → subnet boundaries are multiples of the block size
in whichever octet the mask cuts through → broadcast = next boundary − 1
→ usable hosts = block size − 2.

Practice this until it's automatic — you will not have a calculator
metaphor to lean on for word problems like "split this /24 into 6 equal
subnets," you need the boundaries to just appear in your head. (We'll
drill more of these directly in daily sessions once the schedule starts.)

## 9. IPv6 basics

128 bits, written as 8 groups of 4 hex digits separated by colons, e.g.:
`2001:0db8:0000:0000:0000:ff00:0042:8329`.

**Shorthand rules** (both apply, and the exam loves testing that you know
the second one is a *one-time* substitution):

1. Leading zeros in each group can be dropped: `0db8` → `db8`, `0000` →
   `0`.
2. **One** run of consecutive all-zero groups can be collapsed to `::` —
   but only once per address (otherwise the address would be ambiguous
   about how many zero groups were removed).

Applying both: `2001:0db8:0000:0000:0000:ff00:0042:8329` →
`2001:db8::ff00:42:8329`.

**Address types:**

- **Unicast** — one sender, one specific receiver (the normal case).
- **Multicast** — one sender, a group of subscribed receivers. IPv6 has
  no broadcast at all — multicast replaces it.
- **Anycast** — one address assigned to multiple devices; the network
  delivers to the *nearest* one (used by DNS root servers, CDNs).
- **Link-local** — always starts `fe80::/10`. Auto-assigned, only valid on
  the local link, never routed — roughly IPv6's answer to "this address
  only makes sense on this one wire."

---

*Chapter status: complete. Next chapters to write: Networking
Implementation, Networking Operations, Network Security, Network
Troubleshooting.*
