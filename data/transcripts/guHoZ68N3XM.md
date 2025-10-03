---
video_id: "guHoZ68N3XM"
title: "Complete beginners guide to self-hosting | Part 2 Installing Immich, Audiobookshelf + Home Assistant"
description: "This video is for you if you're a complete beginner who is curious about getting into self-hosting services.

In this part 2 of a new multi-part series for the channel Alex will pick up where we left ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-06-05"
duration_seconds: 3779
youtube_url: "https://www.youtube.com/watch?v=guHoZ68N3XM"
thumbnail_url: "https://i.ytimg.com/vi/guHoZ68N3XM/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:22:20.358799"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 11858
transcription_time_seconds: 107.7
---

# Complete beginners guide to self-hosting | Part 2 Installing Immich, Audiobookshelf + Home Assistant

**[00:00](https://youtube.com/watch?v=guHoZ68N3XM&t=0s)** It's time for part two in our complete beginner's guide to self-hosting. My name's Alex, and I'm from Tailscale. In part one, I showed you how to install Proxmox, a hypervisor OS, onto this little Dell small form factor PC. I'll put a link to that video up here. In today's video though, I'm going to show you how to get started installing a bunch of applications, image to replace Google photos, audio bookshelf to replace audible, and then home assistant to get started with self-hosted privacy respecting open source home automation.

**[00:30](https://youtube.com/watch?v=guHoZ68N3XM&t=30s)** I'll also show you how to access all of those things from wherever you are in the world on your phone over 5G, and you can be on holiday on the other side of the world, and still connect back to this little box running under your stairs over Tailscale completely for free. So, that's what we're going to do in today's video. We're going to show you how to install a bunch of applications, and get started with self-hosting and Tailscale.

**[00:52](https://youtube.com/watch?v=guHoZ68N3XM&t=52s)** Okay, so let's pick things up exactly where we left them a couple of weeks ago. This is a completely fresh Proxmox install. I'm connected to the, essentially I'm using JetKVM here, as if it's a keyboard monitor and mouse, physically plugged into the device to record the screen so I can show you on video. This is exactly the same as if you had literally those physical things on the table in front of you, except I can see it in a web browser. So you can see here, when we boot into Proxmox for the first time, we get a IP address.

**[01:21](https://youtube.com/watch?v=guHoZ68N3XM&t=81s)** IP address, you can kind of think about a little bit analogous to, like an apartment building, for example, like the address of an apartment building, and then the port number, which here is denoted by 80006, that's the apartment within the building.

**[01:36](https://youtube.com/watch?v=guHoZ68N3XM&t=96s)** So you've got the apartment building of 192168.1.10, and then the apartment or the service that we want to access within that building running on port 80006.

**[01:46](https://youtube.com/watch?v=guHoZ68N3XM&t=106s)** So what we do with that information is we take this string here, and we type it into our web browser over here.

**[01:51](https://youtube.com/watch?v=guHoZ68N3XM&t=111s)** So we do HTTPS, colon slash slash 1921681.10, colon 8000 and 6.

**[01:59](https://youtube.com/watch?v=guHoZ68N3XM&t=119s)** We'll probably get the scary. This is an HTTPS on self-signed certificate.

**[02:04](https://youtube.com/watch?v=guHoZ68N3XM&t=124s)** The world's about to end error. Don't worry about that. It's fine. You can just click through.

**[02:08](https://youtube.com/watch?v=guHoZ68N3XM&t=128s)** We're going to deal with how to get rid of that error in the next section.

**[02:11](https://youtube.com/watch?v=guHoZ68N3XM&t=131s)** This section, technically I suppose, because what we're going to do first is installing tail scale.

**[02:16](https://youtube.com/watch?v=guHoZ68N3XM&t=136s)** I've got like a little cheat sheet here, which I'll probably put this document into the GitHub repo.

**[02:23](https://youtube.com/watch?v=guHoZ68N3XM&t=143s)** All of my videos have code snippets, or most of them have code snippets, and like a running order of what's going on.

**[02:30](https://youtube.com/watch?v=guHoZ68N3XM&t=150s)** So I'm going to put this script, this document into the GitHub repo, which will be linked in the description down below.

**[02:36](https://youtube.com/watch?v=guHoZ68N3XM&t=156s)** And as best as I can manage, I'm not going to edit each chapter, because there'll be chapters in the description.

**[02:41](https://youtube.com/watch?v=guHoZ68N3XM&t=161s)** So you can skip to the part of the video that you want.

**[02:44](https://youtube.com/watch?v=guHoZ68N3XM&t=164s)** So to start with, we're going to talk about installing tail scale and how to set up tail scale SSH.

**[02:49](https://youtube.com/watch?v=guHoZ68N3XM&t=169s)** We should probably talk about also setting up a TLS certificate using serve so that we don't have to worry about a reverse proxy.

**[02:57](https://youtube.com/watch?v=guHoZ68N3XM&t=177s)** We'll come on to all that stuff later. Then we'll install Docker.

**[03:00](https://youtube.com/watch?v=guHoZ68N3XM&t=180s)** We're going to partition our data disks, install image.

**[03:03](https://youtube.com/watch?v=guHoZ68N3XM&t=183s)** There's a lot to do today. So it's going to be quite a long video, hence make liberal use of the chapters.

**[03:10](https://youtube.com/watch?v=guHoZ68N3XM&t=190s)** So we want to get logged in now to our proxmox installation using our username and password.

**[03:17](https://youtube.com/watch?v=guHoZ68N3XM&t=197s)** I think I actually set a different password.

**[03:20](https://youtube.com/watch?v=guHoZ68N3XM&t=200s)** I do actually, by the way, have a video on how to, you can probably find that up here, on how to configure proxmox to log in using your tail scale identity,

**[03:27](https://youtube.com/watch?v=guHoZ68N3XM&t=207s)** instead of a username and password.

**[03:29](https://youtube.com/watch?v=guHoZ68N3XM&t=209s)** But we're in that kind of classic chicken and egg problem right now where we don't have tail scale installed on the node.

**[03:36](https://youtube.com/watch?v=guHoZ68N3XM&t=216s)** So we can't use it.

**[03:38](https://youtube.com/watch?v=guHoZ68N3XM&t=218s)** Also, this is a beginner's guide and that replacing authentication is probably step seven, maybe even step 17, and we're on step one here.

**[03:47](https://youtube.com/watch?v=guHoZ68N3XM&t=227s)** So just get logged in with the username and password and you should be all good.

**[03:51](https://youtube.com/watch?v=guHoZ68N3XM&t=231s)** Now, that little subscription nag there, back when I was a proxmox junior several years ago now,

**[03:57](https://youtube.com/watch?v=guHoZ68N3XM&t=237s)** I thought that meant you had to pay for proxmox. Don't worry, it's completely free.

**[04:01](https://youtube.com/watch?v=guHoZ68N3XM&t=241s)** That little subscription nag is only there to remind you to contribute to the upstream project.

**[04:07](https://youtube.com/watch?v=guHoZ68N3XM&t=247s)** Should you wish to, you don't have to pay them a single penny.

**[04:11](https://youtube.com/watch?v=guHoZ68N3XM&t=251s)** Now, in order to make that subscription nag and everything else like go away properly, I think I showed you this in part one,

**[04:17](https://youtube.com/watch?v=guHoZ68N3XM&t=257s)** but just a quick recap, you can go to help us scripts.com and search for post install.

**[04:24](https://youtube.com/watch?v=guHoZ68N3XM&t=264s)** And then you can run this little script against your proxmox server by taking it onto your clipboard, copying it and going to the node, clicking on Shell.

**[04:33](https://youtube.com/watch?v=guHoZ68N3XM&t=273s)** And this is giving you a command line interface effectively like a remote shell to control that remote proxmox instance.

**[04:40](https://youtube.com/watch?v=guHoZ68N3XM&t=280s)** You can then copy and paste it onto the terminal and go through.

**[04:43](https://youtube.com/watch?v=guHoZ68N3XM&t=283s)** So I'm going to start the install script. Yes. I'm going to correct my sources. Yeah, yeah, yeah.

**[04:49](https://youtube.com/watch?v=guHoZ68N3XM&t=289s)** Disabled, yeah, enable high availability. No, this time I made a mistake in the last video, which so many people will lovely people pointed out.

**[04:57](https://youtube.com/watch?v=guHoZ68N3XM&t=297s)** Do I want to update it now? No, do I want to reboot now? No. So I'm going to do is do an apt update.

**[05:03](https://youtube.com/watch?v=guHoZ68N3XM&t=303s)** And then the next thing that proxmox we should do, because it's been a couple of weeks since I touched this system actually,

**[05:09](https://youtube.com/watch?v=guHoZ68N3XM&t=309s)** is we're going to run PVE upgrades. Typically what you would do is apt upgrade with a Debian system, which is of course what proxmox is based on.

**[05:17](https://youtube.com/watch?v=guHoZ68N3XM&t=317s)** But the proxmox project recommend that you use PVE upgrade. There's some proxmox specific stuff it doesn't the background.

**[05:24](https://youtube.com/watch?v=guHoZ68N3XM&t=324s)** And you can see we're going to get a new kernel, we're going to get a whole bunch of new packages.

**[05:29](https://youtube.com/watch?v=guHoZ68N3XM&t=329s)** And essentially it's just good, just good practice to make sure that your box is up to date before you start doing anything else.

**[05:35](https://youtube.com/watch?v=guHoZ68N3XM&t=335s)** So this will take a couple of minutes. I think for the most part, I'm going to leave this video unedited.

**[05:40](https://youtube.com/watch?v=guHoZ68N3XM&t=340s)** But when there's like a two, three minute long bit of text scrolling by, I think I'll do a cut. So see you shortly.

**[05:48](https://youtube.com/watch?v=guHoZ68N3XM&t=348s)** Okay, and we're back. I went ahead and rebooted the node after the packages had all installed because we've got a new kernel.

**[05:55](https://youtube.com/watch?v=guHoZ68N3XM&t=355s)** I followed that process over here in JetKVM. But now if I refresh this page, we are back and we are good to go.

**[06:02](https://youtube.com/watch?v=guHoZ68N3XM&t=362s)** So what do we need to do now? We want to install tail scale for a couple of reasons.

**[06:07](https://youtube.com/watch?v=guHoZ68N3XM&t=367s)** First of all, I don't want to be managing SSH keys like in this directory here, you can see authorized keys.

**[06:13](https://youtube.com/watch?v=guHoZ68N3XM&t=373s)** There's nothing in that file. So I'm probably jumping ahead here. What is an SSH key Alex? Okay.

**[06:19](https://youtube.com/watch?v=guHoZ68N3XM&t=379s)** So typically when you're authenticating with SSH to a remote server, there has to be some kind of way for you to prove you are who you say you are.

**[06:28](https://youtube.com/watch?v=guHoZ68N3XM&t=388s)** Typically, we do that either with a username or password or we do that with something called an SSH key.

**[06:34](https://youtube.com/watch?v=guHoZ68N3XM&t=394s)** This uses the PKI, the public key infrastructure and a concepts of Alison Bob to make a key really easy to reverse engineer in one direction, but hard to work out in the other direction.

**[06:46](https://youtube.com/watch?v=guHoZ68N3XM&t=406s)** So the public and private key pairs come together to basically prove that I am who I say I am.

**[06:52](https://youtube.com/watch?v=guHoZ68N3XM&t=412s)** But that means you have to manage SSH keys, which let's be honest is if you're familiar with the topic, it's kind of a pain.

**[07:01](https://youtube.com/watch?v=guHoZ68N3XM&t=421s)** But with tail scale SSH, there are no use names, well, there are use names, there are no passwords, there are no SSH keys or anything like that.

**[07:08](https://youtube.com/watch?v=guHoZ68N3XM&t=428s)** So first of all, that's why I want to get tail scale on here.

**[07:11](https://youtube.com/watch?v=guHoZ68N3XM&t=431s)** Secondly, is I want to use tail scale serve so we don't have to worry about this pesky insecure message at the top here as well.

**[07:17](https://youtube.com/watch?v=guHoZ68N3XM&t=437s)** And then of course, if this is a note on my tail net, then of course, I can access any of the services running on this box from anywhere I like, such as my phone when I take a picture and have it upload my Google photos, self hosted clone.

**[07:30](https://youtube.com/watch?v=guHoZ68N3XM&t=450s)** For example, so let's head over to tailscale.com slash download and we're going to get the Linux install script from here.

**[07:39](https://youtube.com/watch?v=guHoZ68N3XM&t=459s)** I'm going to copy that onto our clipboard, go back to proxmox and paste that in just here.

**[07:44](https://youtube.com/watch?v=guHoZ68N3XM&t=464s)** This will take 10, 15 seconds to install.

**[07:49](https://youtube.com/watch?v=guHoZ68N3XM&t=469s)** So now we need to log in and create this node or add this node to our tail net.

**[07:53](https://youtube.com/watch?v=guHoZ68N3XM&t=473s)** So we want to go to tailscale.com, no download this time.

**[07:57](https://youtube.com/watch?v=guHoZ68N3XM&t=477s)** And in the top right hand corner, if you don't already have a tail net, you can click on this button, get started, it's free.

**[08:03](https://youtube.com/watch?v=guHoZ68N3XM&t=483s)** There are 100 devices and three users for free.

**[08:06](https://youtube.com/watch?v=guHoZ68N3XM&t=486s)** And we've made a commitment that this will always be free as well.

**[08:10](https://youtube.com/watch?v=guHoZ68N3XM&t=490s)** So you don't need to worry about rug pools and all that kind of stuff in the future.

**[08:14](https://youtube.com/watch?v=guHoZ68N3XM&t=494s)** I already have a tail net, of course, you know, might be biased, but I want to click on my admin console just here.

**[08:21](https://youtube.com/watch?v=guHoZ68N3XM&t=501s)** And then you can see that actually this is a demo instance of PVE. So I'm going to delete that.

**[08:26](https://youtube.com/watch?v=guHoZ68N3XM&t=506s)** But you can see I've literally only got two devices in my tail net right now.

**[08:29](https://youtube.com/watch?v=guHoZ68N3XM&t=509s)** This laptop that I'm connected from, Baldric.

**[08:32](https://youtube.com/watch?v=guHoZ68N3XM&t=512s)** And the other one is my gaming rig downstairs.

**[08:34](https://youtube.com/watch?v=guHoZ68N3XM&t=514s)** So I like to stream video games sometimes over tailscale using one of the Artemis and Moonlight Sunshine, all that stuff.

**[08:41](https://youtube.com/watch?v=guHoZ68N3XM&t=521s)** I've got a video coming on that soon.

**[08:43](https://youtube.com/watch?v=guHoZ68N3XM&t=523s)** So get subscribed, you know, like comments, subscribe, all that good stuff.

**[08:48](https://youtube.com/watch?v=guHoZ68N3XM&t=528s)** So now we are logged in in the browser.

**[08:50](https://youtube.com/watch?v=guHoZ68N3XM&t=530s)** Let's go back to Proxmox and we're going to do tailscale up dash dash two dashes is important SSH.

**[08:58](https://youtube.com/watch?v=guHoZ68N3XM&t=538s)** This is going to give us a URL, which we're going to copy onto our clipboard and paste into the browser.

**[09:03](https://youtube.com/watch?v=guHoZ68N3XM&t=543s)** It's then going to ask me to authenticate to my tail scale account, in which in this case my authentication is done through Gmail.

**[09:11](https://youtube.com/watch?v=guHoZ68N3XM&t=551s)** That bit's not important. Obviously you can use whatever author provider you like when you set up your tail net.

**[09:16](https://youtube.com/watch?v=guHoZ68N3XM&t=556s)** But I just found Gmail the most convenient for these tutorials.

**[09:20](https://youtube.com/watch?v=guHoZ68N3XM&t=560s)** And if we click now on visit console, you'll see that I have the PVE node is now on my tail net.

**[09:27](https://youtube.com/watch?v=guHoZ68N3XM&t=567s)** So time for the big reveal, so far as SSH is concerned at least, I'm now going to do SSH root at PVE.

**[09:35](https://youtube.com/watch?v=guHoZ68N3XM&t=575s)** And that name that string, by the way, must match the name that is specified here.

**[09:39](https://youtube.com/watch?v=guHoZ68N3XM&t=579s)** So I could do the IP address if I want to.

**[09:41](https://youtube.com/watch?v=guHoZ68N3XM&t=581s)** I could do the fully qualified host name of Velociraptor, high for noodle fish.

**[09:45](https://youtube.com/watch?v=guHoZ68N3XM&t=585s)** Or I can just do the node name itself, which is what I'm going to do here.

**[09:49](https://youtube.com/watch?v=guHoZ68N3XM&t=589s)** So SSH root at PVE knows names, no passwords, no SSH keys.

**[09:54](https://youtube.com/watch?v=guHoZ68N3XM&t=594s)** And I'm logged in to my proxmox instance.

**[09:58](https://youtube.com/watch?v=guHoZ68N3XM&t=598s)** Come on, that's pretty cool.

**[10:00](https://youtube.com/watch?v=guHoZ68N3XM&t=600s)** So now we want to get rid of the self-signed TLS certificate.

**[10:04](https://youtube.com/watch?v=guHoZ68N3XM&t=604s)** Now there are two ways we can do this actually.

**[10:06](https://youtube.com/watch?v=guHoZ68N3XM&t=606s)** If we looking Google for tail scale proxmox, we have an article on tail scale on a proxmox host.

**[10:12](https://youtube.com/watch?v=guHoZ68N3XM&t=612s)** And there are two things we can do.

**[10:14](https://youtube.com/watch?v=guHoZ68N3XM&t=614s)** One of them is to enable HTTP access from the proxmox web UI is run this little script here.

**[10:19](https://youtube.com/watch?v=guHoZ68N3XM&t=619s)** We can generate a tail scale certificate and install it into the proxmox.

**[10:23](https://youtube.com/watch?v=guHoZ68N3XM&t=623s)** I guess the key store certificate store.

**[10:25](https://youtube.com/watch?v=guHoZ68N3XM&t=625s)** Or we can just press easy mode and use tail scale serve.

**[10:29](https://youtube.com/watch?v=guHoZ68N3XM&t=629s)** So I guess what I'm going to do.

**[10:31](https://youtube.com/watch?v=guHoZ68N3XM&t=631s)** I'm going to do easy mode.

**[10:33](https://youtube.com/watch?v=guHoZ68N3XM&t=633s)** I'm going to do pseudo tail scale serve.

**[10:35](https://youtube.com/watch?v=guHoZ68N3XM&t=635s)** Go back to my instance.

**[10:37](https://youtube.com/watch?v=guHoZ68N3XM&t=637s)** Copy that and put that on the clipboard.

**[10:39](https://youtube.com/watch?v=guHoZ68N3XM&t=639s)** So it's not found.

**[10:41](https://youtube.com/watch?v=guHoZ68N3XM&t=641s)** Well, I'm rude anyway, so it doesn't matter.

**[10:43](https://youtube.com/watch?v=guHoZ68N3XM&t=643s)** Sudo, by the way, elevates your privileges if you're not familiar with what pseudo does.

**[10:47](https://youtube.com/watch?v=guHoZ68N3XM&t=647s)** You see from being like a standard user, so like Alex, and turns you into a super user.

**[10:51](https://youtube.com/watch?v=guHoZ68N3XM&t=651s)** Super user do.

**[10:53](https://youtube.com/watch?v=guHoZ68N3XM&t=653s)** So SUDO pseudo.

**[10:55](https://youtube.com/watch?v=guHoZ68N3XM&t=655s)** But now you can see that I have a new node on my tail net that I can actually access with a TLS certificate.

**[11:01](https://youtube.com/watch?v=guHoZ68N3XM&t=661s)** So if I have this domain name here of PvE for a loss of Raptor, if I copy that onto my clipboard.

**[11:07](https://youtube.com/watch?v=guHoZ68N3XM&t=667s)** Now this will take 10, 15, 20 seconds the first time, because tail scale now on the back end is reaching out to a certificate provider called Let's Encrypt.

**[11:16](https://youtube.com/watch?v=guHoZ68N3XM&t=676s)** which is completely free.

**[11:18](https://youtube.com/watch?v=guHoZ68N3XM&t=678s)** And generating you a TLS or an HTTPS certificate and encryption certificate.

**[11:24](https://youtube.com/watch?v=guHoZ68N3XM&t=684s)** And there you go.

**[11:26](https://youtube.com/watch?v=guHoZ68N3XM&t=686s)** In real time, there were no cuts or edits there.

**[11:28](https://youtube.com/watch?v=guHoZ68N3XM&t=688s)** You can see that I'm now accessing my Proxmox installation over tail scale with a certificate.

**[11:34](https://youtube.com/watch?v=guHoZ68N3XM&t=694s)** Now a couple of important things I want to point out.

**[11:36](https://youtube.com/watch?v=guHoZ68N3XM&t=696s)** This address is only available within your tail net.

**[11:40](https://youtube.com/watch?v=guHoZ68N3XM&t=700s)** Tail scale also offer a product called tail scale serve.

**[11:44](https://youtube.com/watch?v=guHoZ68N3XM&t=704s)** I say products, it makes it sound like it costs money.

**[11:46](https://youtube.com/watch?v=guHoZ68N3XM&t=706s)** It doesn't. It's free. It's on the free tier.

**[11:48](https://youtube.com/watch?v=guHoZ68N3XM&t=708s)** But tail scale funnel does the exact same thing as serve, except it makes it available on the public internet.

**[11:54](https://youtube.com/watch?v=guHoZ68N3XM&t=714s)** Now please don't go and put your Proxmox server on the public internet.

**[11:58](https://youtube.com/watch?v=guHoZ68N3XM&t=718s)** It's just not a good idea for many, many reasons.

**[12:02](https://youtube.com/watch?v=guHoZ68N3XM&t=722s)** Just don't do it.

**[12:03](https://youtube.com/watch?v=guHoZ68N3XM&t=723s)** But if you have an application you want to share with friends and family who aren't using tail scale for some reason,

**[12:08](https://youtube.com/watch?v=guHoZ68N3XM&t=728s)** or you want to share a prototype of a website you're working on or a project you have hosted locally

**[12:12](https://youtube.com/watch?v=guHoZ68N3XM&t=732s)** with somebody from your laptop or whatever, tail scale funnel is designed and works really well for that use case.

**[12:18](https://youtube.com/watch?v=guHoZ68N3XM&t=738s)** It's not very well suited to long running use cases like hosting stuff like a Proxmox interface or something like that.

**[12:26](https://youtube.com/watch?v=guHoZ68N3XM&t=746s)** So anyway, back to the point, tail scale serve makes this interface or of the Proxmox UI available within your tail net.

**[12:36](https://youtube.com/watch?v=guHoZ68N3XM&t=756s)** So now anywhere you are connected to tail scale, you can also now connect to your Proxmox instance using this fully qualified domain name.

**[12:46](https://youtube.com/watch?v=guHoZ68N3XM&t=766s)** Now use that phrase quite a lot. You might see FQDN in a lot of stuff.

**[12:50](https://youtube.com/watch?v=guHoZ68N3XM&t=770s)** That's what it means.

**[12:51](https://youtube.com/watch?v=guHoZ68N3XM&t=771s)** The fully qualified domain name here of the loss of rap to high for noodle fish dot TS dot net.

**[12:57](https://youtube.com/watch?v=guHoZ68N3XM&t=777s)** That's the fully qualified domain name.

**[12:59](https://youtube.com/watch?v=guHoZ68N3XM&t=779s)** Now a couple of things I didn't mention which I probably should do before we get off this topic under DNS.

**[13:05](https://youtube.com/watch?v=guHoZ68N3XM&t=785s)** You've got to make sure that you have a tail net name. So by default out of the box, all tail nets come with this kind of like placeholder name.

**[13:12](https://youtube.com/watch?v=guHoZ68N3XM&t=792s)** It's not memorable. It's a little bit ugly, but you get it for free.

**[13:16](https://youtube.com/watch?v=guHoZ68N3XM&t=796s)** You also get a real name for free or something with a tail and something with scales.

**[13:21](https://youtube.com/watch?v=guHoZ68N3XM&t=801s)** If you roll the dice and come up with a unique name for your tail net, too. So go ahead and make that change there.

**[13:27](https://youtube.com/watch?v=guHoZ68N3XM&t=807s)** In order to actually utilize the DNS name and the HTTPS certificates as well on a fresh tail net.

**[13:34](https://youtube.com/watch?v=guHoZ68N3XM&t=814s)** At least you need to make sure that magic DNS is turned on and the HTTPS certificates are turned on as well.

**[13:41](https://youtube.com/watch?v=guHoZ68N3XM&t=821s)** So with that done, that's the basics of configuring tail scale on Proxmox.

**[13:46](https://youtube.com/watch?v=guHoZ68N3XM&t=826s)** The next thing we want to do is go ahead and install Docker.

**[13:49](https://youtube.com/watch?v=guHoZ68N3XM&t=829s)** So I'm going to go over to get dot Docker.com and just copy the first little bit of this script right here.

**[13:56](https://youtube.com/watch?v=guHoZ68N3XM&t=836s)** I'm not going to worry about the O install Docker part.

**[14:01](https://youtube.com/watch?v=guHoZ68N3XM&t=841s)** I'm going to paste that into my clipboard, do a pipe to SH and this is going to install Docker on my Proxmox host.

**[14:09](https://youtube.com/watch?v=guHoZ68N3XM&t=849s)** Now Docker, you've probably heard of this. It's a containerization engine that lets you run containerized applications on Proxmox.

**[14:16](https://youtube.com/watch?v=guHoZ68N3XM&t=856s)** Now there are a lot of different schools of thought, shall I say, as to whether you should install things directly on the Proxmox host or create virtual machines

**[14:25](https://youtube.com/watch?v=guHoZ68N3XM&t=865s)** and put things with virtual machines or create what are called LXC containers or LX containers because the C already means containers.

**[14:33](https://youtube.com/watch?v=guHoZ68N3XM&t=873s)** Anyway, to be honest with you though, this is a beginners guide.

**[14:38](https://youtube.com/watch?v=guHoZ68N3XM&t=878s)** And I want to keep things as simple as I can whilst also giving you just enough breadcrumbs to follow

**[14:45](https://youtube.com/watch?v=guHoZ68N3XM&t=885s)** if you just start playing with that stuff moving forward.

**[14:48](https://youtube.com/watch?v=guHoZ68N3XM&t=888s)** So for today, we're going to put everything on the Proxmox host itself.

**[14:53](https://youtube.com/watch?v=guHoZ68N3XM&t=893s)** We're not going to do any VMs. We're not going to do any LXCs.

**[14:56](https://youtube.com/watch?v=guHoZ68N3XM&t=896s)** But what we are going to do is we are going to use Docker compose to declaratively declare what all of our containers look like on the Proxmox host with a text file.

**[15:07](https://youtube.com/watch?v=guHoZ68N3XM&t=907s)** So with Docker install, we're going to do Docker run dash dash RM IT, hello world, just to prove that Docker is actually working.

**[15:15](https://youtube.com/watch?v=guHoZ68N3XM&t=915s)** And hello from Docker. This message shows that your installation appears to be working correctly. Hooray.

**[15:22](https://youtube.com/watch?v=guHoZ68N3XM&t=922s)** Okay, so I'm looking at my little list here. The only thing we've got left to do now is partition our disk.

**[15:28](https://youtube.com/watch?v=guHoZ68N3XM&t=928s)** So how do we do that? Our data disk. Now remember when I showed you in part one, the hardware for this thing, there are two disks in this system.

**[15:36](https://youtube.com/watch?v=guHoZ68N3XM&t=936s)** The first one is a NVMe SSD. So that's this one up here.

**[15:41](https://youtube.com/watch?v=guHoZ68N3XM&t=941s)** And this is a Samsung 980 500 gigabyte NVMe SSD.

**[15:46](https://youtube.com/watch?v=guHoZ68N3XM&t=946s)** This is where Proxmox is installed to. This is where your Docker containers will be running.

**[15:51](https://youtube.com/watch?v=guHoZ68N3XM&t=951s)** But we want to make sure that their data persists somewhere else such that we can back it up later.

**[15:57](https://youtube.com/watch?v=guHoZ68N3XM&t=957s)** And again, this is a beginner's guide. We will probably come on to backups in a future part, or I'm not promising anything to be part of this series.

**[16:05](https://youtube.com/watch?v=guHoZ68N3XM&t=965s)** I think a dedicated video on data backups over Tails goes probably warranted.

**[16:11](https://youtube.com/watch?v=guHoZ68N3XM&t=971s)** But what we want to do is create a partition on this disk here of SDA, our SATA SSD, and create a file system on it.

**[16:21](https://youtube.com/watch?v=guHoZ68N3XM&t=981s)** So remember that little phrase there, SDA. Now you don't want to really rely on those identifiers to reliably exist to identify your disks.

**[16:34](https://youtube.com/watch?v=guHoZ68N3XM&t=994s)** If, and in our case, this won't happen in this little Dell box, but let's say you build a server with four, five, six, seven, eight different SSDs in it.

**[16:42](https://youtube.com/watch?v=guHoZ68N3XM&t=1002s)** And you sort of move them around. It's possible that on each reboot, those devices can enumerate with different namings.

**[16:48](https://youtube.com/watch?v=guHoZ68N3XM&t=1008s)** So if you start putting config files together based on SDA, it can sometimes happen that that name will change and then the config file is invalid.

**[16:58](https://youtube.com/watch?v=guHoZ68N3XM&t=1018s)** What we want to do is, well, first of all, we need to create the partitions and then we'll come on how to actually access the data that stored on those disks.

**[17:06](https://youtube.com/watch?v=guHoZ68N3XM&t=1026s)** But first of all, now this is, you've got to be careful with this next command, okay.

**[17:11](https://youtube.com/watch?v=guHoZ68N3XM&t=1031s)** We're going to use wipe FS and I'm going to put in dev SDA. Be warned, this will delete all the data on your disks.

**[17:21](https://youtube.com/watch?v=guHoZ68N3XM&t=1041s)** You can see here that I have on SDA itself, I have three different entries and then under SDA one, which is the first partition on this disk, I have one EXT4 partition.

**[17:32](https://youtube.com/watch?v=guHoZ68N3XM&t=1052s)** EXT4 refers to the name of the file system. So you know that binder used to carry a school every day that had like different plastic wallets in it.

**[17:40](https://youtube.com/watch?v=guHoZ68N3XM&t=1060s)** You can kind of think of those wallets as like partitions almost. So you've got the big binder, which is the disk and then inside the binder are the different plastic wallets.

**[17:49](https://youtube.com/watch?v=guHoZ68N3XM&t=1069s)** And typically when you're doing a data disk like this, you probably just want one giant partition, which is what we have here.

**[17:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1076s)** But I'm going to create it for you on the stream on the video, at least in real time. But when you're using a used disk or even sometimes when you buy a brand new disk,

**[18:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1087s)** they come pre-formatted with NTFS or like you just don't know what's happened to them before. So it's probably a good idea, although please exercise caution.

**[18:17](https://youtube.com/watch?v=guHoZ68N3XM&t=1097s)** Double check the commands are about to run in this next section because they are destructive.

**[18:21](https://youtube.com/watch?v=guHoZ68N3XM&t=1101s)** So I'm going to go ahead and just do a wipe FS minus a on SDA one and then SDA. And this is going to remove all of those different signatures that we had on the disk.

**[18:33](https://youtube.com/watch?v=guHoZ68N3XM&t=1113s)** And again, if I do wipe FS without without any any commands, you can see that nothing exists on the disk now. It's completely empty.

**[18:42](https://youtube.com/watch?v=guHoZ68N3XM&t=1122s)** So if there was data stored on that disk, it's now, unless you send it to drive save or something, it's now gone. So please, please double check before you run wipe FS on a disk, exercise some caution and don't just run it willingly.

**[18:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1139s)** Okay, now we want to create a partition next. So I'm going to do G disk, which is the application I'm going to use to create a GPT partition table.

**[19:06](https://youtube.com/watch?v=guHoZ68N3XM&t=1146s)** I'm going to press O for a new, you know, GPT MBR.

**[19:11](https://youtube.com/watch?v=guHoZ68N3XM&t=1151s)** I'm going to select yes, and then I'm going to create a new partition. Remember, we're just creating the plastic wallets at this point that everything lives within.

**[19:18](https://youtube.com/watch?v=guHoZ68N3XM&t=1158s)** We're not actually creating the file system yet, which is how to explain that.

**[19:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1163s)** Okay, so you've got the binder, then you've got the plastic wallet, and then within side the wallet is the file system, is the contents, I suppose is the best way to think of it.

**[19:32](https://youtube.com/watch?v=guHoZ68N3XM&t=1172s)** And then I'm going to do right here. So we now have one partition on this disk, and we can look at that by doing F disk minus L dev SDA.

**[19:44](https://youtube.com/watch?v=guHoZ68N3XM&t=1184s)** You can see that SDA one now exists. So I mentioned a moment ago that we don't really want to refer to that SDA moniker, unless we absolutely have to.

**[19:54](https://youtube.com/watch?v=guHoZ68N3XM&t=1194s)** So what do we do instead? Well, if we go to dev disk by ID, we actually get a list of all disks connected to the system with their constituent serial numbers.

**[20:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1207s)** Okay, so this means that this is a unique identifier for the disk, matching the same way that dev SDA is, and you can see it's actually just a simlink anyway.

**[20:15](https://youtube.com/watch?v=guHoZ68N3XM&t=1215s)** So really, for me, this is the best way to refer to disks in your system. So what we want to do now is create that file system using the ATAS PCC blah blah blah.

**[20:28](https://youtube.com/watch?v=guHoZ68N3XM&t=1228s)** Right. So by the way, if you want to clear your screen, you can do a control L. You can also type clear, but I always prefer control L. So just free tip for you there.

**[20:40](https://youtube.com/watch?v=guHoZ68N3XM&t=1240s)** Now, we want to edit a file called FS tab. So we're going to use VIM to do that. So type VI, edit the FS tab you can use now as well if you prefer.

**[20:50](https://youtube.com/watch?v=guHoZ68N3XM&t=1250s)** Now when I open VIM, I'll try and talk you through the keystrokes because I really love VIM. It's one of those editors that once you start using it, and I've been using it now for maybe seven, eight, nine years, there is a hurdle to get there, but it's promise you it's worth it.

**[21:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1267s)** All right. So you open VIM, you do a shift G, that takes us to the bottom of the file in our press O, and this puts you on the next line, but it also puts you into insert mode, which means you can actually type stuff because that's something that often confuses newbies with VIM.

**[21:24](https://youtube.com/watch?v=guHoZ68N3XM&t=1284s)** So we're going to do slash dev slash disk slash by hyphen ID and then put in the name of our partition. We are now going to do mount SSD. So this is where we're going to mount the data directory to.

**[21:38](https://youtube.com/watch?v=guHoZ68N3XM&t=1298s)** We're then going to mention the file system type that we are using. So in this case, I want to keep things incredibly simple excruciatingly simple for this video.

**[21:47](https://youtube.com/watch?v=guHoZ68N3XM&t=1307s)** We could use ZFS here. We could use butter FS or B cache FS.

**[21:53](https://youtube.com/watch?v=guHoZ68N3XM&t=1313s)** But each of those things are what are called copy on right file systems. They can do things like snapshots and replication.

**[22:02](https://youtube.com/watch?v=guHoZ68N3XM&t=1322s)** And they have a huge amount of features. But again, like that's step 73 in the and we're on step one or step two here.

**[22:11](https://youtube.com/watch?v=guHoZ68N3XM&t=1331s)** So I want to keep it really simple with EXT4. It's a really old tried and trusted and true file system on the next.

**[22:18](https://youtube.com/watch?v=guHoZ68N3XM&t=1338s)** If you want to use something else at this point, please go ahead and do that. I won't come and mark your homework down for doing it.

**[22:24](https://youtube.com/watch?v=guHoZ68N3XM&t=1344s)** But if you're just following along, EXT4 will do you just fine for now.

**[22:30](https://youtube.com/watch?v=guHoZ68N3XM&t=1350s)** Next we want to put in defaults, no A time and discard some basic stuff here for the FS tab file. And then we are done.

**[22:39](https://youtube.com/watch?v=guHoZ68N3XM&t=1359s)** So to exit insert mode, we press escape and then we do colon right colon W and then quit.

**[22:46](https://youtube.com/watch?v=guHoZ68N3XM&t=1366s)** And now that file has been modified. So if we do FS tab, we can see here that the edits we made have been persisted, I guess.

**[22:55](https://youtube.com/watch?v=guHoZ68N3XM&t=1375s)** Now we want to create the file system on this disk. I don't think I did that did I.

**[22:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1379s)** So we want to do make make FS MKFS dot EXT4 and then put in the partition that we want to put EXT4 onto.

**[23:08](https://youtube.com/watch?v=guHoZ68N3XM&t=1388s)** That's now created the EXT4 partition on the disk for us.

**[23:12](https://youtube.com/watch?v=guHoZ68N3XM&t=1392s)** The last thing we have to do is create the mount point. This is where the disk is actually going to be mounted by proxmox.

**[23:19](https://youtube.com/watch?v=guHoZ68N3XM&t=1399s)** Actually, I'm going to create mount SSD one because who knows maybe we had another SSD later.

**[23:25](https://youtube.com/watch?v=guHoZ68N3XM&t=1405s)** And then that means I've got to edit my FS tab again. So I know I want to look for the phrase SSD.

**[23:29](https://youtube.com/watch?v=guHoZ68N3XM&t=1409s)** So if I press forward slash SSD, that would take me right to the part of the file I want to go to.

**[23:34](https://youtube.com/watch?v=guHoZ68N3XM&t=1414s)** And then I can do insert one. So insert means letter I type the number one, press escape, press colon right quit.

**[23:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1423s)** And trust me, this stuff becomes muscle memory after a while.

**[23:46](https://youtube.com/watch?v=guHoZ68N3XM&t=1426s)** If you've been looking for a way to start, then them tutors are really good way to do it. Stick that into Google.

**[23:51](https://youtube.com/watch?v=guHoZ68N3XM&t=1431s)** You'll probably lose an evening to it, but you're welcome.

**[23:54](https://youtube.com/watch?v=guHoZ68N3XM&t=1434s)** Alright, so we now have FS tab created. We have the file system on the disk. And I think we're good to go.

**[24:00](https://youtube.com/watch?v=guHoZ68N3XM&t=1440s)** So let's do mount a yes, we need to do system CTL demon reload to pick up the new FS tab file that we just created.

**[24:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1450s)** Mount hyphen a and we can type mount again. And we can see that this disk is now mounted on our system.

**[24:18](https://youtube.com/watch?v=guHoZ68N3XM&t=1458s)** One last tip, here's a new app that I just found that I absolutely adore. It's called duf.

**[24:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1463s)** It just prints you out a really nice, easy to read like overview of all different things on your system.

**[24:29](https://youtube.com/watch?v=guHoZ68N3XM&t=1469s)** There's a bunch of other stuff you can do with it if you do dash dash help.

**[24:32](https://youtube.com/watch?v=guHoZ68N3XM&t=1472s)** We won't get into that for today. So I think if I look back at my original running sheet,

**[24:39](https://youtube.com/watch?v=guHoZ68N3XM&t=1479s)** we've done all of the proxmox setup piece now, which means the next chapter is going to be installing image.

**[24:47](https://youtube.com/watch?v=guHoZ68N3XM&t=1487s)** Next up, it's time to install image, the self hosted Google photos clone.

**[24:52](https://youtube.com/watch?v=guHoZ68N3XM&t=1492s)** And you can find them over at image dot app. Now they have a wonderful getting started section on their on the website.

**[24:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1499s)** But we're going to do things slightly differently. For example, they recommend you use an end file with your local compose file.

**[25:05](https://youtube.com/watch?v=guHoZ68N3XM&t=1505s)** There's a couple of things I'm not going to do the way they recommend.

**[25:08](https://youtube.com/watch?v=guHoZ68N3XM&t=1508s)** I just prefer to keep things fully declarative and have everything in just one single file.

**[25:13](https://youtube.com/watch?v=guHoZ68N3XM&t=1513s)** So link in the description is a copy of this file.

**[25:17](https://youtube.com/watch?v=guHoZ68N3XM&t=1517s)** And the reason I modified it slightly is for a few reasons.

**[25:20](https://youtube.com/watch?v=guHoZ68N3XM&t=1520s)** First of all, we want to put image on our tailnet.

**[25:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1523s)** So we're going to do that using this sidecar method.

**[25:27](https://youtube.com/watch?v=guHoZ68N3XM&t=1527s)** And this effectively creates, so you've got the image application server over here.

**[25:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1531s)** And then you've got the image tailscale connection server.

**[25:35](https://youtube.com/watch?v=guHoZ68N3XM&t=1535s)** We kind of merge those two things together. We've done this many times on the channel now.

**[25:39](https://youtube.com/watch?v=guHoZ68N3XM&t=1539s)** You kind of merge these two things together using this network mode command here.

**[25:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1543s)** And it basically puts image directly onto your tailnet.

**[25:46](https://youtube.com/watch?v=guHoZ68N3XM&t=1546s)** So you can access it from anywhere in the world using tailscale serve with no reverse proxy configuration required.

**[25:52](https://youtube.com/watch?v=guHoZ68N3XM&t=1552s)** So in the description down below will be this file, the whole thing.

**[25:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1556s)** There's several containers in here. You've got the image TS container.

**[25:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1559s)** First of all, you've then got the image application server container.

**[26:03](https://youtube.com/watch?v=guHoZ68N3XM&t=1563s)** And these paths will come onto these in just a minute. Don't worry.

**[26:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1567s)** You've also got the image machine learning container.

**[26:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1570s)** This one's pretty interesting and I have a video linked up here where you can look at how to do remote GPU machine learning for image.

**[26:17](https://youtube.com/watch?v=guHoZ68N3XM&t=1577s)** So if you're importing 100,000 images or something, you could have an Nvidia GPU in your gaming rig.

**[26:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1583s)** Actually do all of the processing and machine learning and face recognition for image and spare the poor CPU of your little Dell box or something like that.

**[26:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1591s)** We're just going to run this all in CPU mode today and all in one place.

**[26:34](https://youtube.com/watch?v=guHoZ68N3XM&t=1594s)** But if you did want to do remote learning, like I say, there's a link to a video already done about that.

**[26:39](https://youtube.com/watch?v=guHoZ68N3XM&t=1599s)** Now, Redis is a piece of software that essentially just acts like a sponge.

**[26:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1603s)** When you're adding all of those pictures, it's not necessarily the case that image can soak up all of that pressure all at once.

**[26:50](https://youtube.com/watch?v=guHoZ68N3XM&t=1610s)** So Redis kind of just acts like a buffer, if you like.

**[26:53](https://youtube.com/watch?v=guHoZ68N3XM&t=1613s)** It pulls in all of the stuff and kind of queues it up and stores it temporarily until image can actually get to processing it later on.

**[27:01](https://youtube.com/watch?v=guHoZ68N3XM&t=1621s)** So it's a queuing piece of software.

**[27:03](https://youtube.com/watch?v=guHoZ68N3XM&t=1623s)** So if you've ever wondered what Redis does, that's what it does.

**[27:06](https://youtube.com/watch?v=guHoZ68N3XM&t=1626s)** And then you've got the database, of course, which is very important piece of software using Postgres in this case.

**[27:12](https://youtube.com/watch?v=guHoZ68N3XM&t=1632s)** Now, the way that Docker works, we're going to need to do something with what are called volumes.

**[27:17](https://youtube.com/watch?v=guHoZ68N3XM&t=1637s)** These are a way to persist data outside of the container runtime environment.

**[27:22](https://youtube.com/watch?v=guHoZ68N3XM&t=1642s)** Such that when you destroy and recreate the Docker containers, all of your database is all of your pictures and everything.

**[27:28](https://youtube.com/watch?v=guHoZ68N3XM&t=1648s)** Remain intact, which is obviously what we want.

**[27:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1651s)** So we've got to make sure that some of these paths exist.

**[27:34](https://youtube.com/watch?v=guHoZ68N3XM&t=1654s)** Now, on our Dell box, we already know that this path exists of Mount SSD1 as defined here.

**[27:39](https://youtube.com/watch?v=guHoZ68N3XM&t=1659s)** But if this data path doesn't exist, Docker will go ahead and try and create it.

**[27:45](https://youtube.com/watch?v=guHoZ68N3XM&t=1665s)** However, further up in our image TS thing, we need to create these paths here because

**[27:51](https://youtube.com/watch?v=guHoZ68N3XM&t=1671s)** we've got to put a couple of config files in there in order to configure the tail scale container.

**[27:55](https://youtube.com/watch?v=guHoZ68N3XM&t=1675s)** So let's go ahead and create those paths.

**[27:57](https://youtube.com/watch?v=guHoZ68N3XM&t=1677s)** I've just copied that path onto my clipboard.

**[28:00](https://youtube.com/watch?v=guHoZ68N3XM&t=1680s)** Again, via SSH, I'm going to do make Dirt minus P.

**[28:04](https://youtube.com/watch?v=guHoZ68N3XM&t=1684s)** It's going to create this whole folder path for us of Mount SSD1 app data image TS config.

**[28:11](https://youtube.com/watch?v=guHoZ68N3XM&t=1691s)** I'm also going to do the same thing with TS state.

**[28:15](https://youtube.com/watch?v=guHoZ68N3XM&t=1695s)** By the way, if you want to delete the whole string, you can do a control W.

**[28:20](https://youtube.com/watch?v=guHoZ68N3XM&t=1700s)** And that will delete the entire word behind the cursor.

**[28:24](https://youtube.com/watch?v=guHoZ68N3XM&t=1704s)** And then on image server, we also want to make sure that we have this directory actually exists.

**[28:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1711s)** It may already contain data in your case.

**[28:34](https://youtube.com/watch?v=guHoZ68N3XM&t=1714s)** You might already have a directory with folders in it, but I don't think we do here do we know data does not exist.

**[28:40](https://youtube.com/watch?v=guHoZ68N3XM&t=1720s)** So we don't have to create this in this case, because like I say,

**[28:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1723s)** image would go ahead and automatically create it for us, but it can't hurt to create these directories.

**[28:48](https://youtube.com/watch?v=guHoZ68N3XM&t=1728s)** Now, I don't think I have this app installed.

**[28:50](https://youtube.com/watch?v=guHoZ68N3XM&t=1730s)** So I'm going to install it right away.

**[28:52](https://youtube.com/watch?v=guHoZ68N3XM&t=1732s)** Tree is an application that lets you list out directory structures.

**[28:55](https://youtube.com/watch?v=guHoZ68N3XM&t=1735s)** Okay?

**[28:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1736s)** So you can see here that we've now created a few different directories.

**[28:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1739s)** We've got app data image TS config TS state.

**[29:02](https://youtube.com/watch?v=guHoZ68N3XM&t=1742s)** We've got data, photos, upload.

**[29:05](https://youtube.com/watch?v=guHoZ68N3XM&t=1745s)** And this is just reflecting what's in our Docker compose file.

**[29:08](https://youtube.com/watch?v=guHoZ68N3XM&t=1748s)** Now, in terms of what we need to do, we need to put a few files and a few places.

**[29:11](https://youtube.com/watch?v=guHoZ68N3XM&t=1751s)** So let's create in here, we've got app data image.

**[29:16](https://youtube.com/watch?v=guHoZ68N3XM&t=1756s)** So in that folder, let's go to here to app data image.

**[29:19](https://youtube.com/watch?v=guHoZ68N3XM&t=1759s)** We're going to create a new file called compose.yaml.

**[29:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1763s)** But we're going to do that from VS code.

**[29:26](https://youtube.com/watch?v=guHoZ68N3XM&t=1766s)** Now, if you didn't know, tail scale make a VS code extension.

**[29:30](https://youtube.com/watch?v=guHoZ68N3XM&t=1770s)** So you can go to the extensions option over here, search for tail scale,

**[29:33](https://youtube.com/watch?v=guHoZ68N3XM&t=1773s)** and install that directly into your VS code editor.

**[29:37](https://youtube.com/watch?v=guHoZ68N3XM&t=1777s)** The benefit of this is you can now click on this little tail scale button.

**[29:40](https://youtube.com/watch?v=guHoZ68N3XM&t=1780s)** And you can see all of the nodes in your tail net.

**[29:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1783s)** Now, I care if I only got a couple.

**[29:45](https://youtube.com/watch?v=guHoZ68N3XM&t=1785s)** But we want to do things like change the SSH username.

**[29:47](https://youtube.com/watch?v=guHoZ68N3XM&t=1787s)** I'm going to change mine to root.

**[29:49](https://youtube.com/watch?v=guHoZ68N3XM&t=1789s)** And then I'm going to change the path, right click,

**[29:53](https://youtube.com/watch?v=guHoZ68N3XM&t=1793s)** and then change root directory to root.

**[29:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1796s)** I think by default, it's the home directory of the root user.

**[29:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1799s)** But I want access to the entire system.

**[30:02](https://youtube.com/watch?v=guHoZ68N3XM&t=1802s)** And now if I click this little carrots icon next to this and expand,

**[30:05](https://youtube.com/watch?v=guHoZ68N3XM&t=1805s)** you can see I've got access to the entire file system of this remote node over tail scale.

**[30:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1810s)** Remember, we haven't done any user names or passwords or SSH keys or anything like that

**[30:15](https://youtube.com/watch?v=guHoZ68N3XM&t=1815s)** to kind of verify identity.

**[30:17](https://youtube.com/watch?v=guHoZ68N3XM&t=1817s)** All we've done is installed tail scale in both places and logged in.

**[30:21](https://youtube.com/watch?v=guHoZ68N3XM&t=1821s)** And it handles the rest.

**[30:22](https://youtube.com/watch?v=guHoZ68N3XM&t=1822s)** It really is Patrick.

**[30:24](https://youtube.com/watch?v=guHoZ68N3XM&t=1824s)** Okay, so under MNT SSD1,

**[30:26](https://youtube.com/watch?v=guHoZ68N3XM&t=1826s)** we can see the same data structure that we just created in the command line.

**[30:30](https://youtube.com/watch?v=guHoZ68N3XM&t=1830s)** And this is useful for us today because we need to put a few files in place.

**[30:34](https://youtube.com/watch?v=guHoZ68N3XM&t=1834s)** So I need to rename that to image.

**[30:37](https://youtube.com/watch?v=guHoZ68N3XM&t=1837s)** By the way, this file is of course linked in the Git repo in the description down below.

**[30:42](https://youtube.com/watch?v=guHoZ68N3XM&t=1842s)** But under here, we've got a couple of files to move around.

**[30:45](https://youtube.com/watch?v=guHoZ68N3XM&t=1845s)** So I need to copy this image.json file.

**[30:48](https://youtube.com/watch?v=guHoZ68N3XM&t=1848s)** I'm going to just copy this onto my clipboard.

**[30:50](https://youtube.com/watch?v=guHoZ68N3XM&t=1850s)** And then go over to the tail scale extension.

**[30:53](https://youtube.com/watch?v=guHoZ68N3XM&t=1853s)** And in TS config, I'm going to create a new file by right clicking,

**[30:57](https://youtube.com/watch?v=guHoZ68N3XM&t=1857s)** new file, and call it image.json.

**[31:01](https://youtube.com/watch?v=guHoZ68N3XM&t=1861s)** So I'm just going to copy the contents of that into my image.json file on the remote server now.

**[31:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1867s)** Okay, so we've got our reverse proxy configuration here done.

**[31:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1870s)** So this is going to handle configuring tail scale serve for us programmatically

**[31:14](https://youtube.com/watch?v=guHoZ68N3XM&t=1874s)** as part of the container deployment.

**[31:16](https://youtube.com/watch?v=guHoZ68N3XM&t=1876s)** We also need to make sure that we've got our auth key.

**[31:19](https://youtube.com/watch?v=guHoZ68N3XM&t=1879s)** So over at tailscale.com,

**[31:22](https://youtube.com/watch?v=guHoZ68N3XM&t=1882s)** we can generate ourselves an auth key by going to our admin console, settings, keys,

**[31:29](https://youtube.com/watch?v=guHoZ68N3XM&t=1889s)** and then generate an auth key.

**[31:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1891s)** And I'm going to call this one image test.

**[31:33](https://youtube.com/watch?v=guHoZ68N3XM&t=1893s)** I'm going to make it reusable because I'm doing a demo.

**[31:35](https://youtube.com/watch?v=guHoZ68N3XM&t=1895s)** And I'll probably tear things up and down a few times.

**[31:38](https://youtube.com/watch?v=guHoZ68N3XM&t=1898s)** You can leave this completely by default if you would like to.

**[31:41](https://youtube.com/watch?v=guHoZ68N3XM&t=1901s)** Now I'm going to copy my auth key into my Docker compose file.

**[31:45](https://youtube.com/watch?v=guHoZ68N3XM&t=1905s)** Just replacing this TS auth key bit here.

**[31:48](https://youtube.com/watch?v=guHoZ68N3XM&t=1908s)** And now I'm going to take this entire compose file.

**[31:53](https://youtube.com/watch?v=guHoZ68N3XM&t=1913s)** And I'm going to put it into this image directory right here.

**[31:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1916s)** So I'm going to click on new file compose.yaml.

**[31:59](https://youtube.com/watch?v=guHoZ68N3XM&t=1919s)** I'm going to open that paste.

**[32:02](https://youtube.com/watch?v=guHoZ68N3XM&t=1922s)** And now we are good to go.

**[32:04](https://youtube.com/watch?v=guHoZ68N3XM&t=1924s)** So if I do a control back tick,

**[32:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1927s)** that's going to bring me up the built-in terminal.

**[32:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1930s)** Or if I want to open a terminal via tail scale

**[32:14](https://youtube.com/watch?v=guHoZ68N3XM&t=1934s)** in the exact directory that I want to be in,

**[32:16](https://youtube.com/watch?v=guHoZ68N3XM&t=1936s)** I can just click on this little button here in the extension.

**[32:19](https://youtube.com/watch?v=guHoZ68N3XM&t=1939s)** And it takes me right to where I want to be.

**[32:22](https://youtube.com/watch?v=guHoZ68N3XM&t=1942s)** Isn't that cool?

**[32:23](https://youtube.com/watch?v=guHoZ68N3XM&t=1943s)** Okay, so for the purposes of video,

**[32:26](https://youtube.com/watch?v=guHoZ68N3XM&t=1946s)** I'm going to make things slightly bigger and just have things here.

**[32:31](https://youtube.com/watch?v=guHoZ68N3XM&t=1951s)** Okay, so we have our compose file.

**[32:33](https://youtube.com/watch?v=guHoZ68N3XM&t=1953s)** Again, I'm going to run tree.

**[32:35](https://youtube.com/watch?v=guHoZ68N3XM&t=1955s)** We have our compose file.

**[32:36](https://youtube.com/watch?v=guHoZ68N3XM&t=1956s)** I think everything's set up in there.

**[32:38](https://youtube.com/watch?v=guHoZ68N3XM&t=1958s)** We have our JSON image file too.

**[32:41](https://youtube.com/watch?v=guHoZ68N3XM&t=1961s)** Next time we started things up.

**[32:43](https://youtube.com/watch?v=guHoZ68N3XM&t=1963s)** So let's do a Docker compose pull.

**[32:45](https://youtube.com/watch?v=guHoZ68N3XM&t=1965s)** This is going to pull all of the images that we need to run image locally.

**[32:49](https://youtube.com/watch?v=guHoZ68N3XM&t=1969s)** Which in my case took about 45 seconds.

**[32:52](https://youtube.com/watch?v=guHoZ68N3XM&t=1972s)** I'm now going to do Docker compose up minus D.

**[32:56](https://youtube.com/watch?v=guHoZ68N3XM&t=1976s)** And then just to view the logs and double check

**[32:58](https://youtube.com/watch?v=guHoZ68N3XM&t=1978s)** about everything's going on and configured correctly,

**[33:00](https://youtube.com/watch?v=guHoZ68N3XM&t=1980s)** I'm going to do Docker compose logs minus F.

**[33:03](https://youtube.com/watch?v=guHoZ68N3XM&t=1983s)** And all being well,

**[33:05](https://youtube.com/watch?v=guHoZ68N3XM&t=1985s)** this is going to do several things.

**[33:07](https://youtube.com/watch?v=guHoZ68N3XM&t=1987s)** It's going to spin up the database.

**[33:09](https://youtube.com/watch?v=guHoZ68N3XM&t=1989s)** It's going to spin up image.

**[33:10](https://youtube.com/watch?v=guHoZ68N3XM&t=1990s)** It's going to add image to my tailnet.

**[33:12](https://youtube.com/watch?v=guHoZ68N3XM&t=1992s)** And hopefully everything will just work.

**[33:15](https://youtube.com/watch?v=guHoZ68N3XM&t=1995s)** Hopefully I've sacrificed enough to the demo gods today.

**[33:18](https://youtube.com/watch?v=guHoZ68N3XM&t=1998s)** Okay, first things first,

**[33:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2000s)** we're off to a good start.

**[33:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2001s)** The image container has automatically added itself to my tailnet.

**[33:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2004s)** So I'm going to copy this URL here.

**[33:26](https://youtube.com/watch?v=guHoZ68N3XM&t=2006s)** And if everything worked correctly,

**[33:28](https://youtube.com/watch?v=guHoZ68N3XM&t=2008s)** it's now going to go away in the background.

**[33:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2011s)** And yet start generating a certificate for image.valosiraptor.

**[33:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2015s)** Again, this can take a minus or two,

**[33:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2017s)** just like the Proxmox one did.

**[33:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2019s)** It's generating the certificate requesting certificate.

**[33:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2022s)** And voila, we're done.

**[33:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2024s)** We've deployed image.

**[33:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2025s)** Now, I get a lot of feedback from people saying that we need

**[33:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2028s)** a UI for Docker.

**[33:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2030s)** We need a UI to manage our containers.

**[33:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2032s)** And I do appreciate that by the time you have to drop to the terminal,

**[33:56](https://youtube.com/watch?v=guHoZ68N3XM&t=2036s)** you've already lost a good portion of your audience.

**[33:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2039s)** But the reality of self-hosting,

**[34:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2041s)** at least in 2025, at least,

**[34:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2043s)** is that you do still have to roll your sleeves up

**[34:05](https://youtube.com/watch?v=guHoZ68N3XM&t=2045s)** and get a little bit dirty.

**[34:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2047s)** However, it's a lot easier than it used to be.

**[34:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2049s)** We just simply deployed two files,

**[34:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2052s)** two YAML files.

**[34:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2053s)** And I think, probably within the realm of most people's ability,

**[34:17](https://youtube.com/watch?v=guHoZ68N3XM&t=2057s)** to just deploy two files.

**[34:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2059s)** We've got the Compose YAML and the image JSON.

**[34:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2061s)** And that's it.

**[34:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2062s)** Reverse proxy is taking care of.

**[34:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2064s)** It's on our town and we can access this now from anywhere in the world.

**[34:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2067s)** So let's just have a very quick poke around within image.

**[34:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2069s)** Let's click on get started.

**[34:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2071s)** Admin email.

**[34:32](https://youtube.com/watch?v=guHoZ68N3XM&t=2072s)** Yep.

**[34:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2073s)** Okay.

**[34:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2075s)** Right, I'm just going to skip past this stuff

**[34:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2077s)** because I don't think we really need to worry about it.

**[34:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2080s)** And the storage template thing,

**[34:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2081s)** I see stability issues here.

**[34:43](https://youtube.com/watch?v=guHoZ68N3XM&t=2083s)** I'm just going to ignore it.

**[34:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2084s)** I'm going to leave it disabled.

**[34:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2085s)** I don't want my photos to be unstable.

**[34:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2088s)** I also added a few photos from my personal collection here

**[34:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2092s)** just so we can see what's going on.

**[34:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2093s)** And I want to show you in real time.

**[34:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2095s)** Actually, I don't think I have H top installed.

**[34:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2097s)** Let's be fast.

**[34:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2099s)** I want to show you just how much CPU image is actually using.

**[35:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2102s)** So you can see that just for a few seconds there,

**[35:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2104s)** it was using all four CPU cores to 100%.

**[35:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2107s)** That's because in the background,

**[35:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2109s)** image is doing a whole bunch of machine learning on these images

**[35:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2111s)** to detect what's in them.

**[35:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2113s)** So I know that all happened very fast,

**[35:15](https://youtube.com/watch?v=guHoZ68N3XM&t=2115s)** but let's just do something like search for the word road.

**[35:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2119s)** Image is now using its machine learning capabilities

**[35:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2122s)** to look for anything in the images that looks like a road.

**[35:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2125s)** Or indeed, let's go for a train.

**[35:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2127s)** I know some of these are really easy and basic,

**[35:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2129s)** but you can start doing things like,

**[35:32](https://youtube.com/watch?v=guHoZ68N3XM&t=2132s)** what should we do?

**[35:34](https://youtube.com/watch?v=guHoZ68N3XM&t=2134s)** A tree sunset.

**[35:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2136s)** And you can start concatenating these things together

**[35:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2139s)** and image will go and find, you know,

**[35:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2141s)** this is not even clearly sunset.

**[35:43](https://youtube.com/watch?v=guHoZ68N3XM&t=2143s)** You've just got a little bit of golden light

**[35:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2145s)** on a mountain in Yosemite.

**[35:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2147s)** And it works out what's going on.

**[35:49](https://youtube.com/watch?v=guHoZ68N3XM&t=2149s)** Like obviously this bison picture at sunset is clearly sunset.

**[35:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2152s)** But I just think it's absolutely phenomenal.

**[35:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2154s)** We're doing all of this without a GPU.

**[35:56](https://youtube.com/watch?v=guHoZ68N3XM&t=2156s)** Now, admittedly, there are only 15 images.

**[36:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2162s)** You can imagine if you start putting 100,000 images through this thing,

**[36:05](https://youtube.com/watch?v=guHoZ68N3XM&t=2165s)** it's going to start crying and being like,

**[36:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2167s)** just where the GPU comes in.

**[36:10](https://youtube.com/watch?v=guHoZ68N3XM&t=2170s)** But like I said, there's a video about that up here.

**[36:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2172s)** So a couple of things to pay attention to in the settings of image.

**[36:15](https://youtube.com/watch?v=guHoZ68N3XM&t=2175s)** You can see there are lots of stuff going on here.

**[36:17](https://youtube.com/watch?v=guHoZ68N3XM&t=2177s)** An interesting one for tail scale users

**[36:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2179s)** might be the partner sharing feature.

**[36:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2181s)** Now, you're going to need to go into your image settings,

**[36:23](https://youtube.com/watch?v=guHoZ68N3XM&t=2183s)** create a new account, and then add a partner.

**[36:26](https://youtube.com/watch?v=guHoZ68N3XM&t=2186s)** And you can see that, well, let's actually do that in real time.

**[36:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2189s)** So I can show you.

**[36:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2191s)** Show, don't tell Alex, that's what you need to do.

**[36:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2193s)** So let's just do test at test.com, ABC123.

**[36:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2197s)** See if it lets me do that one.

**[36:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2200s)** Test, okay, let's create that user.

**[36:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2202s)** Cool, yes, test, yep, fine.

**[36:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2205s)** Let's go to account settings and create the partner sharing option.

**[36:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2210s)** This is neat because it lets you effectively share

**[36:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2214s)** all your photos and videos with your partner.

**[36:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2218s)** So you can have two people access this image instance

**[37:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2222s)** because the lead developer of image, a chap, also called Alex.

**[37:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2226s)** Excellent name, by the way.

**[37:08](https://youtube.com/watch?v=guHoZ68N3XM&t=2228s)** He just wanted a way to share his photos with his wife.

**[37:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2231s)** Image began as a way for this guy to scratch his own itch

**[37:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2234s)** to replace Google photos.

**[37:15](https://youtube.com/watch?v=guHoZ68N3XM&t=2235s)** And it's developed into this absolutely glorious project

**[37:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2239s)** that we have in front of us now.

**[37:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2241s)** And that's really it.

**[37:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2242s)** There's a lot more I could dig into with Image.

**[37:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2244s)** I'm not going to in the interest of time today

**[37:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2247s)** because next up on our agenda

**[37:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2249s)** is installing our audio book app.

**[37:32](https://youtube.com/watch?v=guHoZ68N3XM&t=2252s)** Now, I promised you an introduction

**[37:34](https://youtube.com/watch?v=guHoZ68N3XM&t=2254s)** to the wonderful world of self-hosting

**[37:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2256s)** so far we've looked at how to replace Google photos with Image.

**[37:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2259s)** And now we're going to look at how to replace audible

**[37:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2262s)** with audio bookshelf.

**[37:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2264s)** The ecosystem of applications is constantly growing.

**[37:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2268s)** And in fact, there's a whole list over awesome self-hosted on GitHub

**[37:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2272s)** where if you want to find out more software to host,

**[37:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2275s)** there's a huge list on here.

**[37:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2277s)** So if I type in audio bookshelf, for example,

**[37:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2279s)** there it is, under media streaming, audio streaming.

**[38:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2282s)** There's a bunch of stuff here, stuff that will let you replace things

**[38:05](https://youtube.com/watch?v=guHoZ68N3XM&t=2285s)** like Spotify with Navidrome and there's all sorts of stuff.

**[38:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2289s)** But today we're going to focus on audio bookshelf.

**[38:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2292s)** And much like we did with Image,

**[38:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2294s)** linked in the description down below,

**[38:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2296s)** is this Docker Compose YAML file.

**[38:18](https://youtube.com/watch?v=guHoZ68N3XM&t=2298s)** I'm going to copy my TS auth key

**[38:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2301s)** from my Image deployment into my audio bookshelf YAML file.

**[38:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2307s)** Now something I didn't point out in the Image section

**[38:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2309s)** is this hostname variable here.

**[38:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2311s)** This is the name that the container

**[38:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2313s)** or therefore the service will get when it joins your tailnet.

**[38:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2316s)** So we've got to make sure that that name is something that you want.

**[38:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2320s)** And then also, you've got to make sure that this network mode line

**[38:43](https://youtube.com/watch?v=guHoZ68N3XM&t=2323s)** is present here.

**[38:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2324s)** So service, and then this name here of service,

**[38:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2327s)** must match the name of this key.

**[38:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2330s)** I suppose in the YAML file right here.

**[38:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2332s)** So the syntax needs to look a little bit like this.

**[38:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2335s)** You need network mode, service, colon, image, audio, audio.

**[39:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2341s)** Audio bookshelf.

**[39:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2344s)** And then everything will just work just fine.

**[39:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2347s)** Because we're not exposing...

**[39:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2349s)** So one of the concepts of containers that we didn't get into yet

**[39:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2351s)** is how it's an encapsulated thing.

**[39:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2353s)** Nothing's allowed in or out unless you explicitly define it.

**[39:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2356s)** So right here, we're explicitly defining that this container

**[39:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2359s)** is allowed to reach out onto the host system

**[39:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2362s)** and look for audio books, for example,

**[39:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2364s)** on Mount SSD1 app data.

**[39:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2367s)** Now we also want to modify this file path to be SSD1,

**[39:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2370s)** media, for example, audio books.

**[39:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2373s)** So you can modify these paths to your heart's content.

**[39:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2375s)** I don't really mind where you store anything.

**[39:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2377s)** But the general idea in this scenario, at least,

**[39:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2380s)** is that we're storing the actual data on the second SSD,

**[39:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2384s)** the SSD is called SSD1 confusingly here.

**[39:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2387s)** But not the primary boot SSD for Proxmox.

**[39:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2390s)** We're storing that on like our data drive.

**[39:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2393s)** We store that there for just a separation of concerns, really.

**[39:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2397s)** So much like we did with Image,

**[39:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2399s)** I copy this file now using the tail scale extension.

**[40:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2402s)** And then in here, I'm going to create my compose file.

**[40:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2406s)** Now you could put this stuff in the same compose file

**[40:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2409s)** as you did with Image.

**[40:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2411s)** Really is personal preference as to how you organize things.

**[40:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2414s)** You can have one giant compose file

**[40:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2416s)** and certainly many people do, myself included on my server

**[40:19](https://youtube.com/watch?v=guHoZ68N3XM&t=2419s)** so that I don't have to keep changing directories

**[40:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2421s)** to get the correct context into my Docker commands.

**[40:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2424s)** But I think for the simplicity of a beginner tutorial,

**[40:28](https://youtube.com/watch?v=guHoZ68N3XM&t=2428s)** having that switching of context between different applications

**[40:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2431s)** might actually be helpful.

**[40:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2433s)** Okay, so we need to make sure like we did in part one

**[40:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2436s)** with the image container that this path actually exists.

**[40:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2440s)** So I'm going to change to my terminal here

**[40:43](https://youtube.com/watch?v=guHoZ68N3XM&t=2443s)** and do the make-dirt-p again,

**[40:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2446s)** just to make sure that audio bookshelf.ts config actually exists.

**[40:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2450s)** Then back in my VS code window,

**[40:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2453s)** I'm going to click this little refresh button up here.

**[40:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2455s)** And you'll see that TS config has now been created.

**[40:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2458s)** So what I need to do here is copy across again

**[41:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2461s)** my reverse proxy configuration.

**[41:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2463s)** Now audio bookshelf by default runs on port 80.

**[41:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2466s)** So you can see I've got port 80 configured here.

**[41:08](https://youtube.com/watch?v=guHoZ68N3XM&t=2468s)** That's really the only thing you need to change

**[41:10](https://youtube.com/watch?v=guHoZ68N3XM&t=2470s)** between different applications.

**[41:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2471s)** This audio bookshelf.json looks exactly the same

**[41:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2474s)** as Image.json.

**[41:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2476s)** Look, except for the port number.

**[41:18](https://youtube.com/watch?v=guHoZ68N3XM&t=2478s)** Okay, so let's get the audio bookshelf.json copied over.

**[41:23](https://youtube.com/watch?v=guHoZ68N3XM&t=2483s)** New file audio bookshelf.json.

**[41:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2490s)** Let's open that, paste that in.

**[41:32](https://youtube.com/watch?v=guHoZ68N3XM&t=2492s)** And so now we should be good to go.

**[41:34](https://youtube.com/watch?v=guHoZ68N3XM&t=2494s)** So I'm going to change out of the image directory

**[41:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2497s)** by doing cd.dot to go up a level.

**[41:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2499s)** You can see I'm now in Mount SSD1 app data.

**[41:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2502s)** Just to give you a lay of the land,

**[41:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2505s)** I'm going to do L2 to list two levels deep in the directories.

**[41:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2510s)** So you can see we've got the audio bookshelf directory

**[41:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2513s)** with a compose file.

**[41:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2514s)** And then we've got the image directory with a compose file.

**[41:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2517s)** Image is still running in the background by the way.

**[41:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2519s)** If I do a Docker PS-A,

**[42:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2521s)** you can see the image is still there running in the background.

**[42:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2524s)** But we want to do audio bookshelf now.

**[42:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2526s)** So I'm going to change into the audio bookshelf directory.

**[42:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2529s)** Do a Docker compose pull.

**[42:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2531s)** That's going to do the same thing again.

**[42:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2532s)** Now you'll notice that the image audio bookshelf container,

**[42:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2536s)** in fact, I've just spotted an egregious mistake.

**[42:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2540s)** This, yeah, you can tell I copied and pasted this, can't you?

**[42:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2544s)** I need to change this from image audio bookshelf to audio bookshelf.ts.

**[42:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2550s)** And then, of course, how did I not spot that

**[42:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2553s)** when I was talking to you a minute ago?

**[42:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2555s)** You're probably screaming at the screen going,

**[42:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2557s)** Alex!

**[42:38](https://youtube.com/watch?v=guHoZ68N3XM&t=2558s)** Anyway, it's done now, it's fixed.

**[42:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2560s)** It's okay, we didn't actually create anything.

**[42:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2562s)** So let's go back,

**[42:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2564s)** paste that into our remote node,

**[42:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2566s)** and save the file.

**[42:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2568s)** And so now, when we do a Docker compose pull,

**[42:51](https://youtube.com/watch?v=guHoZ68N3XM&t=2571s)** it has already pulled the images.

**[42:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2573s)** We're good to go.

**[42:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2574s)** So we've got the audio bookshelf app,

**[42:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2575s)** and then app minus TS.

**[42:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2578s)** So if we do a Docker compose up again,

**[43:00](https://youtube.com/watch?v=guHoZ68N3XM&t=2580s)** minus D, it's going to create those applications for us.

**[43:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2583s)** And then again, we do a logs minus F.

**[43:05](https://youtube.com/watch?v=guHoZ68N3XM&t=2585s)** Just to double check that everything's going on

**[43:08](https://youtube.com/watch?v=guHoZ68N3XM&t=2588s)** and working for us just fine beneath the covers.

**[43:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2592s)** So let's go back to our tail scale admin console

**[43:15](https://youtube.com/watch?v=guHoZ68N3XM&t=2595s)** and just verify that that node has been added

**[43:17](https://youtube.com/watch?v=guHoZ68N3XM&t=2597s)** and created.

**[43:18](https://youtube.com/watch?v=guHoZ68N3XM&t=2598s)** And you can see we've now got an audio books node on here.

**[43:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2601s)** So I'm going to copy that to my clipboard

**[43:23](https://youtube.com/watch?v=guHoZ68N3XM&t=2603s)** and paste that in here.

**[43:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2605s)** And all being well,

**[43:26](https://youtube.com/watch?v=guHoZ68N3XM&t=2606s)** we're going to now go out to Let's Encrypt

**[43:28](https://youtube.com/watch?v=guHoZ68N3XM&t=2608s)** and request a certificate with our Acme account.

**[43:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2611s)** This would take just a moment or two.

**[43:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2613s)** And voila, we now have our audio book server on our tailnet.

**[43:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2621s)** So I'm going to create my username here, again, of ZFOD.

**[43:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2624s)** Just create a random junk username and password

**[43:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2626s)** and click submit.

**[43:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2628s)** Okay, let's get logged in with ZFOD.

**[43:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2630s)** So now it's time to create our first library.

**[43:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2634s)** Now, let's look back at the Docker Compose file

**[43:56](https://youtube.com/watch?v=guHoZ68N3XM&t=2636s)** and kind of explain the anatomy a little bit

**[43:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2638s)** of a Docker Compose creation command.

**[44:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2641s)** There are several volumes defined here

**[44:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2644s)** and it might be confusing if you've never seen this before

**[44:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2647s)** as to what's going on.

**[44:08](https://youtube.com/watch?v=guHoZ68N3XM&t=2648s)** This is the path actually exists on the physical Dell host,

**[44:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2652s)** not inside the container.

**[44:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2653s)** So you can think of this thing before the colon

**[44:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2656s)** as being the external point of data

**[44:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2660s)** where it exists on the host.

**[44:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2662s)** You then want to think about after the colon here

**[44:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2665s)** of slash audio books being inside the container.

**[44:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2669s)** And indeed, we can see that now.

**[44:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2670s)** If we go to add your first library,

**[44:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2673s)** I'm just going to call this one audio books

**[44:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2675s)** and I click on browse for folder,

**[44:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2677s)** you can see that audio books exists inside the container.

**[44:40](https://youtube.com/watch?v=guHoZ68N3XM&t=2680s)** Slash audio books.

**[44:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2681s)** If I click select folder path and create,

**[44:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2684s)** we've now got an empty library.

**[44:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2687s)** And if I click on the scan button,

**[44:49](https://youtube.com/watch?v=guHoZ68N3XM&t=2689s)** it's now going to scan for books inside that library,

**[44:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2692s)** and we can see that George Orwell Animal Farm

**[44:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2695s)** indeed now exists.

**[44:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2697s)** Animal Farm by George Orwell.

**[44:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2699s)** Fantastic.

**[45:00](https://youtube.com/watch?v=guHoZ68N3XM&t=2700s)** Okay.

**[45:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2701s)** So what we haven't done yet

**[45:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2703s)** is we haven't connected up our phone

**[45:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2706s)** to either image or audio bookshelf.

**[45:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2709s)** And I think that's a really important part

**[45:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2711s)** of this entire solution.

**[45:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2713s)** So I'm going to put this under a new chapter down below.

**[45:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2716s)** So I'll be right back.

**[45:17](https://youtube.com/watch?v=guHoZ68N3XM&t=2717s)** So one of the entire points of this tutorial series

**[45:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2720s)** is to show you that we're self hosting and tail scale.

**[45:23](https://youtube.com/watch?v=guHoZ68N3XM&t=2723s)** You can access your self hosted services from anywhere.

**[45:26](https://youtube.com/watch?v=guHoZ68N3XM&t=2726s)** No firewalls, no complicated configuration or anything like that.

**[45:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2730s)** So it's time to grab your phone

**[45:32](https://youtube.com/watch?v=guHoZ68N3XM&t=2732s)** and go to the app store of your choice.

**[45:34](https://youtube.com/watch?v=guHoZ68N3XM&t=2734s)** We have apps for iOS, for Android,

**[45:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2736s)** and many other platforms too.

**[45:38](https://youtube.com/watch?v=guHoZ68N3XM&t=2738s)** I'm just going to search for tail scale in the app store here

**[45:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2741s)** and download it to my phone.

**[45:43](https://youtube.com/watch?v=guHoZ68N3XM&t=2743s)** Whilst I'm here, I'm also going to search for the image app

**[45:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2746s)** and download that one too.

**[45:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2748s)** Along with an app called Plapper.

**[45:51](https://youtube.com/watch?v=guHoZ68N3XM&t=2751s)** There are several different audio book clients

**[45:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2755s)** for audio bookshelf for iOS.

**[45:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2757s)** Plapper's one, shelf player is another one.

**[45:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2759s)** You can see that one just a little bit below it.

**[46:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2761s)** I think there might also be an audio bookshelf app,

**[46:05](https://youtube.com/watch?v=guHoZ68N3XM&t=2765s)** but I think it's only in test flight mode.

**[46:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2769s)** So let's just double check that.

**[46:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2774s)** Yeah, I've definitely seen it at some point,

**[46:16](https://youtube.com/watch?v=guHoZ68N3XM&t=2776s)** but I think it's only available in test flight

**[46:18](https://youtube.com/watch?v=guHoZ68N3XM&t=2778s)** and honestly you could use some more work.

**[46:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2780s)** But if you're an Android, the official audio bookshelf app

**[46:22](https://youtube.com/watch?v=guHoZ68N3XM&t=2782s)** actually works pretty well.

**[46:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2784s)** So we've got Plapper,

**[46:26](https://youtube.com/watch?v=guHoZ68N3XM&t=2786s)** and these names come from.

**[46:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2789s)** I'm going to put that on my home screen.

**[46:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2791s)** I'm going to get image and put that on my home screen.

**[46:35](https://youtube.com/watch?v=guHoZ68N3XM&t=2795s)** And then also tail scale too.

**[46:38](https://youtube.com/watch?v=guHoZ68N3XM&t=2798s)** So I'm going to go ahead and connect this device to my tail net

**[46:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2801s)** in order that I can access these different services remotely.

**[46:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2804s)** I'm going to go through and click all of the sort of entry wizard.

**[46:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2807s)** I'm going to install VPN configuration.

**[46:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2810s)** Yes, it's going to ask me for my passcode.

**[46:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2813s)** And then it wants to get logged in.

**[46:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2814s)** Now I'm going to use my Google account,

**[46:56](https://youtube.com/watch?v=guHoZ68N3XM&t=2816s)** the same account that I logged in with my laptop.

**[46:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2818s)** And I've just logged these two different services in as well.

**[47:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2821s)** Of a tail and scales at gmail.com,

**[47:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2823s)** and then connect this device to my tail net.

**[47:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2826s)** So you will see now on the screen.

**[47:07](https://youtube.com/watch?v=guHoZ68N3XM&t=2827s)** Look, I've got image, I've got audio books.

**[47:10](https://youtube.com/watch?v=guHoZ68N3XM&t=2830s)** And if I wanted to, I could just access these things in the browser.

**[47:13](https://youtube.com/watch?v=guHoZ68N3XM&t=2833s)** I could literally go to Safari and put this in here,

**[47:17](https://youtube.com/watch?v=guHoZ68N3XM&t=2837s)** and it will just work.

**[47:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2841s)** But image has some nice features when you get to iOS,

**[47:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2845s)** automatic backup of pictures you take and things like that.

**[47:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2847s)** So let's use the application.

**[47:29](https://youtube.com/watch?v=guHoZ68N3XM&t=2849s)** I'm going to install the or allow notifications,

**[47:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2853s)** pasting the URL for image here into the client,

**[47:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2856s)** get logged in with what did I put a tail and scales at gmail.com,

**[47:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2862s)** and then I'm going to allow it full access to my photos.

**[47:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2865s)** So this icon up here in the top right,

**[47:47](https://youtube.com/watch?v=guHoZ68N3XM&t=2867s)** allows me to back up pictures that I take.

**[47:50](https://youtube.com/watch?v=guHoZ68N3XM&t=2870s)** So let's click on Recent's and for example,

**[47:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2873s)** and now if I click Start Backup,

**[47:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2875s)** it's going to start uploading things from this phone,

**[47:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2878s)** like screen recordings and all sorts of other stuff.

**[48:01](https://youtube.com/watch?v=guHoZ68N3XM&t=2881s)** You can see that photos I took on this phone

**[48:03](https://youtube.com/watch?v=guHoZ68N3XM&t=2883s)** are now automatically uploaded.

**[48:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2884s)** In fact, let's take one in real time and see sort of what happens.

**[48:09](https://youtube.com/watch?v=guHoZ68N3XM&t=2889s)** Here we go.

**[48:10](https://youtube.com/watch?v=guHoZ68N3XM&t=2890s)** Bink.

**[48:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2891s)** All right.

**[48:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2892s)** So going back to the image application,

**[48:15](https://youtube.com/watch?v=guHoZ68N3XM&t=2895s)** I'm just going to quit this thing and reopen it,

**[48:20](https://youtube.com/watch?v=guHoZ68N3XM&t=2900s)** and do a, I think you can start a manual backup each time

**[48:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2905s)** or you can have it automatically backup photos

**[48:27](https://youtube.com/watch?v=guHoZ68N3XM&t=2907s)** when you're charging,

**[48:28](https://youtube.com/watch?v=guHoZ68N3XM&t=2908s)** much like Google Photos within the background.

**[48:30](https://youtube.com/watch?v=guHoZ68N3XM&t=2910s)** And there you go.

**[48:31](https://youtube.com/watch?v=guHoZ68N3XM&t=2911s)** There's the picture I just took.

**[48:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2913s)** So in real time, you know, I've been able to,

**[48:37](https://youtube.com/watch?v=guHoZ68N3XM&t=2917s)** if you can see I'm cheating using the cord

**[48:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2919s)** down the bottom there, look for some commands.

**[48:41](https://youtube.com/watch?v=guHoZ68N3XM&t=2921s)** But you can see really just how easy it is to replace

**[48:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2924s)** some of the hosted services.

**[48:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2926s)** So for example, Image now is pretty much in a position

**[48:49](https://youtube.com/watch?v=guHoZ68N3XM&t=2929s)** to completely replace Google Photos for me.

**[48:52](https://youtube.com/watch?v=guHoZ68N3XM&t=2932s)** All right.

**[48:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2933s)** So that's, that's Image.

**[48:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2934s)** What about audio books?

**[48:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2935s)** Now we want to put in the fully qualified domain name

**[48:58](https://youtube.com/watch?v=guHoZ68N3XM&t=2938s)** for audio bookshelf.

**[48:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2939s)** And to save me a bunch of typing on the phone,

**[49:02](https://youtube.com/watch?v=guHoZ68N3XM&t=2942s)** I'm going to go back to the tail scale app,

**[49:04](https://youtube.com/watch?v=guHoZ68N3XM&t=2944s)** copy the magic DNS name,

**[49:06](https://youtube.com/watch?v=guHoZ68N3XM&t=2946s)** and put that into the audio bookshelf piece right here.

**[49:10](https://youtube.com/watch?v=guHoZ68N3XM&t=2950s)** What username?

**[49:11](https://youtube.com/watch?v=guHoZ68N3XM&t=2951s)** I think I set ZFOD, didn't I?

**[49:12](https://youtube.com/watch?v=guHoZ68N3XM&t=2952s)** Let's do ZFOD.

**[49:14](https://youtube.com/watch?v=guHoZ68N3XM&t=2954s)** And then just the username and password this way.

**[49:18](https://youtube.com/watch?v=guHoZ68N3XM&t=2958s)** On all being well, I should now be able to see

**[49:21](https://youtube.com/watch?v=guHoZ68N3XM&t=2961s)** my Animal Farm audio book.

**[49:23](https://youtube.com/watch?v=guHoZ68N3XM&t=2963s)** Great.

**[49:24](https://youtube.com/watch?v=guHoZ68N3XM&t=2964s)** Blogged in now.

**[49:25](https://youtube.com/watch?v=guHoZ68N3XM&t=2965s)** So I'm going to click on the audio books and just like that,

**[49:28](https://youtube.com/watch?v=guHoZ68N3XM&t=2968s)** I'm able to listen to Animal Farm by George Orwell,

**[49:33](https://youtube.com/watch?v=guHoZ68N3XM&t=2973s)** narrated by Stephen Fry.

**[49:36](https://youtube.com/watch?v=guHoZ68N3XM&t=2976s)** And then I can download the books.

**[49:38](https://youtube.com/watch?v=guHoZ68N3XM&t=2978s)** Okay.

**[49:39](https://youtube.com/watch?v=guHoZ68N3XM&t=2979s)** I didn't know this, but there is a small fee to unlock features

**[49:42](https://youtube.com/watch?v=guHoZ68N3XM&t=2982s)** like downloading audio books for offline listening

**[49:44](https://youtube.com/watch?v=guHoZ68N3XM&t=2984s)** or that kind of stuff.

**[49:45](https://youtube.com/watch?v=guHoZ68N3XM&t=2985s)** Supporting the developer.

**[49:46](https://youtube.com/watch?v=guHoZ68N3XM&t=2986s)** I have no problem with that.

**[49:48](https://youtube.com/watch?v=guHoZ68N3XM&t=2988s)** But you can generally get the idea here that this is a way

**[49:51](https://youtube.com/watch?v=guHoZ68N3XM&t=2991s)** to replace Audible.

**[49:53](https://youtube.com/watch?v=guHoZ68N3XM&t=2993s)** Okay.

**[49:54](https://youtube.com/watch?v=guHoZ68N3XM&t=2994s)** So we've replaced Google Photos.

**[49:55](https://youtube.com/watch?v=guHoZ68N3XM&t=2995s)** We've replaced Audible.

**[49:57](https://youtube.com/watch?v=guHoZ68N3XM&t=2997s)** And they're both now on my phone.

**[49:59](https://youtube.com/watch?v=guHoZ68N3XM&t=2999s)** So, you know, two services that are really very,

**[50:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3002s)** very, very useful in my life.

**[50:05](https://youtube.com/watch?v=guHoZ68N3XM&t=3005s)** I've now replaced with self-hosting.

**[50:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3007s)** Now what about home automation?

**[50:09](https://youtube.com/watch?v=guHoZ68N3XM&t=3009s)** We can come on to home assistant next.

**[50:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3011s)** You see this one up here?

**[50:12](https://youtube.com/watch?v=guHoZ68N3XM&t=3012s)** This is hiding.

**[50:13](https://youtube.com/watch?v=guHoZ68N3XM&t=3013s)** It's ready.

**[50:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3014s)** But we need to actually deploy home assistant.

**[50:17](https://youtube.com/watch?v=guHoZ68N3XM&t=3017s)** This is a bit different how we do this one.

**[50:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3019s)** We're not going to do this with a container.

**[50:21](https://youtube.com/watch?v=guHoZ68N3XM&t=3021s)** We're going to do this using the helper scripts

**[50:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3023s)** from helperscripts.com on top of Proxmox.

**[50:26](https://youtube.com/watch?v=guHoZ68N3XM&t=3026s)** Home Assistant is one of those projects

**[50:28](https://youtube.com/watch?v=guHoZ68N3XM&t=3028s)** that if you haven't heard of it,

**[50:30](https://youtube.com/watch?v=guHoZ68N3XM&t=3030s)** you absolutely should give it a look.

**[50:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3032s)** I'm sure at some point you've gone to Best Buy

**[50:35](https://youtube.com/watch?v=guHoZ68N3XM&t=3035s)** or something like that and bought a smart product

**[50:38](https://youtube.com/watch?v=guHoZ68N3XM&t=3038s)** like a hue light bulb or some kind of internet-connected thing.

**[50:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3042s)** And then each of those things comes with their own app.

**[50:46](https://youtube.com/watch?v=guHoZ68N3XM&t=3046s)** And so you end up having 15 different apps on your phone,

**[50:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3049s)** one to open your garage door and one to turn the lights on

**[50:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3052s)** and it's just a mess.

**[50:54](https://youtube.com/watch?v=guHoZ68N3XM&t=3054s)** Well, home assistant pulls all of those

**[50:56](https://youtube.com/watch?v=guHoZ68N3XM&t=3056s)** different ecosystems together into one place.

**[50:59](https://youtube.com/watch?v=guHoZ68N3XM&t=3059s)** And puts it, that's a local control

**[51:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3062s)** with privacy first smart home system.

**[51:05](https://youtube.com/watch?v=guHoZ68N3XM&t=3065s)** The really cool thing about that is you can then have

**[51:08](https://youtube.com/watch?v=guHoZ68N3XM&t=3068s)** those disparate ecosystems triggering each other.

**[51:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3071s)** So when you turn on the light bulb in the kitchen, for example,

**[51:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3074s)** you could have it turn on the,

**[51:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3076s)** or close your smart shade in your bedroom if you want to.

**[51:20](https://youtube.com/watch?v=guHoZ68N3XM&t=3080s)** I don't know why you would do that specific example.

**[51:22](https://youtube.com/watch?v=guHoZ68N3XM&t=3082s)** But it could be really useful to have

**[51:24](https://youtube.com/watch?v=guHoZ68N3XM&t=3084s)** all these different things be able to trigger each other.

**[51:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3087s)** So let's dig into how we actually go ahead

**[51:29](https://youtube.com/watch?v=guHoZ68N3XM&t=3089s)** and deploy home assistant now in this

**[51:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3092s)** epic beginners guide to self hosting video.

**[51:35](https://youtube.com/watch?v=guHoZ68N3XM&t=3095s)** So I'm going to go back to my old friends over at Helperscripts.

**[51:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3097s)** And I'm going to search for home assistant.

**[51:40](https://youtube.com/watch?v=guHoZ68N3XM&t=3100s)** We're going to deploy home assistant OS as a VM.

**[51:43](https://youtube.com/watch?v=guHoZ68N3XM&t=3103s)** And then I'm just going to copy this string here,

**[51:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3105s)** this how to install option here.

**[51:47](https://youtube.com/watch?v=guHoZ68N3XM&t=3107s)** I'm going to go back to my proxmox box

**[51:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3109s)** and then just copy and paste this into the shell.

**[51:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3112s)** This is going to take us through a little wizard

**[51:54](https://youtube.com/watch?v=guHoZ68N3XM&t=3114s)** and rather than creating home assistant as a container

**[51:58](https://youtube.com/watch?v=guHoZ68N3XM&t=3118s)** or anything else like that,

**[51:59](https://youtube.com/watch?v=guHoZ68N3XM&t=3119s)** we're going to do it as a VM because home assistant OS

**[52:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3122s)** is this fully encapsulated thing for home assistant.

**[52:05](https://youtube.com/watch?v=guHoZ68N3XM&t=3125s)** It contains all of the dependencies

**[52:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3127s)** and it's its own kind of little world for home assistant.

**[52:12](https://youtube.com/watch?v=guHoZ68N3XM&t=3132s)** Yeah, it's just easiest way to go,

**[52:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3134s)** I think, particularly for beginners.

**[52:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3136s)** So let's go through the wizard

**[52:17](https://youtube.com/watch?v=guHoZ68N3XM&t=3137s)** and we're going to go through the advanced options

**[52:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3139s)** just to see what's open to us.

**[52:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3143s)** Stable version, yes, that sounds good.

**[52:25](https://youtube.com/watch?v=guHoZ68N3XM&t=3145s)** Virtual machine ID, 100 would probably be fine,

**[52:28](https://youtube.com/watch?v=guHoZ68N3XM&t=3148s)** but I'm going to set 333, just, I don't actually know why.

**[52:33](https://youtube.com/watch?v=guHoZ68N3XM&t=3153s)** I440x, right through cache, yeah, fine.

**[52:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3157s)** Oh, host name.

**[52:40](https://youtube.com/watch?v=guHoZ68N3XM&t=3160s)** I'm going to set to home assistant.

**[52:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3162s)** And then we're going to do host CPU,

**[52:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3165s)** yeah, that's fine.

**[52:46](https://youtube.com/watch?v=guHoZ68N3XM&t=3166s)** Our little Dell box has four CPU cores,

**[52:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3169s)** so I'm going to set that.

**[52:50](https://youtube.com/watch?v=guHoZ68N3XM&t=3170s)** For RAM, I'm going to do 8192 for 8GB,

**[52:54](https://youtube.com/watch?v=guHoZ68N3XM&t=3174s)** the bridge zero is fine, the MAC address is fine,

**[52:57](https://youtube.com/watch?v=guHoZ68N3XM&t=3177s)** the VLAN is fine.

**[52:58](https://youtube.com/watch?v=guHoZ68N3XM&t=3178s)** The MTU is also fine.

**[53:00](https://youtube.com/watch?v=guHoZ68N3XM&t=3180s)** Start VM when completed, yes, and ready to create, yes.

**[53:03](https://youtube.com/watch?v=guHoZ68N3XM&t=3183s)** So now the script's going to go through

**[53:05](https://youtube.com/watch?v=guHoZ68N3XM&t=3185s)** and create the virtual machine for us.

**[53:08](https://youtube.com/watch?v=guHoZ68N3XM&t=3188s)** We're going to do a couple of things once it's created.

**[53:10](https://youtube.com/watch?v=guHoZ68N3XM&t=3190s)** We're going to attach it to our tailnet

**[53:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3191s)** and then also install a certificate

**[53:13](https://youtube.com/watch?v=guHoZ68N3XM&t=3193s)** so that you can access it from your phone, of course.

**[53:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3196s)** I've asked been the theme of this video, I know.

**[53:18](https://youtube.com/watch?v=guHoZ68N3XM&t=3198s)** But we've done it with containers thus far.

**[53:21](https://youtube.com/watch?v=guHoZ68N3XM&t=3201s)** And one of the reasons I wanted to show home assistant here

**[53:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3203s)** is because, well, first of all, it's a really cool application.

**[53:26](https://youtube.com/watch?v=guHoZ68N3XM&t=3206s)** It's one of those ones that make you feel

**[53:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3207s)** like you're solving real problems in the real world

**[53:30](https://youtube.com/watch?v=guHoZ68N3XM&t=3210s)** with self-hosted software.

**[53:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3212s)** And for me, that's where when you start connecting

**[53:34](https://youtube.com/watch?v=guHoZ68N3XM&t=3214s)** those real problems with real solutions,

**[53:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3217s)** that's where the magic of self-hosting

**[53:40](https://youtube.com/watch?v=guHoZ68N3XM&t=3220s)** really starts to come alive.

**[53:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3222s)** So we can see here that the VM has now been created.

**[53:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3225s)** It's going to boot up for the very first time.

**[53:47](https://youtube.com/watch?v=guHoZ68N3XM&t=3227s)** Let's wait and see what IP address we get.

**[53:50](https://youtube.com/watch?v=guHoZ68N3XM&t=3230s)** You can see, by the way, that a virtual machine

**[53:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3232s)** is basically just emulating a small computer

**[53:55](https://youtube.com/watch?v=guHoZ68N3XM&t=3235s)** within side your little Dell box.

**[53:57](https://youtube.com/watch?v=guHoZ68N3XM&t=3237s)** So it's emulating memory, it's emulating a processor stack,

**[54:00](https://youtube.com/watch?v=guHoZ68N3XM&t=3240s)** a disk stack, it's pretending it's got a real screen,

**[54:03](https://youtube.com/watch?v=guHoZ68N3XM&t=3243s)** a real scusy control, all this stuff.

**[54:06](https://youtube.com/watch?v=guHoZ68N3XM&t=3246s)** It doesn't actually matter.

**[54:08](https://youtube.com/watch?v=guHoZ68N3XM&t=3248s)** But if you want to view the console of the output of that machine,

**[54:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3251s)** you go to the, you select the virtual machine

**[54:13](https://youtube.com/watch?v=guHoZ68N3XM&t=3253s)** in the proxmox web interface, which, by the way,

**[54:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3256s)** why am I not on my little PVE?

**[54:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3259s)** Alex, Alex, Alex, Alex.

**[54:22](https://youtube.com/watch?v=guHoZ68N3XM&t=3262s)** Here we go.

**[54:24](https://youtube.com/watch?v=guHoZ68N3XM&t=3264s)** I should be using my little PVE thing

**[54:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3267s)** with tail scale service, shouldn't I?

**[54:29](https://youtube.com/watch?v=guHoZ68N3XM&t=3269s)** All right, so let's go home assistant console

**[54:31](https://youtube.com/watch?v=guHoZ68N3XM&t=3271s)** and we've got now an IP address of 192-168-1.118.

**[54:36](https://youtube.com/watch?v=guHoZ68N3XM&t=3276s)** And then home assistant runs on port 8123.

**[54:40](https://youtube.com/watch?v=guHoZ68N3XM&t=3280s)** This initial setup can take a minute or two.

**[54:43](https://youtube.com/watch?v=guHoZ68N3XM&t=3283s)** It's doing things like expanding the disk,

**[54:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3285s)** downloading any containers, and just instantiating itself,

**[54:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3289s)** just creating itself, getting itself ready to go.

**[54:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3292s)** So when that's complete, we're back in a minute.

**[54:55](https://youtube.com/watch?v=guHoZ68N3XM&t=3295s)** Okay, the initial installation is complete.

**[54:58](https://youtube.com/watch?v=guHoZ68N3XM&t=3298s)** Now I'm going to create my smart home,

**[55:00](https://youtube.com/watch?v=guHoZ68N3XM&t=3300s)** tail scale towers.

**[55:01](https://youtube.com/watch?v=guHoZ68N3XM&t=3301s)** Sure, why not?

**[55:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3302s)** Username of SayFord.

**[55:04](https://youtube.com/watch?v=guHoZ68N3XM&t=3304s)** Let's just create a random junk username and password.

**[55:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3307s)** Create account, fantastic.

**[55:09](https://youtube.com/watch?v=guHoZ68N3XM&t=3309s)** Location doesn't really matter.

**[55:12](https://youtube.com/watch?v=guHoZ68N3XM&t=3312s)** In this example, you can of course go ahead and configure this.

**[55:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3314s)** However, you would like.

**[55:15](https://youtube.com/watch?v=guHoZ68N3XM&t=3315s)** You can see already this is one of the absolute

**[55:18](https://youtube.com/watch?v=guHoZ68N3XM&t=3318s)** magical things about home assistant.

**[55:20](https://youtube.com/watch?v=guHoZ68N3XM&t=3320s)** It's already detected all of these different

**[55:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3323s)** compatible devices on my network.

**[55:25](https://youtube.com/watch?v=guHoZ68N3XM&t=3325s)** So my Android TV, my Apple TVs,

**[55:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3327s)** ECOB thermostats.

**[55:29](https://youtube.com/watch?v=guHoZ68N3XM&t=3329s)** It's just amazing.

**[55:31](https://youtube.com/watch?v=guHoZ68N3XM&t=3331s)** Absolutely amazing.

**[55:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3332s)** And out of the box, it gives you a very best approximation

**[55:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3337s)** of like a dashboard you might want.

**[55:39](https://youtube.com/watch?v=guHoZ68N3XM&t=3339s)** Like I can already control the light that's up here,

**[55:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3342s)** for example, as part of my filming setup,

**[55:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3345s)** directly from home assistant with no additional configuration.

**[55:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3349s)** How cool is that?

**[55:51](https://youtube.com/watch?v=guHoZ68N3XM&t=3351s)** All right.

**[55:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3352s)** Enough fan-boying out of the way with home assistant.

**[55:56](https://youtube.com/watch?v=guHoZ68N3XM&t=3356s)** It's time to actually get this thing on our tail net.

**[55:59](https://youtube.com/watch?v=guHoZ68N3XM&t=3359s)** So let's go down to settings.

**[56:01](https://youtube.com/watch?v=guHoZ68N3XM&t=3361s)** Let's crack on and install an add-on or two.

**[56:04](https://youtube.com/watch?v=guHoZ68N3XM&t=3364s)** First of all, we're going to want to install the tail scale add-on.

**[56:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3367s)** It's just a case of clicking install here.

**[56:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3371s)** And then we're also going to want to install the studio code server add-on.

**[56:15](https://youtube.com/watch?v=guHoZ68N3XM&t=3375s)** And this will become clear in just a moment as to why we want to do that too.

**[56:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3379s)** Okay.

**[56:20](https://youtube.com/watch?v=guHoZ68N3XM&t=3380s)** So let's go back to settings and add-ons once more.

**[56:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3383s)** And we're going to start up the tail scale container.

**[56:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3387s)** I say container add-on.

**[56:28](https://youtube.com/watch?v=guHoZ68N3XM&t=3388s)** It is really just a container under the hood.

**[56:30](https://youtube.com/watch?v=guHoZ68N3XM&t=3390s)** It's all just Docker masquerading.

**[56:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3392s)** But now there is an option.

**[56:34](https://youtube.com/watch?v=guHoZ68N3XM&t=3394s)** And in fact, I did a tutorial which I'll put a link to up here

**[56:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3397s)** about you can click on open web UI and get logged into tail net.

**[56:40](https://youtube.com/watch?v=guHoZ68N3XM&t=3400s)** But for me, for some reason, it's not working.

**[56:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3402s)** So to get around this, we can go into the logs of the container

**[56:46](https://youtube.com/watch?v=guHoZ68N3XM&t=3406s)** and click on this little URL here and authenticate to our tail net that way.

**[56:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3412s)** So a little workaround, I'm not sure why it's not working.

**[56:55](https://youtube.com/watch?v=guHoZ68N3XM&t=3415s)** I'll file a bug for that internally and hopefully we get that fixed by the time this video comes out.

**[56:59](https://youtube.com/watch?v=guHoZ68N3XM&t=3419s)** So I'm going to click on connect and then visit console.

**[57:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3422s)** And you can see that my home assistant now exists in my tail net.

**[57:05](https://youtube.com/watch?v=guHoZ68N3XM&t=3425s)** So if I want to connect to this instance, I can do 8123.

**[57:10](https://youtube.com/watch?v=guHoZ68N3XM&t=3430s)** And I can now connect two home assistant from anywhere in the world that I'm connected to tail scale.

**[57:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3436s)** But you know me, I like to have full on TLS certificates wherever possible.

**[57:21](https://youtube.com/watch?v=guHoZ68N3XM&t=3441s)** So this is where the studio code option comes in.

**[57:25](https://youtube.com/watch?v=guHoZ68N3XM&t=3445s)** So let's go back to the documentation section of the tail scale community add-on,

**[57:30](https://youtube.com/watch?v=guHoZ68N3XM&t=3450s)** which by the way, is maintained by Frank who seems to be like

**[57:33](https://youtube.com/watch?v=guHoZ68N3XM&t=3453s)** the most prolific home assistant developer going when it comes to all the add-ons.

**[57:38](https://youtube.com/watch?v=guHoZ68N3XM&t=3458s)** He does the tail scale add-on, he does the code studio add-on.

**[57:43](https://youtube.com/watch?v=guHoZ68N3XM&t=3463s)** Anyway, he's a good dude.

**[57:45](https://youtube.com/watch?v=guHoZ68N3XM&t=3465s)** So let's go to documentation and scroll all the way down to where it starts talking about proxy.

**[57:50](https://youtube.com/watch?v=guHoZ68N3XM&t=3470s)** The home assistant add-on calls it proxy.

**[57:53](https://youtube.com/watch?v=guHoZ68N3XM&t=3473s)** We call it tail scale serve.

**[57:55](https://youtube.com/watch?v=guHoZ68N3XM&t=3475s)** So those two things are the same.

**[57:57](https://youtube.com/watch?v=guHoZ68N3XM&t=3477s)** I don't know why it's called proxy in the home assistant add-on.

**[58:00](https://youtube.com/watch?v=guHoZ68N3XM&t=3480s)** So they love me, I guess.

**[58:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3482s)** Okay, so we're going to copy these four lines onto our clipboard.

**[58:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3487s)** And then we're going to go to our add-ons page again and start the studio code add-on.

**[58:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3494s)** I'm going to click show inside bar and so take just a minute to start up.

**[58:18](https://youtube.com/watch?v=guHoZ68N3XM&t=3498s)** Now we could click on open web UI, but I've already clicked the show inside bar button.

**[58:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3503s)** So it shows up here for all time because it's really handy to have this little studio code server available

**[58:28](https://youtube.com/watch?v=guHoZ68N3XM&t=3508s)** as part of home assistant.

**[58:29](https://youtube.com/watch?v=guHoZ68N3XM&t=3509s)** You can see we're basically just loaded now into VS code but in a browser.

**[58:33](https://youtube.com/watch?v=guHoZ68N3XM&t=3513s)** So look for this file here configuration.yaml and paste in those four lines from your clipboard.

**[58:39](https://youtube.com/watch?v=guHoZ68N3XM&t=3519s)** And then because you're in a browser some of the keyboard things don't pass through correctly.

**[58:43](https://youtube.com/watch?v=guHoZ68N3XM&t=3523s)** So file save manually just to make sure that this file does actually get saved.

**[58:48](https://youtube.com/watch?v=guHoZ68N3XM&t=3528s)** Go to settings and then restart home assistant.

**[58:52](https://youtube.com/watch?v=guHoZ68N3XM&t=3532s)** This will take maybe 10 or 15 seconds on the completely fresh install.

**[58:59](https://youtube.com/watch?v=guHoZ68N3XM&t=3539s)** On a more mature install, it could take a minute or two depending on how many add-ons you've got and that kind of thing.

**[59:06](https://youtube.com/watch?v=guHoZ68N3XM&t=3546s)** But once it's back up and running, you want to go back to add-ons and then tail scale and then configuration.

**[59:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3551s)** Click on show unused optional configurations and look for tail scale proxy.

**[59:18](https://youtube.com/watch?v=guHoZ68N3XM&t=3558s)** Check the box, click save, the tail scale add-ons going to have to restart.

**[59:22](https://youtube.com/watch?v=guHoZ68N3XM&t=3562s)** Yes, that's fine. Go ahead and do that.

**[59:26](https://youtube.com/watch?v=guHoZ68N3XM&t=3566s)** And then we want to look in the logs for all of the ACME requests for the TLS certificate.

**[59:31](https://youtube.com/watch?v=guHoZ68N3XM&t=3571s)** In fact, there we go.

**[59:33](https://youtube.com/watch?v=guHoZ68N3XM&t=3573s)** This is now available within your townnet on this URL right here.

**[59:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3577s)** So all being well, home assistant still restarting, of course.

**[59:41](https://youtube.com/watch?v=guHoZ68N3XM&t=3581s)** But the actual add-on is doing exactly what we wanted it to do.

**[59:46](https://youtube.com/watch?v=guHoZ68N3XM&t=3586s)** You can see we've got a full HTTPS certificate at home assistant,

**[59:49](https://youtube.com/watch?v=guHoZ68N3XM&t=3589s)** dot velociraptor, hyphen needle fish and we are now good to go.

**[59:54](https://youtube.com/watch?v=guHoZ68N3XM&t=3594s)** Get logged in with my username and password.

**[59:58](https://youtube.com/watch?v=guHoZ68N3XM&t=3598s)** And voila, I can now access this from anywhere on my tailnet.

**[01:00:02](https://youtube.com/watch?v=guHoZ68N3XM&t=3602s)** So let's do that.

**[01:00:04](https://youtube.com/watch?v=guHoZ68N3XM&t=3604s)** Let's control this light on my desk in front of me over tail scale over 5G.

**[01:00:10](https://youtube.com/watch?v=guHoZ68N3XM&t=3610s)** So let's turn the Wi-Fi off on my phone.

**[01:00:13](https://youtube.com/watch?v=guHoZ68N3XM&t=3613s)** Let's load up home assistant.

**[01:00:15](https://youtube.com/watch?v=guHoZ68N3XM&t=3615s)** In fact, I'm going to load up tail scale once more because I hate typing.

**[01:00:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3619s)** And then I'm going to go to home assistant, copy this URL right here.

**[01:00:23](https://youtube.com/watch?v=guHoZ68N3XM&t=3623s)** I suppose the DNS name.

**[01:00:25](https://youtube.com/watch?v=guHoZ68N3XM&t=3625s)** I'm going to go into the home assistant application.

**[01:00:28](https://youtube.com/watch?v=guHoZ68N3XM&t=3628s)** I'm going to enter my address manually and paste that from my clipboard.

**[01:00:33](https://youtube.com/watch?v=guHoZ68N3XM&t=3633s)** I want HTTPS.

**[01:00:35](https://youtube.com/watch?v=guHoZ68N3XM&t=3635s)** Yes, thank you, home assistant.

**[01:00:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3637s)** I'm going to connect to that.

**[01:00:38](https://youtube.com/watch?v=guHoZ68N3XM&t=3638s)** It's going to ask me to log in.

**[01:00:41](https://youtube.com/watch?v=guHoZ68N3XM&t=3641s)** So I will do to fully do.

**[01:00:44](https://youtube.com/watch?v=guHoZ68N3XM&t=3644s)** And now, but by the way, I'm on 5G.

**[01:00:47](https://youtube.com/watch?v=guHoZ68N3XM&t=3647s)** So I'm not on the same network as this, which means I could literally be anywhere in the world.

**[01:00:53](https://youtube.com/watch?v=guHoZ68N3XM&t=3653s)** And I've belayed with that point, but tail scale is amazing sometimes.

**[01:00:57](https://youtube.com/watch?v=guHoZ68N3XM&t=3657s)** And just simply by pressing the button on my phone over 5G with home assistant in what I've been filming this segment for 13 minutes,

**[01:01:06](https://youtube.com/watch?v=guHoZ68N3XM&t=3666s)** I'm sure in the edit it will be a little bit less, but we've just set up home assistant.

**[01:01:10](https://youtube.com/watch?v=guHoZ68N3XM&t=3670s)** And that's it.

**[01:01:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3671s)** That is the magic of tail scale right there.

**[01:01:14](https://youtube.com/watch?v=guHoZ68N3XM&t=3674s)** The magic of self hosting and tail scale, I suppose, actually.

**[01:01:18](https://youtube.com/watch?v=guHoZ68N3XM&t=3678s)** So what have we done today?

**[01:01:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3679s)** We have set up a Google Photos replacement.

**[01:01:22](https://youtube.com/watch?v=guHoZ68N3XM&t=3682s)** We have set up an audible audio books server replacement.

**[01:01:26](https://youtube.com/watch?v=guHoZ68N3XM&t=3686s)** We have started you down the journey of open source self hosted privacy respecting home automation.

**[01:01:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3692s)** And we've connected all of those things using our phone over 5G using tail scale.

**[01:01:37](https://youtube.com/watch?v=guHoZ68N3XM&t=3697s)** We haven't configured a single firewall rule.

**[01:01:39](https://youtube.com/watch?v=guHoZ68N3XM&t=3699s)** We're not paying for any subscriptions for any of this stuff.

**[01:01:42](https://youtube.com/watch?v=guHoZ68N3XM&t=3702s)** Tail scale is completely free for home users remember 100 devices and 3 users for free.

**[01:01:47](https://youtube.com/watch?v=guHoZ68N3XM&t=3707s)** And a device by the way counts as these.

**[01:01:50](https://youtube.com/watch?v=guHoZ68N3XM&t=3710s)** So we've used 5 devices today towards 100 device limit.

**[01:01:54](https://youtube.com/watch?v=guHoZ68N3XM&t=3714s)** But if you share tail scale with friends and family, you can add 2 devices to that free limit every time you refer someone to tail scale as well.

**[01:02:01](https://youtube.com/watch?v=guHoZ68N3XM&t=3721s)** So I know that was a super long epic two part series on how to get started with self hosting.

**[01:02:07](https://youtube.com/watch?v=guHoZ68N3XM&t=3727s)** If you have any questions about anything you've seen in today's video,

**[01:02:11](https://youtube.com/watch?v=guHoZ68N3XM&t=3731s)** I'll be doing some live streams over the next month or two where you can come and ask me questions directly.

**[01:02:16](https://youtube.com/watch?v=guHoZ68N3XM&t=3736s)** Or indeed, you can just leave a comment down below with a question.

**[01:02:19](https://youtube.com/watch?v=guHoZ68N3XM&t=3739s)** And I'll do my best to reply or even put that into some kind of like an ask tail scale like video at some point in the future.

**[01:02:25](https://youtube.com/watch?v=guHoZ68N3XM&t=3745s)** I should probably do one of those.

**[01:02:27](https://youtube.com/watch?v=guHoZ68N3XM&t=3747s)** But yeah, super long video.

**[01:02:30](https://youtube.com/watch?v=guHoZ68N3XM&t=3750s)** If you've made it to the end, thank you.

**[01:02:32](https://youtube.com/watch?v=guHoZ68N3XM&t=3752s)** Please leave a comment down below with the word bananas.

**[01:02:35](https://youtube.com/watch?v=guHoZ68N3XM&t=3755s)** And until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
