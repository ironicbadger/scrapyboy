---
video_id: "MpxmfpCl20c"
title: "Serve and Funnel | Tailscale Explained"
description: "At Tailscale, we're always adding new features and solving real problems for developers and infrastructure folks alike. In our \"Tailscale Explained\" series we show you all you need to know to get star..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-11-09"
duration_seconds: 382
youtube_url: "https://www.youtube.com/watch?v=MpxmfpCl20c"
thumbnail_url: "https://i.ytimg.com/vi_webp/MpxmfpCl20c/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:43:43.130903"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1223
transcription_time_seconds: 10.4
---

# Serve and Funnel | Tailscale Explained

**[00:00](https://youtube.com/watch?v=MpxmfpCl20c&t=0s)** There have been plenty of times where I've had something on my local laptop that I've thought I wish I could just share it with that person on the other side of this room, without sending them a file over the internet or an email with a zip file or something like that. Well, using Tailscale serve as exactly what we can do. I can share something, a service or a file path or a folder or something on my local computer with anybody else on my tailnet. Now, that's pretty cool. But take it to another level and think, well, if I'm on a client,

**[00:30](https://youtube.com/watch?v=MpxmfpCl20c&t=30s)** meeting or something like that, reviewing a website design or something like that with somebody who's not in the same tailnet as me, wouldn't it be cool if I could temporarily share these assets over the public internet? Well, that's exactly what Tailscale funnel does. So, serve is local, anybody on your tailnet and funnel shares things over the internet.

**[00:50](https://youtube.com/watch?v=MpxmfpCl20c&t=50s)** In today's video, I'm going to go through a couple of basics of the Tailscale serve CLI interface as well as showing you how it integrates with our Visual Studio Code extension.

**[01:01](https://youtube.com/watch?v=MpxmfpCl20c&t=61s)** So, let's make a start with Tailscale serve. This lets you share a path on your file system or a service running on your box with anybody on your tailnet. It's contained privately within just your tailnet.

**[01:14](https://youtube.com/watch?v=MpxmfpCl20c&t=74s)** So, let's take a quick look at what we've got here. In this directory here, slash temp, serve demo, I have a little file called hello.text and literally all it says is hello.world.

**[01:27](https://youtube.com/watch?v=MpxmfpCl20c&t=87s)** Now, you could obviously extrapolate and think about what this was a real website, but let's pretend it is for today.

**[01:34](https://youtube.com/watch?v=MpxmfpCl20c&t=94s)** Let's do Tailscale serve and then all I need to do is pass in the file path or the folder path I want to share. You can think of this kind of like the Python HTTP web server.

**[01:44](https://youtube.com/watch?v=MpxmfpCl20c&t=104s)** Now, if I come over to this tab behind us and refresh the page, you can see that I've got a file listing of that directory and if I click on hello.text, it takes me immediately to hello.world.

**[01:56](https://youtube.com/watch?v=MpxmfpCl20c&t=116s)** I'm sure you can think of plenty of use cases where sharing a file listing of an entire directory with any other device on your tailnet which could include your phone, it could include a coworker, whatever.

**[02:07](https://youtube.com/watch?v=MpxmfpCl20c&t=127s)** I'm sure you could think of plenty of cases where that would be useful.

**[02:11](https://youtube.com/watch?v=MpxmfpCl20c&t=131s)** So, one of the changes we made in version.52 to how the command line interface works is we now run Tailscale serve in foreground by default.

**[02:19](https://youtube.com/watch?v=MpxmfpCl20c&t=139s)** Putting it in the background is nice and easy. So you can see, if I just run Tailscale serve right here, this command, this set of commands is now running in the foreground. I can't do anything else with my terminal.

**[02:29](https://youtube.com/watch?v=MpxmfpCl20c&t=149s)** Until I do a control seat exit that. Now, if I did a serve-bg, that puts the same command in the background.

**[02:40](https://youtube.com/watch?v=MpxmfpCl20c&t=160s)** So, if I wanted to have a quick look and see what's going on, I could do Tailscale serve status and this shows me what's going on here.

**[02:46](https://youtube.com/watch?v=MpxmfpCl20c&t=166s)** Now, if there's a situation where you think to yourself, right, I want to stop that. We can now do Tailscale serve, reset.

**[02:53](https://youtube.com/watch?v=MpxmfpCl20c&t=173s)** And again, we'll just check the status and there is now no serve conflict going on.

**[02:57](https://youtube.com/watch?v=MpxmfpCl20c&t=177s)** So those are the basics of Tailscale serve. Similar concepts apply to Tailscale follow in the command line as well.

**[03:03](https://youtube.com/watch?v=MpxmfpCl20c&t=183s)** But I wanted to show you how to use follow as part of the VS code extension we released in October. So let's jump into that.

**[03:10](https://youtube.com/watch?v=MpxmfpCl20c&t=190s)** Well, over here, I've got a static website. Now, this is built using an 11T framework, a static site generator framework.

**[03:18](https://youtube.com/watch?v=MpxmfpCl20c&t=198s)** And all I'm going to do here is do an MPM run start. So this is just running node package manager which builds the static website and then serves it on localhost8080.

**[03:28](https://youtube.com/watch?v=MpxmfpCl20c&t=208s)** And I'm going to show you that here. So localhost8080, I have a website running through node, nothing too clever there.

**[03:36](https://youtube.com/watch?v=MpxmfpCl20c&t=216s)** But this is where the Tailscale extension starts to get really interesting. So we've got this thing shared on our local computer, but we want to share it across the internet next.

**[03:47](https://youtube.com/watch?v=MpxmfpCl20c&t=227s)** So poor 8080 was started by node. Would you like to share this over the internet using funnel? And this is where it gets really cool.

**[03:55](https://youtube.com/watch?v=MpxmfpCl20c&t=235s)** So if I click on copy URL and then go here, we can see that this is now available on the public internet using this URL.

**[04:04](https://youtube.com/watch?v=MpxmfpCl20c&t=244s)** So I'm on 5G here on my phone, picture yourself being in an important business meeting where you're trying to do like a content review or something like that.

**[04:13](https://youtube.com/watch?v=MpxmfpCl20c&t=253s)** And you want to bring this up, you want to show this to your client, but you want to put it on the internet temporarily.

**[04:19](https://youtube.com/watch?v=MpxmfpCl20c&t=259s)** Well, that's exactly what funnel is for. And over here, you can see that I'm on 5G up in the corner, so it can't possibly be served over the local network in this house.

**[04:29](https://youtube.com/watch?v=MpxmfpCl20c&t=269s)** And there we go. I mean, I've got my awesombo.pangolin.tl net, you know, URL that's there. And I can go in and look at my blog and check out that I think I wish I could just change one little thing about it.

**[04:42](https://youtube.com/watch?v=MpxmfpCl20c&t=282s)** Maybe I could change the title of a day at the zoo. So let's go and do that. I'll just leave my phone up in the corner as I do that.

**[04:49](https://youtube.com/watch?v=MpxmfpCl20c&t=289s)** And look at the posts section, a day at the, let's say aquarium. Don't know why a pangolin would be at the aquarium, but there you go.

**[04:59](https://youtube.com/watch?v=MpxmfpCl20c&t=299s)** You can see the site rebuilding in real time and you saw my phone over the public internet, also update in real time with that change.

**[05:08](https://youtube.com/watch?v=MpxmfpCl20c&t=308s)** So you might be wondering how tail scale funnel works under the hood. When you turn it on for the first time, we create a public DNS record,

**[05:15](https://youtube.com/watch?v=MpxmfpCl20c&t=315s)** which is a combination of your tail net name in my case, Pango, Hyphen, Lin, and your machine name in my case, that's awesombo.

**[05:23](https://youtube.com/watch?v=MpxmfpCl20c&t=323s)** So you end up with a public facing URL. Now when someone visits that URL, they actually hit the tail scale relay servers.

**[05:33](https://youtube.com/watch?v=MpxmfpCl20c&t=333s)** Those relay servers then forward that traffic over TCP to your tail scale node, at which point your tail scale node itself terminates the TLS traffic.

**[05:42](https://youtube.com/watch?v=MpxmfpCl20c&t=342s)** This therefore guarantees that all of the traffic traversing any tail scale infrastructure is encrypted and we can't read any of it.

**[05:51](https://youtube.com/watch?v=MpxmfpCl20c&t=351s)** These relay nodes don't have direct access to your nodes. The only purpose they can serve is to send TCP traffic in or out of the nodes,

**[05:59](https://youtube.com/watch?v=MpxmfpCl20c&t=359s)** which is controlled by the tail scale client itself as to whether those requests get accepted or rejected.

**[06:05](https://youtube.com/watch?v=MpxmfpCl20c&t=365s)** And so that's just scratching the surface of the power of tail scale serve and funnel put together.

**[06:10](https://youtube.com/watch?v=MpxmfpCl20c&t=370s)** And let us know what you're doing with these tools in the comments down below. Maybe you're sharing a game serve with your friends or doing something even more interesting.

**[06:16](https://youtube.com/watch?v=MpxmfpCl20c&t=376s)** We'd love to hear from you. And until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
