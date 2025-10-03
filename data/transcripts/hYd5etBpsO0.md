---
video_id: "hYd5etBpsO0"
title: "Your Apple TV is a Subnet Router for Tailscale now!"
description: "You asked, we delivered! Your Apple TV, now with 100% more Tailscale subnet routing.

* Subnet Routing - https://tailscale.com/kb/1019/subnets
* How Tailscale Assigns IP Address - https://tailscale.co..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-01-18"
duration_seconds: 500
youtube_url: "https://www.youtube.com/watch?v=hYd5etBpsO0"
thumbnail_url: "https://i.ytimg.com/vi/hYd5etBpsO0/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:40:27.578855"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1414
transcription_time_seconds: 13.3
---

# Your Apple TV is a Subnet Router for Tailscale now!

**[00:00](https://youtube.com/watch?v=hYd5etBpsO0&t=0s)** Hi, I'm Alex from Tailscale. I want to talk to you today about the Apple TV. We made

**[00:04](https://youtube.com/watch?v=hYd5etBpsO0&t=4s)** a video about this late last year and told you about how to use Apple TV as an exit

**[00:09](https://youtube.com/watch?v=hYd5etBpsO0&t=9s)** node, how you could use it with Mulvad. There'll be a link to that video just up here.

**[00:15](https://youtube.com/watch?v=hYd5etBpsO0&t=15s)** But today I wanted to highlight something that we asked you about in that video, subnet

**[00:21](https://youtube.com/watch?v=hYd5etBpsO0&t=21s)** routers. I'm delighted to say that as of Tailscale 1.56, we've actually added subnet routing

**[00:29](https://youtube.com/watch?v=hYd5etBpsO0&t=29s)** functionality to the Apple TV. Now, we do recommend installing Tailscale directly on as many

**[00:36](https://youtube.com/watch?v=hYd5etBpsO0&t=36s)** clients as possible. That's because each connection is end-to-end encrypted and when you move

**[00:40](https://youtube.com/watch?v=hYd5etBpsO0&t=40s)** those devices between different sites, you don't need to do any reconfiguration. They'll

**[00:45](https://youtube.com/watch?v=hYd5etBpsO0&t=45s)** automatically figure out with the NAT punching that Tailscale does how to reconnect to one

**[00:50](https://youtube.com/watch?v=hYd5etBpsO0&t=50s)** another. However, in some situations, we do understand that it's not possible to install

**[00:55](https://youtube.com/watch?v=hYd5etBpsO0&t=55s)** Tailscale on every single client device, a printer or a coffee pot or a random Wi-Fi access point

**[01:02](https://youtube.com/watch?v=hYd5etBpsO0&t=62s)** that one of your relatives just brought home from the store and says, hey, can you configure

**[01:07](https://youtube.com/watch?v=hYd5etBpsO0&t=67s)** this for me remotely? It happens, right? In this situation, you probably want something called

**[01:13](https://youtube.com/watch?v=hYd5etBpsO0&t=73s)** a subnet router. Let's use the Apple TV as an example here. We're going to turn it into a subnet

**[01:18](https://youtube.com/watch?v=hYd5etBpsO0&t=78s)** router using the new functionality that we just added and use this as a low power always on

**[01:25](https://youtube.com/watch?v=hYd5etBpsO0&t=85s)** device, because even when the Apple TV is asleep, it's using a couple of watts. It's still usable

**[01:30](https://youtube.com/watch?v=hYd5etBpsO0&t=90s)** as an exit node and a subnet router, which makes it perfect to just stick onto the TV and just

**[01:35](https://youtube.com/watch?v=hYd5etBpsO0&t=95s)** forget about it. It's not using really hardly any power at all. Time for a little bit of networking

**[01:41](https://youtube.com/watch?v=hYd5etBpsO0&t=101s)** theory. Hopefully, by this point, you're all familiar with the fact that when a device connects to

**[01:46](https://youtube.com/watch?v=hYd5etBpsO0&t=106s)** Wi-Fi or you plug in an ethernet cable, it gets an IP address. Well, it does that from a DHCP

**[01:53](https://youtube.com/watch?v=hYd5etBpsO0&t=113s)** server, which typically lives on a router. So in a lot of residential settings, this is the box

**[01:59](https://youtube.com/watch?v=hYd5etBpsO0&t=119s)** that your cable internet provider gives you or your ISP or whatever. In a residential scenario,

**[02:05](https://youtube.com/watch?v=hYd5etBpsO0&t=125s)** we're probably all used to seeing the 192.168 IP address space. This is a reserved block of IP

**[02:12](https://youtube.com/watch?v=hYd5etBpsO0&t=132s)** addresses. So if you start trying to type 192.168.whatever to try and get to Google or something,

**[02:19](https://youtube.com/watch?v=hYd5etBpsO0&t=139s)** it's not going to work. That's because these addresses don't route across the public internet.

**[02:24](https://youtube.com/watch?v=hYd5etBpsO0&t=144s)** They stay local. There are a couple of other ranges to the 10.whatever range, I think, is also

**[02:30](https://youtube.com/watch?v=hYd5etBpsO0&t=150s)** another one. There are different RFCs that govern which IP address ranges are reserved. Now, interestingly

**[02:37](https://youtube.com/watch?v=hYd5etBpsO0&t=157s)** enough, actually, the tailscale 100.ip address space is actually a carrier grade NAT reserved IP

**[02:46](https://youtube.com/watch?v=hYd5etBpsO0&t=166s)** address block as well. So if you want to read more about that, I'll put a link to the tailscale

**[02:49](https://youtube.com/watch?v=hYd5etBpsO0&t=169s)** documentation about our IP address space down below. So when we look at the anatomy of an IP address,

**[02:55](https://youtube.com/watch?v=hYd5etBpsO0&t=175s)** we've got four different octets and then we have a subnet mask. So in our case here, we have 192.168.168.whatever the

**[03:07](https://youtube.com/watch?v=hYd5etBpsO0&t=187s)** client IP address, the final octet is the subnet mask. You've probably seen this written as 255.255.255.0.

**[03:18](https://youtube.com/watch?v=hYd5etBpsO0&t=198s)** We have a shorthand in networking circles called cider notation, CIDR. And in this case,

**[03:24](https://youtube.com/watch?v=hYd5etBpsO0&t=204s)** we can shorthand notate that horrible 255.long name to just a slash 24. What that means is that there

**[03:33](https://youtube.com/watch?v=hYd5etBpsO0&t=213s)** are 254 IP addresses available within that subnet. You might see other shorthand notations of like a

**[03:40](https://youtube.com/watch?v=hYd5etBpsO0&t=220s)** slash 16 or something like that where there are 65,536.35. I always forget. IP address is available.

**[03:52](https://youtube.com/watch?v=hYd5etBpsO0&t=232s)** Now, obviously, that's not going to be suitable for most residential deployments but it's just useful

**[03:56](https://youtube.com/watch?v=hYd5etBpsO0&t=236s)** to know when you're seeing what these different slash notations might be useful. And so in my case here,

**[04:02](https://youtube.com/watch?v=hYd5etBpsO0&t=242s)** what I want to do is allow access to all of those 255 devices on the slash 24 subnet,

**[04:09](https://youtube.com/watch?v=hYd5etBpsO0&t=249s)** which belongs to the 192.168.16 subnet. In my case, I've got an IPMI interface on my server

**[04:17](https://youtube.com/watch?v=hYd5etBpsO0&t=257s)** that can't run tailscale. That's because it's an HTML5 web console built in as an embedded chip

**[04:25](https://youtube.com/watch?v=hYd5etBpsO0&t=265s)** onto my server's motherboard that lets me remote control the server as if I'm physically sat a

**[04:31](https://youtube.com/watch?v=hYd5etBpsO0&t=271s)** keyboard and monitor in the remote network. IPMI is super cool, by the way. If you've never tried

**[04:36](https://youtube.com/watch?v=hYd5etBpsO0&t=276s)** it out, just type it into YouTube and have a look. You're in for a treat. But in our case,

**[04:42](https://youtube.com/watch?v=hYd5etBpsO0&t=282s)** I want to be able to access the IPMI interface even if I'm not physically in that remote network.

**[04:48](https://youtube.com/watch?v=hYd5etBpsO0&t=288s)** So by using a subnet router, I can rewrite the traffic. So when I make a request for that subnet,

**[04:55](https://youtube.com/watch?v=hYd5etBpsO0&t=295s)** our tailscale infrastructure has the knowledge that you have allowed that subnet router to forward

**[05:00](https://youtube.com/watch?v=hYd5etBpsO0&t=300s)** packets for that specific destination subnet. So it doesn't match and it goes, hey, you probably

**[05:05](https://youtube.com/watch?v=hYd5etBpsO0&t=305s)** want to route the traffic through this particular subnet router. And then the subnet router

**[05:10](https://youtube.com/watch?v=hYd5etBpsO0&t=310s)** rewrites the packets as if they originated from that specific device itself. What's particularly

**[05:16](https://youtube.com/watch?v=hYd5etBpsO0&t=316s)** interesting for me, at least, is that that IPMI device or the printer or whatever other device

**[05:22](https://youtube.com/watch?v=hYd5etBpsO0&t=322s)** is in the subnet that's not on your tailnet has absolutely no idea that tailscale is involved in

**[05:28](https://youtube.com/watch?v=hYd5etBpsO0&t=328s)** the transaction whatsoever. So far as that remote client is concerned, the traffic originated from

**[05:34](https://youtube.com/watch?v=hYd5etBpsO0&t=334s)** the subnet router itself, whether that's a Apple TV, a Linux box or your firewall. Now, if you're

**[05:40](https://youtube.com/watch?v=hYd5etBpsO0&t=340s)** a little bit paranoid about allowing every device on your tailnet access through a subnet router

**[05:46](https://youtube.com/watch?v=hYd5etBpsO0&t=346s)** to a remote network, you can lock this down in ACLs. I'll put a link to the ACL documentation

**[05:50](https://youtube.com/watch?v=hYd5etBpsO0&t=350s)** down below. That's a topic for an entirely separate video. What remains as a topic for this video

**[05:57](https://youtube.com/watch?v=hYd5etBpsO0&t=357s)** is talking you through the Apple TV interface. So here we are at the Apple TV. I'm going to load up

**[06:02](https://youtube.com/watch?v=hYd5etBpsO0&t=362s)** the network page just here. And you can see I'm connected to my Wi-Fi. I've got an IP address. This

**[06:07](https://youtube.com/watch?v=hYd5etBpsO0&t=367s)** again is a local IP address of 10.42.10.10.105. And if I open up the tailscale VPN section, I want to

**[06:17](https://youtube.com/watch?v=hYd5etBpsO0&t=377s)** just dig into some of the connection details that are here. You can see that the connect on demand

**[06:22](https://youtube.com/watch?v=hYd5etBpsO0&t=382s)** is true. You can see all the different search domains that I have as split DNS within my tail

**[06:27](https://youtube.com/watch?v=hYd5etBpsO0&t=387s)** scale tailnet. And then also underneath we've got an option to actually open up the tailscale app.

**[06:33](https://youtube.com/watch?v=hYd5etBpsO0&t=393s)** So let's go ahead and do that. And you can see we've added a new section here. You've seen the

**[06:39](https://youtube.com/watch?v=hYd5etBpsO0&t=399s)** exit node thing before because I showed you that in the previous video. But if we go down to here

**[06:45](https://youtube.com/watch?v=hYd5etBpsO0&t=405s)** subnet router. Oh yes, here it is folks. So let's have a quick look at advertising a new route on

**[06:53](https://youtube.com/watch?v=hYd5etBpsO0&t=413s)** here. So by default, you know, the route that it's going to advertise is 192.168.1.0 slash 24.

**[07:02](https://youtube.com/watch?v=hYd5etBpsO0&t=422s)** Go ahead and customize that to your needs. So once you've got the advertised routes configured

**[07:07](https://youtube.com/watch?v=hYd5etBpsO0&t=427s)** correctly on the Apple TV side of things, go ahead and jump over to tailscale.com,

**[07:11](https://youtube.com/watch?v=hYd5etBpsO0&t=431s)** click into your admin console up in the top right hand corner, find the Apple TV in question.

**[07:16](https://youtube.com/watch?v=hYd5etBpsO0&t=436s)** In my situation, this is Apple TV travel. This is the one I take with me when I take a business trip

**[07:21](https://youtube.com/watch?v=hYd5etBpsO0&t=441s)** or something. And then click on the three dot menu on the right over here, click on edit route

**[07:26](https://youtube.com/watch?v=hYd5etBpsO0&t=446s)** settings, check the box, click save and we're done. This Apple TV is now configured as a subnet router

**[07:34](https://youtube.com/watch?v=hYd5etBpsO0&t=454s)** for your tailnet. Now the whole reason that subnet routing came to the Apple TV was because you

**[07:39](https://youtube.com/watch?v=hYd5etBpsO0&t=459s)** asked for it in the comment section of our last video, loads of you let us know that you wanted to see

**[07:45](https://youtube.com/watch?v=hYd5etBpsO0&t=465s)** subnet routing brought to the Apple TV. That's why the feature was created. So well done to everybody

**[07:51](https://youtube.com/watch?v=hYd5etBpsO0&t=471s)** that commented down below. Now, if there's a feature that we're not yet working on, you'd love to see

**[07:56](https://youtube.com/watch?v=hYd5etBpsO0&t=476s)** us do let us know in the comments down below. We read every single one. Now until the next video,

**[08:02](https://youtube.com/watch?v=hYd5etBpsO0&t=482s)** you have to go forth and spread tailscale subnet routers and exit nodes on low power devices,

**[08:08](https://youtube.com/watch?v=hYd5etBpsO0&t=488s)** wherever you go. Thank you so much for watching everyone. Until next time, I've been Alex from

**[08:14](https://youtube.com/watch?v=hYd5etBpsO0&t=494s)** tailscale.

---

*Automatically generated transcript. May contain errors.*
