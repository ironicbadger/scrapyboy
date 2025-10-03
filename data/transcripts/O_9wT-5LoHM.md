---
video_id: "O_9wT-5LoHM"
title: "Beszel - The easiest monitoring solution you've probably never heard of for Windows, Linux and Mac!"
description: "Beszel is a new, super lightweight and simple monitoring solution. In today's video, Alex will walk you through the process of setting up the Beszel Hub, adding it to your tailnet and monitoring serve..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-01-15"
duration_seconds: 2000
youtube_url: "https://www.youtube.com/watch?v=O_9wT-5LoHM"
thumbnail_url: "https://i.ytimg.com/vi/O_9wT-5LoHM/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:25:02.149274"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 6218
transcription_time_seconds: 52.8
---

# Beszel - The easiest monitoring solution you've probably never heard of for Windows, Linux and Mac!

**[00:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=0s)** They don't get me wrong. Sometimes Telegraph and Grafana and Prometheus and all of these

**[00:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=5s)** inflex DB, sometimes all of these heavyweight monitoring systems have a place. They are robust,

**[00:11](https://youtube.com/watch?v=O_9wT-5LoHM&t=11s)** they are battle-tested, and let's be honest, sometimes it can be really fun to know exactly

**[00:16](https://youtube.com/watch?v=O_9wT-5LoHM&t=16s)** nitty gritty details about your remote system. Sometimes though, all you want is a lightweight

**[00:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=21s)** dashboard to show you, well, this host has been using this much CPU today and has this much

**[00:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=26s)** disk space left and my hard drives are running at this temperature. If that sounds like you and

**[00:31](https://youtube.com/watch?v=O_9wT-5LoHM&t=31s)** you don't fancy setting up an entire stack of stuff, bezel might be what you've been looking for.

**[00:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=36s)** It's a lightweight, simple way of monitoring servers, not just Linux, but you can also run it

**[00:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=42s)** on Windows 2, I'll show you how to do that towards the end of the video, and also I'm going to

**[00:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=46s)** show you how to connect a remote proxmox system, in my case running in England, across the Atlantic

**[00:52](https://youtube.com/watch?v=O_9wT-5LoHM&t=52s)** ocean back here to Raleigh North Carolina, using nothing but tailscale with no ports open in your

**[00:57](https://youtube.com/watch?v=O_9wT-5LoHM&t=57s)** firewall. I'm Alex from tailscale, and today we're going to look at bezel. It's really easy to get

**[01:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=63s)** started with bezel, and thankfully it's completely self-hosted, it's completely free, and it supports

**[01:09](https://youtube.com/watch?v=O_9wT-5LoHM&t=69s)** a whole bunch of monitoring and alerting stuff too, so you can plug it into telegrams, slack,

**[01:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=75s)** discord, email, notify, like it's a whole bunch of stuff. Go take a look at the docs for yourself

**[01:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=81s)** if that sounds of interest to you, also cover the notification stuff at the end of the video briefly,

**[01:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=86s)** but essentially the thing that caught my attention about this project is just how lightweight it is.

**[01:31](https://youtube.com/watch?v=O_9wT-5LoHM&t=91s)** The agent uses about eight megabytes of RAM when it's in use, and the hub not much more than that.

**[01:37](https://youtube.com/watch?v=O_9wT-5LoHM&t=97s)** I can also plug it into OIDC, so you remember in a previous video I talked about TSIDP,

**[01:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=102s)** that's an OIDC provider, so you can actually authenticate to bezel using tailscale. I'm not going

**[01:47](https://youtube.com/watch?v=O_9wT-5LoHM&t=107s)** to show you how to do that today. What I am going to do, though, is show you how to configure bezel

**[01:51](https://youtube.com/watch?v=O_9wT-5LoHM&t=111s)** hub to run inside an LXC container on top of Proxmox using Docker. Also, I'm going to show you how to

**[01:57](https://youtube.com/watch?v=O_9wT-5LoHM&t=117s)** configure the binary agent on Linux and Windows 11.2 as a service. That's not as easy as you might

**[02:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=123s)** think, and then also we're going to configure Proxmox, like I talked about, across the Atlantic,

**[02:08](https://youtube.com/watch?v=O_9wT-5LoHM&t=128s)** so I can monitor servers no matter where they are in the world using bezel and tailscale.

**[02:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=135s)** So bezel works on the concept of like a hub and spoke type model, and being that I'm using

**[02:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=141s)** tailscales part of this solution, it doesn't actually matter where I run the centralized hub of bezel.

**[02:29](https://youtube.com/watch?v=O_9wT-5LoHM&t=149s)** So I'm going to run this on a Proxmox node in my little home lab cluster that I use for all of these

**[02:34](https://youtube.com/watch?v=O_9wT-5LoHM&t=154s)** demos. It's just running on one of those little Dell one-litre small form factor PCs. You don't

**[02:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=159s)** need anything super powerful to run bezel. It's one of my favorite things about the light weight

**[02:44](https://youtube.com/watch?v=O_9wT-5LoHM&t=164s)** ness of it. So you can see here, I've just got a standard sort of Proxmox cluster, nothing special

**[02:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=170s)** going on. I'm just going to create a very basic LXC container here. I'm going to run Docker inside

**[02:57](https://youtube.com/watch?v=O_9wT-5LoHM&t=177s)** the LXC container, and then spin up the bezel hub inside the LXC inside Docker. Too much

**[03:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=185s)** inception. I need a spinning top here, don't I? I think I'm in the real world anyway. So that's

**[03:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=190s)** what I'm going to do, and I will cut to after I've created the LXC. So now the LXC container is

**[03:16](https://youtube.com/watch?v=O_9wT-5LoHM&t=196s)** created. It's completely blank. There's no Docker on it. There's no tailscale in it or anything.

**[03:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=201s)** And I've just got this little helper script. I need curl for this of course, and Debian doesn't

**[03:25](https://youtube.com/watch?v=O_9wT-5LoHM&t=205s)** ship with curl because it's too bloaty. Let's see. Anyway, so what I want to show you is just a

**[03:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=212s)** little helper script. I've got over here at SH dot ktz dot me LXC.sh. Very basic. It's just

**[03:40](https://youtube.com/watch?v=O_9wT-5LoHM&t=220s)** copying the tailscale install script and the Docker install script. If you don't trust me to host

**[03:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=226s)** that script, you can go ahead and do your own thing. I'm just going to pipe that to SH and then let

**[03:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=230s)** that run in the background. So it's going to install Docker inside the LXC. It's also going to

**[03:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=235s)** install tailscale as well. So the end goal here for me at least is to have an environment where I have

**[04:01](https://youtube.com/watch?v=O_9wT-5LoHM&t=241s)** tailscale installed and Docker installed. That's because I'm going to use Docker to run the bezel

**[04:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=246s)** hub and then obviously tailscale to connect everything together. So all of the remote nodes that

**[04:12](https://youtube.com/watch?v=O_9wT-5LoHM&t=252s)** I'm going to be monitoring. The remote nodes reach out over SSH to the hub. They need to be

**[04:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=259s)** rootable between each other, which is why I'm installing tailscale everywhere I possibly can.

**[04:24](https://youtube.com/watch?v=O_9wT-5LoHM&t=264s)** Tailscale is now installed, but of course, because this is an LXC, we're going to need to add a

**[04:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=268s)** couple of extra permissions underneath. Obviously, if you're not running an LXC, this won't apply

**[04:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=273s)** to you. But in the tailscale documentation, you can see here there is a little, there's a couple of

**[04:40](https://youtube.com/watch?v=O_9wT-5LoHM&t=280s)** lines here that you need to modify in your LXC configuration. So I'm going to go to this file here,

**[04:45](https://youtube.com/watch?v=O_9wT-5LoHM&t=285s)** at CPVE, LXC and then the container number. So I'm going to get a shell on the Clarkson host. So the

**[04:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=294s)** XCPVE LXC100. I'm literally just going to add at the bottom these two lines and then just write that

**[05:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=303s)** file out. I'll do a PCT stop 100, which will stop the bezel hub container and then a PCT start 100,

**[05:12](https://youtube.com/watch?v=O_9wT-5LoHM&t=312s)** which will start the container. And that's just so it picks up the config changes, which allow it to

**[05:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=319s)** bind to the DevNet Tun device underneath. This is a containerized thing. Again, it's not a bezel

**[05:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=326s)** specific thing, but if you want to deploy tailscale inside an LXC, that's how you go about doing it.

**[05:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=332s)** Okay, so now if we go into our LXC container and do a tailscale up dash dash SSH,

**[05:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=339s)** tailscale demon is running and everybody is happy. So I'm going to copy my login URL right here.

**[05:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=346s)** It's going to ask me to sign in as usual with my tailscale authentication provider. I'm going

**[05:52](https://youtube.com/watch?v=O_9wT-5LoHM&t=352s)** to pick my standard demo Google account that I use for all of this stuff. And voila, bezel hub is

**[05:58](https://youtube.com/watch?v=O_9wT-5LoHM&t=358s)** now on my tailnet, as we can see here, fully qualified domain name of bezel hub dot in my case,

**[06:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=363s)** Velociraptor. Now, I'm aware I tell you this in every video, but I can't assume everybody watches

**[06:07](https://youtube.com/watch?v=O_9wT-5LoHM&t=367s)** every single video. So in the DNS tab of the tailscale interface, there is this option here,

**[06:13](https://youtube.com/watch?v=O_9wT-5LoHM&t=373s)** tailnet name. If you want a fancy slash funny name for your tailnet, we give everybody's

**[06:20](https://youtube.com/watch?v=O_9wT-5LoHM&t=380s)** tailnet a TS.net domain for free. You can roll your own name here. So if you want to come up with

**[06:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=388s)** something other than, I think my default is like tail, hold on a minute, let me go here. Yeah,

**[06:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=393s)** so my my default name was tail6e5bf, rolls right off the tongue. So what I wanted to do was use

**[06:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=401s)** the tailscale kind of name generator to come up with something I could actually say on camera

**[06:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=406s)** or memorize whatever you prefer. There's a whole long list of these names. Go ahead and roll

**[06:51](https://youtube.com/watch?v=O_9wT-5LoHM&t=411s)** yourself a DNS name. They're all free. Everybody gets one for free. The other thing you're going to want

**[06:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=415s)** to do is enable HTTPS certificates and magic DNS in order for all of the different layers of

**[07:02](https://youtube.com/watch?v=O_9wT-5LoHM&t=422s)** what we're about to do to work with TLS certificates and all the rest of it. So with that taken care of,

**[07:08](https://youtube.com/watch?v=O_9wT-5LoHM&t=428s)** we now have bezel hub LXC container on our tailnet. We're going to want to go ahead now and

**[07:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=435s)** create the bezel hub container itself. Now, according to the bezel documentation, there are two

**[07:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=441s)** ways to do this. One is to run the hub as a binary directly on the host. I'm deciding to issue

**[07:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=448s)** that option. I just prefer managing services in Docker. Your mileage may vary, but I just like the

**[07:34](https://youtube.com/watch?v=O_9wT-5LoHM&t=454s)** the ease with which I can manage services using Docker. It's just what I prefer. So that's

**[07:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=461s)** what I'm going to go ahead and do because this is my video. So they have a couple of options here.

**[07:48](https://youtube.com/watch?v=O_9wT-5LoHM&t=468s)** So the first one is basically a two in one file. We are just going to deploy just the hub inside

**[07:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=475s)** this LXC container. We're not going to do quite yet. Anyway, we'll get to it in a moment. We're not

**[08:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=480s)** going to deploy the agent just yet. So what we're going to want to do is modify this bezel service

**[08:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=485s)** definition so that we can put it on to our tailnet and lucky for you, dear viewer, I have a file

**[08:11](https://youtube.com/watch?v=O_9wT-5LoHM&t=491s)** just here which is going to allow us to drop the bezel hub directly onto our tailnet inside Docker.

**[08:18](https://youtube.com/watch?v=O_9wT-5LoHM&t=498s)** This is leveraging stuff that we've done previously on the channel. Docker deep dives all that

**[08:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=502s)** kind of stuff. There'll be links to the previous Docker videos I've done going into all of the

**[08:27](https://youtube.com/watch?v=O_9wT-5LoHM&t=507s)** nitty gritty details. But for today, if you just copy and paste this Docker file as Docker

**[08:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=512s)** compose file, you should be good to go. So we're spinning up two containers. Essentially,

**[08:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=516s)** this container is going to handle the attaching of bezel to our tailnet. And of course,

**[08:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=521s)** we have the bezel hub application itself. I'm going to copy and paste that entire file inside my

**[08:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=526s)** LXC container, which is running at bezel hub. I'm going to SSH root using tail scale SSH,

**[08:51](https://youtube.com/watch?v=O_9wT-5LoHM&t=531s)** now SSH keys required. Wow, chef's kiss. Okay, so I'm going to create myself a compose.yaml

**[08:59](https://youtube.com/watch?v=O_9wT-5LoHM&t=539s)** file. And I'm just going to simply copy and paste everything from VS code straight into here.

**[09:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=545s)** As a couple of other things, we're going to have to set up on the tailnet side. So we need to

**[09:09](https://youtube.com/watch?v=O_9wT-5LoHM&t=549s)** create a tag. Don't know if you noticed, but in the Docker compose file, there is a tag here called

**[09:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=554s)** bezel. And we can actually use something inside tail scales, ACL and grants features to limit

**[09:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=561s)** which nodes can see which other nodes. So there could be a situation where you have a remote

**[09:27](https://youtube.com/watch?v=O_9wT-5LoHM&t=567s)** monitoring node. And you think to yourself, well, I don't really want that seeing everything else

**[09:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=572s)** on my tailnet. And so by using these tags, we can limit the scope of the view of the world that

**[09:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=579s)** these things have. And then it just makes things a lot more secure. So let's go ahead and create

**[09:45](https://youtube.com/watch?v=O_9wT-5LoHM&t=585s)** that tag in our ACLs, first of all, it's straightforward enough to do. So all we want to do is literally

**[09:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=590s)** just create this line here of tag bezel. You can call the tag whatever you would like. Then the other

**[09:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=595s)** thing that we're going to want to do is go ahead and generate ourselves a orth client. So generating

**[10:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=600s)** an orth client has changed a little bit in recent weeks. We want to generate ourselves an orth

**[10:07](https://youtube.com/watch?v=O_9wT-5LoHM&t=607s)** key or more accurately. We want to create an orth token that's going to allow us to generate an

**[10:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=614s)** orth key or contain a boot to generate an orth key when the container starts. So all we need to

**[10:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=619s)** select is orth keys. And this is under our orth client. And then of course, add the tag that we

**[10:24](https://youtube.com/watch?v=O_9wT-5LoHM&t=624s)** want to put in here. So in my case, it's bezel. And then I'm going to just click generate client.

**[10:29](https://youtube.com/watch?v=O_9wT-5LoHM&t=629s)** I'm going to copy this secret into my compose.yaml file. And then the other thing that we have to do

**[10:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=636s)** before we press go is just verify that we have this bezel hub JSON file in place. So where are we

**[10:43](https://youtube.com/watch?v=O_9wT-5LoHM&t=643s)** looking for that at the moment? We are mounting a volume here. And this file will enable tailscale

**[10:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=649s)** serve. Tailscale service is a really easy way of think of it like a reverse proxy for your service

**[10:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=655s)** on your tailnet. Like you don't have to worry about spinning up a separate reverse proxy

**[10:59](https://youtube.com/watch?v=O_9wT-5LoHM&t=659s)** anywhere else. And you'll get a TLS certificate for your hub service. There's a couple of moving

**[11:04](https://youtube.com/watch?v=O_9wT-5LoHM&t=664s)** pieces I'm aware, but it is it is worth it. So in the Git repo, the company in Git repo,

**[11:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=670s)** which by the way, will include a snippet for the Docker compose file. I've just pasted for you.

**[11:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=675s)** I'll also include this little snippet. And this is really fun. This is the JSON output of tailscale

**[11:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=681s)** serve. So what we can do is feed that into the container and have the bezel hub show up on our

**[11:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=688s)** tailnet without doing any other configuration. It's all done completely programmatically. So

**[11:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=693s)** where do we need to put this file? Well, for today, at least my volumes are all referencing the

**[11:38](https://youtube.com/watch?v=O_9wT-5LoHM&t=698s)** print working directory file, which is slash root. So I'm going to do make dash p slash root.

**[11:47](https://youtube.com/watch?v=O_9wT-5LoHM&t=707s)** What else do we have bezel hub? And then tailscale slash config. And then in that directory that we

**[11:56](https://youtube.com/watch?v=O_9wT-5LoHM&t=716s)** just created, bezel hub, tailscale config, I am going to put bezel hub dot json bezel hub dot json

**[12:08](https://youtube.com/watch?v=O_9wT-5LoHM&t=728s)** boom. And so this is essentially going to proxy the port 8090 from inside the container out to

**[12:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=734s)** port 443 on our tailnet. And in the process, because TS net is owned by tailscale, we do a little

**[12:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=741s)** bit of magic behind the scenes to enable TLS certificates for free. So wish me luck. If I now

**[12:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=748s)** type a Docker compose up, hopefully this is going to pull the bezel hub image. It's also going to

**[12:35](https://youtube.com/watch?v=O_9wT-5LoHM&t=755s)** pull the tailscale image to and then it's going to add the two to our tailnet. And hopefully

**[12:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=761s)** everything will just work. So if we go back now to our tailscale admin console and view bezel hub,

**[12:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=769s)** we can see that that's on our tailnet as before. This of course is the LXC container. And then

**[12:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=774s)** the container itself bezel is right here. So now if I want to copy this fully qualified domain name,

**[13:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=780s)** if I just copy and paste that into my browser, you can see that I've got a full TLS certificate.

**[13:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=785s)** I've got a little padlock connection is secure. If we look at the certificate here, it's a

**[13:09](https://youtube.com/watch?v=O_9wT-5LoHM&t=789s)** let's encrypt certificate that was generated this morning. So I'm just going to go ahead and create

**[13:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=794s)** myself here a tail and scales gmail.com. This is where we can actually start getting into the

**[13:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=801s)** configuration of bezel itself now. Hooray. And we have a working hub. That's it. That's all it took.

**[13:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=808s)** So let's just recap the steps because I'm always aware that when I'm explaining things, it takes

**[13:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=813s)** a long time to explain what is it ostensibly just a two or three step process. So we created an

**[13:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=821s)** LXC. We updated the packages. We installed tail scale and then Docker as well inside the LXC.

**[13:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=829s)** Arguably you could get away with that installing tail scale inside the LXC, but I like to do that

**[13:53](https://youtube.com/watch?v=O_9wT-5LoHM&t=833s)** just because of tail scale ssh so I can get in there and do stuff. Once we had the bare, you know,

**[14:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=840s)** the bare necessities in place, thinking of a song now. Once we had the bare necessities in place

**[14:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=845s)** of tail scale and Docker inside the LXC, we modified a composed.yaml file such that we created

**[14:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=855s)** the TS auth the OAuth client on the tail scale side. We made sure our DNS was set up.

**[14:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=861s)** It's actually quite a few steps on there. And then we also made sure that our tail scale serve

**[14:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=866s)** configuration was in the right directory as well. And then we created it. It was as simple as that.

**[14:31](https://youtube.com/watch?v=O_9wT-5LoHM&t=871s)** Very, very straightforward 97 step process, but the upshot is we now have the bezel hub running.

**[14:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=879s)** Now we can start to connect different agents from across wherever your infrastructure is running.

**[14:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=886s)** So we're going to start just by monitoring these three proxmox hosts in the same land.

**[14:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=890s)** And then we'll do a couple of other more exciting things later on.

**[14:56](https://youtube.com/watch?v=O_9wT-5LoHM&t=896s)** Now the real fun can start. This is where we're going to start installing the agent on multiple

**[15:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=900s)** different operating systems. I'm going to focus primarily on Linux here. And we've already shown you

**[15:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=906s)** how to spin things up using Docker compose for the hub. So why don't we jump to installing the agent

**[15:13](https://youtube.com/watch?v=O_9wT-5LoHM&t=913s)** on top of a proxmox host and connect the bezel hub to an agent to start with. So in the bezel

**[15:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=919s)** documentation, there is an agent installation page. You can see that they support running the agent as

**[15:24](https://youtube.com/watch?v=O_9wT-5LoHM&t=924s)** both a Docker container and also a binary. Now I've kind of shown you the the gist of running a

**[15:31](https://youtube.com/watch?v=O_9wT-5LoHM&t=931s)** container, a bezel container through the hub already. So I'm going to deploy my first agent as

**[15:37](https://youtube.com/watch?v=O_9wT-5LoHM&t=937s)** a binary on top of proxmox on top of Clarkson, my primary host in this proxmox cluster.

**[15:43](https://youtube.com/watch?v=O_9wT-5LoHM&t=943s)** They've got a one line install script. There are a bunch of manual steps here if you would prefer,

**[15:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=949s)** but I'm lazy and I don't actually mind these one line is too much, especially where I'm doing

**[15:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=954s)** these demos. So I'm going to run this install agent script. Now and now it's going to ask me

**[16:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=960s)** from my SSH key. So I need to jump back to bezel back to my hub that we deployed earlier and click

**[16:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=966s)** on this button up here of add a system. So I'm going to call it Clarkson. And for the host or IP,

**[16:13](https://youtube.com/watch?v=O_9wT-5LoHM&t=973s)** I could use a tail scale IP or I could use in this case, the local LAN IP because it's rootable

**[16:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=979s)** on my sort of local LAN subnet. But just for the sake of argument, I am going to use the tail scale

**[16:25](https://youtube.com/watch?v=O_9wT-5LoHM&t=985s)** IP just to prove to you that that works. And I suppose in doing so it also shows that this host could

**[16:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=992s)** literally be anywhere in the world. I also need to make sure I select binary here too. I just

**[16:37](https://youtube.com/watch?v=O_9wT-5LoHM&t=997s)** nearly missed that. Now there is a one line option here of copy Linux command. I'm actually going to

**[16:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1002s)** do that and see what difference that makes to the install install command right here. Oh, I see

**[16:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=1009s)** so I just embedded the SSH key directly as an argument that it passes to the script. Nice.

**[16:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=1015s)** Okay, so now I've done that. It should just be hands-off keyboard time, apart from answering

**[17:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=1020s)** questions, daily updates for the agent. Yes, please. That sounds good. And now if we go back to bezel,

**[17:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=1026s)** it's already working. Goodness, I love this software. It's so many times where these things

**[17:12](https://youtube.com/watch?v=O_9wT-5LoHM&t=1032s)** are like these little gotchas and all that kind of stuff. But we can see here it's pulling in the

**[17:17](https://youtube.com/watch?v=O_9wT-5LoHM&t=1037s)** IP address, the tail scale IP address. Uptime is zero hours because I only rebooted it just before

**[17:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1042s)** I started recording. Kernel is a proxmox PVE kernel of 6.8 and here is the CPU. I told you it wasn't

**[17:29](https://youtube.com/watch?v=O_9wT-5LoHM&t=1049s)** a powerful system. A 6600 Ti5 CPU. And you can see here that it's just monitoring now quite a few

**[17:38](https://youtube.com/watch?v=O_9wT-5LoHM&t=1058s)** little things. It's picked up things like the NVMe sensors, the core temperatures of CPUs,

**[17:44](https://youtube.com/watch?v=O_9wT-5LoHM&t=1064s)** all that kind of stuff. Network bandwidth you can see is still pretty low. So we probably need

**[17:49](https://youtube.com/watch?v=O_9wT-5LoHM&t=1069s)** to let this run for a little while in order to have some actually useful stats. But in order to

**[17:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=1075s)** just give you some kind of an idea of the scaling you can get with bezel when you have it across

**[18:01](https://youtube.com/watch?v=O_9wT-5LoHM&t=1081s)** multiple different agents and different hosts and that kind of thing. Here's what my personal

**[18:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=1086s)** deployment of bezel looks like. So I'm going to go to the grid view here and you can see I've got

**[18:11](https://youtube.com/watch?v=O_9wT-5LoHM&t=1091s)** what's that? Six, seven hosts. Two of which happen to be the same. I'm going to get onto

**[18:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=1095s)** Windows in just a minute because there's a whole couple of extra steps to run a service on Windows

**[18:20](https://youtube.com/watch?v=O_9wT-5LoHM&t=1100s)** that is a barrel of laughs. But essentially, you can see I've got the home assistant plugin

**[18:25](https://youtube.com/watch?v=O_9wT-5LoHM&t=1105s)** turned on here. So you can monitor things like home assistant. There is an add-on for bezel in here.

**[18:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1110s)** So if I literally just search for bezel, I think I had to put a custom repository in. I won't get too

**[18:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=1116s)** much into the home assistant side of things in this video. But you can see there's a custom repo

**[18:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1122s)** here for the bezel agent on home assistant. I can monitor Linux hosts. Deep thought is another

**[18:47](https://youtube.com/watch?v=O_9wT-5LoHM&t=1127s)** proxmox host I have. Morphnix is a NixOS host that I'm monitoring. This is actually my primary media

**[18:53](https://youtube.com/watch?v=O_9wT-5LoHM&t=1133s)** server. So if I go back, I don't know, 24 hours, you can see last night, this is roundabout when we

**[19:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=1140s)** were watching some TV. You know, not a big spike or doing some downloads or something. Not a big

**[19:04](https://youtube.com/watch?v=O_9wT-5LoHM&t=1144s)** spike of stuff going on really. But I like that I can see what each of my different containers are

**[19:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1150s)** up to in terms of like their RAM usage. Over time, there's just some nice stuff in there.

**[19:16](https://youtube.com/watch?v=O_9wT-5LoHM&t=1156s)** This go through put again 120, I guess there was some kind of like a ZFS scrub going on or something

**[19:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1162s)** like that. It's just really nice to be able to spot these patterns. And you can see that all

**[19:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=1166s)** of my hard drives, for example, temperature wise, pretty, pretty stable. You can do things as well,

**[19:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=1173s)** like add and monitor extra file systems by passing extra environment variables to the agent,

**[19:40](https://youtube.com/watch?v=O_9wT-5LoHM&t=1180s)** either through a Docker containers environment variables or just setting them on the host itself.

**[19:45](https://youtube.com/watch?v=O_9wT-5LoHM&t=1185s)** So we're going to dig into documentation slightly over here and just take a look at the environment

**[19:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=1190s)** variables section. And you can see here are all the different things that you can configure,

**[19:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1194s)** all the different syspath for sensors and that kind of thing in case some certain things aren't

**[19:59](https://youtube.com/watch?v=O_9wT-5LoHM&t=1199s)** being picked up or indeed a white list of temperature sensors to monitor if too much stuff is

**[20:04](https://youtube.com/watch?v=O_9wT-5LoHM&t=1204s)** being picked up. But where it really started to peak my interest was GPU monitoring. Now I've got

**[20:11](https://youtube.com/watch?v=O_9wT-5LoHM&t=1211s)** a couple of Olama instances running in this house, just testing stuff again for this channel and

**[20:17](https://youtube.com/watch?v=O_9wT-5LoHM&t=1217s)** doing some stuff with home assistant and their LLM integrations. And you can see that bezel uses

**[20:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1222s)** Nvidia SMI to monitor Nvidia GPUs. Now my personal installation of bezel has a node in it called

**[20:31](https://youtube.com/watch?v=O_9wT-5LoHM&t=1231s)** NYX NV Lama. And this is a NYXOS host with an Nvidia GPU passed through to it on top of an AMD

**[20:37](https://youtube.com/watch?v=O_9wT-5LoHM&t=1237s)** Epic 7402 system that I have in my basement. And I wanted a way of monitoring the GPU power draw.

**[20:44](https://youtube.com/watch?v=O_9wT-5LoHM&t=1244s)** You can see that idle is sat right now at 15 watts give or take. And you can see it's just

**[20:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=1250s)** it's drawing 15 watts doing absolutely nothing at all. But we can see like if I want to you know

**[20:55](https://youtube.com/watch?v=O_9wT-5LoHM&t=1255s)** solve fizz buzz in TypeScript for example, it's now going to pull in my NYX NV Lama host is going to

**[21:07](https://youtube.com/watch?v=O_9wT-5LoHM&t=1267s)** be running fully locally using the latest LLM3.2 model. This is using Open Web UI which again is a

**[21:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=1274s)** bit of a departure from bezel. But I'm just trying to show you like if you put load on these things

**[21:18](https://youtube.com/watch?v=O_9wT-5LoHM&t=1278s)** you can actually see that you can monitor that in pretty much real time inside bezel. And you can

**[21:23](https://youtube.com/watch?v=O_9wT-5LoHM&t=1283s)** see that my A4000 GPU here has had some stuff come through on it. So I'm a huge fan of this bezel

**[21:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1290s)** agent. But where it gets interesting at least is how it picks up that Nvidia SMI path. So in my case

**[21:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=1299s)** I work with my good friend Claude to write a NYXOS module a very simple basic module for deploying

**[21:45](https://youtube.com/watch?v=O_9wT-5LoHM&t=1305s)** the bezel agent on top of NYX. If you're interested in that the source code will be linked in

**[21:50](https://youtube.com/watch?v=O_9wT-5LoHM&t=1310s)** the description down below. You have to make sure that your path includes Nvidia SMI. And the

**[21:56](https://youtube.com/watch?v=O_9wT-5LoHM&t=1316s)** way to do that for me at least in NYX was to include the current system bin path as part of my path

**[22:01](https://youtube.com/watch?v=O_9wT-5LoHM&t=1321s)** as part of the service configurations you can see here for the system D unit. This also applies

**[22:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=1326s)** to the Windows installation a little bit later on because in WSL2 Nvidia SMI isn't quite where

**[22:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=1334s)** bezel expected it to be. I'm connected in here to a Windows 11 desktop. This just so happens

**[22:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1342s)** to be my gaming desktop next door. And the reason I wanted to monitor it was because it's

**[22:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=1348s)** got an Nvidia 3080 in it. What I wanted to do was spin up bezel agent in WSL2 because that was

**[22:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=1356s)** the recommended way that the developer for bezel suggested we go about running bezel agent on

**[22:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1362s)** Windows. The downside of doing it in WSL2 though is that it's running inside a virtual machine

**[22:48](https://youtube.com/watch?v=O_9wT-5LoHM&t=1368s)** and as such the agent only has a view of the world that matches the view of the world that the

**[22:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1374s)** virtual machine has. So it's got the same limitations of CPU and of memory and all the rest of it.

**[23:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=1380s)** So whilst it does work under WSL2 and I've written a blog post explaining how to do it,

**[23:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=1385s)** I'm actually not going to show you how to do the WSL2 part today because I figured out how to compile

**[23:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1390s)** the native go binary for Windows and then you get all of the metrics from your Windows host

**[23:16](https://youtube.com/watch?v=O_9wT-5LoHM&t=1396s)** directly through into the agent as well. Now what I must say at the beginning of this is instructions

**[23:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1402s)** for both the WSL2 and the native Windows service compiled version are available on my personal blog

**[23:29](https://youtube.com/watch?v=O_9wT-5LoHM&t=1409s)** but you must proceed at your own risk because there is a GitHub issue on the project for bezel

**[23:35](https://youtube.com/watch?v=O_9wT-5LoHM&t=1415s)** stating that Windows Defender finds an issue with the agent.exe file once it's compiled.

**[23:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=1421s)** I didn't personally run into this issue but you might and I just want to you know in the interest

**[23:47](https://youtube.com/watch?v=O_9wT-5LoHM&t=1427s)** of full transparency in disclosure just say proceed at your own risk okay here be dragons.

**[23:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1434s)** Now compiling this is actually pretty straightforward if you've got access to a Linux box and of

**[23:59](https://youtube.com/watch?v=O_9wT-5LoHM&t=1439s)** course you're from Windows these days you do through WSL2 have access to a Linux box.

**[24:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=1445s)** So what we can do is well first of all we've got to make sure that we've got golang installed

**[24:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1450s)** on our Ubuntu desktop so pseudo apt install golang go I think is what it is. Yes already installed

**[24:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=1459s)** because I've already done it before I made the video but such is life. Next up we want to clone

**[24:23](https://youtube.com/watch?v=O_9wT-5LoHM&t=1463s)** the Git repo. Now the end result that I'm aiming for here is to be running the agent.exe file

**[24:29](https://youtube.com/watch?v=O_9wT-5LoHM&t=1469s)** as a native binary on the Windows host but running it as a Windows service and that was the tricky part

**[24:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=1476s)** for me that took a little bit of figuring out using something called NSSM non-socking service manager.

**[24:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1482s)** We'll get to that don't worry we will get there but in the meantime you need to compile the agent

**[24:48](https://youtube.com/watch?v=O_9wT-5LoHM&t=1488s)** for Windows so clone the Git repo go into the bezel directory and then you want to look for this

**[24:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1494s)** command next. We want to go into bezel bezel command agent so we're already inside bezel so

**[25:02](https://youtube.com/watch?v=O_9wT-5LoHM&t=1502s)** change directory into bezel command agent and then we need to compile it. So we're going to just

**[25:09](https://youtube.com/watch?v=O_9wT-5LoHM&t=1509s)** put these command line flags in place here go OS equals Windows the architecture is AMD 64

**[25:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=1515s)** couple of other build flags blah blah boring boring boring boring and this is going to compile now

**[25:20](https://youtube.com/watch?v=O_9wT-5LoHM&t=1520s)** if I look in this directory here we've just compiled the go code into an exe file which

**[25:27](https://youtube.com/watch?v=O_9wT-5LoHM&t=1527s)** I've ever seen now we can execute on Windows but how do we get it out of WSL 2 onto our Windows host

**[25:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=1533s)** well aha Microsoft thankfully made that pretty easy so if we look under mount c you can see that

**[25:40](https://youtube.com/watch?v=O_9wT-5LoHM&t=1540s)** we've just got our standard Windows file system just here so if I look under users Alex desktop

**[25:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=1546s)** I can list all the files that are on my desktop which means I can literally just copy

**[25:52](https://youtube.com/watch?v=O_9wT-5LoHM&t=1552s)** agent.exe out of there not CD I want copy copy agent.exe onto my desktop and now on my Windows

**[26:04](https://youtube.com/watch?v=O_9wT-5LoHM&t=1564s)** machine I should have agent.exe now the next step we're going to want to do is create a directory

**[26:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1570s)** under program files I just call by and bezel agent you can call it whatever you want and you can

**[26:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=1574s)** see I've actually got some previous stuff from where I was messing about you don't need half of

**[26:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=1579s)** this stuff you literally just need the agent. Okay once you've copied the agent file over into your

**[26:25](https://youtube.com/watch?v=O_9wT-5LoHM&t=1585s)** program files directory I'm not going to do that because mine's working just fine in the background

**[26:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1590s)** we need to go ahead and configure the nssm side of things so this is a super old project

**[26:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=1596s)** might honestly hadn't been to this website in maybe a decade or more and I'm not sure it's seen

**[26:41](https://youtube.com/watch?v=O_9wT-5LoHM&t=1601s)** any the website at least has seen any updates since then but it doesn't matter it still works

**[26:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=1606s)** so nssm I use chocolatey to manage packages on my windows hosts because I'm a Linux guy and I like

**[26:52](https://youtube.com/watch?v=O_9wT-5LoHM&t=1612s)** the command line so we go to power shell and then run as administrator and we can just do choco install

**[27:01](https://youtube.com/watch?v=O_9wT-5LoHM&t=1621s)** nssm and that's going to pull down the nssm binary for us and put it onto our path so now we can do things

**[27:08](https://youtube.com/watch?v=O_9wT-5LoHM&t=1628s)** like create services start them stop them all the rest of it and you can see in here that we have a

**[27:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=1634s)** very simple set of instructions to follow we're going to install a service named bezel agent pointing

**[27:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=1641s)** to the xe file that we just compiled and put into our program files directory obviously make sure

**[27:26](https://youtube.com/watch?v=O_9wT-5LoHM&t=1646s)** these paths match up with what you created a few moments ago and then in terms of what we want to

**[27:32](https://youtube.com/watch?v=O_9wT-5LoHM&t=1652s)** do for configuring the host itself within bezel we need to grab the ssh key the public ssh key from

**[27:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=1659s)** bezel so we would go to add system like this and then binary and we'd call this windows and I think in

**[27:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=1666s)** my case it's 7.54 I would copy the ssh key just here not the Linux command this time I'm going to

**[27:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1674s)** add this system you can see it's just called windows for right now but if I go back into my windows

**[27:59](https://youtube.com/watch?v=O_9wT-5LoHM&t=1679s)** app here what I'd want to do is run this nssm set bezel agent command and we're just basically setting

**[28:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=1685s)** an environment variable same as we would do with like a system d service or something like that

**[28:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1690s)** of key equals and then the ssh key and then we quite simply just start the bezel agent services

**[28:16](https://youtube.com/watch?v=O_9wT-5LoHM&t=1696s)** and that's that it should just pick it up right away and I'm not going to break my existing deployment

**[28:21](https://youtube.com/watch?v=O_9wT-5LoHM&t=1701s)** just for the sake of this demo because I don't have loads of windows systems in this house to

**[28:25](https://youtube.com/watch?v=O_9wT-5LoHM&t=1705s)** demonstrate this on but you can see that windows 11 is up I just turned it on a few minutes ago

**[28:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1710s)** before recording this segment which is why the graph was empty and you can see it picks up

**[28:35](https://youtube.com/watch?v=O_9wT-5LoHM&t=1715s)** everything I've got in there so I've got windows 11 desktop uptime is 44 hours even the most of

**[28:40](https://youtube.com/watch?v=O_9wT-5LoHM&t=1720s)** that was just spent in suspend and sleep mode here's the specific kernel build of windows that I'm

**[28:45](https://youtube.com/watch?v=O_9wT-5LoHM&t=1725s)** running and it's got a 9800 x3d in it and then if we scroll down we can see that the GPU

**[28:53](https://youtube.com/watch?v=O_9wT-5LoHM&t=1733s)** power drawer is picked up so it's using the native Nvidia tooling to pick up some of the GPU

**[28:58](https://youtube.com/watch?v=O_9wT-5LoHM&t=1738s)** metrics and that kind of thing I'm actually going to amazed that this is working hog hog warts legacy

**[29:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=1743s)** over windows remote desktop of all things I'm not even doing anything fancy like moon lights or

**[29:08](https://youtube.com/watch?v=O_9wT-5LoHM&t=1748s)** anything like that so the general point though is just to show you that you know I've put some load

**[29:12](https://youtube.com/watch?v=O_9wT-5LoHM&t=1752s)** on the GPU and you can see that CPU's gone up memories gone up a little bit this guy out all

**[29:18](https://youtube.com/watch?v=O_9wT-5LoHM&t=1758s)** that kind of stuff but GPU power drawer now is starting to get where we would expect it to be running

**[29:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1762s)** a AAA title these days so for me I think bezel is really useful across multiple operating systems

**[29:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1770s)** and there are ways to run bezel with launch d on macOS as well which I won't get into today

**[29:35](https://youtube.com/watch?v=O_9wT-5LoHM&t=1775s)** because it's a pain to be honest but it does work um so you know the the gist of bezel here is that

**[29:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1782s)** you could create a very lightweight way of monitoring your entire tailnet using nothing

**[29:48](https://youtube.com/watch?v=O_9wT-5LoHM&t=1788s)** but a very simple you know couple of commands to add things via the tailnet using the public ssh

**[29:54](https://youtube.com/watch?v=O_9wT-5LoHM&t=1794s)** key authentication model that it uses to talk between the agent and the hub and so in situations where

**[30:00](https://youtube.com/watch?v=O_9wT-5LoHM&t=1800s)** something like maybe Prometheus and Grafana is a bit too heavy weight for you or something like net data

**[30:06](https://youtube.com/watch?v=O_9wT-5LoHM&t=1806s)** might be a bit too big and a bit too heavy bezel is the perfect situation like it's it's a beautiful

**[30:12](https://youtube.com/watch?v=O_9wT-5LoHM&t=1812s)** middle ground between uptime kuma which is just monitoring things like a ping pong web request

**[30:19](https://youtube.com/watch?v=O_9wT-5LoHM&t=1819s)** and that kind of stuff although uptime kuma's awesome in its own right this is much more useful

**[30:24](https://youtube.com/watch?v=O_9wT-5LoHM&t=1824s)** for monitoring things like system stats like you can see like GPU power drawer temperature

**[30:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=1828s)** disc temperatures whether your fast system fills up and all that kind of stuff and I haven't even

**[30:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=1833s)** touched upon any of the notification features that bezel offers either it supports this shelter

**[30:39](https://youtube.com/watch?v=O_9wT-5LoHM&t=1839s)** library which supports as you can see notifications for discord email if this then that matter

**[30:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=1846s)** most notify that's great because that's another self hosted so you can keep it completely

**[30:51](https://youtube.com/watch?v=O_9wT-5LoHM&t=1851s)** the self hosted notifications stacks you can keep everything in house if you need to slack as well

**[30:57](https://youtube.com/watch?v=O_9wT-5LoHM&t=1857s)** telegram my goodness um this tool is legit and I think bezel is going to become a real part of my

**[31:04](https://youtube.com/watch?v=O_9wT-5LoHM&t=1864s)** arsenal moving forward so as you can see it's a really quick and easy way to monitor multiple hosts

**[31:10](https://youtube.com/watch?v=O_9wT-5LoHM&t=1870s)** across not just your land but also your tail net too and again just look how easy this is to add a

**[31:15](https://youtube.com/watch?v=O_9wT-5LoHM&t=1875s)** new host this host is in England I'm in North Carolina and we're going to add a host on the other side

**[31:22](https://youtube.com/watch?v=O_9wT-5LoHM&t=1882s)** of the Atlantic to bezel in a couple of minutes so I'm going to go in here I'm going to name

**[31:28](https://youtube.com/watch?v=O_9wT-5LoHM&t=1888s)** this snowball which is the name of the host I'm going to go into my tail net and grab the

**[31:33](https://youtube.com/watch?v=O_9wT-5LoHM&t=1893s)** IP of snowball so snowball is over here and I'm going to do this I'm going to copy 100 dot whatever

**[31:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1902s)** put that in here copy the Linux command and then I'm going to go to my terminal window and just

**[31:46](https://youtube.com/watch?v=O_9wT-5LoHM&t=1906s)** copy and paste the install agent script in here and I'm going to add a host on the other side of

**[31:52](https://youtube.com/watch?v=O_9wT-5LoHM&t=1912s)** the world to bezel using tail scale in how long was that like 30 seconds so there we are I have

**[31:58](https://youtube.com/watch?v=O_9wT-5LoHM&t=1918s)** just added a host on the other side of the Atlantic to my bezel hub using tail scale as a

**[32:05](https://youtube.com/watch?v=O_9wT-5LoHM&t=1925s)** connecting fabric as almost those two hosts can actually see each other you know they're both

**[32:09](https://youtube.com/watch?v=O_9wT-5LoHM&t=1929s)** on the same tail net and are rootable so you can check that with tail scale ping on the command line

**[32:14](https://youtube.com/watch?v=O_9wT-5LoHM&t=1934s)** make sure you've not got any ACLs or grants in the way to prevent them from seeing each other

**[32:18](https://youtube.com/watch?v=O_9wT-5LoHM&t=1938s)** it's very easily done once you start messing around with those things those two hosts can now see

**[32:23](https://youtube.com/watch?v=O_9wT-5LoHM&t=1943s)** each other and my bezel hub can now monitor that remote Linux host in England with no firewall rules

**[32:30](https://youtube.com/watch?v=O_9wT-5LoHM&t=1950s)** open or any other configuration reasons like this think projects like this are just why this job

**[32:36](https://youtube.com/watch?v=O_9wT-5LoHM&t=1956s)** for me is so easy because I find this stuff really fun just connecting stuff together that perhaps

**[32:42](https://youtube.com/watch?v=O_9wT-5LoHM&t=1962s)** shouldn't be talking to each other using bezel like a now monitor this host remotely and I didn't

**[32:47](https://youtube.com/watch?v=O_9wT-5LoHM&t=1967s)** have to really do a whole bunch to make that happen just ah it's so cliche it sounds so

**[32:53](https://youtube.com/watch?v=O_9wT-5LoHM&t=1973s)** cheeseball but I love tail scale so a big thank you to those of you that have made it to the end

**[32:58](https://youtube.com/watch?v=O_9wT-5LoHM&t=1978s)** of this rather long video today and until next time thank you so much for watching I hope you have a

**[33:03](https://youtube.com/watch?v=O_9wT-5LoHM&t=1983s)** wonderful 2025 I've been Alex from tail scale

---

*Automatically generated transcript. May contain errors.*
