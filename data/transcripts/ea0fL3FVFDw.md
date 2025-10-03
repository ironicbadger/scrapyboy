---
video_id: "ea0fL3FVFDw"
title: "Tailscale Up: All the buttons"
description: "This talk was given by Emily Trau at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 1145
youtube_url: "https://www.youtube.com/watch?v=ea0fL3FVFDw"
thumbnail_url: "https://i.ytimg.com/vi_webp/ea0fL3FVFDw/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:02:50.517921"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2214
transcription_time_seconds: 24.2
---

# Tailscale Up: All the buttons

**[00:00](https://youtube.com/watch?v=ea0fL3FVFDw&t=0s)** Is titled All the Buttons Abusing Features Old, New, and Unreleased. So, a little bit

**[00:07](https://youtube.com/watch?v=ea0fL3FVFDw&t=7s)** about me. I'm 22. I'm from Melbourne. And nowadays, I'm nowhere. I do a little bit of security

**[00:17](https://youtube.com/watch?v=ea0fL3FVFDw&t=17s)** research, as mentioned, but I work on just open-source projects a lot of nix packages lately.

**[00:27](https://youtube.com/watch?v=ea0fL3FVFDw&t=27s)** And those are my social media. But the project that I'm, oh, sorry, talking about today,

**[00:37](https://youtube.com/watch?v=ea0fL3FVFDw&t=37s)** is coming from my experience last year when I went to Athens and participated in the

**[00:47](https://youtube.com/watch?v=ea0fL3FVFDw&t=47s)** International Cybersecurity Challenge. We had 115 people from seven teams around the

**[00:56](https://youtube.com/watch?v=ea0fL3FVFDw&t=56s)** world come together and compete over two days in this cyber security game. And it was

**[01:11](https://youtube.com/watch?v=ea0fL3FVFDw&t=71s)** just super fun. One of the games was Attack Defense. So, in Attack Defense, we have this

**[01:20](https://youtube.com/watch?v=ea0fL3FVFDw&t=80s)** hyper-fetical situation. Let's say that you're an ops engineer and you have a product. And you've

**[01:29](https://youtube.com/watch?v=ea0fL3FVFDw&t=89s)** just been told that, hey, suddenly we have all of these attackers coming at it. And, well, you don't

**[01:37](https://youtube.com/watch?v=ea0fL3FVFDw&t=97s)** know what's wrong. You just know that there are people actively trying to exploit your app. Now,

**[01:46](https://youtube.com/watch?v=ea0fL3FVFDw&t=106s)** what your job is is to try and figure out what's going on, how they're getting in and try and patch

**[01:58](https://youtube.com/watch?v=ea0fL3FVFDw&t=118s)** up your code that you've been given. That's got a few vulnerabilities in it to try and make it safe

**[02:07](https://youtube.com/watch?v=ea0fL3FVFDw&t=127s)** again. The twist being, also, at the same time, your teammates are working on the other side of

**[02:14](https://youtube.com/watch?v=ea0fL3FVFDw&t=134s)** the fence. They are the attackers. They are trying to break into every other team's app. Everyone has

**[02:24](https://youtube.com/watch?v=ea0fL3FVFDw&t=144s)** identical apps that they've hosted up. And so, for every vulnerability, you find every point you

**[02:33](https://youtube.com/watch?v=ea0fL3FVFDw&t=153s)** score, every team you hack, you get points, and you lose points when you get hacked. Also, most

**[02:42](https://youtube.com/watch?v=ea0fL3FVFDw&t=162s)** importantly, you must remain up. You can't let your app go down for even a second, or you're deeply,

**[02:52](https://youtube.com/watch?v=ea0fL3FVFDw&t=172s)** deeply penalized on the scoreboard. So, yeah, all fun and games, I'm sure it's never happened to

**[02:58](https://youtube.com/watch?v=ea0fL3FVFDw&t=178s)** anybody in real life. So, yeah, this is the scoreboard app from last year, and you can see how all the

**[03:22](https://youtube.com/watch?v=ea0fL3FVFDw&t=202s)** different teams were tracking at this moment. So, this goes for a couple hours. It's really quite a

**[03:30](https://youtube.com/watch?v=ea0fL3FVFDw&t=210s)** high pressure situation, and it's just a lot of fun. So, when I went home, I decided that I wanted to

**[03:39](https://youtube.com/watch?v=ea0fL3FVFDw&t=219s)** kind of recreate this, to replicate this game, and because I love tail scale, I want to do it all with

**[03:49](https://youtube.com/watch?v=ea0fL3FVFDw&t=229s)** tail scale, and at the same time, make it the best, most intuitive user-friendly experience that

**[03:57](https://youtube.com/watch?v=ea0fL3FVFDw&t=237s)** you can have. Yeah, so, this is not a very simple system. So, this is sort of how the network was

**[04:14](https://youtube.com/watch?v=ea0fL3FVFDw&t=254s)** set up on the day. So, you can see there's multiple different subnets. Every single player gets given

**[04:24](https://youtube.com/watch?v=ea0fL3FVFDw&t=264s)** a username and password for the scoreboard. They get given a wireguard key to go into the network,

**[04:30](https://youtube.com/watch?v=ea0fL3FVFDw&t=270s)** and they're also given an API key so that they can write scripts to talk to the scoreboard. This

**[04:35](https://youtube.com/watch?v=ea0fL3FVFDw&t=275s)** is all information that has to be emailed to the players beforehand that they have to test that

**[04:42](https://youtube.com/watch?v=ea0fL3FVFDw&t=282s)** it works. Each of the virtual machines have a vulnerable application. They're set up so that

**[04:52](https://youtube.com/watch?v=ea0fL3FVFDw&t=292s)** only the teams themselves can access it until the game starts, and which it's a complete

**[04:57](https://youtube.com/watch?v=ea0fL3FVFDw&t=297s)** free for all. Just to make sure that the game's place fair, you have this router in the middle

**[05:08](https://youtube.com/watch?v=ea0fL3FVFDw&t=308s)** that makes it so that any data that gets up to the virtual machines is completely anonymized.

**[05:15](https://youtube.com/watch?v=ea0fL3FVFDw&t=315s)** It hides all of the IP addresses using a source NAT so that you can't just easily say,

**[05:24](https://youtube.com/watch?v=ea0fL3FVFDw&t=324s)** hey, I can see all of my attackers are coming from this place in that place. So, this is kind of the

**[05:28](https://youtube.com/watch?v=ea0fL3FVFDw&t=328s)** network that we are trying to replicate. Do it better. So, now I'm going to go into a bunch of

**[05:36](https://youtube.com/watch?v=ea0fL3FVFDw&t=336s)** demos, so wish me luck. First off, with tail scale, we don't have to make user names and

**[05:55](https://youtube.com/watch?v=ea0fL3FVFDw&t=355s)** passwords for everybody. We don't have to give them a password to a VM or take their SSH keys.

**[06:03](https://youtube.com/watch?v=ea0fL3FVFDw&t=363s)** We can just invite them to a tailnet. In this case, it could be through a GitHub organization

**[06:08](https://youtube.com/watch?v=ea0fL3FVFDw&t=368s)** that I've made. Once users are on the tailnet, we can put them into groups and use access control

**[06:16](https://youtube.com/watch?v=ea0fL3FVFDw&t=376s)** lists to control who can talk to shoe. You can make it so that if you're on the same team,

**[06:24](https://youtube.com/watch?v=ea0fL3FVFDw&t=384s)** you can connect directly to each other, share files, have complete freedom, but tightly control

**[06:32](https://youtube.com/watch?v=ea0fL3FVFDw&t=392s)** what other devices that you can talk to. This is all completely invisible to the end user.

**[06:43](https://youtube.com/watch?v=ea0fL3FVFDw&t=403s)** As an end user, if I just say I want to SH as root into my team's box, let's say I'm on

**[06:51](https://youtube.com/watch?v=ea0fL3FVFDw&t=411s)** team Oshania, I can just do a section to Oshania, and I think it's crossed. There you go. We're into

**[07:07](https://youtube.com/watch?v=ea0fL3FVFDw&t=427s)** our team's unique virtual machine, and this is pretty automatic. I didn't need to be given

**[07:17](https://youtube.com/watch?v=ea0fL3FVFDw&t=437s)** any passwords or keys or anything. It's all no masks, no fuss. You just download tail scale and

**[07:23](https://youtube.com/watch?v=ea0fL3FVFDw&t=443s)** login, and it works perfectly first try, which is amazing for a user experience, especially if you

**[07:36](https://youtube.com/watch?v=ea0fL3FVFDw&t=456s)** have to muck around with wire guard and Linux networking, and all that tailscale can just

**[07:43](https://youtube.com/watch?v=ea0fL3FVFDw&t=463s)** wash it all away. The next thing that we can do is that scoreboard that you showed earlier.

**[08:05](https://youtube.com/watch?v=ea0fL3FVFDw&t=485s)** This is actually my clone of it, and you can see here that I'm running it on a tailscale address. This

**[08:15](https://youtube.com/watch?v=ea0fL3FVFDw&t=495s)** is using tailscale HTTPS certificates, and that up there is actually a funnel address. What should

**[08:26](https://youtube.com/watch?v=ea0fL3FVFDw&t=506s)** happen is I was testing this, and I don't think it's working right now, but if you go to this,

**[08:32](https://youtube.com/watch?v=ea0fL3FVFDw&t=512s)** this would be a public scoreboard, so any observers can keep tabs on the game and see what's happening,

**[08:41](https://youtube.com/watch?v=ea0fL3FVFDw&t=521s)** but at the same time, through only logging into the tailnet, you don't have to sign in with

**[08:48](https://youtube.com/watch?v=ea0fL3FVFDw&t=528s)** username password, you don't even have to sign in with your single sign-on provider, simply just

**[08:54](https://youtube.com/watch?v=ea0fL3FVFDw&t=534s)** being on the tailnet. Let's our scoreboard know who we are. You can see in the bottom right corner,

**[09:00](https://youtube.com/watch?v=ea0fL3FVFDw&t=540s)** it's got my name and picture right there. Teams can then just use a scoreboard. They don't have

**[09:08](https://youtube.com/watch?v=ea0fL3FVFDw&t=548s)** to log in when they write their apps and scripts to interact with this. They don't need API keys.

**[09:15](https://youtube.com/watch?v=ea0fL3FVFDw&t=555s)** It all just works, because the scoreboard is smart enough to see exactly who you are.

**[09:21](https://youtube.com/watch?v=ea0fL3FVFDw&t=561s)** As you mentioned in a talk earlier, this is really not all because this is the first time

**[09:36](https://youtube.com/watch?v=ea0fL3FVFDw&t=576s)** I'm either able to have a service that is both internal that I can access through a VPN and do all

**[09:44](https://youtube.com/watch?v=ea0fL3FVFDw&t=584s)** these privileged actions like have my admin interface. At the same time, serving a copy of that,

**[09:51](https://youtube.com/watch?v=ea0fL3FVFDw&t=591s)** that's just read-only and public that for the whole intensity. The coolest part is it's both

**[09:58](https://youtube.com/watch?v=ea0fL3FVFDw&t=598s)** at the same address. You don't need to say, hey, use this address for when you're on the VPN,

**[10:05](https://youtube.com/watch?v=ea0fL3FVFDw&t=605s)** but use this if you want to see it publicly. The user just sees, hey, I'll just go to this one

**[10:10](https://youtube.com/watch?v=ea0fL3FVFDw&t=610s)** website and I can do everything there, which is, yeah, I'm a really big fan that tailscale lets you

**[10:19](https://youtube.com/watch?v=ea0fL3FVFDw&t=619s)** do that. Now, when I was implementing this a few months ago, it wasn't completely bum-free, so

**[10:38](https://youtube.com/watch?v=ea0fL3FVFDw&t=638s)** funnel is sort of a new thing and tailscale off, which I'm using here to try and figure out who's

**[10:48](https://youtube.com/watch?v=ea0fL3FVFDw&t=648s)** who, is a little bit of a niche feature. So when I was combining the two, I actually ran into a

**[10:57](https://youtube.com/watch?v=ea0fL3FVFDw&t=657s)** little bit of technical problems, especially because this is not a go app, this is a dinner app,

**[11:04](https://youtube.com/watch?v=ea0fL3FVFDw&t=664s)** and so I'm actually not able to use TSnet here. So I actually have to go into the tailscale client

**[11:12](https://youtube.com/watch?v=ea0fL3FVFDw&t=672s)** and sort of do a little cheeky hack to just to get this to work, but hopefully that can all get,

**[11:21](https://youtube.com/watch?v=ea0fL3FVFDw&t=681s)** that was all smoothed out now. But it did show me that, say, it's surprisingly easy and approachable,

**[11:30](https://youtube.com/watch?v=ea0fL3FVFDw&t=690s)** if tailscale needs to do a little bit more than you want to dive into the open source code on

**[11:38](https://youtube.com/watch?v=ea0fL3FVFDw&t=698s)** GitHub and just play around with it. I'm not a go engineer, I wouldn't say that I know any go,

**[11:45](https://youtube.com/watch?v=ea0fL3FVFDw&t=705s)** but I managed to do enough to get it to work for me, and that's fantastic. Can't say that about

**[11:52](https://youtube.com/watch?v=ea0fL3FVFDw&t=712s)** every product, but yeah, that's a really great thing that I really appreciate being able to do.

**[12:05](https://youtube.com/watch?v=ea0fL3FVFDw&t=725s)** Then one last thing that I want to highlight with this network that we want to replicate,

**[12:14](https://youtube.com/watch?v=ea0fL3FVFDw&t=734s)** a very important feature of it to actually, that makes the game work, is this router that can do

**[12:19](https://youtube.com/watch?v=ea0fL3FVFDw&t=739s)** that IP anonymization. It can actually hide all of where the traffic's coming from.

**[12:27](https://youtube.com/watch?v=ea0fL3FVFDw&t=747s)** Now, how do we bring that into the world of tailscale? The concept of anonymous

**[12:33](https://youtube.com/watch?v=ea0fL3FVFDw&t=753s)** tailnets, nodes that can talk to each other and send traffic, but without knowing who each other

**[12:40](https://youtube.com/watch?v=ea0fL3FVFDw&t=760s)** are. This is kind of a contradiction. Tailscale is a peer-to-peer network. It's

**[12:47](https://youtube.com/watch?v=ea0fL3FVFDw&t=767s)** for humans making connections, so we're reaching a little bit outside of the bounds of where

**[12:53](https://youtube.com/watch?v=ea0fL3FVFDw&t=773s)** you'd normally go here, but it does work if you are interpret the rules a little generously.

**[13:07](https://youtube.com/watch?v=ea0fL3FVFDw&t=787s)** There is one feature that tailscale has built in that allows you to aggregate traffic,

**[13:15](https://youtube.com/watch?v=ea0fL3FVFDw&t=795s)** that lets you take requests from a whole bunch of different users and push them through one

**[13:22](https://youtube.com/watch?v=ea0fL3FVFDw&t=802s)** place. That's the subnet router. In fact, the subnet router lets you have a device on another

**[13:31](https://youtube.com/watch?v=ea0fL3FVFDw&t=811s)** network that's not on tailscale and that you can then expose to your tailnet and have all of

**[13:37](https://youtube.com/watch?v=ea0fL3FVFDw&t=817s)** your traffic when you go to the route through tailscale automatically. While it's doing this,

**[13:44](https://youtube.com/watch?v=ea0fL3FVFDw&t=824s)** it's also acting as a NAT. It's rewriting all of the traffic so it comes from the router's

**[13:53](https://youtube.com/watch?v=ea0fL3FVFDw&t=833s)** IP address, and it's just sending it through. This is just things that a normal subnet router is

**[13:57](https://youtube.com/watch?v=ea0fL3FVFDw&t=837s)** doing automatically for you that you may not have known. If we get a little bit generous,

**[14:05](https://youtube.com/watch?v=ea0fL3FVFDw&t=845s)** what if we don't make just any old subnet? Tailscale has

**[14:13](https://youtube.com/watch?v=ea0fL3FVFDw&t=853s)** formed millions of IP addresses. They're all randomly generated and assigned,

**[14:20](https://youtube.com/watch?v=ea0fL3FVFDw&t=860s)** and so what if we could make a subnet over every single one of those millions of IP addresses,

**[14:32](https://youtube.com/watch?v=ea0fL3FVFDw&t=872s)** then if this subnet router advertised every single tailscale IP and you went to that new IP

**[14:42](https://youtube.com/watch?v=ea0fL3FVFDw&t=882s)** address, it would route all your tailscale traffic through it and it would be completely anonymous.

**[14:47](https://youtube.com/watch?v=ea0fL3FVFDw&t=887s)** So what I actually did was I can show you in this dashboard. You can see here are the subnet

**[14:57](https://youtube.com/watch?v=ea0fL3FVFDw&t=897s)** router that I'm advertising. This big whopping subnet on IPv6. So basically every address in here

**[15:11](https://youtube.com/watch?v=ea0fL3FVFDw&t=911s)** gets automatically mapped to a tailscale address and it gets anonymized. The demo here,

**[15:18](https://youtube.com/watch?v=ea0fL3FVFDw&t=918s)** I can refresh this. This is just a hollow-world service running on TSNET. If I use this IP address

**[15:27](https://youtube.com/watch?v=ea0fL3FVFDw&t=927s)** and I transform and get the equivalent IPv6 and I refresh it, you can see that even though I'm

**[15:36](https://youtube.com/watch?v=ea0fL3FVFDw&t=936s)** sending the traffic from my laptop, it gets automatically, completely anonymized. That's

**[15:49](https://youtube.com/watch?v=ea0fL3FVFDw&t=949s)** how you make tailscale networks that don't know who each other are.

**[15:55](https://youtube.com/watch?v=ea0fL3FVFDw&t=955s)** There is one more thing that I don't know if it will work.

**[16:10](https://youtube.com/watch?v=ea0fL3FVFDw&t=970s)** We have another user interface problem because we've just given every single device a second IP

**[16:16](https://youtube.com/watch?v=ea0fL3FVFDw&t=976s)** address. You can see up there, like each virtual machine already has an IP address that if you're

**[16:21](https://youtube.com/watch?v=ea0fL3FVFDw&t=981s)** connecting into a using tailscale SSH, that's perfect. But now we've just given a second one

**[16:28](https://youtube.com/watch?v=ea0fL3FVFDw&t=988s)** that we want to give out. And it's a little bit. I don't quite love it if I have to say,

**[16:34](https://youtube.com/watch?v=ea0fL3FVFDw&t=994s)** hey, use this IPv4 if you're connecting your own one, but use this completely random IPv6

**[16:42](https://youtube.com/watch?v=ea0fL3FVFDw&t=1002s)** if you're connecting to another team. So instead, what I did was I made the DNS server that lies to you.

**[16:52](https://youtube.com/watch?v=ea0fL3FVFDw&t=1012s)** So here you can see, if I look up Oshania, okay, I'm getting this from our regular normal tailscale

**[17:14](https://youtube.com/watch?v=ea0fL3FVFDw&t=1034s)** IP address, but here I have, this machine is on another team. So imagine this is a second

**[17:35](https://youtube.com/watch?v=ea0fL3FVFDw&t=1055s)** team's machine. And so the other team is on this. But if I try and connect into the team Oshania

**[17:44](https://youtube.com/watch?v=ea0fL3FVFDw&t=1064s)** server now, oh no, this should, sorry for the demo, but this should give that IPv6 address instead.

**[17:59](https://youtube.com/watch?v=ea0fL3FVFDw&t=1079s)** And what's this, how this is happening is I have a TSnet DNS server. This is something that you

**[18:06](https://youtube.com/watch?v=ea0fL3FVFDw&t=1086s)** can do if you've been keeping careful attention on the tailscale source code. But you can now run

**[18:11](https://youtube.com/watch?v=ea0fL3FVFDw&t=1091s)** UDP services over TSnet. So I've written a TSnet DNS server that when a client asks it, hey, what's

**[18:22](https://youtube.com/watch?v=ea0fL3FVFDw&t=1102s)** the IP address of this host name? It actually checks which client it's is making the request, whether

**[18:29](https://youtube.com/watch?v=ea0fL3FVFDw&t=1109s)** you're on that team or not. And if you are, it gives you the real one, if it's not, it gives you the

**[18:35](https://youtube.com/watch?v=ea0fL3FVFDw&t=1115s)** mask one. So as a user, this whole subnet is completely invisible. This whole subnet router is

**[18:43](https://youtube.com/watch?v=ea0fL3FVFDw&t=1123s)** completely invisible to you. You can just use the one source of truth host name to do all of the

**[18:50](https://youtube.com/watch?v=ea0fL3FVFDw&t=1130s)** actions. And yeah, I think that's like really great. And yeah, thank you.

---

*Automatically generated transcript. May contain errors.*
