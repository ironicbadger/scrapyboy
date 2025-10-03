---
video_id: "wCqXYPQFNuE"
title: "Ask a Tailscale Engineer: Throughput Improvements to Wireguard-go"
description: "This video walks through improvements Tailscale engineers Jordan Whited and James Tucker made to wireguard-go, which is the userspace WireGuard® implementation that Tailscale uses.

What this means fo..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-12-13"
duration_seconds: 497
youtube_url: "https://www.youtube.com/watch?v=wCqXYPQFNuE"
thumbnail_url: "https://i.ytimg.com/vi/wCqXYPQFNuE/hqdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:12:43.826761"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1451
transcription_time_seconds: 13.5
---

# Ask a Tailscale Engineer: Throughput Improvements to Wireguard-go

**[00:04](https://youtube.com/watch?v=wCqXYPQFNuE&t=4s)** Hi, my name is Jeff Spencer and I lead product marketing here at Tailscale. Today I'm joined by James Tucker and Jordan Whited, who are here to tell us a bit more about some really cool throughput upgrades for Tailscale. James and Jordan, before we get started, can you tell me a bit more about yourself and what you work on just broadly here at Tailscale and James will start with you? So yeah, work kind of bit of everything from the control planes through the client, mostly sort of focused on things that affect the user experience.

**[00:34](https://youtube.com/watch?v=wCqXYPQFNuE&t=34s)** Once I started, I've been looking at performance periodically and then when Jordan joined, started doing the same thing, so we eventually joined forces.

**[00:43](https://youtube.com/watch?v=wCqXYPQFNuE&t=43s)** Great, and Jordan, I enjoy working on networking performance problems and I've been primarily focused on the Tailscale client code since joining and improving its performance.

**[00:53](https://youtube.com/watch?v=wCqXYPQFNuE&t=53s)** Cool, so for throughput, let's start at the beginning. Now, when we talk about throughput for Tailscale, what do we mean and why doesn't matter for Tailscale users?

**[01:02](https://youtube.com/watch?v=wCqXYPQFNuE&t=62s)** James? Yeah, so throughput is how fast your downloads, your uploads are going, right? And particularly it's the number, it's related to the number that you see when it hits peak, when you have a large file, you typically see it sort of, it gets faster over time.

**[01:22](https://youtube.com/watch?v=wCqXYPQFNuE&t=82s)** So it's mostly affecting things like if you're fetching files from a network storage, something like that, that's where you'll see it.

**[01:29](https://youtube.com/watch?v=wCqXYPQFNuE&t=89s)** And what does throughput depend on? How do you optimize it in your network?

**[01:34](https://youtube.com/watch?v=wCqXYPQFNuE&t=94s)** Yes, there's a lot of factors, so latency is a big thing. And so if you have very high latency on your network, then you will often find that throughput slower, but there's things that network engineers do, and we'll talk more about this, to improve throughput in those scenarios.

**[01:51](https://youtube.com/watch?v=wCqXYPQFNuE&t=111s)** But the first thing with Tailscale, the most important thing is, is make sure you've established a direct connection. So we have some knowledge based articles on making sure that you've established a direct connection. 90% of our nodes do.

**[02:04](https://youtube.com/watch?v=wCqXYPQFNuE&t=124s)** It's something that we pride ourselves on being very good at, but if you're noticing slow speed, that's the first things check is that you have a direct connection.

**[02:12](https://youtube.com/watch?v=wCqXYPQFNuE&t=132s)** Cool. So taking it just a quick step back here, Tails has built on Wireguard, which is a modern way to connect devices together in an end and encrypted way.

**[02:22](https://youtube.com/watch?v=wCqXYPQFNuE&t=142s)** But Tailscale uses Wireguard Go, which runs in the user space, so it's been less performant traditionally than kernel Wireguard. How do these improvements compare to Wireguard?

**[02:31](https://youtube.com/watch?v=wCqXYPQFNuE&t=151s)** Yeah, so both implementations are Wireguard, right? They're both upstream Wireguard, and what we're really talking about today, the root of those patches and the stuff that we're doing is going upstream to Wireguard Go.

**[02:44](https://youtube.com/watch?v=wCqXYPQFNuE&t=164s)** Our use of Wireguard Go is user space implementation has been a common concern for a number of users who look at it and go, well, user space is slow, and that can be kind of a common thing.

**[02:56](https://youtube.com/watch?v=wCqXYPQFNuE&t=176s)** What we have been able to achieve is, you know, in an ideal scenario in the best case, we're sometimes faster than the current kernel implementation. Now that will change over time, everybody will improve performance over time as they put work in.

**[03:11](https://youtube.com/watch?v=wCqXYPQFNuE&t=191s)** But really this shouldn't start to elase some concerns that like just because it's user space, it's slow. We were making improvements that mean that all of the implementation should be pretty close to equal performance and all of them should be performing really well.

**[03:25](https://youtube.com/watch?v=wCqXYPQFNuE&t=205s)** That's really amazing. So what kind of throughputs can users expect to see?

**[03:29](https://youtube.com/watch?v=wCqXYPQFNuE&t=209s)** Yeah, so in many sort of, you know, in your typical home lab scenario, in your typical like you're on Wi-Fi or you, you know, you've got a one gig bit per second home network kind of scenario or small office network, you should see line rate most of the time.

**[03:44](https://youtube.com/watch?v=wCqXYPQFNuE&t=224s)** And if you don't, then there's there's probably stuff that is worth us looking into.

**[03:50](https://youtube.com/watch?v=wCqXYPQFNuE&t=230s)** If you're on a very fast internet connection, there were oftentimes that we wouldn't quite reach peak line rate, you know, sort of max out your connection.

**[04:00](https://youtube.com/watch?v=wCqXYPQFNuE&t=240s)** Nowadays, we should be able to particularly if it's a Linux to Linux transfer, and we'll talk more about that, but these improvements focused on Linux.

**[04:08](https://youtube.com/watch?v=wCqXYPQFNuE&t=248s)** So if you're on a 10 gig network, we're not going to reach line rate today.

**[04:12](https://youtube.com/watch?v=wCqXYPQFNuE&t=252s)** 10 gig is an interesting challenge, not just for us, but for anyone who's doing encrypted VPN type transports 10 gigs, 10 gigs, a big number to reach.

**[04:22](https://youtube.com/watch?v=wCqXYPQFNuE&t=262s)** But we have made a big dent there, right? So we were, we're getting, you know, really into those speeds very much above one gig a bit per second. So big improvements there.

**[04:32](https://youtube.com/watch?v=wCqXYPQFNuE&t=272s)** But there will be more to come in that space.

**[04:34](https://youtube.com/watch?v=wCqXYPQFNuE&t=274s)** Got it. Well, why don't we peek under the hood a bit and we'll turn it over to you Jordan to tell us how you actually went about increasing throughput.

**[04:41](https://youtube.com/watch?v=wCqXYPQFNuE&t=281s)** Sure, we increased throughput by changing the IO model, which is the way in which we move data through tail scale from handling single packets to handling batches of packets.

**[04:54](https://youtube.com/watch?v=wCqXYPQFNuE&t=294s)** This changed greatly reduced the amount of CPU time spent interfacing with the Linux kernel at the system call boundary, and it also reduced time spent on the kernel side traversing its networking stack with CPU time reduced on both sides.

**[05:12](https://youtube.com/watch?v=wCqXYPQFNuE&t=312s)** We also are now moving larger amounts of data through the effectively the data pipeline within tail scale and this translates to increase throughput.

**[05:22](https://youtube.com/watch?v=wCqXYPQFNuE&t=322s)** Got it. Now I've heard you both mentioned Linux a couple of times throughout this talk. So just want to ask are there any differences depending on which operating system you're using.

**[05:30](https://youtube.com/watch?v=wCqXYPQFNuE&t=330s)** Yeah, this initial set of changes is is enabled for Linux. It's not yet enabled for other platforms that we plan to extend these performance benefits to other platforms as time goes on.

**[05:41](https://youtube.com/watch?v=wCqXYPQFNuE&t=341s)** Well, figures crossed those are sooner rather than later. Now the users need to do anything to turn on this functionality.

**[05:46](https://youtube.com/watch?v=wCqXYPQFNuE&t=346s)** No, these changes are enabled by default on Linux. Awesome. All right. Well, again, taking sort of a step back, you know, looking more at your experience, sort of building this. Did you learn anything from working on throughput?

**[05:59](https://youtube.com/watch?v=wCqXYPQFNuE&t=359s)** Definitely. One of the biggest lessons I learned and relearned was to take a step back and kind of survey the landscape of what already exists before diving into a problem.

**[06:13](https://youtube.com/watch?v=wCqXYPQFNuE&t=373s)** I found a function in the Linux ton driver that was ultimately the feature set that we leaned on to enable us to send batches, send or receive batches of packets on the ton driver side.

**[06:28](https://youtube.com/watch?v=wCqXYPQFNuE&t=388s)** And this feature has actually existed in the Linux kernel since 2008.

**[06:34](https://youtube.com/watch?v=wCqXYPQFNuE&t=394s)** But it had largely gone unnoticed.

**[06:38](https://youtube.com/watch?v=wCqXYPQFNuE&t=398s)** And we really benefited just from taking a step back and reading reading the code always good advice for engineers.

**[06:47](https://youtube.com/watch?v=wCqXYPQFNuE&t=407s)** With that James, I think I'll give you the last word. Is there anything else that people should know about throughput?

**[06:52](https://youtube.com/watch?v=wCqXYPQFNuE&t=412s)** I think the big thing. I just want to reiterate is, you know, it's Linux only for this version.

**[06:57](https://youtube.com/watch?v=wCqXYPQFNuE&t=417s)** We were going to work on on bringing these improvements to other platforms. Windows is very likely the next one. It has a nice equivalent interface that we're going to use.

**[07:07](https://youtube.com/watch?v=wCqXYPQFNuE&t=427s)** Direct connections. You know, if you're seeing slow performance, the first thing to look at is, is are you establishing a direct connection as I say we do in most cases.

**[07:16](https://youtube.com/watch?v=wCqXYPQFNuE&t=436s)** But if you're seeing slow performance, that's the first thing to look for.

**[07:20](https://youtube.com/watch?v=wCqXYPQFNuE&t=440s)** We've also addressed a number of other bugs along the path to this work. So we've done a lot of analysis of like what's going on in flows. And so,

**[07:29](https://youtube.com/watch?v=wCqXYPQFNuE&t=449s)** latency also matters as I mentioned earlier, if you have a high latency link if you're halfway around the world that should you should see greatly improved performance.

**[07:39](https://youtube.com/watch?v=wCqXYPQFNuE&t=459s)** If your other node is halfway around the world from previously, but that will still have an impact. So, you know, you can expect very fast performance on the line, not always the same performance.

**[07:51](https://youtube.com/watch?v=wCqXYPQFNuE&t=471s)** If you're going halfway around the world, it should be much improved, but we will continue to be making improvements in those kind of areas over time.

**[07:58](https://youtube.com/watch?v=wCqXYPQFNuE&t=478s)** Well, James and Jordan, thank you so much for that great overview of throughput.

**[08:02](https://youtube.com/watch?v=wCqXYPQFNuE&t=482s)** You should start seeing higher throughput immediately and you can visit tailscale.com for more information and to try tail scale for free.

**[08:10](https://youtube.com/watch?v=wCqXYPQFNuE&t=490s)** Thanks everyone, and we'll see you next time.

---

*Automatically generated transcript. May contain errors.*
