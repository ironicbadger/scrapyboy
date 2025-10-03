---
video_id: "LmfWyeHhay8"
title: "Tailscale Up: Bingo"
description: "This talk was given by Brad Fitzpatrick at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 386
youtube_url: "https://www.youtube.com/watch?v=LmfWyeHhay8"
thumbnail_url: "https://i.ytimg.com/vi_webp/LmfWyeHhay8/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:12:11.120457"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1146
transcription_time_seconds: 11.3
---

# Tailscale Up: Bingo

**[00:00](https://youtube.com/watch?v=LmfWyeHhay8&t=0s)** All right, this is a lightning talk, lightning talk, time. I'll do interest later. There's a lot of talks today, talks are fun, but let's play a game. We're going to play Bingo. More specifically, we're going to play Lingo Bingo. If you've been living under a rock, or not true ship age, Bingo is that game where you try to get five in a row. Except for instead of playing with numbers, we're going to play with letters, and we're going to play more specifically with Tailscale Lingo. Lingo is the nerdy crap that a bunch of people say in a certain group.

**[00:30](https://youtube.com/watch?v=LmfWyeHhay8&t=30s)** We're going to play some gibberish and start with the G, so you get a G. Got it? Okay, everyone open up your laptops and phones, and go here. Except for this is a lightning talk, I don't have time to wait for you, so you get a timer. So far, we've got 10 people joined. That's great. 12, 17, 19 of you using funnel. One person is using Tailscale directly. There is a little mushroom in the middle. If you click that, you can join the tailnet, and you can connect to it directly, and stay within this building and not use the ISP.

**[01:02](https://youtube.com/watch?v=LmfWyeHhay8&t=62s)** But it gets you the free square. Hi, Will. Hi, Besson. There's a people joining right now over Tailscale. Z. Oh, intro. All right, go to Tailscale. It's a great code. I used to travel, speak, now live in Seattle. Okay, game on. Everyone ready? Anyone still waiting? Okay. So we're going to talk about Tailscale D. This is the daemon that runs on your machine, the little agent. There's a lot of protocols in that thing, and so we're going to go through some of the things it can do. Obviously, it can do wire guard.

**[01:34](https://youtube.com/watch?v=LmfWyeHhay8&t=94s)** Anyone get a W? All right, all right. Wireguard does the IP encryption of the IP packets. This is the data plane. It does IPv4. It does IPv6. It also, we also have HTTP client in there that talks out to our control plane to manage the keys and stuff. We also have an HTTP server that's used for peer API and the local pair. Anyone get two in a row yet? Anyone got three in a row? I forgot, you have to yell bingo, by the way, when you have bingo, if you want the full experience.

**[02:07](https://youtube.com/watch?v=LmfWyeHhay8&t=127s)** There's also a HTTP server in Tailscale funnel, which you're all hitting right now to play this, or at least 59 of you are hitting. We have an ACME client in there. So let's encrypt, gets your HTTP certs over the ACME protocol. We speak HTTP1, we speak HTTP2, we speak TLS, we speak noise. Magic DNS means there's a DNS implementation inside Tailscale D, both for the client and the server. So we get the things on quad 100, we speak DNS server, we optionally forward them out elsewhere. We have a DOH, a DNS server HTTP client.

**[02:36](https://youtube.com/watch?v=LmfWyeHhay8&t=156s)** So if you have Cloudflare or Google configured, then we automatically upgrade it to DOH. So when it leaves your home or whatever, it isn't going in clear text.

**[02:45](https://youtube.com/watch?v=LmfWyeHhay8&t=165s)** For natural reversal, that's all about making sure that UDP packets can come and go directly. As a fallback and as a method to upgrade, we have this protocol called DURP, which I think stands for something, but we always forget what it is.

**[03:00](https://youtube.com/watch?v=LmfWyeHhay8&t=180s)** We also have this little protocol that goes over DURP and over UDP called DiscoShore for Discovery, and we send these little disco pings around.

**[03:07](https://youtube.com/watch?v=LmfWyeHhay8&t=187s)** We also send ICMP pings around, and then we also have this weird protocol we made called TSNP, which is another IP, it's INA protocol 99, which is reserved for private use for maybe encryption or something.

**[03:19](https://youtube.com/watch?v=LmfWyeHhay8&t=199s)** So we stole that number. So we use this mostly for debugging connectivity to see where things are failing at.

**[03:27](https://youtube.com/watch?v=LmfWyeHhay8&t=207s)** For opening up ports on your home router or whatever, there's three common protocols that are in use. There's NAT PMP, which Apple made was small and beautiful, and then it got standardized into something less beautiful called PCP, and then there's the old UPP, which has like 50 variants of XML goop.

**[03:41](https://youtube.com/watch?v=LmfWyeHhay8&t=221s)** So we just try all these variants and see what your home router will do to open up ports.

**[03:46](https://youtube.com/watch?v=LmfWyeHhay8&t=226s)** Tailscale by default is a layer three network, so IP packets, we use the ton interface when available on your operating system.

**[03:53](https://youtube.com/watch?v=LmfWyeHhay8&t=233s)** We also have a weird kind of experimental level layer two mode that does ethernet stuff and speaks enough Mac and uses the tap interface in the operating system on Linux only, where we speak enough of ARP in the Intel scale D and enough of DHCP to let you do things like plug in a printer to a little like travel router thing, and that travel router can speak tailscale for you.

**[04:14](https://youtube.com/watch?v=LmfWyeHhay8&t=254s)** So give out a DHCP address to like your printer that is a tailscale address, and then the little travel router does the tailscale for you. That's not really a released feature, but it's there.

**[04:26](https://youtube.com/watch?v=LmfWyeHhay8&t=266s)** Coming soon lies. If you don't have a ton or tap, there's also a user space mode. We bring in a G visor. G visor is a Google project that includes net stack, which is a TCP IP implementation that's on pure go.

**[04:41](https://youtube.com/watch?v=LmfWyeHhay8&t=281s)** So we can do all the TCP stack and go without having the kernel do anything.

**[04:46](https://youtube.com/watch?v=LmfWyeHhay8&t=286s)** To get things out of the machine when you're running in user space mode, we have a HTTP proxy that you can run tailscale D dash as HTTP proxy or something, and we can do it speaks HTTP connect. It also has a socks five implementation.

**[05:00](https://youtube.com/watch?v=LmfWyeHhay8&t=300s)** So it has SSH server in it now, so that's a tailscale SSH, and if you try to like SCP to it, nowadays the SSH implementation will also switch to sftp, so we have a sftp server in there as well.

**[05:11](https://youtube.com/watch?v=LmfWyeHhay8&t=311s)** In terms of platforms, we run on Linux, Mac, Windows, iOS, Android, FreeBSD, OpenBSD, I think a lumos is there, but I forgot about that.

**[05:20](https://youtube.com/watch?v=LmfWyeHhay8&t=320s)** No, I don't believe you. No, you didn't log into tailscale. You don't have the free one. But do you see a mushroom? Is it black behind it? Okay, I'll check you later. I'll check you later, but okay, I'll remember you.

**[05:45](https://youtube.com/watch?v=LmfWyeHhay8&t=345s)** There's a web assembly. Web assembly does web sockets in and out. There's Synology, we're on Synology, we're on QNAP, pfSense, opnSense, TrueNAS, we're on a various container things, we're on Docker, Docker desktop, Kubernetes, we have Kubernetes operator.

**[06:03](https://youtube.com/watch?v=LmfWyeHhay8&t=363s)** For clouds, we have like AWS specific integration, we have Azure specific integration, GCP.

**[06:10](https://youtube.com/watch?v=LmfWyeHhay8&t=370s)** Miscellaneous stuff, there's a Prometheus NodeExporter in tailscale D, we also speak some BGP stuff.

**[06:22](https://youtube.com/watch?v=LmfWyeHhay8&t=382s)** So, all right, thank you.

---

*Automatically generated transcript. May contain errors.*
