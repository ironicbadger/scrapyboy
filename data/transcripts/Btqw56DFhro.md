---
video_id: "Btqw56DFhro"
title: "Remotely access any system with a PiKVM and Tailscale"
description: "Remotely accessing a physical system as if you are there was the reserve of expensive \"server grade\" gear until quite recently. PiKVM changes that. In today's video Alex will walk you through the proc..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-06-03"
duration_seconds: 1269
youtube_url: "https://www.youtube.com/watch?v=Btqw56DFhro"
thumbnail_url: "https://i.ytimg.com/vi/Btqw56DFhro/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:21:14.894617"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 4149
transcription_time_seconds: 36.3
---

# Remotely access any system with a PiKVM and Tailscale

**[00:00](https://youtube.com/watch?v=Btqw56DFhro&t=0s)** Welcome into today's video, everyone. I'm Alex from Tailscale. When building out a home lab or deploying some physical hardware in a remote location, we have to think about how we're going to look after that stuff when it breaks. Relying on walking friends or relatives through remote troubleshooting over FaceTime, admit it, we've all done it, isn't a super fun experience for either party. Now wouldn't it be great if we could just be at the console of this remote machine? Well, PyKVM is a free and open-source project, which lets us do just

**[00:30](https://youtube.com/watch?v=Btqw56DFhro&t=30s)** that. And in today's video, we're going to cover the basics of the PyKVM project and also walk you through the process of installing Tailscale on your PyKVM device. In so doing, we'll make it accessible from anywhere in your town at using Tailscale's natural virtual technology. As usual, there are chat to markers for you to find the bit of the video that you're looking for down below, as well as a bunch of links in the description too. But what is IPMI? Well, typically it's a remote management technology that's reserved for server-grade gear, serious stuff I promise.

**[01:00](https://youtube.com/watch?v=Btqw56DFhro&t=60s)** But PyKVM means you can actually now remotely manage pretty much any system with an HDMI port using nothing but a Raspberry Pi. This makes the pool of hardware available for such builds vastly bigger and more affordable. And a DIY PyKVM can be put together for as little as $100 US dollars. If you'd like to buy a pre-made package, you can find the latest PyKVM V4 starting at around $380 or so linked in the description down below. This might seem a bit steep at first until you look at other commercial PyKVM offerings.

**[01:30](https://youtube.com/watch?v=Btqw56DFhro&t=90s)** So in today's video, I'm going to walk you through the process of installing Tailscale on your PyKVM. And at the end, I'm going to talk you through how I use PyKVM with an 8 port physical hardware switch to use one Raspberry Pi to control 8 physical servers.

**[01:47](https://youtube.com/watch?v=Btqw56DFhro&t=107s)** The PyKVM project runs on a Raspberry Pi, hence the name I guess. And all you really need to make it work is an HDMI CSI bridge. So this takes an HDMI cable in one side and spits out over this ribbon cable into the camera connector on the motherboard of the Raspberry Pi, something that the PyKVM software can actually record and stream to you in a web browser.

**[02:09](https://youtube.com/watch?v=Btqw56DFhro&t=129s)** As well as the CSI bridge, you'll also need a USB power splitter. That's because the Raspberry Pi 4 only has one USB C port. And the developers of PyKVM use this port not only to power the device, but also to get the on-the-go serial information, USB serial information, from the remote host you're trying to connect to into the PyKVM software.

**[02:28](https://youtube.com/watch?v=Btqw56DFhro&t=148s)** So once you've got the hardware side of things configured, and I won't focus too much on that today because there's some great documentation over on the PyKVM side,

**[02:36](https://youtube.com/watch?v=Btqw56DFhro&t=156s)** you're presented with a web browser running some web software. So you can actually go to a website and IP address and access this remote computer in a browser. You don't need to install any software on the client device on my MacBook here, for example.

**[02:49](https://youtube.com/watch?v=Btqw56DFhro&t=169s)** So I jumped straight into the KVM tab, and I'm able to connect to a Windows host in another room, or I mean, ostensibly this could be anywhere in the world, but it just happens to be in this house on my tailnet.

**[03:01](https://youtube.com/watch?v=Btqw56DFhro&t=181s)** And this is running Windows 11, and I actually use this box as my Blue Iris NVR software, but you can do this with any computer that outputs a 1080p HDMI signal.

**[03:11](https://youtube.com/watch?v=Btqw56DFhro&t=191s)** And you can see that I've got full video access here, I've got keyboard and mouse control, so I can go into notepad++.

**[03:17](https://youtube.com/watch?v=Btqw56DFhro&t=197s)** Now I can't copy and paste between these devices, but what I can do along the top here is a bunch of options. I can go into this text box here, and I can paste in a bunch of PyKVM related text.

**[03:28](https://youtube.com/watch?v=Btqw56DFhro&t=208s)** And it's actually going to simulate 295 character presses, as if I was typing away furiously.

**[03:34](https://youtube.com/watch?v=Btqw56DFhro&t=214s)** So as you can see, it's just simulated 295 character presses for me. This could be really useful for things like zero numbers, that kind of thing.

**[03:41](https://youtube.com/watch?v=Btqw56DFhro&t=221s)** Now because PyKVM isn't running in software on the remote system, this is running on a Raspberry Pi next to the remote system, we can do all sorts of fun things like reboot the system and go directly into the BIOS.

**[03:54](https://youtube.com/watch?v=Btqw56DFhro&t=234s)** This is where PyKVM really differs from any other kind of remote software, and you can see I'm just going to jump straight into the BIOS here.

**[04:01](https://youtube.com/watch?v=Btqw56DFhro&t=241s)** I'm going to press the Escape key for the start-up menu, and then I'm going to press F10 to jump into the BIOS of the remote system.

**[04:08](https://youtube.com/watch?v=Btqw56DFhro&t=248s)** Just think about what's happening here. I am connected to a remote system through a Raspberry Pi over my tailnet, and I'm logged into the BIOS of a remote system, and I have full keyboard and mouse control.

**[04:21](https://youtube.com/watch?v=Btqw56DFhro&t=261s)** You just close my mind what's possible these days. You can see here I've got a 9500, a CPU 12 gigs around that kind of thing, and if I need to go in and change any of my device configuration in the BIOS,

**[04:33](https://youtube.com/watch?v=Btqw56DFhro&t=273s)** thankfully this system just works, and I don't need to go in and make any changes, so I'm going to reboot back now into the OS.

**[04:39](https://youtube.com/watch?v=Btqw56DFhro&t=279s)** And you'll see that I get the entire boot process from the post-screen right here all the way through the boot cycle, so I could actually use this to install an operating system if I wanted to on this remote system using this drive function that's up here.

**[04:53](https://youtube.com/watch?v=Btqw56DFhro&t=293s)** You can actually mount storage onto your remote system from your PiKVM as well.

**[04:57](https://youtube.com/watch?v=Btqw56DFhro&t=297s)** That's because the Pi is connected via USB to the remote host system, so you put a USB-C cable into the power port, and it's also acting as a data connection

**[05:07](https://youtube.com/watch?v=Btqw56DFhro&t=307s)** to the remote system as well using an on-the-go cable.

**[05:10](https://youtube.com/watch?v=Btqw56DFhro&t=310s)** And this allows you to attach remote storage to the remote node, so if I need to attach an ISO and boot into it to install the software, for example, I can go ahead and do that.

**[05:19](https://youtube.com/watch?v=Btqw56DFhro&t=319s)** Now I'm going to click on Connect Drive to Server, and you'll see in just a second, I think, yeah there we go, AutoPlay has opened up the ISO file on the remote windows host for me.

**[05:28](https://youtube.com/watch?v=Btqw56DFhro&t=328s)** So I'm going to walk you through the process now of installing tail scale on your PiKVM.

**[05:32](https://youtube.com/watch?v=Btqw56DFhro&t=332s)** Let's take a look at the documentation over here. So on PiKVM.org, they actually have over at docs.piKVM.org, a first steps page.

**[05:42](https://youtube.com/watch?v=Btqw56DFhro&t=342s)** This is really important if you have a completely fresh install of PiKVM, which is what I do.

**[05:48](https://youtube.com/watch?v=Btqw56DFhro&t=348s)** What we're going to do, first of all, is just update the OS. They have a section down here called PiKVM updating the OS.

**[05:54](https://youtube.com/watch?v=Btqw56DFhro&t=354s)** So I happen to know the IP address on my local network of the freshly installed PiKVM is 10.42.7.115.

**[06:04](https://youtube.com/watch?v=Btqw56DFhro&t=364s)** And you'll notice that I have a self-signed TLS certificate, so I get the warning of doom at the beginning.

**[06:11](https://youtube.com/watch?v=Btqw56DFhro&t=371s)** Also that the admin admin default password that PiKVM ships with is insecure to say the least.

**[06:19](https://youtube.com/watch?v=Btqw56DFhro&t=379s)** So we're going to go ahead and update the OS and change the password as well.

**[06:23](https://youtube.com/watch?v=Btqw56DFhro&t=383s)** So you can see here completely fresh install going to jump into the terminal, the web terminal right here.

**[06:29](https://youtube.com/watch?v=Btqw56DFhro&t=389s)** And it will jump us, it will drop us into this shell that has KVMD hyphen web term as the user.

**[06:35](https://youtube.com/watch?v=Btqw56DFhro&t=395s)** Now we can't do much as this user by design. So we're going to drop to root using SU space dash hyphen minus whatever you want to call it.

**[06:44](https://youtube.com/watch?v=Btqw56DFhro&t=404s)** I think there's another thing some people call it sometimes. And this password I can scarcely believe it is root.

**[06:51](https://youtube.com/watch?v=Btqw56DFhro&t=411s)** So to log into the web interface is admin admin and to get root access is root root.

**[06:57](https://youtube.com/watch?v=Btqw56DFhro&t=417s)** So we can go ahead and change that password right away by doing pass WD and typing your new super secure password.

**[07:05](https://youtube.com/watch?v=Btqw56DFhro&t=425s)** And now the root password is updated on the PiKVM. So that's great.

**[07:09](https://youtube.com/watch?v=Btqw56DFhro&t=429s)** Next thing we want to do is actually go ahead and update the OS. So jumping back to the PiKVM documentation.

**[07:15](https://youtube.com/watch?v=Btqw56DFhro&t=435s)** We can see they've got this command here. PiKVM underneath is running arch Linux which those of you that know the Linux world will know that it's a very fast moving Linux distribution.

**[07:27](https://youtube.com/watch?v=Btqw56DFhro&t=447s)** So you would typically just run Pacman minus SYU to do a full system update but in my experience running PiKVM in my home lab.

**[07:36](https://youtube.com/watch?v=Btqw56DFhro&t=456s)** There have been a couple occasions where things don't always go 100% smoothly doing that.

**[07:41](https://youtube.com/watch?v=Btqw56DFhro&t=461s)** So I would highly recommend sticking to the documented update path using this PiKVM update script that they have here.

**[07:49](https://youtube.com/watch?v=Btqw56DFhro&t=469s)** So let's jump back to our terminal and see if we have this available.

**[07:54](https://youtube.com/watch?v=Btqw56DFhro&t=474s)** No, we don't. So they give us another step to do here. So we need to enter read right mode.

**[08:00](https://youtube.com/watch?v=Btqw56DFhro&t=480s)** PiKVM boots into a read only mode. So in order to make changes to the file system such as doing updates, installing packages, changing configuration files.

**[08:09](https://youtube.com/watch?v=Btqw56DFhro&t=489s)** We actually need to use the RW command to switch to read right mode.

**[08:14](https://youtube.com/watch?v=Btqw56DFhro&t=494s)** It's all documented in the documentation on PiKVM just over here.

**[08:18](https://youtube.com/watch?v=Btqw56DFhro&t=498s)** The next thing to do is a Pacman minus SYU which forces all of the back end package repositories to do an update like a refresh from what's upstream.

**[08:28](https://youtube.com/watch?v=Btqw56DFhro&t=508s)** So this is analogous on certainly a Ubuntu type distributions to doing a apt update.

**[08:35](https://youtube.com/watch?v=Btqw56DFhro&t=515s)** Whereas the upgrade is the command that actually does the upgrade Pacman's got some other syntax.

**[08:39](https://youtube.com/watch?v=Btqw56DFhro&t=519s)** You could kind of chain these all together on Pacman if you wanted to with an SYU like this.

**[08:44](https://youtube.com/watch?v=Btqw56DFhro&t=524s)** But why why just forces all of these repos to be updated.

**[08:49](https://youtube.com/watch?v=Btqw56DFhro&t=529s)** Okay, now that's done. I'm going to do a Pacman minus S which is what we use to actually install packages on arch Linux.

**[08:55](https://youtube.com/watch?v=Btqw56DFhro&t=535s)** And then do a hyphen with PiKVM hyphen OS hyphen up data.

**[09:00](https://youtube.com/watch?v=Btqw56DFhro&t=540s)** This is going to install that upgrade helper script that I've talked about a few moments ago.

**[09:05](https://youtube.com/watch?v=Btqw56DFhro&t=545s)** Once that's done remember it's running from an SD card probably.

**[09:08](https://youtube.com/watch?v=Btqw56DFhro&t=548s)** So it's going to be a little bit slow.

**[09:10](https://youtube.com/watch?v=Btqw56DFhro&t=550s)** We're going to run the PiKVM up data update script.

**[09:16](https://youtube.com/watch?v=Btqw56DFhro&t=556s)** And it's going to go ahead and do its things.

**[09:18](https://youtube.com/watch?v=Btqw56DFhro&t=558s)** So quite a few packages to update.

**[09:20](https://youtube.com/watch?v=Btqw56DFhro&t=560s)** You can see for yourself right here 279 packages.

**[09:23](https://youtube.com/watch?v=Btqw56DFhro&t=563s)** So first of all it's going to go ahead and pull down those packages and then it will do the upgrade second.

**[09:28](https://youtube.com/watch?v=Btqw56DFhro&t=568s)** So I'll be right back when it's finished.

**[09:30](https://youtube.com/watch?v=Btqw56DFhro&t=570s)** And we're back. Okay, so the PiKVM has now rebooted.

**[09:34](https://youtube.com/watch?v=Btqw56DFhro&t=574s)** So I'm going to once again jump into the web terminal and again become root using the SYU space hyphen.

**[09:42](https://youtube.com/watch?v=Btqw56DFhro&t=582s)** Now we're going to actually install the tail scale package.

**[09:46](https://youtube.com/watch?v=Btqw56DFhro&t=586s)** Again, we need to enter read right mode and we're going to do a pack man minus SYU to refresh the package repositories if needed.

**[09:55](https://youtube.com/watch?v=Btqw56DFhro&t=595s)** Then we're going to install the tail scale hyphen PiKVM package.

**[10:00](https://youtube.com/watch?v=Btqw56DFhro&t=600s)** There are some PiKVM specific fixes in this package.

**[10:04](https://youtube.com/watch?v=Btqw56DFhro&t=604s)** Mostly to do with how the read only operating system is handled on a couple of system D units that kind of thing.

**[10:09](https://youtube.com/watch?v=Btqw56DFhro&t=609s)** I'll put a link in the description down below to the source code of this if you want to go and audit that for yourself.

**[10:14](https://youtube.com/watch?v=Btqw56DFhro&t=614s)** But to install it, it's just a case of a pack man minus SYU tail scale hyphen PiKVM going to go ahead and proceed with the installation.

**[10:22](https://youtube.com/watch?v=Btqw56DFhro&t=622s)** You can see it's going to install a couple of things.

**[10:24](https://youtube.com/watch?v=Btqw56DFhro&t=624s)** The tail scale 1.66.4 package as well as tail scale PiKVM, which is like a meta package provided by the PiKVM project.

**[10:32](https://youtube.com/watch?v=Btqw56DFhro&t=632s)** Once the tail scale package is installed, we need to go ahead and actually enable the tail scale demon.

**[10:39](https://youtube.com/watch?v=Btqw56DFhro&t=639s)** We do system CTL or system control or system cuttle, which are you? Let me know down in the comments.

**[10:46](https://youtube.com/watch?v=Btqw56DFhro&t=646s)** I'm always like a system CTL in my head and now I say it out loud for I think one of the first times.

**[10:51](https://youtube.com/watch?v=Btqw56DFhro&t=651s)** I'm like, which ones are you? Let me know, I'd love to know.

**[10:56](https://youtube.com/watch?v=Btqw56DFhro&t=656s)** System CTL, enable, tail scale D, dash dash now. This is a pretty neat trick actually.

**[11:03](https://youtube.com/watch?v=Btqw56DFhro&t=663s)** I only discovered this a few months ago. You can just enable a service by doing enable.

**[11:09](https://youtube.com/watch?v=Btqw56DFhro&t=669s)** All that does is it means the service will automatically start when the system boots.

**[11:14](https://youtube.com/watch?v=Btqw56DFhro&t=674s)** But if you do a dash dash now, it will enable the service and also start it as well.

**[11:19](https://youtube.com/watch?v=Btqw56DFhro&t=679s)** Typically what I was doing in the past was doing an enable and then a separate command of start.

**[11:24](https://youtube.com/watch?v=Btqw56DFhro&t=684s)** That's actually redundant. If we do, you can see I actually did the dash dash now on the second iteration.

**[11:30](https://youtube.com/watch?v=Btqw56DFhro&t=690s)** If we do a status of tail scale D here, you can see the tail scale demon is actually active and running in the background.

**[11:38](https://youtube.com/watch?v=Btqw56DFhro&t=698s)** Next we need to do a tail scale up and I'm just going to add dash dash SSH into here.

**[11:44](https://youtube.com/watch?v=Btqw56DFhro&t=704s)** This is totally optional, but I love tail scale SSH. It means I don't have to worry about putting SSH keys on this box

**[11:50](https://youtube.com/watch?v=Btqw56DFhro&t=710s)** and I can get to it from anywhere in my tail net that my ACLs permit.

**[11:53](https://youtube.com/watch?v=Btqw56DFhro&t=713s)** So I'm going to just put that as part of the initial login procedure.

**[11:56](https://youtube.com/watch?v=Btqw56DFhro&t=716s)** And I'm already logged into my tail net in this browser session.

**[11:59](https://youtube.com/watch?v=Btqw56DFhro&t=719s)** So I'm going to do a signing with Google, follow through with the tail and scales at gmail.com account.

**[12:04](https://youtube.com/watch?v=Btqw56DFhro&t=724s)** I always using these videos.

**[12:06](https://youtube.com/watch?v=Btqw56DFhro&t=726s)** And you can see that pi kvm is now logged into this tail net.

**[12:11](https://youtube.com/watch?v=Btqw56DFhro&t=731s)** So easy.

**[12:13](https://youtube.com/watch?v=Btqw56DFhro&t=733s)** Okay, cool. So I can now do tail scale status and see all of the other nodes in my tail net including things in Amazon.

**[12:20](https://youtube.com/watch?v=Btqw56DFhro&t=740s)** If I wanted to or this laptop, Baldric or my phone or whatever, I can now access this pi kvm from any of those devices.

**[12:29](https://youtube.com/watch?v=Btqw56DFhro&t=749s)** So we can take this a step further.

**[12:31](https://youtube.com/watch?v=Btqw56DFhro&t=751s)** You remember at the beginning when I said that there's a self-signed TLS certificate.

**[12:34](https://youtube.com/watch?v=Btqw56DFhro&t=754s)** So you get the warning of doom when you're trying to access a self-signed TLS certificate.

**[12:40](https://youtube.com/watch?v=Btqw56DFhro&t=760s)** We can use tail scale serve to actually automatically generate us electing crypt certificate for our tail scale DNS name.

**[12:48](https://youtube.com/watch?v=Btqw56DFhro&t=768s)** So what I'm going to do is just paste in a command I've got here tail scale serve dash dash BG HTTPS plus sign insecure and then local host and then proxy that on port 443.

**[12:59](https://youtube.com/watch?v=Btqw56DFhro&t=779s)** And you can see that right away.

**[13:01](https://youtube.com/watch?v=Btqw56DFhro&t=781s)** And we can now access our pi kvm on this domain name right here.

**[13:06](https://youtube.com/watch?v=Btqw56DFhro&t=786s)** Now the first time you click on this is going to take a few seconds, maybe 10 or 15 seconds or so.

**[13:11](https://youtube.com/watch?v=Btqw56DFhro&t=791s)** That's because in the background we're actually generating and doing that TLS certificate generation with let's encrypt via the ACME and Lego APIs.

**[13:20](https://youtube.com/watch?v=Btqw56DFhro&t=800s)** And you can see here.

**[13:21](https://youtube.com/watch?v=Btqw56DFhro&t=801s)** Here we go. My pi kvm is now on my tail net with a full on TLS certificate.

**[13:25](https://youtube.com/watch?v=Btqw56DFhro&t=805s)** We can actually verify that if we jump into the connection is secure certificate is valid boom.

**[13:30](https://youtube.com/watch?v=Btqw56DFhro&t=810s)** Now we can see let's encrypt for the pi kvm at velociraptor.

**[13:35](https://youtube.com/watch?v=Btqw56DFhro&t=815s)** By the way, if you're not familiar with all of this DNS stuff, we can actually just jump over to the admin console and I'll just talk you through it real quick.

**[13:41](https://youtube.com/watch?v=Btqw56DFhro&t=821s)** Every single tail scale domain account gets a name through the DNS option, the magic DNS option that's here.

**[13:49](https://youtube.com/watch?v=Btqw56DFhro&t=829s)** And now mine, I have already generated one that I like of velociraptor high for noodle fish and you can see that matches the certificate that we just generated from let's encrypt.

**[13:59](https://youtube.com/watch?v=Btqw56DFhro&t=839s)** And this name here, pi kvm, this matches the node name in your tail net.

**[14:04](https://youtube.com/watch?v=Btqw56DFhro&t=844s)** So if we jump back to the machines page of our tail net and typing pi kvm.

**[14:09](https://youtube.com/watch?v=Btqw56DFhro&t=849s)** We'll see here that this name here actually we should click on this drop down.

**[14:13](https://youtube.com/watch?v=Btqw56DFhro&t=853s)** You can see the fully qualified domain name right here, pi kvm dot velociraptor whatever.

**[14:18](https://youtube.com/watch?v=Btqw56DFhro&t=858s)** Now if you wanted to change that to be, you know, pi kvm 1, pi kvm 2, whatever if you've got multiple instances, you can do that right here.

**[14:25](https://youtube.com/watch?v=Btqw56DFhro&t=865s)** You can click on the three dot menu on the right and then going to edit machine name and do pi kvm on check this auto generate box.

**[14:32](https://youtube.com/watch?v=Btqw56DFhro&t=872s)** Of course, pi kvm 2 and it will say this machine will now be accessible here using magic DNS and pi kvm will no longer point to this machine.

**[14:40](https://youtube.com/watch?v=Btqw56DFhro&t=880s)** You'll also have to refresh the tail scale, serve stuff in the background, but hopefully that gives you an idea of some of the possibilities you can do with the magic DNS side of things.

**[14:48](https://youtube.com/watch?v=Btqw56DFhro&t=888s)** Now you just added a new node, probably an always on node to your tail net.

**[14:53](https://youtube.com/watch?v=Btqw56DFhro&t=893s)** So it's probably quite likely that you're going to want to do a couple of other things with this box to things like a subnet router.

**[15:00](https://youtube.com/watch?v=Btqw56DFhro&t=900s)** So that if you want to access other devices in this LAN without having to install tail scale on every single one, you could set this up as a subnet router.

**[15:08](https://youtube.com/watch?v=Btqw56DFhro&t=908s)** Same goes for setting pi kvm up as an exit node too.

**[15:12](https://youtube.com/watch?v=Btqw56DFhro&t=912s)** You can do that in the terminal because it's just Linux underneath the case arch Linux, but it's still real Linux, I promise, by the way.

**[15:19](https://youtube.com/watch?v=Btqw56DFhro&t=919s)** So in order to set up an exit node, of course, we have some documentation on that and there'll be a link to that in the description down below.

**[15:24](https://youtube.com/watch?v=Btqw56DFhro&t=924s)** But it's really quite a straightforward process, just a couple of commands.

**[15:27](https://youtube.com/watch?v=Btqw56DFhro&t=927s)** We need to make sure we're in root mode, first of all, same as we did before.

**[15:31](https://youtube.com/watch?v=Btqw56DFhro&t=931s)** And then we need to enable packet forwarding so that how this works underneath is we take every incoming packet to the pi kvm through the tail scale demon or through the tail scale network.

**[15:41](https://youtube.com/watch?v=Btqw56DFhro&t=941s)** And we rewrite those packets as if they're coming out through this device.

**[15:45](https://youtube.com/watch?v=Btqw56DFhro&t=945s)** And in order to do that, we've got to add a couple of bits into the CIS CTL configuration.

**[15:50](https://youtube.com/watch?v=Btqw56DFhro&t=950s)** So I'm going to paste these two lines in here that allow both IPv4 and IPv6 packet forwarding.

**[15:56](https://youtube.com/watch?v=Btqw56DFhro&t=956s)** And then I'm going to do CIS CTL hyphen P and just basically apply these changes right now instead of having to reboot.

**[16:05](https://youtube.com/watch?v=Btqw56DFhro&t=965s)** The last step is just using tail scale set.

**[16:08](https://youtube.com/watch?v=Btqw56DFhro&t=968s)** So this is the way that you would change the configuration of tail scale after it's installed.

**[16:12](https://youtube.com/watch?v=Btqw56DFhro&t=972s)** You can see all of the different options we got available to us here.

**[16:16](https://youtube.com/watch?v=Btqw56DFhro&t=976s)** And then I'll just do a dash dash advertise exit node.

**[16:21](https://youtube.com/watch?v=Btqw56DFhro&t=981s)** Now if we jump back to our tail scale machines page, we can see we've got an exit node button that's just appeared here waiting for approval.

**[16:29](https://youtube.com/watch?v=Btqw56DFhro&t=989s)** We'll click again on root settings and then check the box that says use as exit node.

**[16:34](https://youtube.com/watch?v=Btqw56DFhro&t=994s)** We'll see now that in my macOS client under exit nodes, I now have pi kvm as an option for exit nodes as well.

**[16:44](https://youtube.com/watch?v=Btqw56DFhro&t=1004s)** Now one last thing you might want to consider is because this is potentially going to be quite a critical piece of infrastructure for you.

**[16:50](https://youtube.com/watch?v=Btqw56DFhro&t=1010s)** I don't know what you're connecting this pi kvm to.

**[16:53](https://youtube.com/watch?v=Btqw56DFhro&t=1013s)** You might want to consider disabling key expiry.

**[16:56](https://youtube.com/watch?v=Btqw56DFhro&t=1016s)** By disabling key expiry, we don't end up rotating those wire guard keys that are underneath, you know, gluing everything together, making it all secure.

**[17:04](https://youtube.com/watch?v=Btqw56DFhro&t=1024s)** So it's totally up to you and your threat profile and that kind of thing.

**[17:08](https://youtube.com/watch?v=Btqw56DFhro&t=1028s)** But if this is a truly critical piece of infrastructure for you, I would probably encourage disabling key expiry and then going in and doing when you are physically at the console because this is probably going to be deployed remotely somewhere.

**[17:21](https://youtube.com/watch?v=Btqw56DFhro&t=1041s)** When you're physically at that building, just do a tail scale, log out, log in, and that will rotate the keys for you.

**[17:28](https://youtube.com/watch?v=Btqw56DFhro&t=1048s)** Now, there are some more advanced things you can do with pi kvm.

**[17:31](https://youtube.com/watch?v=Btqw56DFhro&t=1051s)** For example, in my basement, I've got about five or six servers down there that I all hook into a single pi kvm.

**[17:38](https://youtube.com/watch?v=Btqw56DFhro&t=1058s)** I have a network-based eight port kvm switch that I cost about $250, I think.

**[17:45](https://youtube.com/watch?v=Btqw56DFhro&t=1065s)** I'll put a link in the description down below to all of the details there.

**[17:48](https://youtube.com/watch?v=Btqw56DFhro&t=1068s)** But take no time put me on to this one actually. It's the TES smart or test smart. There's one to few S's.

**[17:54](https://youtube.com/watch?v=Btqw56DFhro&t=1074s)** Anyway, you can see here that I have a Proxmox virtual environment hooked into this specific pi kvm instance running in the basement.

**[18:02](https://youtube.com/watch?v=Btqw56DFhro&t=1082s)** But there's also a GPIO tab up here.

**[18:04](https://youtube.com/watch?v=Btqw56DFhro&t=1084s)** And if I want to change to a different server, all I have to do is click on this button and it will over the serial network connection configured in pi kvm.

**[18:13](https://youtube.com/watch?v=Btqw56DFhro&t=1093s)** Switch the inputs of the remote kvm instance.

**[18:16](https://youtube.com/watch?v=Btqw56DFhro&t=1096s)** There is an eight port physical unit in the rack downstairs.

**[18:19](https://youtube.com/watch?v=Btqw56DFhro&t=1099s)** And then the pi kvm is a separate unit hooked into the back of that.

**[18:23](https://youtube.com/watch?v=Btqw56DFhro&t=1103s)** And you can see I can just switch between multiple nodes.

**[18:25](https://youtube.com/watch?v=Btqw56DFhro&t=1105s)** You know, I've got one running NYXOS. I've got this one that's running Proxmox.

**[18:28](https://youtube.com/watch?v=Btqw56DFhro&t=1108s)** My HL15s turned off right now.

**[18:30](https://youtube.com/watch?v=Btqw56DFhro&t=1110s)** Zoydberg is running a bunch of my network services.

**[18:33](https://youtube.com/watch?v=Btqw56DFhro&t=1113s)** OpenSense, for example, doing a bunch of other stuff for me as well.

**[18:37](https://youtube.com/watch?v=Btqw56DFhro&t=1117s)** Of course, provided me with internet.

**[18:39](https://youtube.com/watch?v=Btqw56DFhro&t=1119s)** Using the TE Smart eight port HDMI switch, it has a little bit of extra configuration we've got to do inside pi kvm.

**[18:46](https://youtube.com/watch?v=Btqw56DFhro&t=1126s)** So we're going to jump back over to the web terminal, do SU- so we can become root once more.

**[18:52](https://youtube.com/watch?v=Btqw56DFhro&t=1132s)** And then I'm just going to show you this one file, kvmdoverride.yaml.

**[18:58](https://youtube.com/watch?v=Btqw56DFhro&t=1138s)** And in this file, this defines everything that pi kvm knows about the remote physical switch that it wants to switch the inputs of.

**[19:07](https://youtube.com/watch?v=Btqw56DFhro&t=1147s)** So you can see, first of all, we're giving the names of these devices in a table here, also which LEDs and which buttons are mapped to which devices.

**[19:16](https://youtube.com/watch?v=Btqw56DFhro&t=1156s)** And scroll all the way back up here because there are eight switches plus a couple of others to reboot pi kvm itself and restart the service.

**[19:23](https://youtube.com/watch?v=Btqw56DFhro&t=1163s)** But you can see just at the top, this is how it's over GPIO.

**[19:27](https://youtube.com/watch?v=Btqw56DFhro&t=1167s)** It's a network serial GPIO configuration.

**[19:30](https://youtube.com/watch?v=Btqw56DFhro&t=1170s)** It's talking to the TE Smart switch on the IP address 10.42.0.7.

**[19:36](https://youtube.com/watch?v=Btqw56DFhro&t=1176s)** And that is how the switching is done.

**[19:38](https://youtube.com/watch?v=Btqw56DFhro&t=1178s)** The pi kvm project even has an entire page dedicated to these multi port kvm over IP switches.

**[19:44](https://youtube.com/watch?v=Btqw56DFhro&t=1184s)** The one that I'm using is on their compatibility matrix here. It is the TE Smart eight port one that's right here.

**[19:52](https://youtube.com/watch?v=Btqw56DFhro&t=1192s)** Now, configuring this thing was a bit of a pain in the backside.

**[19:56](https://youtube.com/watch?v=Btqw56DFhro&t=1196s)** I had to use a Windows VM and run some crusty old app to actually statically IP configure the switch to be what I needed it to be, all that kind of stuff.

**[20:05](https://youtube.com/watch?v=Btqw56DFhro&t=1205s)** Once you get over that initial configuration, which took about 10 or 15 minutes, it's been no problem and it's been nice and stable for me for many months now.

**[20:13](https://youtube.com/watch?v=Btqw56DFhro&t=1213s)** I would also point you to look down the bottom of this page, the limitation section specifically most importantly at least for me was the HDMI back power situation.

**[20:23](https://youtube.com/watch?v=Btqw56DFhro&t=1223s)** I did this with a four port version several months ago and I ran into some really weird issues with things back powering each other and switching and doing things they shouldn't do.

**[20:32](https://youtube.com/watch?v=Btqw56DFhro&t=1232s)** So just pay attention to the compatibility matrix and you should be good to go.

**[20:36](https://youtube.com/watch?v=Btqw56DFhro&t=1236s)** So, you know, you get the idea that, you know, I can just have one box here. I've got one pi kvm controlling up to eight systems.

**[20:44](https://youtube.com/watch?v=Btqw56DFhro&t=1244s)** That makes the initial price a little bit easier to swallow, doesn't it?

**[20:48](https://youtube.com/watch?v=Btqw56DFhro&t=1248s)** So there we are. That's how we installed tail scale on a pi kvm.

**[20:52](https://youtube.com/watch?v=Btqw56DFhro&t=1252s)** As always, thank you so much for watching and don't forget to check the description down below for all the links of the things I just talked about, particularly that eight port hardware kvm switch.

**[21:00](https://youtube.com/watch?v=Btqw56DFhro&t=1260s)** Until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
