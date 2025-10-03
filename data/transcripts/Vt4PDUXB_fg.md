---
video_id: "Vt4PDUXB_fg"
title: "Remotely access and share your self-hosted services"
description: "We're going to use Tailscale and the reverse proxy Caddy to share self-hosted services on your Tailnet with friends and family.

Personal accounts are always free on Tailscale and can include up to 3 ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-03-08"
duration_seconds: 1084
youtube_url: "https://www.youtube.com/watch?v=Vt4PDUXB_fg"
thumbnail_url: "https://i.ytimg.com/vi/Vt4PDUXB_fg/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:15:51.604461"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3586
transcription_time_seconds: 31.8
---

# Remotely access and share your self-hosted services

**[00:00](https://youtube.com/watch?v=Vt4PDUXB_fg&t=0s)** Hi, I'm Alex from Tailscale, and in today's video I'm going to show you how to use image,

**[00:04](https://youtube.com/watch?v=Vt4PDUXB_fg&t=4s)** a self-hosted photo backup solution, and share that with friends and family.

**[00:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=9s)** Let's say you've just taken a big trip and you want to share all the pictures that are

**[00:13](https://youtube.com/watch?v=Vt4PDUXB_fg&t=13s)** on your hard drive with your family that live somewhere else.

**[00:16](https://youtube.com/watch?v=Vt4PDUXB_fg&t=16s)** While using Tailscale and Caddy, a reverse proxy in today's video, I'm going to show you

**[00:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=21s)** how to do just that.

**[00:25](https://youtube.com/watch?v=Vt4PDUXB_fg&t=25s)** Alright, so who is this video for?

**[00:27](https://youtube.com/watch?v=Vt4PDUXB_fg&t=27s)** Well, it's for those of you that already have some self-hosted services running,

**[00:31](https://youtube.com/watch?v=Vt4PDUXB_fg&t=31s)** I'm not going to cover how to set up image or audio bookshelf or anything like that in this video.

**[00:36](https://youtube.com/watch?v=Vt4PDUXB_fg&t=36s)** But what I am going to do, and there'll be chat to markers down below, is cover how to set

**[00:41](https://youtube.com/watch?v=Vt4PDUXB_fg&t=41s)** the remote person portion up. So you could share this video with the relative, all with the friend

**[00:47](https://youtube.com/watch?v=Vt4PDUXB_fg&t=47s)** and say, follow these steps in this video, download Tailscale in this way, and this is how you,

**[00:53](https://youtube.com/watch?v=Vt4PDUXB_fg&t=53s)** as the remote person, can actually go about getting access to the service that I am hosting.

**[00:58](https://youtube.com/watch?v=Vt4PDUXB_fg&t=58s)** If you do need a helping hand-setting up these applications, there are some links down below

**[01:02](https://youtube.com/watch?v=Vt4PDUXB_fg&t=62s)** to some sample code for setting up jellyfin, audio bookshelf as well as image, and Caddy as well.

**[01:08](https://youtube.com/watch?v=Vt4PDUXB_fg&t=68s)** But like I say, that isn't the focus for today's video.

**[01:11](https://youtube.com/watch?v=Vt4PDUXB_fg&t=71s)** We're going to be focusing on Tailscale today, and specifically custom domain support,

**[01:16](https://youtube.com/watch?v=Vt4PDUXB_fg&t=76s)** that's the key part, because you can share a lot of this stuff already just using Tailscale

**[01:20](https://youtube.com/watch?v=Vt4PDUXB_fg&t=80s)** serve that's built into Tailscale. What makes today's solution unique is that we're using

**[01:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=84s)** Caddy as a reverse proxy to support a domain name that you already own. So, Alex is domain.com,

**[01:30](https://youtube.com/watch?v=Vt4PDUXB_fg&t=90s)** something like that. And so the service that we're going to use today is image. This is basically

**[01:35](https://youtube.com/watch?v=Vt4PDUXB_fg&t=95s)** a self-hosted replacement for Google Photos. Any pictures I take on my phone get automatically backed

**[01:41](https://youtube.com/watch?v=Vt4PDUXB_fg&t=101s)** up to image. I can create albums, I can scan for faces, I can, you know, do all that kind of stuff

**[01:47](https://youtube.com/watch?v=Vt4PDUXB_fg&t=107s)** that you would do on Google Photos, except for the fact that data never leaves my server and

**[01:53](https://youtube.com/watch?v=Vt4PDUXB_fg&t=113s)** never leaves my infrastructure. So, taking a look at what we've got over here, you can see that I've

**[01:57](https://youtube.com/watch?v=Vt4PDUXB_fg&t=117s)** already got image running at image.rdu.docs and stuff.dev. This is a domain name that I own,

**[02:04](https://youtube.com/watch?v=Vt4PDUXB_fg&t=124s)** I purchased it for about $13 from Namecheap. You can buy your own, again, for a that sort of $10,

**[02:10](https://youtube.com/watch?v=Vt4PDUXB_fg&t=130s)** $15 price point. It's not too expensive to have your own domain name these days. Image is currently

**[02:15](https://youtube.com/watch?v=Vt4PDUXB_fg&t=135s)** being served through a reverse proxy called Caddy. This automatically handles all of my TLS

**[02:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=141s)** certificates and everything like that from Let's Encrypt. But I've never really liked the name

**[02:25](https://youtube.com/watch?v=Vt4PDUXB_fg&t=145s)** reverse proxy. It doesn't explain very well what it does. And I thought about this the other day.

**[02:31](https://youtube.com/watch?v=Vt4PDUXB_fg&t=151s)** And when you walk into a bar, there's a bartender, right? You want to buy a drink, there's a bunch of

**[02:35](https://youtube.com/watch?v=Vt4PDUXB_fg&t=155s)** bottles behind the bartender, you know, some whiskey, some jeans, that kind of thing. And you

**[02:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=159s)** think to yourself, I want access to those resources behind the bartender. Well, that's what a

**[02:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=165s)** reverse proxy is doing. You place a request, you order a drink, and the bartender or the reverse

**[02:51](https://youtube.com/watch?v=Vt4PDUXB_fg&t=171s)** proxy has permission to go and get that resource for you on the backend. It has the logic of knowing

**[02:57](https://youtube.com/watch?v=Vt4PDUXB_fg&t=177s)** which server is able to serve that web request. And so what we're going to do today is share that

**[03:02](https://youtube.com/watch?v=Vt4PDUXB_fg&t=182s)** reverse proxy out over your tailnet. We're going to put a C name into a public registrar pointing to

**[03:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=189s)** the ts.net entry, which is your personal private DNS name given to your tailnet so that it only

**[03:16](https://youtube.com/watch?v=Vt4PDUXB_fg&t=196s)** resolves over your tailnet. You're not exposing any of this to the internet. And that's such a crucial

**[03:20](https://youtube.com/watch?v=Vt4PDUXB_fg&t=200s)** difference between doing this with something like port forwarding or firewall rules or something

**[03:25](https://youtube.com/watch?v=Vt4PDUXB_fg&t=205s)** like that. All of this remains completely offline, you know, that we're not exposing any of this

**[03:32](https://youtube.com/watch?v=Vt4PDUXB_fg&t=212s)** to the public internet. And so you as the administrator of the image instance, your role here is to make

**[03:38](https://youtube.com/watch?v=Vt4PDUXB_fg&t=218s)** sure that your reverse proxy is working. So in our case, that's caddy. And then you're going to need

**[03:43](https://youtube.com/watch?v=Vt4PDUXB_fg&t=223s)** to put an entry into cloud flare as a public DNS record. Well, come on to that in just a second.

**[03:48](https://youtube.com/watch?v=Vt4PDUXB_fg&t=228s)** So let's take a look at my tailscale admin console over here. You can see that I've got a caddy

**[03:53](https://youtube.com/watch?v=Vt4PDUXB_fg&t=233s)** node in my tailnet. The actual image service is being served through this Ubuntu server down here

**[03:59](https://youtube.com/watch?v=Vt4PDUXB_fg&t=239s)** at the bottom. But at the top here, we've got caddy as the reverse proxy as another node on the

**[04:05](https://youtube.com/watch?v=Vt4PDUXB_fg&t=245s)** tailnet. Now I'm using proxmox under the hood. You can do this however you like, but I'm going to

**[04:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=249s)** use proxmox to show you today. In here, we can see that we have caddy running. So if I type caddy,

**[04:15](https://youtube.com/watch?v=Vt4PDUXB_fg&t=255s)** for example, it's installed. I have it installed as a system D service. And there'll be links in the

**[04:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=261s)** description down below to all of the resources. If you want to do this in an LXC container using system

**[04:27](https://youtube.com/watch?v=Vt4PDUXB_fg&t=267s)** D to run caddy as a service as well. Now if I do a tailscale status inside this LXC container,

**[04:33](https://youtube.com/watch?v=Vt4PDUXB_fg&t=273s)** you can see that it's just behaving like any other tailscale node on my tailnet. But what's

**[04:38](https://youtube.com/watch?v=Vt4PDUXB_fg&t=278s)** interesting is if we take a look at the caddy file that I'm using, by the way, the caddy file is

**[04:42](https://youtube.com/watch?v=Vt4PDUXB_fg&t=282s)** the way that we tell caddy what we want to proxy where. So you can see here, for example, I've got

**[04:47](https://youtube.com/watch?v=Vt4PDUXB_fg&t=287s)** three services that I'm proxying through my caddy instance. First of all, we've got image running on

**[04:53](https://youtube.com/watch?v=Vt4PDUXB_fg&t=293s)** 192168.110.13 on port 2283. The next one we've got is audio bookshelf. This is a self-hosted audio

**[05:03](https://youtube.com/watch?v=Vt4PDUXB_fg&t=303s)** book app. And you can see that this one is actually running on the tailnet IP of the Ubuntu

**[05:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=309s)** server as well. And then finally, we've got jelly fin, which is a self-hosted media server that

**[05:14](https://youtube.com/watch?v=Vt4PDUXB_fg&t=314s)** doesn't need the cloud or anything like that. And all we're using there is the DNS name through

**[05:19](https://youtube.com/watch?v=Vt4PDUXB_fg&t=319s)** tailscale's magic DNS feature of Ubuntu 2204-server. Now I chose these three services in this way

**[05:28](https://youtube.com/watch?v=Vt4PDUXB_fg&t=328s)** to show you the different ways you could configure your caddy file using a local LAN IP address. So this

**[05:34](https://youtube.com/watch?v=Vt4PDUXB_fg&t=334s)** box could be something that's not even on your tailnet, for example, so long as it's rootable

**[05:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=339s)** from the caddy instance itself. Audio books, for example, could be any node anywhere else on your

**[05:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=345s)** tailnet anywhere in the world. And again, the same principle applies to jelly fin because it's

**[05:50](https://youtube.com/watch?v=Vt4PDUXB_fg&t=350s)** just using the tailscale magic DNS name. Now the other thing I wanted to draw your attention to

**[05:55](https://youtube.com/watch?v=Vt4PDUXB_fg&t=355s)** is at the top of this file is this cloud flare section here. This is how caddy automatically generates

**[06:01](https://youtube.com/watch?v=Vt4PDUXB_fg&t=361s)** the HTTPS, the TLS certificates for these self-hosted services. You can see when I do the import

**[06:08](https://youtube.com/watch?v=Vt4PDUXB_fg&t=368s)** cloud flare here, it imports that cloud flare token, and caddy has some logic in it under the hood

**[06:14](https://youtube.com/watch?v=Vt4PDUXB_fg&t=374s)** that knows, oh, he's specified cloud flare. That means I'm going to have to go and do the ACME

**[06:18](https://youtube.com/watch?v=Vt4PDUXB_fg&t=378s)** request to go and generate the TLS certificates automatically for cloud flare. So what's required

**[06:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=384s)** on the tailscale side? Okay, we need to make sure that it's a node on our tailnet. Okay, so I'll do

**[06:28](https://youtube.com/watch?v=Vt4PDUXB_fg&t=388s)** a tailscale status. I've already done tailscale login just to save us a bit of time in the video.

**[06:34](https://youtube.com/watch?v=Vt4PDUXB_fg&t=394s)** Now the next thing we're going to have to do is configure the public DNS side of this solution.

**[06:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=399s)** We're going to need to know where our domain names name servers are pointing. In my case,

**[06:44](https://youtube.com/watch?v=Vt4PDUXB_fg&t=404s)** I've pointed my domain dots and stuff dot dev. I've pointed the name servers for that domain

**[06:49](https://youtube.com/watch?v=Vt4PDUXB_fg&t=409s)** to cloud flare so that I can use cloud flare as my public DNS entry to manage all of my DNS records.

**[06:56](https://youtube.com/watch?v=Vt4PDUXB_fg&t=416s)** So once you've gone ahead and got logged into cloud flare, it's going to be a case of heading over

**[07:00](https://youtube.com/watch?v=Vt4PDUXB_fg&t=420s)** to the domain itself. And then on the left hand side here you can see there's a DNS section just

**[07:05](https://youtube.com/watch?v=Vt4PDUXB_fg&t=425s)** here. And then the entire thing is configured here in one entry. So I've got star.rdu as a wild card

**[07:12](https://youtube.com/watch?v=Vt4PDUXB_fg&t=432s)** entry pointing to caddy dot velociraptor hyphen noodle fish dot TS net. Now you will get this value here

**[07:20](https://youtube.com/watch?v=Vt4PDUXB_fg&t=440s)** that the target which is required to create a C name. You'll get that by heading over to your

**[07:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=444s)** tailscale admin console, go to DNS and whatever value is here, whatever value is in this box here

**[07:31](https://youtube.com/watch?v=Vt4PDUXB_fg&t=451s)** under tailnet name. In my case, velociraptor hyphen noodle fish dot TS dot net. That's the value

**[07:38](https://youtube.com/watch?v=Vt4PDUXB_fg&t=458s)** that you want to put into here. This must be a fully qualified domain name. This is because when

**[07:43](https://youtube.com/watch?v=Vt4PDUXB_fg&t=463s)** you share the node to another tailnet, it's not accessible by the short name. It's only accessible

**[07:48](https://youtube.com/watch?v=Vt4PDUXB_fg&t=468s)** by the full fully qualified domain name of caddy dot whatever dot TS dot net. And with that done,

**[07:55](https://youtube.com/watch?v=Vt4PDUXB_fg&t=475s)** click save and you can verify this by opening a terminal windows. I'll just drag this one in from

**[08:00](https://youtube.com/watch?v=Vt4PDUXB_fg&t=480s)** over here. And we'll do a dig. What did I, I mean, I, yeah, test dot rdu dot and stuff dot dev.

**[08:08](https://youtube.com/watch?v=Vt4PDUXB_fg&t=488s)** And because this is a wild card, you should see that we return a C name here for caddy dot your

**[08:15](https://youtube.com/watch?v=Vt4PDUXB_fg&t=495s)** tailnet name dot TS dot net doesn't have to be caddy. By the way, it just has to match the name

**[08:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=501s)** of the node in your tailscale admin console. So again, just to get that, we go over to the

**[08:26](https://youtube.com/watch?v=Vt4PDUXB_fg&t=506s)** tailscale admin console, click on the drop down here. And whatever this second entry is here,

**[08:31](https://youtube.com/watch?v=Vt4PDUXB_fg&t=511s)** this is the fully qualified domain name for the node itself. All right. So that was a lot. Have

**[08:36](https://youtube.com/watch?v=Vt4PDUXB_fg&t=516s)** we got it? First of all, we need to know what our fully qualified domain name is for caddy,

**[08:40](https://youtube.com/watch?v=Vt4PDUXB_fg&t=520s)** the node on your tailnet. So we get that in the admin console, click on the drop down,

**[08:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=525s)** second option over here. We then in cloud flare need to make sure that the name servers for our

**[08:51](https://youtube.com/watch?v=Vt4PDUXB_fg&t=531s)** domain, wherever we registered it, in my case, I registered mine at name cheap, but, you know,

**[08:56](https://youtube.com/watch?v=Vt4PDUXB_fg&t=536s)** other registrars are available. And I pointed my name service for that domain to cloud flare.

**[09:01](https://youtube.com/watch?v=Vt4PDUXB_fg&t=541s)** Once I've done that and everything had propagated properly, which can take a few hours, by the way.

**[09:07](https://youtube.com/watch?v=Vt4PDUXB_fg&t=547s)** I simply went and created a new record. You click the add record button over here,

**[09:11](https://youtube.com/watch?v=Vt4PDUXB_fg&t=551s)** click on the drop down, C name, you know, blah, blah, blah, whatever put that in. And then my target

**[09:17](https://youtube.com/watch?v=Vt4PDUXB_fg&t=557s)** here, for example, is, you know, test dot velociraptor. That has to match the fully qualified domain name

**[09:25](https://youtube.com/watch?v=Vt4PDUXB_fg&t=565s)** in your tailnet, remember? And then TTL time to live. I mean, whilst I'm doing a bunch of testing

**[09:30](https://youtube.com/watch?v=Vt4PDUXB_fg&t=570s)** for this video, I set mine to one minute. If you leave yours to auto, you probably won't have

**[09:35](https://youtube.com/watch?v=Vt4PDUXB_fg&t=575s)** any issues. So just leave that one alone. Click save. And then it might take a moment or two to

**[09:40](https://youtube.com/watch?v=Vt4PDUXB_fg&t=580s)** propagate. But if I do, what did I call it? I've already forgotten blah, blah, blah.

**[09:48](https://youtube.com/watch?v=Vt4PDUXB_fg&t=588s)** If I do blah, blah, blah, we should see that, yeah, there you go. The C name now resolves to test

**[09:54](https://youtube.com/watch?v=Vt4PDUXB_fg&t=594s)** dot velociraptor. And so the next thing to do is to go ahead and share it with your relative.

**[09:59](https://youtube.com/watch?v=Vt4PDUXB_fg&t=599s)** To do that, we head over to the tailscar admin console once more. Click on this button here,

**[10:04](https://youtube.com/watch?v=Vt4PDUXB_fg&t=604s)** which says share next to the three dot menu and generate and copy and invite link. Once we've

**[10:10](https://youtube.com/watch?v=Vt4PDUXB_fg&t=610s)** done that, you share this with your friend or relative. They can do this from a mobile device

**[10:14](https://youtube.com/watch?v=Vt4PDUXB_fg&t=614s)** or a laptop doesn't really matter. So long as it's logged into the tailnet that they created.

**[10:19](https://youtube.com/watch?v=Vt4PDUXB_fg&t=619s)** Now in terms of the chronological order of this video, this is where things get a little confusing.

**[10:23](https://youtube.com/watch?v=Vt4PDUXB_fg&t=623s)** I wanted to create a dedicated chapter so that you could share this with friends or family and say,

**[10:27](https://youtube.com/watch?v=Vt4PDUXB_fg&t=627s)** hey, go to this timestamp and play from this moment forward. So I'm going to skip ahead or skip

**[10:33](https://youtube.com/watch?v=Vt4PDUXB_fg&t=633s)** back in time a little bit, go through the process of creating a brand new tailnet for your relative.

**[10:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=639s)** And then once we get towards the end of that chapter, that's where this invite link part

**[10:44](https://youtube.com/watch?v=Vt4PDUXB_fg&t=644s)** will actually get used. Hello, and welcome to the remote setup part of this video.

**[10:50](https://youtube.com/watch?v=Vt4PDUXB_fg&t=650s)** I'm going to walk you through creating a brand new tailnet and connecting it to that remote

**[10:54](https://youtube.com/watch?v=Vt4PDUXB_fg&t=654s)** service that your friend or relative is trying to share with you. Creating a tailscale account

**[10:58](https://youtube.com/watch?v=Vt4PDUXB_fg&t=658s)** is completely free. Head over to tailscale.com to get started. Once there, click on the button

**[11:04](https://youtube.com/watch?v=Vt4PDUXB_fg&t=664s)** in the top right, which says get started. And then you'll need to choose your identity provider.

**[11:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=669s)** In today's video, we're going to use Google. I've created a dedicated Google account just for

**[11:15](https://youtube.com/watch?v=Vt4PDUXB_fg&t=675s)** this video called my mums tailnet at gmail.com. Nice and straightforward. So I'm going to click on

**[11:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=681s)** sign up with Google and I'm already authenticated in this browser session with that Google account.

**[11:27](https://youtube.com/watch?v=Vt4PDUXB_fg&t=687s)** So it presents me the choose and account option just here. I'm going to click on that one.

**[11:32](https://youtube.com/watch?v=Vt4PDUXB_fg&t=692s)** Click continue. And easy as that, we've created a tailscale account. So let's add our first device.

**[11:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=699s)** I'm going to make it this laptop that we're using right here. Head over to tailscale.com slash

**[11:44](https://youtube.com/watch?v=Vt4PDUXB_fg&t=704s)** download. Now if you're on a mobile device, you will go to the app store for your device and

**[11:49](https://youtube.com/watch?v=Vt4PDUXB_fg&t=709s)** search tailscale and download the app there. But on a laptop, in this case, it's macOS, we're

**[11:55](https://youtube.com/watch?v=Vt4PDUXB_fg&t=715s)** actually going to go to the Mac app store to download tailscale. Click on the little get button or

**[11:59](https://youtube.com/watch?v=Vt4PDUXB_fg&t=719s)** the cloud icon if you've already done it with this Apple ID like I have here. Download and install

**[12:04](https://youtube.com/watch?v=Vt4PDUXB_fg&t=724s)** the application. Click on open and you'll see up here in the menu bar, we now have a new app.

**[12:10](https://youtube.com/watch?v=Vt4PDUXB_fg&t=730s)** This is where we'll log in. So I'm going to go ahead and just check the toggle box here,

**[12:14](https://youtube.com/watch?v=Vt4PDUXB_fg&t=734s)** which is going to turn tailscale on and then I'm going to click the login button. Now we should be

**[12:19](https://youtube.com/watch?v=Vt4PDUXB_fg&t=739s)** familiar with this page by now, but this is the sign in with Google. This is where we use the same

**[12:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=744s)** Google account that we used to create the towner in the previous step. Once you click that button,

**[12:31](https://youtube.com/watch?v=Vt4PDUXB_fg&t=751s)** we're going to be presented with a screen here which says do you want to connect this device,

**[12:35](https://youtube.com/watch?v=Vt4PDUXB_fg&t=755s)** this laptop, do you want to connect this device to your tailnet and then once you click on the

**[12:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=759s)** big blue button to say connect my device, it's going to take you to your admin console. This is where

**[12:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=765s)** you will see all of the different devices on your tailnet and this is the point where if someone

**[12:51](https://youtube.com/watch?v=Vt4PDUXB_fg&t=771s)** sent you an invite link, we now click on that invite link and add that shared node into this tailnet.

**[12:57](https://youtube.com/watch?v=Vt4PDUXB_fg&t=777s)** So I'm going to go and pretend to be the friend or relative that's sharing this service with you

**[13:01](https://youtube.com/watch?v=Vt4PDUXB_fg&t=781s)** for just a second and generate an invite link. I go to the share button here, generate and copy

**[13:07](https://youtube.com/watch?v=Vt4PDUXB_fg&t=787s)** an invite link. What you will see as the remote person is an invite link that looks something like

**[13:12](https://youtube.com/watch?v=Vt4PDUXB_fg&t=792s)** this log in dot tailscale dot com slash admin slash invite and then a string of characters. When you

**[13:19](https://youtube.com/watch?v=Vt4PDUXB_fg&t=799s)** put that into a web browser or click on it on a mobile device, some magic will happen and we will

**[13:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=804s)** ask you if you want to have this shared device added to your tailnet. I'm going to click on the button

**[13:28](https://youtube.com/watch?v=Vt4PDUXB_fg&t=808s)** here which says accept invite and when I do, you'll notice that inside your tailnet now, notice

**[13:34](https://youtube.com/watch?v=Vt4PDUXB_fg&t=814s)** the tailnet name at the top here, my mum's tailnet at gmail.com. You've now got two nodes, you've

**[13:39](https://youtube.com/watch?v=Vt4PDUXB_fg&t=819s)** got your laptop and also the shared service that the other person is trying to share with you.

**[13:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=825s)** What this means is if they've given you a website to go to, so in my case here for this demo is

**[13:50](https://youtube.com/watch?v=Vt4PDUXB_fg&t=830s)** image.rdu.dotsandstuff.dev. You can now access that service on any device that you're logged in

**[13:58](https://youtube.com/watch?v=Vt4PDUXB_fg&t=838s)** with tailscale. Remember, we logged in using the tailscale up up here in the corner to my mum's

**[14:03](https://youtube.com/watch?v=Vt4PDUXB_fg&t=843s)** tailnet and now any service that that friend or relative has shared with you, you can now access

**[14:08](https://youtube.com/watch?v=Vt4PDUXB_fg&t=848s)** on any device that you are logged in with tailscale on. I'm going to go ahead and get logged in with

**[14:13](https://youtube.com/watch?v=Vt4PDUXB_fg&t=853s)** the username that the person has provided to me, which in this case is a tail and scale at gmail.com.

**[14:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=861s)** Get logged in and suddenly I can see my photos. This is the crux of the solution. I can now go ahead

**[14:26](https://youtube.com/watch?v=Vt4PDUXB_fg&t=866s)** and create albums if I want to. This is an image-specific thing, not a tailscale-specific thing,

**[14:32](https://youtube.com/watch?v=Vt4PDUXB_fg&t=872s)** of course. I'm going to create an album called Canada 23, create a new shared album,

**[14:37](https://youtube.com/watch?v=Vt4PDUXB_fg&t=877s)** and image has a bunch of users within it, for example. If you want to go ahead and create a bunch

**[14:42](https://youtube.com/watch?v=Vt4PDUXB_fg&t=882s)** of users for your friends and family as the server admin, you go into the administration section

**[14:46](https://youtube.com/watch?v=Vt4PDUXB_fg&t=886s)** of image over here and just create a different user account within image for every user that you

**[14:52](https://youtube.com/watch?v=Vt4PDUXB_fg&t=892s)** want to have their own view of the image application. Earlier on in the video, I also showed how we

**[15:00](https://youtube.com/watch?v=Vt4PDUXB_fg&t=900s)** could use audio books and jellyfin as well. Whoever shared this service with you may have a

**[15:05](https://youtube.com/watch?v=Vt4PDUXB_fg&t=905s)** few other things they want to share with you up their sleeve and it should just be a case of

**[15:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=909s)** going and typing in whatever URL they've given you. In my case, rdu.docsonstuff.dev loads an

**[15:17](https://youtube.com/watch?v=Vt4PDUXB_fg&t=917s)** audio book server, for example. If I wanted to go ahead and load up jellyfin, which is a self-hosted

**[15:24](https://youtube.com/watch?v=Vt4PDUXB_fg&t=924s)** media server, again, it's just.docsonstuff.dev. You can see that we can share a whole bunch of

**[15:30](https://youtube.com/watch?v=Vt4PDUXB_fg&t=930s)** self-hosted services using this method. What if we want to do this on a phone? For example,

**[15:36](https://youtube.com/watch?v=Vt4PDUXB_fg&t=936s)** I want to access image from this iPhone right here. Well, I need to install tail scale on that

**[15:40](https://youtube.com/watch?v=Vt4PDUXB_fg&t=940s)** device. I don't need to accept the invite more than once, though, because once we accept the invite

**[15:46](https://youtube.com/watch?v=Vt4PDUXB_fg&t=946s)** into our tailnet, because all the devices are connected together with direct connections

**[15:51](https://youtube.com/watch?v=Vt4PDUXB_fg&t=951s)** as part of the tailnet grouping of devices, there's no need to accept the invite on each device

**[15:56](https://youtube.com/watch?v=Vt4PDUXB_fg&t=956s)** just once per tailnet will suffice. Now to download tail scale on the iPhone, we go to the app store

**[16:02](https://youtube.com/watch?v=Vt4PDUXB_fg&t=962s)** and just search for tail scale. Once we see it appear in the search results, we just click on the

**[16:09](https://youtube.com/watch?v=Vt4PDUXB_fg&t=969s)** little cloud icon or get or open. If you're on Google Play, it'll be the same type of deal here.

**[16:15](https://youtube.com/watch?v=Vt4PDUXB_fg&t=975s)** And then once the app is downloaded, let's click on open to open the tail scale application.

**[16:20](https://youtube.com/watch?v=Vt4PDUXB_fg&t=980s)** Now we're going to walk through the getting started wizard. I'm going to click on get started.

**[16:23](https://youtube.com/watch?v=Vt4PDUXB_fg&t=983s)** Yes, I understand about the privacy stuff. I'm going to allow notifications and then click on

**[16:29](https://youtube.com/watch?v=Vt4PDUXB_fg&t=989s)** install VPN configuration. This is so that tail scale can manage the VPN configurations on this

**[16:35](https://youtube.com/watch?v=Vt4PDUXB_fg&t=995s)** particular iPhone. The next thing we've got to do is actually get logged into the tailnet. Now,

**[16:40](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1000s)** I'm going to click on the login button. And again, I'm going to use the Google Authentication

**[16:45](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1005s)** provider using the same mymumstailnet.gmail.com Google account that we created earlier in the video.

**[16:52](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1012s)** Again, I'm going to click on the big blue connect button to connect this device to my

**[16:56](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1016s)** tailnet. And you can see we've got all of our devices showing up right here, as well as the

**[17:01](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1021s)** shared node that we accepted the invite for in the previous step on the laptop. Remember,

**[17:06](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1026s)** you don't need to accept the invite more than once. Just once per tailnet will suffice.

**[17:11](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1031s)** And so now if I go to the image app on my phone and log in, you can see I've put the image.rdu

**[17:16](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1036s)** address in here. I'm going to log in with the username and password that whoever shared the service

**[17:21](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1041s)** with me gave me. And just like that over 5g, I'm able to connect to image on my phone.

**[17:28](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1048s)** Remember, 5g means I can't possibly be in the same building and connecting to this thing.

**[17:32](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1052s)** So I could be in England. I could be in Japan or America right now. It wouldn't matter.

**[17:37](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1057s)** As long as I had internet connectivity, I could actually resolve this image service.

**[17:41](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1061s)** And of course, on my laptop as well, I'm able to resolve image overtale scale using the shared

**[17:47](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1067s)** node technique with a custom domain that we just set up. So this is a little

**[17:52](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1072s)** taster of what you can do with tailscale. Thank you so much for joining me on this little

**[17:56](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1076s)** little choose your own adventure with friends and family with tailscale type video.

**[18:00](https://youtube.com/watch?v=Vt4PDUXB_fg&t=1080s)** And until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
