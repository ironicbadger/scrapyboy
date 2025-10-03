---
video_id: "833pTn_3HYI"
title: "Remotely unlock a Filevault encrypted disk with macOS 26 Tahoe via SSH and a Tailscale Subnet Router"
description: "Apple just released macOS 26 “Tahoe”, and with it comes a small but game-changing feature: you can now remotely unlock FileVault-encrypted disks via SSH. In this video, I walk you through how it works..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-18"
duration_seconds: 837
youtube_url: "https://www.youtube.com/watch?v=833pTn_3HYI"
thumbnail_url: "https://i.ytimg.com/vi_webp/833pTn_3HYI/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:01:54.308315"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2544
transcription_time_seconds: 22.7
---

# Remotely unlock a Filevault encrypted disk with macOS 26 Tahoe via SSH and a Tailscale Subnet Router

**[00:00](https://youtube.com/watch?v=833pTn_3HYI&t=0s)** Apple released MacOS 26 Tahoe this week and among the many big changes, one tiny little

**[00:05](https://youtube.com/watch?v=833pTn_3HYI&t=5s)** one caught my attention. You can now remotely unlock FileVolt disks via SSH. So that's

**[00:13](https://youtube.com/watch?v=833pTn_3HYI&t=13s)** what we're going to dig into in today's video. But before we do, did you know that we've

**[00:17](https://youtube.com/watch?v=833pTn_3HYI&t=17s)** just launched a brand new Discord server over at discord.gge slash Tailscale. Come over

**[00:22](https://youtube.com/watch?v=833pTn_3HYI&t=22s)** there to find me at AlexKTZ and tell me what you're using your Mac for as a server.

**[00:28](https://youtube.com/watch?v=833pTn_3HYI&t=28s)** Now, in today's video, we are going to test this remote unlocking and I even found a way

**[00:33](https://youtube.com/watch?v=833pTn_3HYI&t=33s)** to shove Tailscale into this video because if you want to use this to remotely unlock your

**[00:39](https://youtube.com/watch?v=833pTn_3HYI&t=39s)** Mac, well, it's not running the full user space tools yet. So we have to use the Tailscale

**[00:44](https://youtube.com/watch?v=833pTn_3HYI&t=44s)** subnet routing feature. So in the typical Mac boot process, if you have FileVolt enabled,

**[00:51](https://youtube.com/watch?v=833pTn_3HYI&t=51s)** the system does a few things. Firstly, it turns on and does what's called, I guess, a post,

**[00:56](https://youtube.com/watch?v=833pTn_3HYI&t=56s)** at least that's what we call it in PC land. I don't know what Apple call it, but basically,

**[01:00](https://youtube.com/watch?v=833pTn_3HYI&t=60s)** that's the point in time where the Mac checks all of its hardware is in order and it can

**[01:05](https://youtube.com/watch?v=833pTn_3HYI&t=65s)** continue with the boot process and it has a boot volume that is ready to go. Secondly,

**[01:11](https://youtube.com/watch?v=833pTn_3HYI&t=71s)** it then tries to boot into an OS proper. But if you use disk encryption and the system can't

**[01:18](https://youtube.com/watch?v=833pTn_3HYI&t=78s)** load the OS until you decrypt the drive by entering your password, you end up in a bit of a catch

**[01:23](https://youtube.com/watch?v=833pTn_3HYI&t=83s)** 22 situation because there are no user space services running at that point. So no Tailscale,

**[01:29](https://youtube.com/watch?v=833pTn_3HYI&t=89s)** no full SSH Demon, no Rust Desk, no way to remotely unlock that disk unless you walk over to the

**[01:37](https://youtube.com/watch?v=833pTn_3HYI&t=97s)** terminal of that computer and type the password in on the keyboard. Once you've done that,

**[01:42](https://youtube.com/watch?v=833pTn_3HYI&t=102s)** though, once you've typed that password in, the OS will continue to boot and automatically

**[01:47](https://youtube.com/watch?v=833pTn_3HYI&t=107s)** log you into the desktop. And this happens so fast on modern Macs that I'm sure many of you

**[01:52](https://youtube.com/watch?v=833pTn_3HYI&t=112s)** didn't even think about that when you type your password in, you actually just watched your

**[01:57](https://youtube.com/watch?v=833pTn_3HYI&t=117s)** computer cold boot and log you in to your user session all at once. Now this is all fine when

**[02:04](https://youtube.com/watch?v=833pTn_3HYI&t=124s)** we're dealing with Mac OS that's on a laptop on your desk in front of you. There's right there

**[02:10](https://youtube.com/watch?v=833pTn_3HYI&t=130s)** in front of you because you have all the stages of the boot process laid bare for you to see.

**[02:15](https://youtube.com/watch?v=833pTn_3HYI&t=135s)** But what about if it's a Mac Mini or some other Mac system that you want to leave running 24-7

**[02:20](https://youtube.com/watch?v=833pTn_3HYI&t=140s)** as maybe a local LLM host or aplex media server or a room core instance? Well, as of this week

**[02:28](https://youtube.com/watch?v=833pTn_3HYI&t=148s)** with Mac OS Tahoe, we can now unlock the remote fire vault disk encrypted disks via SSH.

**[02:35](https://youtube.com/watch?v=833pTn_3HYI&t=155s)** Now, there is still no wake on LAN support, at least as far as I know for Mac OS. Please tell me

**[02:41](https://youtube.com/watch?v=833pTn_3HYI&t=161s)** I'm wrong down below because that's probably the final piece of this jigsaw for remote server

**[02:47](https://youtube.com/watch?v=833pTn_3HYI&t=167s)** administration. But this really has leveled up or completely removed a problem that has played

**[02:53](https://youtube.com/watch?v=833pTn_3HYI&t=173s)** those of us trying to use Apple hardware as small power efficient little servers. Now how do we set

**[02:59](https://youtube.com/watch?v=833pTn_3HYI&t=179s)** this up? It's actually pretty straightforward. So if we go into system preferences, wait, note they

**[03:04](https://youtube.com/watch?v=833pTn_3HYI&t=184s)** renamed it system settings. We want to then look for the sharing menu. So let's just type that in here.

**[03:14](https://youtube.com/watch?v=833pTn_3HYI&t=194s)** Next, we want to go to remote login. Check that box. That's it. That's what we have to do. Technically,

**[03:22](https://youtube.com/watch?v=833pTn_3HYI&t=202s)** I found that I had to actually go and do a successful SSH connection one time before I rebooted

**[03:31](https://youtube.com/watch?v=833pTn_3HYI&t=211s)** and then it worked. So what would what would we do here? I'm going to show you how this actually works

**[03:36](https://youtube.com/watch?v=833pTn_3HYI&t=216s)** on a real host. I have a Mac Studio downstairs which is on 10.42.7.213 and I have enabled

**[03:44](https://youtube.com/watch?v=833pTn_3HYI&t=224s)** remote access. So I can do sudo, Alex sudo, SSH, Alex at the IP address of that remote computer.

**[03:51](https://youtube.com/watch?v=833pTn_3HYI&t=231s)** Type in my password and I'm running on a Mac, right? Let me see if I've got fast fetch on there.

**[03:58](https://youtube.com/watch?v=833pTn_3HYI&t=238s)** I do. Okay, so so Mac Studio, M2 Macs running Mac OS has been up for 12 hours. Great.

**[04:03](https://youtube.com/watch?v=833pTn_3HYI&t=243s)** I am going to reboot that computer now and it has file vault turned on. So you'll see that now if I

**[04:09](https://youtube.com/watch?v=833pTn_3HYI&t=249s)** do 10.42.7.213, it's going to do the reboot process and then I'm going to sort of SSH into this

**[04:21](https://youtube.com/watch?v=833pTn_3HYI&t=261s)** kind of small pre-boot SSH server. It's this dedicated tiny little SSH server that runs in the

**[04:29](https://youtube.com/watch?v=833pTn_3HYI&t=269s)** pre-boot phase before any of the user space services actually come up. Now, with the ping,

**[04:34](https://youtube.com/watch?v=833pTn_3HYI&t=274s)** we can see that the reboot is happening slowly but surely. It's shut the Mac Studio down now and

**[04:41](https://youtube.com/watch?v=833pTn_3HYI&t=281s)** I guess it's doing that kind of post phase that I talked about where it's checking all the hardware,

**[04:46](https://youtube.com/watch?v=833pTn_3HYI&t=286s)** still exists, and kind of spinning up that micro SSH server in the pre-boot phase and there we go.

**[04:54](https://youtube.com/watch?v=833pTn_3HYI&t=294s)** It's the pre-boot phase now. So if I do the same thing again, SSH, Alex at 10.42.7.213,

**[05:02](https://youtube.com/watch?v=833pTn_3HYI&t=302s)** notice this, right? Notice this. The system is locked to unlock it, use a local account name and

**[05:10](https://youtube.com/watch?v=833pTn_3HYI&t=310s)** password. So I literally just type in the same password that I would type in at my desk downstairs

**[05:18](https://youtube.com/watch?v=833pTn_3HYI&t=318s)** and you'll see that the ping drop out for a second or two whilst it boots because the pre-boot SSH

**[05:25](https://youtube.com/watch?v=833pTn_3HYI&t=325s)** server terminates and then we end up in a user space SSH server instead. So I'm now going to do

**[05:31](https://youtube.com/watch?v=833pTn_3HYI&t=331s)** tailscaled ping Mac Studio because well, there we go. It's already booted. It does happen fast.

**[05:40](https://youtube.com/watch?v=833pTn_3HYI&t=340s)** So yeah, essentially, we've just done it right there in video in real time. We've rebooted a Mac

**[05:45](https://youtube.com/watch?v=833pTn_3HYI&t=345s)** and unlocked the file vault disk via SSH. So that's all you have to do in the sharing menu,

**[05:50](https://youtube.com/watch?v=833pTn_3HYI&t=350s)** just enable remote login, make sure you SSH into your host one time. I think so it like generates

**[05:58](https://youtube.com/watch?v=833pTn_3HYI&t=358s)** a bunch of like pre-shared keys and the node and host key and stuff like that the SSH uses.

**[06:03](https://youtube.com/watch?v=833pTn_3HYI&t=363s)** You can't use things like SSH keys like your public private key pair that you would normally use.

**[06:09](https://youtube.com/watch?v=833pTn_3HYI&t=369s)** You have to enter the password because that's what's unlocking the physical disk. So a couple of

**[06:14](https://youtube.com/watch?v=833pTn_3HYI&t=374s)** caveats, but nothing too, nothing too difficult to set up. I don't think remote login and you'll be

**[06:19](https://youtube.com/watch?v=833pTn_3HYI&t=379s)** good to go. Now, I did promise you that you can do this remotely from your phone. So let's run a ping

**[06:25](https://youtube.com/watch?v=833pTn_3HYI&t=385s)** to start with. This is going to be going through a subnet router that I have in my network and I've

**[06:30](https://youtube.com/watch?v=833pTn_3HYI&t=390s)** got a video about subnet routers up here, but essentially the concept is this. You are in a remote

**[06:36](https://youtube.com/watch?v=833pTn_3HYI&t=396s)** network and you want to connect to a device in this network that can't run tailscale. In this case,

**[06:42](https://youtube.com/watch?v=833pTn_3HYI&t=402s)** the Mac Studio isn't running tailscale because the user space services haven't started yet.

**[06:48](https://youtube.com/watch?v=833pTn_3HYI&t=408s)** And so what we need to do is have a device somewhere else in the network that can reach the Mac

**[06:54](https://youtube.com/watch?v=833pTn_3HYI&t=414s)** Studio on the local network because it's not running the tailscale client so it can't do all of

**[06:59](https://youtube.com/watch?v=833pTn_3HYI&t=419s)** the natural virtual magic that tailscale normally does. So you can see here, I've got a ping running

**[07:04](https://youtube.com/watch?v=833pTn_3HYI&t=424s)** and let me do this. I will do SSH Alex at 7.213, which is the Mac Studio downstairs. Fast fetch just

**[07:14](https://youtube.com/watch?v=833pTn_3HYI&t=434s)** to prove that. Yep. So now we'll do pseudo reboot and we will see in the pings up above that the

**[07:23](https://youtube.com/watch?v=833pTn_3HYI&t=443s)** Mac Studio is now going to reboot. So what I want to do is make sure that I'm connected to tailscale

**[07:28](https://youtube.com/watch?v=833pTn_3HYI&t=448s)** on my phone, first of all. So I'm going to open up the tailscale app on my phone, make sure that I'm

**[07:34](https://youtube.com/watch?v=833pTn_3HYI&t=454s)** logged into the same tailnet as the subnet router in this network. So this phone is on 5G, so effectively

**[07:42](https://youtube.com/watch?v=833pTn_3HYI&t=462s)** this is simulating that it could be anywhere in the world. It's not on this physical network. It's

**[07:48](https://youtube.com/watch?v=833pTn_3HYI&t=468s)** outside of the firewall here. So in order to reach the 10.42 subnet, you would have to either open

**[07:56](https://youtube.com/watch?v=833pTn_3HYI&t=476s)** a port in your firewall, which you definitely don't want to do for SSH or use the tailscale subnet

**[08:01](https://youtube.com/watch?v=833pTn_3HYI&t=481s)** router, which will run on an Apple TV or a Raspberry Pi or indeed any other headless system.

**[08:07](https://youtube.com/watch?v=833pTn_3HYI&t=487s)** Now what we want to do is verify that I can reach the Raspberry Pi. I'm going to press and hold

**[08:12](https://youtube.com/watch?v=833pTn_3HYI&t=492s)** on the Raspberry Pi and press ping. This is going to establish or at least try to establish a direct

**[08:16](https://youtube.com/watch?v=833pTn_3HYI&t=496s)** connection from my phone here over my cellular provider back to the Raspberry Pi. It's actually

**[08:22](https://youtube.com/watch?v=833pTn_3HYI&t=502s)** running on the bench just over there, but in order for this phone to talk to it, it has to go out

**[08:27](https://youtube.com/watch?v=833pTn_3HYI&t=507s)** over T-Mobile through their network and then in through AT&T and then in through their network and

**[08:32](https://youtube.com/watch?v=833pTn_3HYI&t=512s)** then it's a whole thing. Anyway, we're establishing a direct connection in 50 to 100ms from my phone here,

**[08:39](https://youtube.com/watch?v=833pTn_3HYI&t=519s)** does all that magic and ends up on the rack over there. So we have our way into my network from

**[08:45](https://youtube.com/watch?v=833pTn_3HYI&t=525s)** the outside. What we now need to do is use this app called Blink. This is an iOS shell app,

**[08:52](https://youtube.com/watch?v=833pTn_3HYI&t=532s)** gives me a terminal, it makes me feel like a real hacker. Now remember this phone is outside the

**[08:58](https://youtube.com/watch?v=833pTn_3HYI&t=538s)** network. I'm going to try and ping 7.213 and we can see that we do indeed get a ping, fantastic.

**[09:04](https://youtube.com/watch?v=833pTn_3HYI&t=544s)** So I'll now do SSH and then use my Mac username of Alex at that IP address. It's going to ask me

**[09:12](https://youtube.com/watch?v=833pTn_3HYI&t=552s)** for my password, which I will beautifully enter. This is the same one that I would enter at the

**[09:16](https://youtube.com/watch?v=833pTn_3HYI&t=556s)** physical keyboard in person. And you can see, you may now use SSH to authenticate normally. The

**[09:23](https://youtube.com/watch?v=833pTn_3HYI&t=563s)** system was successfully unlocked. So hypothetical scenario that I create for these videos, I'm out

**[09:30](https://youtube.com/watch?v=833pTn_3HYI&t=570s)** and about and I need to get into my Mac remotely or whatever. I can now do that from my phone and

**[09:35](https://youtube.com/watch?v=833pTn_3HYI&t=575s)** unlock the disk as you know. Now if I SSH again to that same IP address, it's going to once again

**[09:41](https://youtube.com/watch?v=833pTn_3HYI&t=581s)** ask me for my password, which I will again enter. But this time, it's logging me into the full

**[09:47](https://youtube.com/watch?v=833pTn_3HYI&t=587s)** user space session with all of my tools available like tail scale, like fast fetch, like rust desk,

**[09:54](https://youtube.com/watch?v=833pTn_3HYI&t=594s)** all of this stuff, right? And it's magic. And that's how you do it remotely. Now in order to set up

**[10:00](https://youtube.com/watch?v=833pTn_3HYI&t=600s)** a subnet router, it's quite a straightforward process. You want to make sure that you've got a Raspberry

**[10:06](https://youtube.com/watch?v=833pTn_3HYI&t=606s)** Pi, for example. So I'm going to do Z4 at Raspberry Pi, because that's the username I set on my

**[10:11](https://youtube.com/watch?v=833pTn_3HYI&t=611s)** Raspberry Pi. And then I'm going to want to do pseudo tail scale set. And then dash dash,

**[10:16](https://youtube.com/watch?v=833pTn_3HYI&t=616s)** advertise routes equals. And then the subnet that I want to expose. So in my case, that subnet is 10.42.0.0.0.21,

**[10:26](https://youtube.com/watch?v=833pTn_3HYI&t=626s)** 21, which means it's like six or seven thousand IP addresses available in this house for me to use

**[10:32](https://youtube.com/watch?v=833pTn_3HYI&t=632s)** all sorts of nonsense. Yours will probably look something like 192 168 1.0 slash 24. And you

**[10:43](https://youtube.com/watch?v=833pTn_3HYI&t=643s)** would find that out by going to IPA on the Raspberry Pi or whatever device you're running. And

**[10:48](https://youtube.com/watch?v=833pTn_3HYI&t=648s)** basically look for your DHCP range that your router is advertising. And you can see here that my

**[10:53](https://youtube.com/watch?v=833pTn_3HYI&t=653s)** Raspberry Pi is running in the 192 168 range. So yours will probably look something like that.

**[10:58](https://youtube.com/watch?v=833pTn_3HYI&t=658s)** I have to have two subnets going on here. I don't wish to confuse you, but I've got one VLAN

**[11:03](https://youtube.com/watch?v=833pTn_3HYI&t=663s)** on the 192 168 subnet that I usually use for these videos. And then my max studio is on my private

**[11:09](https://youtube.com/watch?v=833pTn_3HYI&t=669s)** subnet that I normally don't show on camera in the 10.42 subnet range. I appreciate that

**[11:15](https://youtube.com/watch?v=833pTn_3HYI&t=675s)** is over complicating the Pi today and probably not needed. But essentially what you want to do

**[11:21](https://youtube.com/watch?v=833pTn_3HYI&t=681s)** is tail scale set dash dash advertise routes equals and then whatever subnet your max studio or

**[11:29](https://youtube.com/watch?v=833pTn_3HYI&t=689s)** Mac mini or whatever Mac that you're trying to unlock remotely lives in. And once you've done that

**[11:34](https://youtube.com/watch?v=833pTn_3HYI&t=694s)** you have to go to tail scale admin console in your browser. The reason for that is that we don't

**[11:40](https://youtube.com/watch?v=833pTn_3HYI&t=700s)** normally allow people to publish routes without manually checking a box just to just a security really

**[11:46](https://youtube.com/watch?v=833pTn_3HYI&t=706s)** to make sure that you are who you say you are. So if I want to go to edit route settings and then if I

**[11:50](https://youtube.com/watch?v=833pTn_3HYI&t=710s)** uncheck this I have to make sure that these boxes are checked essentially. So I have to make sure

**[11:55](https://youtube.com/watch?v=833pTn_3HYI&t=715s)** that the subnets that I want to be advertised remotely are allowed to be forwarded through the

**[12:01](https://youtube.com/watch?v=833pTn_3HYI&t=721s)** Raspberry Pi so that when those packets come in from the outside they then get passed onto the correct

**[12:07](https://youtube.com/watch?v=833pTn_3HYI&t=727s)** destination. So that's really a very quick overview like I say I'll put links to documentation about

**[12:12](https://youtube.com/watch?v=833pTn_3HYI&t=732s)** subnet routers and links to videos and cards and all that kind of stuff throughout peppered throughout

**[12:17](https://youtube.com/watch?v=833pTn_3HYI&t=737s)** this video because it's it's a fairly straightforward topic once you get ahead around it but I'm

**[12:23](https://youtube.com/watch?v=833pTn_3HYI&t=743s)** aware that the first time you do it it's like you have to rewire a couple of new rock neurons so it

**[12:28](https://youtube.com/watch?v=833pTn_3HYI&t=748s)** it can take a beat and like I said there are videos up there and links in the description

**[12:33](https://youtube.com/watch?v=833pTn_3HYI&t=753s)** that should help you out. And probably speaking I think that's pretty much all you need to know

**[12:37](https://youtube.com/watch?v=833pTn_3HYI&t=757s)** just a reminder that in the pre-boot phase there isn't a full typical SSH server running

**[12:42](https://youtube.com/watch?v=833pTn_3HYI&t=762s)** no user space services so things like tail scale and rust desk and all the stuff you'd use to

**[12:47](https://youtube.com/watch?v=833pTn_3HYI&t=767s)** normally remotely access a Mac won't work but that's okay because with the subnet router that I

**[12:53](https://youtube.com/watch?v=833pTn_3HYI&t=773s)** just showed you we can tell tail scale to publish a route to your client devices that says hey if you

**[12:59](https://youtube.com/watch?v=833pTn_3HYI&t=779s)** try to make a request or a connection to this range of IPs or this IP and this specific subnet

**[13:05](https://youtube.com/watch?v=833pTn_3HYI&t=785s)** and you should probably try and send those packets via that subnet router over there and then

**[13:09](https://youtube.com/watch?v=833pTn_3HYI&t=789s)** those packets will appear as if they originated from the subnet router in my case the Raspberry Pi.

**[13:15](https://youtube.com/watch?v=833pTn_3HYI&t=795s)** And the real beauty of this is that the subnet router can be something as simple as an Apple TV

**[13:21](https://youtube.com/watch?v=833pTn_3HYI&t=801s)** or a Raspberry Pi in fact I have a video about Apple TVs and subnet routing up here.

**[13:25](https://youtube.com/watch?v=833pTn_3HYI&t=805s)** Now you can get subscribed to the channel for a bunch more videos about CICD and tail scale and how

**[13:30](https://youtube.com/watch?v=833pTn_3HYI&t=810s)** you can connect to all of your different devices together and as always you can go over to

**[13:33](https://youtube.com/watch?v=833pTn_3HYI&t=813s)** tailscale.com to get started today for free. We offer a hundred devices and three users for free

**[13:39](https://youtube.com/watch?v=833pTn_3HYI&t=819s)** on our free plan that we've committed will be free forever. As always thank you so much for

**[13:44](https://youtube.com/watch?v=833pTn_3HYI&t=824s)** watching and until next time I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
