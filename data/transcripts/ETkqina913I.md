---
video_id: "ETkqina913I"
title: "Ask a Tailscale Engineer: What's new and exciting about Tailscale 1.6?"
description: "Episode 01 of 'Ask a software engineer @Tailscale' features Sonia Appasamy and Dave Anderson sharing a key new feature of Tailscale 1.6 - exit nodes. To try exit nodes before 1.6 is released you can d..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2021-03-09"
duration_seconds: 257
youtube_url: "https://www.youtube.com/watch?v=ETkqina913I"
thumbnail_url: "https://i.ytimg.com/vi/ETkqina913I/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:51:30.849260"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 695
transcription_time_seconds: 6.4
---

# Ask a Tailscale Engineer: What's new and exciting about Tailscale 1.6?

**[00:00](https://youtube.com/watch?v=ETkqina913I&t=0s)** Hello, and welcome everyone to the first episode of Ask a Software Engineer at Tailscale. I am your host, Laura Francisi, and today I am joined by Sonia Apazini. Hi, everyone. And Dave Anderson. Hello. What's new and exciting about tailscale 1.6. So I'll pass it over to Sonia and Dave to walk us through it. Perfect. Thanks, Laura.

**[00:30](https://youtube.com/watch?v=ETkqina913I&t=30s)** The highlight feature in 1.6 is a feature called exit nodes, which is the ability for you to route your internet traffic through another machine on your tailscale network. So we want to show you today how to configure that for your network and then show you what it looks like in action. So Dave on his screen has one of his personal tailscale networks up there. You see the admin panel. If he goes on, you can see that he has one of his machines, Amsterdam, already advertises an exit node.

**[01:00](https://youtube.com/watch?v=ETkqina913I&t=60s)** So this means that he's already set up this machine to be used as an exit node on his network. So we're going to show you how to set that up first. So if we jump over to the terminal, an SSH and turn on the machine, his San Francisco machine.

**[01:14](https://youtube.com/watch?v=ETkqina913I&t=74s)** Advertise this machine as an exit node. So to do that, it's really simple. When you're running tailscale up, just include the advertise exit node flag. So if we go ahead and do that.

**[01:25](https://youtube.com/watch?v=ETkqina913I&t=85s)** Now, if we go back to the admin panel, you could see that the San Francisco machine is requested to be an exit node. So you see that little exit node banner pop up with a little info icon that tells you that you have to review this. So there's two steps actually in creating an exit node. First, the machine that you want to act as an exit node needs to choose to advertise itself as an exit node.

**[01:45](https://youtube.com/watch?v=ETkqina913I&t=105s)** And then a admin on your network needs to actually approve this. So if we go into review route settings, we can turn this on as an exit node.

**[01:54](https://youtube.com/watch?v=ETkqina913I&t=114s)** Cool. So now we have two exit nodes on our network, and we can choose to route any of our internet traffic from our other machines through either of these two nodes.

**[02:06](https://youtube.com/watch?v=ETkqina913I&t=126s)** So to show how this works, let's first check out where we currently are. So if we open a tab and we check where am I.

**[02:14](https://youtube.com/watch?v=ETkqina913I&t=134s)** There we are. We are in line for just outside Victoria, British Columbia right now.

**[02:23](https://youtube.com/watch?v=ETkqina913I&t=143s)** Nice. So now let's choose to route our traffic through a different machine in our network. Let's start out with our San Francisco machine.

**[02:33](https://youtube.com/watch?v=ETkqina913I&t=153s)** Cool. So we selected that. And now if we refresh and check out where we are again.

**[02:38](https://youtube.com/watch?v=ETkqina913I&t=158s)** There we go. We are now coming from Santa Clara County South San Francisco Bay.

**[02:50](https://youtube.com/watch?v=ETkqina913I&t=170s)** Cool. And so we can do this again. We cannot jump to Amsterdam. We want to route our traffic through there and said.

**[02:57](https://youtube.com/watch?v=ETkqina913I&t=177s)** Alright, there we go. If we hit refresh.

**[03:01](https://youtube.com/watch?v=ETkqina913I&t=181s)** I folks a second to get used to the new network. There we go.

**[03:05](https://youtube.com/watch?v=ETkqina913I&t=185s)** And we are now in downtown Amsterdam somewhere.

**[03:10](https://youtube.com/watch?v=ETkqina913I&t=190s)** So that's exit nodes in action. Dave, do you want to talk about how users can try this out now?

**[03:16](https://youtube.com/watch?v=ETkqina913I&t=196s)** Sure. So tailscale 1.6 is scheduled to come out on March 15 through thereabouts.

**[03:23](https://youtube.com/watch?v=ETkqina913I&t=203s)** If you want to try it before that, you can install our unstable packages by going to PKGS dot tailscale dot com slash unstable.

**[03:35](https://youtube.com/watch?v=ETkqina913I&t=215s)** You will find install instructions for a whole bunch of Linux distributions and for windows.

**[03:41](https://youtube.com/watch?v=ETkqina913I&t=221s)** So you'll need to install the unstable version on both the machine you want to be your exit node and on your client that you want to select the exit node from.

**[03:51](https://youtube.com/watch?v=ETkqina913I&t=231s)** Amazing.

**[03:52](https://youtube.com/watch?v=ETkqina913I&t=232s)** Pretty much it. And please give us feedback if it works or it doesn't work for you.

**[03:56](https://youtube.com/watch?v=ETkqina913I&t=236s)** This is really exciting and super simple for how complex it is. I'm excited for 1.6 to come out on the 15th.

**[04:06](https://youtube.com/watch?v=ETkqina913I&t=246s)** So thanks so much for your time. Everyone will catch you on the next ask a software engineer at tailscale.

**[04:15](https://youtube.com/watch?v=ETkqina913I&t=255s)** Bye guys.

**[04:16](https://youtube.com/watch?v=ETkqina913I&t=256s)** Bye.

---

*Automatically generated transcript. May contain errors.*
