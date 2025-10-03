---
video_id: "27apZcZrwks"
title: "Rustdesk and Tailscale is a remote desktop access dream team"
description: "In today's video, we'll be covering why pairing Rustdesk with Tailscale is the absolute bee's knees of remote access solutions.

Rustdesk suggests we as users spin up our own self-hosted relay servers..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-07-10"
duration_seconds: 570
youtube_url: "https://www.youtube.com/watch?v=27apZcZrwks"
thumbnail_url: "https://i.ytimg.com/vi_webp/27apZcZrwks/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:08:19.746694"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1796
transcription_time_seconds: 16.3
---

# Rustdesk and Tailscale is a remote desktop access dream team

**[00:00](https://youtube.com/watch?v=27apZcZrwks&t=0s)** I've played tech support for my family for years at this point, and an indispensable tool

**[00:05](https://youtube.com/watch?v=27apZcZrwks&t=5s)** in my tool belt during that time has been team viewer. However, over time, it's gotten

**[00:10](https://youtube.com/watch?v=27apZcZrwks&t=10s)** more and more aggressive about the pop-ups asking, are you sure you're not running a business?

**[00:15](https://youtube.com/watch?v=27apZcZrwks&t=15s)** An OS native tooling such as Microsoft's remote desktop but Apple's screen sharing

**[00:19](https://youtube.com/watch?v=27apZcZrwks&t=19s)** VNC implementation lack the user friendliness of typing in a code and punching through firewalls

**[00:25](https://youtube.com/watch?v=27apZcZrwks&t=25s)** to help your family out without configuring port forwarding and that kind of stuff.

**[00:30](https://youtube.com/watch?v=27apZcZrwks&t=30s)** And as a result of these network complexities and nag screens, some remote desktop alternatives

**[00:35](https://youtube.com/watch?v=27apZcZrwks&t=35s)** have popped up over the years, such as any desk and to some extent VNC too. But this is where

**[00:41](https://youtube.com/watch?v=27apZcZrwks&t=41s)** today's video hero comes in, Rustdesk. This isn't a new project by any means, but it is an open

**[00:47](https://youtube.com/watch?v=27apZcZrwks&t=47s)** source and mostly free, as in cost, alternative to team viewer. Rustdesk purports to give you a reliable

**[00:55](https://youtube.com/watch?v=27apZcZrwks&t=55s)** remote desktop experience with your own self-hosted servers. Someone say self-hosted servers, I'm in.

**[01:02](https://youtube.com/watch?v=27apZcZrwks&t=62s)** But this is the tail scale channel after all, and we don't need someone else to punch through

**[01:06](https://youtube.com/watch?v=27apZcZrwks&t=66s)** NAT for us, that's literally what tail scale does best. No relay servers here, for the most part,

**[01:13](https://youtube.com/watch?v=27apZcZrwks&t=73s)** at least, just direct connections and end to end encrypted wire guard tunnels behind the scenes.

**[01:18](https://youtube.com/watch?v=27apZcZrwks&t=78s)** So in today's video, I will cover the basics of Rustdesk and how to set it up with tail scale.

**[01:23](https://youtube.com/watch?v=27apZcZrwks&t=83s)** Now in the description down below, I've linked to a blog post by my colleague Kevin Perdi,

**[01:27](https://youtube.com/watch?v=27apZcZrwks&t=87s)** formerly of ours Technica fame, though, and he's going to dive into some aspects I didn't cover

**[01:32](https://youtube.com/watch?v=27apZcZrwks&t=92s)** in the video today, such as the web front end and some other intricacies too. I'll leave a link

**[01:37](https://youtube.com/watch?v=27apZcZrwks&t=97s)** to that post in the description down below. What other free and open source remote desktop

**[01:44](https://youtube.com/watch?v=27apZcZrwks&t=104s)** technology lets you connect, not only to Windows, as we have here, but also to Mac, as we have here,

**[01:51](https://youtube.com/watch?v=27apZcZrwks&t=111s)** in fact, you can see this is the screen just over my shoulder right here, or to Linux.

**[01:58](https://youtube.com/watch?v=27apZcZrwks&t=118s)** And this is the magic of Rustdesk. We can connect to all the big three operating systems

**[02:03](https://youtube.com/watch?v=27apZcZrwks&t=123s)** from a single system. Yes, I know VNCs let us do this for years, but the magic of Rustdesk

**[02:09](https://youtube.com/watch?v=27apZcZrwks&t=129s)** is it does a lot of the hard work for us, like the client server stuff can be a little complicated

**[02:14](https://youtube.com/watch?v=27apZcZrwks&t=134s)** to set up sometimes with VNC. But with Rustdesk, we've got all sorts of fun stuff we can play with

**[02:19](https://youtube.com/watch?v=27apZcZrwks&t=139s)** in the menus too. Like, we can look at scaling, we can change the codex, we can change image quality,

**[02:25](https://youtube.com/watch?v=27apZcZrwks&t=145s)** copy and paste works, you can look at the actual, you know, I'm a framerate nerd, I love looking at

**[02:31](https://youtube.com/watch?v=27apZcZrwks&t=151s)** video bit rates and all that kind of stuff. And when you pair Rustdesk with tail scale,

**[02:37](https://youtube.com/watch?v=27apZcZrwks&t=157s)** you don't even have to worry about setting up your own self-hosted Rustdesk relay server either,

**[02:42](https://youtube.com/watch?v=27apZcZrwks&t=162s)** because every node on your telnet, this assumes every node you want to connect to,

**[02:46](https://youtube.com/watch?v=27apZcZrwks&t=166s)** is a node on your telnet. But with tail scale as the connection fabric between everything,

**[02:52](https://youtube.com/watch?v=27apZcZrwks&t=172s)** everything can talk to everything else, you don't have to worry about setting up these relay

**[02:56](https://youtube.com/watch?v=27apZcZrwks&t=176s)** servers that Rustdesk typically ask you to do. It just works over tail scale, you enter your tail

**[03:02](https://youtube.com/watch?v=27apZcZrwks&t=182s)** scale, node IP address and you can connect to any Rustdesk server, no matter the operating system.

**[03:09](https://youtube.com/watch?v=27apZcZrwks&t=189s)** Performance is pretty good too, so let's just load up my favourite video game of all time,

**[03:14](https://youtube.com/watch?v=27apZcZrwks&t=194s)** Factorio, any day where I get to play Factorio at work, is a good day in my book. I'm going to set

**[03:20](https://youtube.com/watch?v=27apZcZrwks&t=200s)** the adaptive scaling here and just give you a sort of an idea of what's going on with the

**[03:23](https://youtube.com/watch?v=27apZcZrwks&t=203s)** performance, I'll make this full screen too. Now this is all happening over my local network,

**[03:28](https://youtube.com/watch?v=27apZcZrwks&t=208s)** this laptop is connected over Wi-Fi to an access point, that just add a shot just up there,

**[03:32](https://youtube.com/watch?v=27apZcZrwks&t=212s)** so that's not going very far and then this computer is connected via ethernet into the rest of my

**[03:37](https://youtube.com/watch?v=27apZcZrwks&t=217s)** network. But you can kind of see that like the performance is pretty good, like the codex able to

**[03:43](https://youtube.com/watch?v=27apZcZrwks&t=223s)** handle some pretty unpleasant, in terms of compression, the accumulators there with their

**[03:49](https://youtube.com/watch?v=27apZcZrwks&t=229s)** lightning beams, it's pretty unpleasant to try and render that. You can kind of see some pixelation

**[03:54](https://youtube.com/watch?v=27apZcZrwks&t=234s)** and some some smoothing I guess going on there, but we can go into the settings and set image

**[03:58](https://youtube.com/watch?v=27apZcZrwks&t=238s)** quality as good image quality and it does make a noticeable difference to the quality that's going

**[04:03](https://youtube.com/watch?v=27apZcZrwks&t=243s)** on. You can see that the current target bitrate is eight, eight megabits a second and the codex is

**[04:09](https://youtube.com/watch?v=27apZcZrwks&t=249s)** H265, FPS is 30 FPS, it's good enough, I could absolutely make do with playing Factorio this way,

**[04:16](https://youtube.com/watch?v=27apZcZrwks&t=256s)** there's a little bit of lag, but honestly for the things we're going to actually use Rust Desk for,

**[04:20](https://youtube.com/watch?v=27apZcZrwks&t=260s)** which is probably not gaming, you want to use Apollo and Sunshine and Parsec for those kinds of

**[04:25](https://youtube.com/watch?v=27apZcZrwks&t=265s)** things probably. You can see that even when there's a lot going on on the screen, you could absolutely

**[04:30](https://youtube.com/watch?v=27apZcZrwks&t=270s)** just watch a video and can you even tell right now that this is not your local system?

**[04:37](https://youtube.com/watch?v=27apZcZrwks&t=277s)** It's just awesome. I am absolutely in love with Rust Desk at the minute and then you can jump

**[04:42](https://youtube.com/watch?v=27apZcZrwks&t=282s)** between, like I say, all the different operating systems between the laptop behind me on the table.

**[04:47](https://youtube.com/watch?v=27apZcZrwks&t=287s)** Again, that's just cool, isn't it? All right, so let's go into scale original,

**[04:53](https://youtube.com/watch?v=27apZcZrwks&t=293s)** I want to bring up the Rust Desk client because there are a couple of things we've got a tweak to

**[04:58](https://youtube.com/watch?v=27apZcZrwks&t=298s)** make sure that our remote tail scale node, in my case, this laptop on the desk in front of me,

**[05:03](https://youtube.com/watch?v=27apZcZrwks&t=303s)** can reach out over the tailnet to connect to this node wherever it happens to be.

**[05:08](https://youtube.com/watch?v=27apZcZrwks&t=308s)** So it's not the most intuitive settings menu ever, but it's right here. If you go to the ID

**[05:13](https://youtube.com/watch?v=27apZcZrwks&t=313s)** option and click on this three dot menu right here, you want to go to Security. Click on Unlock

**[05:19](https://youtube.com/watch?v=27apZcZrwks&t=319s)** Security Settings and then scroll down just a little bit until it says Use Permanent Password.

**[05:25](https://youtube.com/watch?v=27apZcZrwks&t=325s)** So first of all, sit yourself a permanent password, pretty straightforward, and then second of all,

**[05:30](https://youtube.com/watch?v=27apZcZrwks&t=330s)** we're going to want to make sure that we check this box here. This is of critical importance.

**[05:34](https://youtube.com/watch?v=27apZcZrwks&t=334s)** Make sure you check the box that says Enable Direct IP Access. What this will allow you to do is

**[05:40](https://youtube.com/watch?v=27apZcZrwks&t=340s)** instead of in this box here when you're connecting to a new host, instead of typing in your remote

**[05:45](https://youtube.com/watch?v=27apZcZrwks&t=345s)** person's ID and password, you simply type in the tailnet IP address of the remote host.

**[05:51](https://youtube.com/watch?v=27apZcZrwks&t=351s)** So let's see what kind of level of inception we can get to here. Let's see if I can bring up,

**[05:56](https://youtube.com/watch?v=27apZcZrwks&t=356s)** let's see if I can bring up the Ubuntu host through Rustdesk through Rustdesk to Ubuntu.

**[06:02](https://youtube.com/watch?v=27apZcZrwks&t=362s)** That's a bit silly, but let's try it. So under my network devices, you can see here that I've

**[06:06](https://youtube.com/watch?v=27apZcZrwks&t=366s)** got one called UbuTest, which is my Ubuntu test box. I'm going to copy the tailscale IP address,

**[06:13](https://youtube.com/watch?v=27apZcZrwks&t=373s)** note that unfortunately the Rustdesk client doesn't respect magic DNS names. Like if I put

**[06:19](https://youtube.com/watch?v=27apZcZrwks&t=379s)** UbuTest in here, for example, that's the magic DNS name of this node on my tailnet.

**[06:25](https://youtube.com/watch?v=27apZcZrwks&t=385s)** It just says ID does not exist. However, if you put an actual IP address into this box,

**[06:32](https://youtube.com/watch?v=27apZcZrwks&t=392s)** everything works as we would expect. So let's do a little bit of Rustdesk inception. Here we go.

**[06:38](https://youtube.com/watch?v=27apZcZrwks&t=398s)** I've got Rustdesk with inside Rustdesk and I could go another level deep if I wanted to,

**[06:42](https://youtube.com/watch?v=27apZcZrwks&t=402s)** but there you go. So you can see that using Rustdesk over tailscale, getting the IP address,

**[06:47](https://youtube.com/watch?v=27apZcZrwks&t=407s)** I can just connect anywhere. So why is this a big deal? Why is Alex so excited about tailscale and

**[06:52](https://youtube.com/watch?v=27apZcZrwks&t=412s)** Rustdesk coming together in a peanut butter and chocolate sandwich that's just of deliciousness?

**[06:58](https://youtube.com/watch?v=27apZcZrwks&t=418s)** Well, what happens when I take this laptop outside of this house? How would this laptop

**[07:05](https://youtube.com/watch?v=27apZcZrwks&t=425s)** connect back to these nodes? Well, I'd either have to open supports in my firewall,

**[07:10](https://youtube.com/watch?v=27apZcZrwks&t=430s)** probably don't want to do because this is remote control after all, which is quite a big security hole,

**[07:15](https://youtube.com/watch?v=27apZcZrwks&t=435s)** or I'd have to host some kind of a public relay server. And this is what Rustdesk actually

**[07:19](https://youtube.com/watch?v=27apZcZrwks&t=439s)** suggest you do. They suggest that you spin up a server on a VPS in the cloud somewhere,

**[07:25](https://youtube.com/watch?v=27apZcZrwks&t=445s)** doesn't use a lot of resources, but it's essentially there to act as this kind of in between

**[07:30](https://youtube.com/watch?v=27apZcZrwks&t=450s)** bounce a node, this kind of like relay node, and all the traffic from node A, your laptop,

**[07:35](https://youtube.com/watch?v=27apZcZrwks&t=455s)** to node B, traverses that relay node up in the cloud. So it's kind of hairpinning in and hairpinning

**[07:41](https://youtube.com/watch?v=27apZcZrwks&t=461s)** out again. It's not, it's not ideal. But with tailscale, nodes make direct connections to each other

**[07:47](https://youtube.com/watch?v=27apZcZrwks&t=467s)** nodes. So I could go to the coffee shop right now. I can just pick up right where I left off. So

**[07:51](https://youtube.com/watch?v=27apZcZrwks&t=471s)** for example, here's the same laptop I was using five minutes ago at my house, connected over 5G

**[07:58](https://youtube.com/watch?v=27apZcZrwks&t=478s)** to the public internet. And now this laptop is connected via tailscale to my tailnet. I can now

**[08:04](https://youtube.com/watch?v=27apZcZrwks&t=484s)** connect to any of these nodes without any further configuration. This is why I love tailscale so much.

**[08:10](https://youtube.com/watch?v=27apZcZrwks&t=490s)** It just completely makes network topologies disappear. And Rustdesk is a layer that runs on top of that

**[08:18](https://youtube.com/watch?v=27apZcZrwks&t=498s)** overlay network that tailscale creates for you. So I can basically now connect into my editing laptop

**[08:25](https://youtube.com/watch?v=27apZcZrwks&t=505s)** as if I'll sat on my desk back at my house, connect into my gaming rig as if I'll sat at my desk

**[08:31](https://youtube.com/watch?v=27apZcZrwks&t=511s)** back in my house from the coffee shop. It's just awesome. It's just awesome. And it makes my life

**[08:37](https://youtube.com/watch?v=27apZcZrwks&t=517s)** so, so much easier to do it this way. So I don't think there's anything else tailscale specific

**[08:42](https://youtube.com/watch?v=27apZcZrwks&t=522s)** to cover today. The real magic is that each of these nodes was just another node on my tailnet,

**[08:48](https://youtube.com/watch?v=27apZcZrwks&t=528s)** same as any other video that I make. All I did was I installed Rustdesk on each of those nodes,

**[08:54](https://youtube.com/watch?v=27apZcZrwks&t=534s)** set up an unattended password, and then also allowed direct IP access. And suddenly,

**[08:58](https://youtube.com/watch?v=27apZcZrwks&t=538s)** I can access any of these nodes from anywhere else in the world thanks to the magic of tailscales

**[09:03](https://youtube.com/watch?v=27apZcZrwks&t=543s)** natural virtual technology. So that's a very quick overview of Rustdesk and tailscale and how it can

**[09:08](https://youtube.com/watch?v=27apZcZrwks&t=548s)** make your life your remote network life easier than ever. Thank you so much for watching.

**[09:14](https://youtube.com/watch?v=27apZcZrwks&t=554s)** And until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
