---
video_id: "Q6MH3URLHfM"
title: "Your Legacy VPN is Slowing Down Your Business—Here’s How to Fix It with Tailscale"
description: "In this video, we explore why traditional VPNs are creating bottlenecks for businesses and how Tailscale offers a superior solution. Join Alex as he breaks down the common pain points with legacy VPNs..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-03-05"
duration_seconds: 666
youtube_url: "https://www.youtube.com/watch?v=Q6MH3URLHfM"
thumbnail_url: "https://i.ytimg.com/vi_webp/Q6MH3URLHfM/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:49:42.300672"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1705
transcription_time_seconds: 16.4
---

# Your Legacy VPN is Slowing Down Your Business—Here’s How to Fix It with Tailscale

**[00:00](https://youtube.com/watch?v=Q6MH3URLHfM&t=0s)** Now, I don't mean to alarm you, but your legacy VPN is holding you and your company back. Slow

**[00:06](https://youtube.com/watch?v=Q6MH3URLHfM&t=6s)** connections, security concerns, performance issues, rooting all of your VPN traffic through

**[00:11](https://youtube.com/watch?v=Q6MH3URLHfM&t=11s)** centralized, expensive, dedicated, black box appliances, complicated on and offboarding procedures.

**[00:19](https://youtube.com/watch?v=Q6MH3URLHfM&t=19s)** These are just some of the many issues we've heard from our customers that they run into

**[00:23](https://youtube.com/watch?v=Q6MH3URLHfM&t=23s)** with legacy VPN solutions. In today's video, we're going to discuss why Tailscale might

**[00:28](https://youtube.com/watch?v=Q6MH3URLHfM&t=28s)** be the solution you've been looking for. As a mesh VPN product, Tailscale provides a

**[00:33](https://youtube.com/watch?v=Q6MH3URLHfM&t=33s)** fundamentally different approach to secure networking. Instead of tunneling all of your traffic

**[00:38](https://youtube.com/watch?v=Q6MH3URLHfM&t=38s)** through those centralized servers, Tailscale creates a secure mesh network where devices

**[00:44](https://youtube.com/watch?v=Q6MH3URLHfM&t=44s)** connect securely to each other using WireGuard encryption under the hood. It operates at

**[00:49](https://youtube.com/watch?v=Q6MH3URLHfM&t=49s)** layer three of the networking stack, bringing identity down to the networking layer itself,

**[00:54](https://youtube.com/watch?v=Q6MH3URLHfM&t=54s)** which means that you get enhanced security without sacrificing any performance at all. Tailscale

**[01:01](https://youtube.com/watch?v=Q6MH3URLHfM&t=61s)** also combines the security benefits of a VPN with the convenience of modern zero trust solutions,

**[01:07](https://youtube.com/watch?v=Q6MH3URLHfM&t=67s)** all without the traditional headaches of legacy VPNs. Now, we speak to a lot of customers

**[01:14](https://youtube.com/watch?v=Q6MH3URLHfM&t=74s)** about VPNs, and they're often very honest with us about the pain points that they have with

**[01:20](https://youtube.com/watch?v=Q6MH3URLHfM&t=80s)** traditional VPNs. Probably the biggest one that we hear though is performance. We're talking

**[01:25](https://youtube.com/watch?v=Q6MH3URLHfM&t=85s)** up to 10 times slower speeds with frustrating connection drops, especially when switching between

**[01:31](https://youtube.com/watch?v=Q6MH3URLHfM&t=91s)** networks, between your phone and Wi-Fi or on the train or something like that. Second,

**[01:37](https://youtube.com/watch?v=Q6MH3URLHfM&t=97s)** the overall management posture of these legacy solutions is a headache. Onboarding and offboarding

**[01:42](https://youtube.com/watch?v=Q6MH3URLHfM&t=102s)** users is often a time-consuming and complex process, especially a given that they only have limited

**[01:48](https://youtube.com/watch?v=Q6MH3URLHfM&t=108s)** integrations with the more modern identity providers such as Octa and some of the other OIDC

**[01:54](https://youtube.com/watch?v=Q6MH3URLHfM&t=114s)** people that Tailscale support. And if you're managing certificates and keys, you know just how

**[01:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=119s)** cumbersome that process can be. I recall a previous job. We had an Ansible Playbook that managed

**[02:05](https://youtube.com/watch?v=Q6MH3URLHfM&t=125s)** who was allowed access via open VPN to AWS or not. And it was not uncommon to see people in that

**[02:13](https://youtube.com/watch?v=Q6MH3URLHfM&t=133s)** playbook who hadn't even worked for the company for six months. So I sat down with Chris Chang,

**[02:18](https://youtube.com/watch?v=Q6MH3URLHfM&t=138s)** who's our director of new business sales here at Tailscale and asked him what some of the most

**[02:23](https://youtube.com/watch?v=Q6MH3URLHfM&t=143s)** common pain points were about why people switched to Tailscale.

**[02:26](https://youtube.com/watch?v=Q6MH3URLHfM&t=146s)** When enough employees are frustrated and they can't be productive and do their work,

**[02:33](https://youtube.com/watch?v=Q6MH3URLHfM&t=153s)** that's the number one catalyst for folks looking for a new solution. And the reason why they have

**[02:40](https://youtube.com/watch?v=Q6MH3URLHfM&t=160s)** difficulties in these poor end user experiences is because a lot of the legacy VPNs are connecting

**[02:46](https://youtube.com/watch?v=Q6MH3URLHfM&t=166s)** to a central hub and that adds more latency and decreases, you know, throughput and performance

**[02:53](https://youtube.com/watch?v=Q6MH3URLHfM&t=173s)** for end users. And as if all of that wasn't enough, finally, there's the security factor.

**[02:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=179s)** Centralized servers create single points of failure and many legacy solutions have limited

**[03:04](https://youtube.com/watch?v=Q6MH3URLHfM&t=184s)** mobile and Linux support if they even have either of those things supported at all. And this

**[03:10](https://youtube.com/watch?v=Q6MH3URLHfM&t=190s)** weakens your overall security posture. This is what happens with legacy VPNs when you start adding layers

**[03:16](https://youtube.com/watch?v=Q6MH3URLHfM&t=196s)** of fixes to address various problems on top of layers of fixes to address various problems.

**[03:22](https://youtube.com/watch?v=Q6MH3URLHfM&t=202s)** Before you know it, you've created a complicated mess of VPN hubs and gateways and authentication

**[03:28](https://youtube.com/watch?v=Q6MH3URLHfM&t=208s)** layers and misconfigured firewalls. So how do you know it's time to switch to Tailscale?

**[03:33](https://youtube.com/watch?v=Q6MH3URLHfM&t=213s)** Well, your users will probably tell you if you're constantly hearing complaints about VPN issues

**[03:39](https://youtube.com/watch?v=Q6MH3URLHfM&t=219s)** or performance of things not connecting first thing in the morning when everybody logs on all at once,

**[03:45](https://youtube.com/watch?v=Q6MH3URLHfM&t=225s)** that's often a big red flag. If you've experienced these things, you count as a user too. So you

**[03:50](https://youtube.com/watch?v=Q6MH3URLHfM&t=230s)** probably know. Now the other thing to consider are things like compliance postures. We support

**[03:57](https://youtube.com/watch?v=Q6MH3URLHfM&t=237s)** things like SOC 2 ISO 27001, HIPPER and PCI DSS. Your legacy VPN might support these things for now,

**[04:06](https://youtube.com/watch?v=Q6MH3URLHfM&t=246s)** but these specs are always changing. So it's worth keeping an eye on a modern solution like

**[04:11](https://youtube.com/watch?v=Q6MH3URLHfM&t=251s)** Tailscale that's going to allow you to scale your business with acquisitions and expand into

**[04:16](https://youtube.com/watch?v=Q6MH3URLHfM&t=256s)** new geographies and keep up with the regulatory compliance issues that can come with all of those

**[04:22](https://youtube.com/watch?v=Q6MH3URLHfM&t=262s)** minefields. Your old VPN probably wasn't designed for that kind of growth. And speaking of growth,

**[04:28](https://youtube.com/watch?v=Q6MH3URLHfM&t=268s)** I sat down with Rob Clark, an engineer over at CloudBees, the guys behind Jenkins,

**[04:33](https://youtube.com/watch?v=Q6MH3URLHfM&t=273s)** and asked him about why CloudBees made the switch to Tailscale.

**[04:37](https://youtube.com/watch?v=Q6MH3URLHfM&t=277s)** That was largely around the performance. We tried, so we have about 20 different GitHub

**[04:44](https://youtube.com/watch?v=Q6MH3URLHfM&t=284s)** organizations, and we managed successfully with OpenVPN to move one team in their organization.

**[04:53](https://youtube.com/watch?v=Q6MH3URLHfM&t=293s)** They had to GitHub IP restrictions, and they had to use the VPN to use GitHub. We added a second

**[04:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=299s)** team. At that point, the VPN server started to struggle, and obviously we could put work into

**[05:07](https://youtube.com/watch?v=Q6MH3URLHfM&t=307s)** scaling up and productionising it and doing all those things. So I wouldn't say it was a hard

**[05:13](https://youtube.com/watch?v=Q6MH3URLHfM&t=313s)** blocker, but it was basically a choice between using something else or doing that productionisation

**[05:20](https://youtube.com/watch?v=Q6MH3URLHfM&t=320s)** work and making the OpenVPN server more of a first-class citizen within the systems that we

**[05:29](https://youtube.com/watch?v=Q6MH3URLHfM&t=329s)** operate. Another common trigger that we see is folks migrating to the cloud or adding new features

**[05:34](https://youtube.com/watch?v=Q6MH3URLHfM&t=334s)** to products that just simply aren't compatible with these legacy solutions. They expose weaknesses

**[05:41](https://youtube.com/watch?v=Q6MH3URLHfM&t=341s)** in your current setup, both including technical and human. So this is where Tailscale enters the

**[05:47](https://youtube.com/watch?v=Q6MH3URLHfM&t=347s)** picture. Tailscale creates a modern network at Layer 3, bringing identity and wireguard encryption

**[05:54](https://youtube.com/watch?v=Q6MH3URLHfM&t=354s)** all the way down to the networking layer. Unlike traditional VPNs or even some competing zero

**[05:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=359s)** trust tools that handle identity at layers 5, 6 or 7, Tailscale handles it at the network layer

**[06:06](https://youtube.com/watch?v=Q6MH3URLHfM&t=366s)** itself, and this is a fundamental difference as to why Tailscale is a future-proof next-generation

**[06:12](https://youtube.com/watch?v=Q6MH3URLHfM&t=372s)** VPN replacement solution. There are several major benefits from switching to Tailscale. The first

**[06:17](https://youtube.com/watch?v=Q6MH3URLHfM&t=377s)** is hassle-free setup. We provide a fast seamless experience for end users that boosts productivity

**[06:24](https://youtube.com/watch?v=Q6MH3URLHfM&t=384s)** and minimises shadow IT. Now if you'd like to see a video on just how quick you can get started

**[06:29](https://youtube.com/watch?v=Q6MH3URLHfM&t=389s)** with Tailscale, we have a 10-minute getting started guide just up here for you. Our high-performance

**[06:34](https://youtube.com/watch?v=Q6MH3URLHfM&t=394s)** client is built on top of the secure wireguard protocol underneath, which significantly reduces

**[06:40](https://youtube.com/watch?v=Q6MH3URLHfM&t=400s)** the implementation burden on our side. This means we can keep up to date more easily with security

**[06:46](https://youtube.com/watch?v=Q6MH3URLHfM&t=406s)** and regulatory requirements. Second is Tailscale's robust security posture. End-to-end encryption

**[06:52](https://youtube.com/watch?v=Q6MH3URLHfM&t=412s)** is the default for every single connection. No infrastructure is exposed to the public internet.

**[06:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=419s)** So just think about this for a second. You have a cell phone in your hand on the train,

**[07:04](https://youtube.com/watch?v=Q6MH3URLHfM&t=424s)** and you want to connect to a random piece of infrastructure in AWS behind several layers

**[07:09](https://youtube.com/watch?v=Q6MH3URLHfM&t=429s)** of VPS gateways and all that kind of security structure that's kind of between you and the thing

**[07:15](https://youtube.com/watch?v=Q6MH3URLHfM&t=435s)** you want to get to. You have a secure direct end-to-end encrypted connection between your phone

**[07:22](https://youtube.com/watch?v=Q6MH3URLHfM&t=442s)** and that piece of infrastructure. And that mesh network establishes itself between all of the

**[07:27](https://youtube.com/watch?v=Q6MH3URLHfM&t=447s)** different places that Tailscale can run. We have over a hundred integrations spanning all the

**[07:33](https://youtube.com/watch?v=Q6MH3URLHfM&t=453s)** major hyperscaler cloud providers all the way down to things like running Tailscale on a coffee

**[07:38](https://youtube.com/watch?v=Q6MH3URLHfM&t=458s)** machine. Yes, it is possible technically at least. The third reason you should consider switching

**[07:43](https://youtube.com/watch?v=Q6MH3URLHfM&t=463s)** to Tailscale is our superior performance. It's easy to connect to anything regardless of location

**[07:48](https://youtube.com/watch?v=Q6MH3URLHfM&t=468s)** using Tailscale. And we streamline distributed workflows with software-based infrastructure

**[07:54](https://youtube.com/watch?v=Q6MH3URLHfM&t=474s)** agnostic solutions that work seamlessly across offices, clouds, data centers, and all the major

**[08:01](https://youtube.com/watch?v=Q6MH3URLHfM&t=481s)** platforms. So let's talk for a moment about what secure access looks like with Tailscale.

**[08:06](https://youtube.com/watch?v=Q6MH3URLHfM&t=486s)** You can reduce infrastructure complexity by skipping things like bastion hosts and jump servers,

**[08:13](https://youtube.com/watch?v=Q6MH3URLHfM&t=493s)** by making secure direct connections to individual machines, as I mentioned earlier.

**[08:17](https://youtube.com/watch?v=Q6MH3URLHfM&t=497s)** You can automate access control and compliance by integrating with existing SSO providers,

**[08:22](https://youtube.com/watch?v=Q6MH3URLHfM&t=502s)** IDPs, IAC tools, and other GitHub-style workflows. You can also minimize your network's

**[08:29](https://youtube.com/watch?v=Q6MH3URLHfM&t=509s)** attack services by keeping as many firewall ports closed as possible thanks to Tailscale's natural

**[08:34](https://youtube.com/watch?v=Q6MH3URLHfM&t=514s)** traversal technology. And that unlocks a lot of quality of life and ease of use benefits.

**[08:43](https://youtube.com/watch?v=Q6MH3URLHfM&t=523s)** I think the main thing that I'm realizing with Tailscale is the time to value is unparalleled.

**[08:52](https://youtube.com/watch?v=Q6MH3URLHfM&t=532s)** You can install Tailscale on your laptop and then in whatever network you're trying to access

**[08:59](https://youtube.com/watch?v=Q6MH3URLHfM&t=539s)** and get connectivity extremely quickly. That's actually the key thing that our founders

**[09:04](https://youtube.com/watch?v=Q6MH3URLHfM&t=544s)** are focused on, which is being the easiest way to connect two devices in the world seamlessly.

**[09:09](https://youtube.com/watch?v=Q6MH3URLHfM&t=549s)** And we see real results with companies that are adopting Tailscale. Instacart senior staff

**[09:15](https://youtube.com/watch?v=Q6MH3URLHfM&t=555s)** software engineer Mike Deak said, because of Tailscale simplicity both in architecture and end-user

**[09:21](https://youtube.com/watch?v=Q6MH3URLHfM&t=561s)** experience, we can solve our acute problems quickly and easily. So Tailscale isn't just a VPN

**[09:28](https://youtube.com/watch?v=Q6MH3URLHfM&t=568s)** replacement, it's a path to ZTNA or zero trust network access. So here's how Tailscale compares

**[09:34](https://youtube.com/watch?v=Q6MH3URLHfM&t=574s)** with legacy solutions. For management, whilst legacy solutions require large, costly and

**[09:39](https://youtube.com/watch?v=Q6MH3URLHfM&t=579s)** complex enterprise-scale deployments, Tailscale is easy to get started with, even with a single

**[09:45](https://youtube.com/watch?v=Q6MH3URLHfM&t=585s)** person administering the platform. You can start small and scale out. For infrastructure,

**[09:51](https://youtube.com/watch?v=Q6MH3URLHfM&t=591s)** there's no vendor lock-in or seeding control. You manage your own edge network without

**[09:56](https://youtube.com/watch?v=Q6MH3URLHfM&t=596s)** needing to trust Tailscale or anyone else. For privacy, no more man-in-the-middle proxies

**[10:01](https://youtube.com/watch?v=Q6MH3URLHfM&t=601s)** breaking encryption. Tailscale provides end-to-end encryption built atop of Wireguard.

**[10:07](https://youtube.com/watch?v=Q6MH3URLHfM&t=607s)** And for deployment, you're not limited by gateways or edge-based deployment models,

**[10:12](https://youtube.com/watch?v=Q6MH3URLHfM&t=612s)** Tailscale is mesh-capable with an iterative deployment model giving you ZTNA everywhere.

**[10:18](https://youtube.com/watch?v=Q6MH3URLHfM&t=618s)** So there you have it. If your legacy VPN is causing you more problems than it solves,

**[10:22](https://youtube.com/watch?v=Q6MH3URLHfM&t=622s)** it might be time to consider Tailscale. If you found this video helpful,

**[10:26](https://youtube.com/watch?v=Q6MH3URLHfM&t=626s)** welcome to the Tailscale YouTube channel, I'm Alex. There is a link down below to all

**[10:31](https://youtube.com/watch?v=Q6MH3URLHfM&t=631s)** of the resources you need to get started by reaching out to our sales team and bringing

**[10:34](https://youtube.com/watch?v=Q6MH3URLHfM&t=634s)** Tailscale to work at tailscale.com slash BTW. If you'd like to see more content like this,

**[10:40](https://youtube.com/watch?v=Q6MH3URLHfM&t=640s)** you can subscribe to the channel down below or indeed drop a comment and ask any questions you

**[10:44](https://youtube.com/watch?v=Q6MH3URLHfM&t=644s)** might have about making the switch from legacy VPNs to Tailscale. Thank you so much for watching,

**[10:50](https://youtube.com/watch?v=Q6MH3URLHfM&t=650s)** and until next time, I've been Alex from Tailscale.

---

*Automatically generated transcript. May contain errors.*
