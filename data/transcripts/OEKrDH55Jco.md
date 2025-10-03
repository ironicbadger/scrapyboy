---
video_id: "OEKrDH55Jco"
title: "Ask A Tailscale Engineer: What is Tailscale SSH? (short)"
description: "This video walks through Tailscale SSH in beta and details how it works with Tailscale engineers, Brad Fitzpatrick and Maisem Ali.

Tailscale SSH connections leverage the same control mechanism as oth..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-06-22"
duration_seconds: 199
youtube_url: "https://www.youtube.com/watch?v=OEKrDH55Jco"
thumbnail_url: "https://i.ytimg.com/vi/OEKrDH55Jco/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:18:19.990447"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 668
transcription_time_seconds: 5.6
---

# Ask A Tailscale Engineer: What is Tailscale SSH? (short)

**[00:04](https://youtube.com/watch?v=OEKrDH55Jco&t=4s)** Hi there, I'm Jessica Kennedy from the Tailscale Marketing team, and today I'm joined by Brad and Mesim, who are here to tell us a bit more about a new feature they've been working on. Tailscale SSH. Brad and Mesim, can you tell us a bit more about yourselves and what you've been working on here? I'm an engineer at Tailscale, working on code things and like the Tailscale shared client code that runs on people's machines, but also like the back end and the data plane and the control plane servers that coordinate everything.

**[00:34](https://youtube.com/watch?v=OEKrDH55Jco&t=34s)** That doesn't involve the web or Swift. Basically the same. I'm also an engineer at Tailscale and I also work on all the things that do not involve me designing stuff. That's great. So what was the motivation to build Tailscale SSH?

**[00:49](https://youtube.com/watch?v=OEKrDH55Jco&t=49s)** Primarily we got tired of like SHQ distribution. SSHQ distribution is such a pain. The more employees you have, the more complex it gets, the more servers you have, the more complex it gets, auditing, trying to figure out who has access to what, who should have access to what is a pain and then like SHGs go out of sync, and then you have really built this entire system to distribute SHGs, which we thought we don't really need to because we have WireGuard and WireGuard already tells us who you are.

**[01:19](https://youtube.com/watch?v=OEKrDH55Jco&t=79s)** Yeah, so I actually have built like the first prototype of this in like early 2020, like right after I joined Tailscale because everyone's early questions was, well I want to make SSH be only accessible over Tailscale.

**[01:31](https://youtube.com/watch?v=OEKrDH55Jco&t=91s)** We've since been doing that tailscale off thing for more things like we have a blog post about our graphana off proxy. So internally when we look at our graphana instance, we don't have to log into graphana. It just knows who we are from our tailscale identity.

**[01:42](https://youtube.com/watch?v=OEKrDH55Jco&t=102s)** We have like an engine X off proxy basically that does the same thing that it passes on the identity information to engine X, which can pass it on to your backend application.

**[01:51](https://youtube.com/watch?v=OEKrDH55Jco&t=111s)** So we're probably going to be doing more and more of this like protocol specific integration with Tailscale off for more things because it's just so convenient.

**[01:59](https://youtube.com/watch?v=OEKrDH55Jco&t=119s)** So how do you use Tailscale SSH and how is it different from what users might expect?

**[02:04](https://youtube.com/watch?v=OEKrDH55Jco&t=124s)** I mean, from like a client side, it's no different. You just use your normal SSH client either it will just work because you've configured it to like not have any double checks, but you can also configure in your policy something called check mode where it like verifies again that you're still present and you know do whatever your off provider wants you to do again.

**[02:21](https://youtube.com/watch?v=OEKrDH55Jco&t=141s)** So in that case, when you connect, you'll get a little message saying like you have to like do some extra authentication step to prove that you know you're still who you are whatever.

**[02:29](https://youtube.com/watch?v=OEKrDH55Jco&t=149s)** And people can configure this to be like, you know, once a day, so the beginning of your work day, the first time you SSH you get a little prompt.

**[02:35](https://youtube.com/watch?v=OEKrDH55Jco&t=155s)** And you can go to a URL to finish it, but instead of having copy paste that if you're already running tailscale on your machine, we just pop your browser up to where you want to go in addition to the message.

**[02:44](https://youtube.com/watch?v=OEKrDH55Jco&t=164s)** And so then once you go through the web off flow, your SSH session just unblocks and your SSH to wherever you need to be, but then if you do it again, like throughout the rest of the day or whatever the configured period is, then it just works.

**[02:56](https://youtube.com/watch?v=OEKrDH55Jco&t=176s)** And without a prompt and the tailscale control plane is out of the loop at that point.

**[03:01](https://youtube.com/watch?v=OEKrDH55Jco&t=181s)** That sounds great. Well, thank you so much, Brad and messim tailscale SSH is now available for all tailscale plans and we can't wait for you to go try it.

**[03:10](https://youtube.com/watch?v=OEKrDH55Jco&t=190s)** Thanks guys.

**[03:11](https://youtube.com/watch?v=OEKrDH55Jco&t=191s)** Go. See you.

**[03:13](https://youtube.com/watch?v=OEKrDH55Jco&t=193s)** Yeah.

---

*Automatically generated transcript. May contain errors.*
