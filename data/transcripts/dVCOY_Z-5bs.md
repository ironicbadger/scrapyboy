---
video_id: "dVCOY_Z-5bs"
title: "How to install Tailscale on Windows and configure Remote Desktop | Remotely access your Windows PC"
description: "In today's video Alex will walk you through installing and configuring Tailscale on a Windows PC. Towards the end of the video we will show how to set up Windows RDP (Remote Desktop) to work via Tails..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-06-19"
duration_seconds: 773
youtube_url: "https://www.youtube.com/watch?v=dVCOY_Z-5bs"
thumbnail_url: "https://i.ytimg.com/vi/dVCOY_Z-5bs/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:37:26.944098"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2508
transcription_time_seconds: 21.5
---

# How to install Tailscale on Windows and configure Remote Desktop | Remotely access your Windows PC

**[00:00](https://youtube.com/watch?v=dVCOY_Z-5bs&t=0s)** Hi I'm Alex from Tailscale and in today's video I'm going to show you how to set up Tailscale on Windows and also configure remote desktop so that you can connect to your Windows desktop system from wherever you are in the world. So Tailscale can be really useful to access your Windows computer from anywhere in the world. Tailscale is kind of a VPN but it's also kind of a lot more as well. Certainly in today's video we're going to use it to create a point-to-point connection between two devices that are separated by complete

**[00:30](https://youtube.com/watch?v=dVCOY_Z-5bs&t=30s)** different network topologies. So I'm going to connect to my Windows system over a cellular connection over remote desktop after we've installed Tailscale. So first things first we need to get Tailscale installed and configured and logged in on our Windows system. Now here I have a completely fresh, well box fresh ish at least, Windows 11 installation. To get started head over to Tailscale.com slash download. Next click on the download Tailscale for Windows button.

**[01:00](https://youtube.com/watch?v=dVCOY_Z-5bs&t=60s)** In your downloads folder you will now have a Tailscale setup XE file. You can either click on this directly in your browser or click on this folder icon followed by a double click on the XE file itself. This will load the Tailscale installer.

**[01:15](https://youtube.com/watch?v=dVCOY_Z-5bs&t=75s)** Next you're going to want to agree to the license terms and conditions and now we're going to follow the install process through. This will take a moment it's going to create a system restore point in your Windows installation.

**[01:26](https://youtube.com/watch?v=dVCOY_Z-5bs&t=86s)** And then it's going to download and install the Tailscale binary. It's pretty straightforward to be honest with you but it just takes a few seconds. Now once the installation is complete we now need to log this node into or authenticate this node to your tailnet.

**[01:42](https://youtube.com/watch?v=dVCOY_Z-5bs&t=102s)** And a tailnet is the name we give to the grouping of devices that form a tailscale network a tailnet. That's where the name comes from.

**[01:52](https://youtube.com/watch?v=dVCOY_Z-5bs&t=112s)** So I'm going to go ahead and click on the get started button here in the wizard and then follow that with sign in to your network.

**[01:58](https://youtube.com/watch?v=dVCOY_Z-5bs&t=118s)** This is going to now open up your default web browser in Windows. Now I don't want to use Edge. I want to use Chrome.

**[02:05](https://youtube.com/watch?v=dVCOY_Z-5bs&t=125s)** So I'm just going to copy and paste this string from here into this browser session. And the reason I'm doing that is because I'm already logged in using my Google accounts into Google Chrome, whereas I'm not logged in with Edge.

**[02:17](https://youtube.com/watch?v=dVCOY_Z-5bs&t=137s)** Now as you can see, we support a wide range of identity providers, Google, Microsoft, GitHub, Apple can also sign in with past keys if you like.

**[02:26](https://youtube.com/watch?v=dVCOY_Z-5bs&t=146s)** I would probably recommend if this is your first time sticking with one of the big providers that's listed here, totally up to you. And there aren't really any caveats as to which one you should be using.

**[02:36](https://youtube.com/watch?v=dVCOY_Z-5bs&t=156s)** In today's video though, I'm going to use Google because I use this pangolin demo account in every single video I do here on the tailscale channel.

**[02:44](https://youtube.com/watch?v=dVCOY_Z-5bs&t=164s)** So I'm going to go ahead and click on the connect button. And what that's just done is that has now authenticated. There's a bunch of stuff going on in the background which allows this node now this Windows computer to communicate with the tailscale control server in the background in real time.

**[02:59](https://youtube.com/watch?v=dVCOY_Z-5bs&t=179s)** There's been a whole bunch of key exchange and magic happened behind the scenes such that this node, which is actually called blue iris.

**[03:06](https://youtube.com/watch?v=dVCOY_Z-5bs&t=186s)** I use this as my local NVR system in in this house actually. Well, that's not important for this video. This node is called blue iris and the key exchange process now gives this node permission to be a member of my talent and that all happened in just a few clicks.

**[03:21](https://youtube.com/watch?v=dVCOY_Z-5bs&t=201s)** There was no config files. There was no complicated configuration that you as the end user had to do besides authenticating the node and logging in using your identity provider.

**[03:31](https://youtube.com/watch?v=dVCOY_Z-5bs&t=211s)** So now this nodes on our tailnet, we should probably just clean up and make sure that everything is looking as we want it to.

**[03:38](https://youtube.com/watch?v=dVCOY_Z-5bs&t=218s)** So if we go back to the tailscale install wizard, you can see that now you're connected. You can manage settings by right clicking on the tailscale icon down in the cis tray down here.

**[03:48](https://youtube.com/watch?v=dVCOY_Z-5bs&t=228s)** So you Windows users are probably very familiar with this area down here, but you can drag and drop this into your cis tray down here, your system tray so that you can always see the status of tailscale regardless of whether it's sort of in behind the hidden area or not.

**[04:04](https://youtube.com/watch?v=dVCOY_Z-5bs&t=244s)** And then you can right click on this thing and you get a whole bunch of options.

**[04:08](https://youtube.com/watch?v=dVCOY_Z-5bs&t=248s)** So first of all, I want to point out that you can actually log in to multiple accounts on the same computer.

**[04:14](https://youtube.com/watch?v=dVCOY_Z-5bs&t=254s)** So if you have a work tailnet, let's say your company uses tailscale at work and then you also want to use tailscale at home to connect some of your private services, you can do that just here by clicking on the add another account option.

**[04:26](https://youtube.com/watch?v=dVCOY_Z-5bs&t=266s)** You can also take this as a shortcut to the admin console at tailscale.com. If we click on that again, you can see trying to open it up in an edge. I don't want to use edge.

**[04:36](https://youtube.com/watch?v=dVCOY_Z-5bs&t=276s)** Maybe I should set my default browser before the next video, but again, clicking on that icon down in the corner shows me that this device is called blue iris on this tailnet and the IP address it's been given is a 100 dot IP address.

**[04:50](https://youtube.com/watch?v=dVCOY_Z-5bs&t=290s)** Now this IP address in the 100 range is what's called a CG net IP address. It's a very complicated way of saying that it's a private IP range behind carrier grade net.

**[05:00](https://youtube.com/watch?v=dVCOY_Z-5bs&t=300s)** So this IP address isn't something you need to worry about giving out. If somebody asks you for this IP address, I don't know why they would, but if they did, you could give it to them perfectly safely.

**[05:10](https://youtube.com/watch?v=dVCOY_Z-5bs&t=310s)** The reason for that is because only people inside your tailnet can actually route packets to this IP address.

**[05:18](https://youtube.com/watch?v=dVCOY_Z-5bs&t=318s)** So if, for example, you watching this video wanted to try and route packets from your computer to my blue iris box without being a member of my tailnet, you just wouldn't have a route available to do that.

**[05:30](https://youtube.com/watch?v=dVCOY_Z-5bs&t=330s)** So you couldn't send those packets from point A to point B.

**[05:34](https://youtube.com/watch?v=dVCOY_Z-5bs&t=334s)** Now under the device network devices section, you can see here I've got a list of all the other devices in my tailnet.

**[05:41](https://youtube.com/watch?v=dVCOY_Z-5bs&t=341s)** And indeed, if we look here in the tailscar admin console in the background, you can see that a couple of videos ago, you can see a link to this up here.

**[05:49](https://youtube.com/watch?v=dVCOY_Z-5bs&t=349s)** I was talking about how they get started with self hosting and sort of self host audio books and, you know, photos and that kind of stuff and access it from your phone.

**[05:57](https://youtube.com/watch?v=dVCOY_Z-5bs&t=357s)** Well, you can see here that this device now this window system is now a member of that tailnet.

**[06:02](https://youtube.com/watch?v=dVCOY_Z-5bs&t=362s)** So we can now access all of those services, those self hosted services from anywhere.

**[06:07](https://youtube.com/watch?v=dVCOY_Z-5bs&t=367s)** So if this was a laptop, we could now take this computer to the coffee shop and access or hotel and access this stuff, wherever we are using tailscales, natural versus technology.

**[06:18](https://youtube.com/watch?v=dVCOY_Z-5bs&t=378s)** Pretty cool, I think. Now exit node is an interesting one.

**[06:21](https://youtube.com/watch?v=dVCOY_Z-5bs&t=381s)** So the concept of an exit node, you can think of it pretty much like any other VPN that you're familiar with.

**[06:27](https://youtube.com/watch?v=dVCOY_Z-5bs&t=387s)** So you connect to a VPN and all of your traffic gets funneled out through a specific endpoint.

**[06:33](https://youtube.com/watch?v=dVCOY_Z-5bs&t=393s)** Well, with an exit node, all of your traffic exits through that exit node.

**[06:39](https://youtube.com/watch?v=dVCOY_Z-5bs&t=399s)** And it's the name.

**[06:40](https://youtube.com/watch?v=dVCOY_Z-5bs&t=400s)** So if I wanted all of my traffic to exit through Bob, for example, which is running, I think in digital ocean in New York City, I would just check this box.

**[06:49](https://youtube.com/watch?v=dVCOY_Z-5bs&t=409s)** And suddenly, instead of all of the packets traversing out through my residential firewall as the endpoint.

**[06:54](https://youtube.com/watch?v=dVCOY_Z-5bs&t=414s)** So the IP address would be an AT&T provided address for me here in America.

**[06:59](https://youtube.com/watch?v=dVCOY_Z-5bs&t=419s)** All of my packets would now go out through the digital ocean data center instead as their final endpoint on the internet.

**[07:05](https://youtube.com/watch?v=dVCOY_Z-5bs&t=425s)** And of course, between those two places, it's all going over an encrypted wire guard tunnel in the background.

**[07:11](https://youtube.com/watch?v=dVCOY_Z-5bs&t=431s)** So exit nodes are pretty cool.

**[07:13](https://youtube.com/watch?v=dVCOY_Z-5bs&t=433s)** And I have a dedicated video about exit nodes up here, if you want to check out more about that.

**[07:18](https://youtube.com/watch?v=dVCOY_Z-5bs&t=438s)** Now preferences, this one is actually pretty interesting.

**[07:21](https://youtube.com/watch?v=dVCOY_Z-5bs&t=441s)** So allow incoming connections.

**[07:23](https://youtube.com/watch?v=dVCOY_Z-5bs&t=443s)** We'll leave that one checked because we want people to be able to connect into this box so that when we want to connect using remote desktop to this system,

**[07:31](https://youtube.com/watch?v=dVCOY_Z-5bs&t=451s)** we're allowing those connections to come inbound.

**[07:34](https://youtube.com/watch?v=dVCOY_Z-5bs&t=454s)** I also want to use the tail scale DNS setting so that if I want to connect to something somewhere else on my tail net, I don't have to type in IP addresses.

**[07:41](https://youtube.com/watch?v=dVCOY_Z-5bs&t=461s)** I can just use the nice, friendly, fully qualified domain names and DNS names instead of having to worry about IP addresses.

**[07:49](https://youtube.com/watch?v=dVCOY_Z-5bs&t=469s)** So that's nice. We'll leave that one set as default as well.

**[07:52](https://youtube.com/watch?v=dVCOY_Z-5bs&t=472s)** I'm also going to use tail scale subnets as well so that all the roots and things that get published as part of the tail scale key exchange process,

**[07:59](https://youtube.com/watch?v=dVCOY_Z-5bs&t=479s)** the coordination server process that we did just a couple of minutes ago.

**[08:03](https://youtube.com/watch?v=dVCOY_Z-5bs&t=483s)** I'm going to leave use tail scale subnets checked as well.

**[08:06](https://youtube.com/watch?v=dVCOY_Z-5bs&t=486s)** Now, these two are where things might start to get a little unusual, I suppose, automatically install updates.

**[08:14](https://youtube.com/watch?v=dVCOY_Z-5bs&t=494s)** I guess that one's not that unusual, but run unattended.

**[08:19](https://youtube.com/watch?v=dVCOY_Z-5bs&t=499s)** So tail scale at the moment is installed in, I think the correct terminology is single user mode or something like that anyway.

**[08:27](https://youtube.com/watch?v=dVCOY_Z-5bs&t=507s)** When you want to run tail scale as a service, a system level service on windows, you have to select this option here, which is run unattended.

**[08:36](https://youtube.com/watch?v=dVCOY_Z-5bs&t=516s)** This will put tail scale in the background, regardless of whether your user is logged in or not.

**[08:42](https://youtube.com/watch?v=dVCOY_Z-5bs&t=522s)** Now, if you're going to use this as a remote desktop target, this checkbox here of unattended mode, in fact it even tells us here, in unattended mode, tail scale keeps running as your identity when you log out of windows.

**[08:56](https://youtube.com/watch?v=dVCOY_Z-5bs&t=536s)** So if you're going to use this windows box as a remote desktop kind of server, if you like, or you want to connect to it from somewhere else, this is almost certainly a box you want to be checking.

**[09:06](https://youtube.com/watch?v=dVCOY_Z-5bs&t=546s)** So I'm going to make sure that we enable unattended mode and beyond that, there's just a couple of other things.

**[09:13](https://youtube.com/watch?v=dVCOY_Z-5bs&t=553s)** In terms of remote desktop, I'm just going to come in here and search for allow remote desktop.

**[09:19](https://youtube.com/watch?v=dVCOY_Z-5bs&t=559s)** Now, I've already got remote desktop turned on on this system, but if you don't just check the box and you should be good to go.

**[09:25](https://youtube.com/watch?v=dVCOY_Z-5bs&t=565s)** Now, you need to also make sure that your remote desktop users are set up correctly.

**[09:29](https://youtube.com/watch?v=dVCOY_Z-5bs&t=569s)** So in my case here, this is just a single user system with the username of Alex, but if you have other users or group policies or some kind of other more complicated setup, make sure you set that up first.

**[09:42](https://youtube.com/watch?v=dVCOY_Z-5bs&t=582s)** Then what we need to do is go behind the curtain just a little bit because this was already done over remote desktop on a on a Mac.

**[09:52](https://youtube.com/watch?v=dVCOY_Z-5bs&t=592s)** So what I want to do now is make sure I'm connected to my tailnet from this Mac PC and I want to connect over tail scale to that windows system.

**[10:02](https://youtube.com/watch?v=dVCOY_Z-5bs&t=602s)** Now, forget the fact they're on the same LAN for right now because in the minute, we'll switch to cellular, but just for illustrative purposes to pretend they're on a separate network on different sides of a city or something like that.

**[10:13](https://youtube.com/watch?v=dVCOY_Z-5bs&t=613s)** So what I want to do is just go in here and grab the blue iris IP address. Now, I could just use the DNS name if I want to.

**[10:20](https://youtube.com/watch?v=dVCOY_Z-5bs&t=620s)** In fact, when I click on add PC, I'm just going to do that. I am just literally going to type in blue iris. No IP addresses or anything, even though I just put it on my clipboard.

**[10:30](https://youtube.com/watch?v=dVCOY_Z-5bs&t=630s)** Credentials. I'm just going to put Alex and then I'm going to click add. Now, remember this is now connecting over tail scale. It's doing all the DNS over tail scale.

**[10:39](https://youtube.com/watch?v=dVCOY_Z-5bs&t=639s)** It's doing all the rooting over tail scale. Everything is running through tail scale. So again, this remote PC could be literally anywhere in the world.

**[10:48](https://youtube.com/watch?v=dVCOY_Z-5bs&t=648s)** I can unplug it, take it to England when I go on holiday, leave another parent's house. And now I've got a window server that I can just connect to from anywhere in the world.

**[10:58](https://youtube.com/watch?v=dVCOY_Z-5bs&t=658s)** And boom, we're in to remote desktop using the Windows app from macOS. So let's just put my money where my mouth is and let's actually connect using 5G.

**[11:09](https://youtube.com/watch?v=dVCOY_Z-5bs&t=669s)** So if I click on iPhone tail scale here, this is going to now use this phone's tethering capabilities. Yes, I want to allow this.

**[11:17](https://youtube.com/watch?v=dVCOY_Z-5bs&t=677s)** So she's going to now have this laptop go out over this cellular connection probably like you would do at a coffee shop with spotty wife or something.

**[11:24](https://youtube.com/watch?v=dVCOY_Z-5bs&t=684s)** You know, you just tether to your phone. We've all done that at some point. I'm sure.

**[11:28](https://youtube.com/watch?v=dVCOY_Z-5bs&t=688s)** And now I want to prove to you that this is still going to work regardless of whether I am on the same land or not.

**[11:36](https://youtube.com/watch?v=dVCOY_Z-5bs&t=696s)** So if I click continue now, this is now remember sending all these packets out through my phone over the internet through my AT&T firewall,

**[11:45](https://youtube.com/watch?v=dVCOY_Z-5bs&t=705s)** coming back up through the cables in my walls back to the box that's in this house.

**[11:51](https://youtube.com/watch?v=dVCOY_Z-5bs&t=711s)** And again, we're connected to the blue Iris box from anywhere in the world using remote desktop. Isn't that cool?

**[11:58](https://youtube.com/watch?v=dVCOY_Z-5bs&t=718s)** And that really is the magic of tail scale. Perhaps you've seen some of my other videos and you see me waxing here a cool about how much I love tail scale.

**[12:04](https://youtube.com/watch?v=dVCOY_Z-5bs&t=724s)** But in the old days, this would have been an absolute mess of firewall rules or setting up some kind of complicated open VPN server.

**[12:12](https://youtube.com/watch?v=dVCOY_Z-5bs&t=732s)** None of that anymore. It's just a few clicks. And I know this video is quite a few minutes because I'm explaining things.

**[12:17](https://youtube.com/watch?v=dVCOY_Z-5bs&t=737s)** But I legitimately think you could speedrun this in under a minute. In fact, if you do that, leave a comment down below.

**[12:23](https://youtube.com/watch?v=dVCOY_Z-5bs&t=743s)** Let's set some records. Let's see how fast we can do this.

**[12:26](https://youtube.com/watch?v=dVCOY_Z-5bs&t=746s)** So that's how you install tail scale on Windows. And until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
