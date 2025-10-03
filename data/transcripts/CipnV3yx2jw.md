---
video_id: "CipnV3yx2jw"
title: "You need to try this Linux distro - Fedora uCore is absolutely fantastic!"
description: "This video discusses Fedora CoreOS. Today, we'll be using uBlue's uCore variant which comes with Tailscale pre-installed out of the box! 

uCore provides an immutable operating system where the base s..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-06-11"
duration_seconds: 1609
youtube_url: "https://www.youtube.com/watch?v=CipnV3yx2jw"
thumbnail_url: "https://i.ytimg.com/vi/CipnV3yx2jw/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:48:07.945693"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 4685
transcription_time_seconds: 43.3
---

# You need to try this Linux distro - Fedora uCore is absolutely fantastic!

**[00:00](https://youtube.com/watch?v=CipnV3yx2jw&t=0s)** In today's video, we're going to talk about Fedora Core OS. Specifically, we're going to talk about Fedora Core OS U-Blue. Specifically specifically, we're going to talk about Fedora Core OS U-Blue U-Core, Minimal, Stable, ZFS, Nvidia thing. Right, so what is this, first of all, Fedora Core OS is an immutable Linux distribution. So what that means is you can't change it once it's created.

**[00:30](https://youtube.com/watch?v=CipnV3yx2jw&t=30s)** It's in a very different way to any typical Linux distribution. The Fedora Core OS project, of course, is backed by Red Hat and the wonderful Fedora project. But Core OS specifically is designed to run containers. So everything that you're doing on this host is really targeted at containerization, to be honest. But what drew my attention to this specific distro is for the last little while, I've been doing a self-hosting series on this channel,

**[01:00](https://youtube.com/watch?v=CipnV3yx2jw&t=60s)** and I've been doing a self-hosting series up here, or part one or part two, actually, I think they're out now, is I've been looking for a way that I don't have to worry about installing Nvidia drivers on Linux anymore, because, see, these gray hairs in this beard, they're all due to Nvidia and installing the Nvidia drivers on Linux, I gest, but it can be a pain. I did a video a few months ago on using NICSOS to do this specific thing, but I'm slowly falling out of love with NICS, to be honest.

**[01:29](https://youtube.com/watch?v=CipnV3yx2jw&t=89s)** I want enough pressure release valves when things go wrong, and doing an immutable distro declaratively is hard. And the thing I like about Fedora Core OS is that they ship with a whole bunch of batteries included sane defaults. You can get Nvidia installed out of the box, you can get ZFS, you can get tail scale in one of their default images.

**[01:51](https://youtube.com/watch?v=CipnV3yx2jw&t=111s)** So, in today's video, I'm going to show you how to install Fedora Core OS, and talk about some of the intricacies along the way, and hopefully by the end of this, you're going to be able to start using your little Dell small form factor PC to not only run things like Home Assistant and Audio Bookshelf and Image, but also to start having some fun with virtual machines as well, because after all, you do have a home lab at your disposal now.

**[02:18](https://youtube.com/watch?v=CipnV3yx2jw&t=138s)** You can find more information about part one and two, as I probably already linked up here in the corner, and there'll be links to all of the co snippets and the playlist and everything else we're doing about self hosting on the channel at the moment in the description down below.

**[02:31](https://youtube.com/watch?v=CipnV3yx2jw&t=151s)** Now, hopefully you caught the last couple of videos, if not as a link to them up here, where we started building our little self hosted view of the world. And one of the top comments in that video was Alex. Why did you use Proxmox for this? You didn't actually use any of the Proxmox features.

**[02:47](https://youtube.com/watch?v=CipnV3yx2jw&t=167s)** Well, the reason was was because step three or step four of self hosting is experimentation. And that's what we're going to do today with you blue and you core and for whatever it's called.

**[02:58](https://youtube.com/watch?v=CipnV3yx2jw&t=178s)** Right. So we're going to download and install Fedora, you blue, you core, the thing that cannot quite figure out what I can't even figure out what his name is.

**[03:08](https://youtube.com/watch?v=CipnV3yx2jw&t=188s)** We're going to put that on top of Proxmox today. So we've got a few steps ahead of us. So if we take a look at the you core documentation,

**[03:15](https://youtube.com/watch?v=CipnV3yx2jw&t=195s)** we can see that it says like it's a batteries included this, right. But if we go down to the installation option here, the first step is that we have to install or figure out how to install Core OS.

**[03:28](https://youtube.com/watch?v=CipnV3yx2jw&t=208s)** And Core OS is basically the upstream, I suppose version of Fedora, the immutable operating system that you blue or you core these names is based on top of.

**[03:41](https://youtube.com/watch?v=CipnV3yx2jw&t=221s)** If you think it's confusing, try researching a video on this topic.

**[03:46](https://youtube.com/watch?v=CipnV3yx2jw&t=226s)** So I'm going to try and make this as easy as I possibly can to get started with Fedora, Core OS, all we need to do to begin with is download an ISO.

**[03:56](https://youtube.com/watch?v=CipnV3yx2jw&t=236s)** So to do that, we need to go to the Fedora, there'll be a link to all this stuff in the description, of course.

**[04:01](https://youtube.com/watch?v=CipnV3yx2jw&t=241s)** And we're going to download the latest ISO from the download page. Now another area of confusion potentially is that there's 25 different options on this page.

**[04:10](https://youtube.com/watch?v=CipnV3yx2jw&t=250s)** We just want the live DVD ISO file. So I'm going to click the download button, go here, stop this, because I don't actually want to do it this way, go to my full download history and copy this link here.

**[04:23](https://youtube.com/watch?v=CipnV3yx2jw&t=263s)** Now I am assuming at this point that you have a proxmox installation, because we're going to do this as a virtual machine, but you could just as easily do this with vert manager on a Linux desktop or a believe with virtual box or essentially all we're doing at this point is creating a virtual machine.

**[04:37](https://youtube.com/watch?v=CipnV3yx2jw&t=277s)** But there are, you know, I put together a whole series for you to get started with proxmox, so I'm going to use it.

**[04:45](https://youtube.com/watch?v=CipnV3yx2jw&t=285s)** Okay, so under local, we can go to ISO images. This is assuming everything is still set as default in proxmox, of course, which if it's a fresh install, it probably is.

**[04:55](https://youtube.com/watch?v=CipnV3yx2jw&t=295s)** You want to click on that little download from URL button, paste in the URL that you just put on your clipboard from the download page.

**[05:01](https://youtube.com/watch?v=CipnV3yx2jw&t=301s)** This guy over here, so copy that URL, put that onto your clipboard, click query URL and then tap on download.

**[05:10](https://youtube.com/watch?v=CipnV3yx2jw&t=310s)** This is going to download the Koro S, the Fedora Koro S ISO, just checking the names. I don't want to misspeak.

**[05:18](https://youtube.com/watch?v=CipnV3yx2jw&t=318s)** So this is downloading the Fedora Koro S ISO from the Fedora project, and all we're going to do with that is boot into Koro S.

**[05:28](https://youtube.com/watch?v=CipnV3yx2jw&t=328s)** Once we've done that, we then have to start providing all of our configuration files, but let's get Fedora Koro S booting, first of all, it's not too terribly difficult.

**[05:37](https://youtube.com/watch?v=CipnV3yx2jw&t=337s)** Because now we have the ISO file, we want to jump up to this button here that says create VM.

**[05:42](https://youtube.com/watch?v=CipnV3yx2jw&t=342s)** So I'm just going to give this a VM idea of 1000 and FCOS for Fedora Koro S, I suppose you call wouldn't hurt as a name.

**[05:51](https://youtube.com/watch?v=CipnV3yx2jw&t=351s)** I'm going to select Koro S here, system, I'm going to leave all of this alone, disks again just for now for this little demo.

**[06:01](https://youtube.com/watch?v=CipnV3yx2jw&t=361s)** None of this stuff really matters what you pick.

**[06:04](https://youtube.com/watch?v=CipnV3yx2jw&t=364s)** 4 CPU cores, yeah, let's do that. Memory, I'm just going to bump this up to 8GB, 8192 being 1024 times 8.

**[06:15](https://youtube.com/watch?v=CipnV3yx2jw&t=375s)** Network, yeah, that all looks good, confirm. All right, so with Proxmox, we can now see that we've got our virtual machine here, it's not doing anything.

**[06:26](https://youtube.com/watch?v=CipnV3yx2jw&t=386s)** So we want to click on the start button right here, and then on this option here, we want to head over to the VM console.

**[06:33](https://youtube.com/watch?v=CipnV3yx2jw&t=393s)** And you can see this looks an awful lot like a computer booting because it is, it's a virtual computer, a virtual machine.

**[06:39](https://youtube.com/watch?v=CipnV3yx2jw&t=399s)** So now we're loaded into our Fedora Koro S ISO, we have some work to do.

**[06:46](https://youtube.com/watch?v=CipnV3yx2jw&t=406s)** At least once it's initialized anyway, we have to generate what's called a ignition file.

**[06:51](https://youtube.com/watch?v=CipnV3yx2jw&t=411s)** And in order to do that, we have to create a human readable butane file as a few steps today.

**[06:59](https://youtube.com/watch?v=CipnV3yx2jw&t=419s)** But don't worry, all of the resources for everything we're doing will be linked in the description down below as ever in the Git repo.

**[07:05](https://youtube.com/watch?v=CipnV3yx2jw&t=425s)** Now, you can see that we are booted into Fedora Koro S. This is just like, it's like a live Linux ISO environment.

**[07:12](https://youtube.com/watch?v=CipnV3yx2jw&t=432s)** So let's do F disk minus L. In fact, I've just had the answer that I was looking for right here, but I need to do pseudo F disk minus L to get the name of the physical disk onto which we're going to install Fedora Koro S.

**[07:28](https://youtube.com/watch?v=CipnV3yx2jw&t=448s)** But we're also going to install Fedora Koro S that's been rebased to you, blue, you core.

**[07:36](https://youtube.com/watch?v=CipnV3yx2jw&t=456s)** Okay, I will get it straight in my head one of these days.

**[07:40](https://youtube.com/watch?v=CipnV3yx2jw&t=460s)** But just remember that, write it down on a piece of paper or whatever, however you take notes whilst you're doing these projects.

**[07:45](https://youtube.com/watch?v=CipnV3yx2jw&t=465s)** Dev SDA, that's what we need.

**[07:48](https://youtube.com/watch?v=CipnV3yx2jw&t=468s)** Okay, so we have got Fedora Koro S booting, but next we need to, as it says right here, produce an ignition file.

**[08:00](https://youtube.com/watch?v=CipnV3yx2jw&t=480s)** So this ignition file should at a minimum set a password or an SSH key for the default user.

**[08:06](https://youtube.com/watch?v=CipnV3yx2jw&t=486s)** The default username is core and then do and then do a bunch of other stuff too.

**[08:10](https://youtube.com/watch?v=CipnV3yx2jw&t=490s)** So I found this page actually quite overwhelming when I was researching this video.

**[08:15](https://youtube.com/watch?v=CipnV3yx2jw&t=495s)** So what we're looking at here is a butane configuration file.

**[08:18](https://youtube.com/watch?v=CipnV3yx2jw&t=498s)** This is the way that you configure a Koro S machine.

**[08:23](https://youtube.com/watch?v=CipnV3yx2jw&t=503s)** So the butane file gets transpiled and output as an ignition file.

**[08:29](https://youtube.com/watch?v=CipnV3yx2jw&t=509s)** And it's that ignition file that gets fed to the installer later on.

**[08:32](https://youtube.com/watch?v=CipnV3yx2jw&t=512s)** You can kind of think of it a little bit like a kickstart file if you're familiar with that kind of thing.

**[08:37](https://youtube.com/watch?v=CipnV3yx2jw&t=517s)** But we do need to grab your SSH key.

**[08:41](https://youtube.com/watch?v=CipnV3yx2jw&t=521s)** So we can go to the home directory with a little tilde icon and do a dot SSH ID ED 255 blah blah blah.

**[08:50](https://youtube.com/watch?v=CipnV3yx2jw&t=530s)** And then pipe that to PB copy on a Mac at least that puts the output of this command cat dot my public SSH key.

**[08:59](https://youtube.com/watch?v=CipnV3yx2jw&t=539s)** I put it on the clipboard.

**[09:01](https://youtube.com/watch?v=CipnV3yx2jw&t=541s)** So what I want to do is replace the authorized SSH keys with my public SSH key, which that's not quite what I meant PB copy.

**[09:09](https://youtube.com/watch?v=CipnV3yx2jw&t=549s)** Here we go.

**[09:11](https://youtube.com/watch?v=CipnV3yx2jw&t=551s)** Paste that and there we go.

**[09:13](https://youtube.com/watch?v=CipnV3yx2jw&t=553s)** So now I've got my SSH key as part of the butane configuration.

**[09:18](https://youtube.com/watch?v=CipnV3yx2jw&t=558s)** If you do not have an SSH key, you can go to the root of your home directory on your system.

**[09:25](https://youtube.com/watch?v=CipnV3yx2jw&t=565s)** So this will work on WSL this will work on macOS this will work on Linux to all SSH to all the same across all of those platforms.

**[09:33](https://youtube.com/watch?v=CipnV3yx2jw&t=573s)** You can go into the dot SSH directory if it exists and see what you've got.

**[09:37](https://youtube.com/watch?v=CipnV3yx2jw&t=577s)** You can do an LS now.

**[09:40](https://youtube.com/watch?v=CipnV3yx2jw&t=580s)** The difference between the public key and a private key is while the private key should stay private should always remain private.

**[09:47](https://youtube.com/watch?v=CipnV3yx2jw&t=587s)** Never tell or show that to anybody.

**[09:50](https://youtube.com/watch?v=CipnV3yx2jw&t=590s)** And that's this one here without the dot pub never show that to anybody.

**[09:54](https://youtube.com/watch?v=CipnV3yx2jw&t=594s)** But the pub file, that's pretty easy to show.

**[09:57](https://youtube.com/watch?v=CipnV3yx2jw&t=597s)** And the difference here is IDRSA is kind of like an older style.

**[10:02](https://youtube.com/watch?v=CipnV3yx2jw&t=602s)** So if you look at the length of this key, for example, you can see it's like four or five lines long.

**[10:07](https://youtube.com/watch?v=CipnV3yx2jw&t=607s)** Whereas a two five five one nine key uses a different cryptography algorithm, different curve.

**[10:13](https://youtube.com/watch?v=CipnV3yx2jw&t=613s)** If it's a cryptic curve, I believe.

**[10:16](https://youtube.com/watch?v=CipnV3yx2jw&t=616s)** And look at the length of that key.

**[10:18](https://youtube.com/watch?v=CipnV3yx2jw&t=618s)** So I switched to two five five one nine a long time ago, just simply because it's shorter and easier to read.

**[10:24](https://youtube.com/watch?v=CipnV3yx2jw&t=624s)** So go ahead, make the switch.

**[10:26](https://youtube.com/watch?v=CipnV3yx2jw&t=626s)** Get that into your config and then after that, you should be good to go.

**[10:31](https://youtube.com/watch?v=CipnV3yx2jw&t=631s)** Okay, so let's take a look at the rest of this butane file.

**[10:34](https://youtube.com/watch?v=CipnV3yx2jw&t=634s)** We've updated our SSH key.

**[10:36](https://youtube.com/watch?v=CipnV3yx2jw&t=636s)** You don't really need to worry about a great deal of the rest of this stuff.

**[10:39](https://youtube.com/watch?v=CipnV3yx2jw&t=639s)** Only add your user to the docker group if you're using docker rather than podman, which will come on to later.

**[10:45](https://youtube.com/watch?v=CipnV3yx2jw&t=645s)** I've customized the host name here.

**[10:48](https://youtube.com/watch?v=CipnV3yx2jw&t=648s)** Yes, I nicknamed this host DURP because Telska has DURP nodes and I think it's a funny word.

**[10:55](https://youtube.com/watch?v=CipnV3yx2jw&t=655s)** Well, we've got Zincati, which is the automatic way that Fedora CoroS keeps itself up to date.

**[11:03](https://youtube.com/watch?v=CipnV3yx2jw&t=663s)** But you core or you you blue you core names doesn't actually support or has some kind of an issue with Zincati.

**[11:13](https://youtube.com/watch?v=CipnV3yx2jw&t=673s)** So there is a way built into you core to keep itself automatically up to date already.

**[11:19](https://youtube.com/watch?v=CipnV3yx2jw&t=679s)** We just need to disable Zincati is an issue in GitHub, which I'll link to in the description down below.

**[11:25](https://youtube.com/watch?v=CipnV3yx2jw&t=685s)** But this is where it starts to get pretty cool.

**[11:28](https://youtube.com/watch?v=CipnV3yx2jw&t=688s)** So when we're installing you blue, you core, when we're installing you core, it's not actually installing CoroS.

**[11:40](https://youtube.com/watch?v=CipnV3yx2jw&t=700s)** It's re but it installs CoroS that this is how I understand it.

**[11:44](https://youtube.com/watch?v=CipnV3yx2jw&t=704s)** It installs CoroS and then it rebases itself off an OCI compliant image using RPM OS tree pretty, pretty cool.

**[11:52](https://youtube.com/watch?v=CipnV3yx2jw&t=712s)** But where do we get this string from?

**[11:55](https://youtube.com/watch?v=CipnV3yx2jw&t=715s)** How do we know which image, which whatever we're going to use?

**[11:58](https://youtube.com/watch?v=CipnV3yx2jw&t=718s)** How do we know what to pick?

**[12:00](https://youtube.com/watch?v=CipnV3yx2jw&t=720s)** Well, in the Github repo, which again will be linked in the description down below, you can see there's a whole bunch of different images here.

**[12:07](https://youtube.com/watch?v=CipnV3yx2jw&t=727s)** They've got Fedora CoroS, like the main upstream version.

**[12:11](https://youtube.com/watch?v=CipnV3yx2jw&t=731s)** You've got you core minimal, which is a batteries included with a bunch of same defaults.

**[12:16](https://youtube.com/watch?v=CipnV3yx2jw&t=736s)** You've got you core and then you core HCI.

**[12:19](https://youtube.com/watch?v=CipnV3yx2jw&t=739s)** And the documentation takes you through all of the different permutations of each of these different things.

**[12:25](https://youtube.com/watch?v=CipnV3yx2jw&t=745s)** So you can see that this Fedora CoroS is just a generic Fedora CoroS image with some add-on modules specifically around ZFS and Nvidia.

**[12:36](https://youtube.com/watch?v=CipnV3yx2jw&t=756s)** Now, if you know anything about Linux and licensing and that kind of stuff, you'll appreciate why this is such a big deal.

**[12:41](https://youtube.com/watch?v=CipnV3yx2jw&t=761s)** You don't have to worry about DKMS, you don't have to worry about compiling kernels or all the rest of it, it just works.

**[12:48](https://youtube.com/watch?v=CipnV3yx2jw&t=768s)** If you've been looking for some really easy way to have a virtual machine with Nvidia drivers installed on Linux, you don't have to ever have to worry about ever again.

**[12:59](https://youtube.com/watch?v=CipnV3yx2jw&t=779s)** And it auto updates itself.

**[13:01](https://youtube.com/watch?v=CipnV3yx2jw&t=781s)** Here is your answer.

**[13:03](https://youtube.com/watch?v=CipnV3yx2jw&t=783s)** I'm very excited to have discovered this project in the last couple of weeks.

**[13:06](https://youtube.com/watch?v=CipnV3yx2jw&t=786s)** I absolutely love it.

**[13:07](https://youtube.com/watch?v=CipnV3yx2jw&t=787s)** Now, if you want to take this a little bit further and extend it using you core, you can look at the other packages that are installed inside.

**[13:14](https://youtube.com/watch?v=CipnV3yx2jw&t=794s)** Now, the one that I'm going to pick today is you core minimal because it includes tail scale, of course.

**[13:19](https://youtube.com/watch?v=CipnV3yx2jw&t=799s)** Now, I don't have to worry about installing tail scale on this host.

**[13:23](https://youtube.com/watch?v=CipnV3yx2jw&t=803s)** It comes pre-baked as part of this image along with the Nvidia and ZFS drivers and cockpit and all the rest of it that you can see on the screen right here.

**[13:32](https://youtube.com/watch?v=CipnV3yx2jw&t=812s)** You core itself takes you core minimal and extends that again by adding a few more packages, such as merger FS.

**[13:39](https://youtube.com/watch?v=CipnV3yx2jw&t=819s)** If you're a media server aficionado, such as myself, perfect media server.com, give you all the details there.

**[13:46](https://youtube.com/watch?v=CipnV3yx2jw&t=826s)** You can see that Samber is there, snap rate is there, merger FS are clone.

**[13:52](https://youtube.com/watch?v=CipnV3yx2jw&t=832s)** If you want to synchronize or mount cloud storage, those tools are invaluable.

**[13:59](https://youtube.com/watch?v=CipnV3yx2jw&t=839s)** And if you'd like to use you core to replace or at least attempt to replace proxmox, you can use the HCI image.

**[14:08](https://youtube.com/watch?v=CipnV3yx2jw&t=848s)** It's a really interesting project.

**[14:10](https://youtube.com/watch?v=CipnV3yx2jw&t=850s)** I think, hopefully, by the time you've got to this point in the video, you're starting to see why I'm so excited about it and just why you've got so many options here.

**[14:17](https://youtube.com/watch?v=CipnV3yx2jw&t=857s)** So I'm going to pick just for our purposes in this video.

**[14:21](https://youtube.com/watch?v=CipnV3yx2jw&t=861s)** So I put stable Nvidia ZFS kind of regretting that choice.

**[14:26](https://youtube.com/watch?v=CipnV3yx2jw&t=866s)** I might just do stable ZFS because I don't have an Nvidia GPU in that system.

**[14:31](https://youtube.com/watch?v=CipnV3yx2jw&t=871s)** But I might do some playing around with ZFS.

**[14:34](https://youtube.com/watch?v=CipnV3yx2jw&t=874s)** And this is the magic of having a home lab, of having a self-hosting ecosystem.

**[14:38](https://youtube.com/watch?v=CipnV3yx2jw&t=878s)** It's up to you to make these choices.

**[14:41](https://youtube.com/watch?v=CipnV3yx2jw&t=881s)** Nobody telling you what you should or shouldn't be doing like it's up to you.

**[14:44](https://youtube.com/watch?v=CipnV3yx2jw&t=884s)** So that's where this string comes from.

**[14:47](https://youtube.com/watch?v=CipnV3yx2jw&t=887s)** We're going to replace this image here with stable ZFS so we don't get the Nvidia drivers because we don't need them here.

**[14:54](https://youtube.com/watch?v=CipnV3yx2jw&t=894s)** Now, I have asked to replace the podman engine that ships by default with Docker.

**[15:02](https://youtube.com/watch?v=CipnV3yx2jw&t=902s)** You can remove this and go full podman if you want to.

**[15:05](https://youtube.com/watch?v=CipnV3yx2jw&t=905s)** Totally, this is totally Alex's opinion here and absolutely not needed.

**[15:10](https://youtube.com/watch?v=CipnV3yx2jw&t=910s)** In fact, do I even need this part here with the Nvidia thing?

**[15:15](https://youtube.com/watch?v=CipnV3yx2jw&t=915s)** Probably not because this was me testing around earlier for my little machine learning virtual machine.

**[15:20](https://youtube.com/watch?v=CipnV3yx2jw&t=920s)** It does my image stuff and alarm and a bunch of other stuff, but kind of then reused it for this video.

**[15:26](https://youtube.com/watch?v=CipnV3yx2jw&t=926s)** ZFS is here mod probe.

**[15:28](https://youtube.com/watch?v=CipnV3yx2jw&t=928s)** Yeah.

**[15:29](https://youtube.com/watch?v=CipnV3yx2jw&t=929s)** Okay.

**[15:30](https://youtube.com/watch?v=CipnV3yx2jw&t=930s)** So I think that means our butane file is now compiled.

**[15:33](https://youtube.com/watch?v=CipnV3yx2jw&t=933s)** Well, not compiled.

**[15:34](https://youtube.com/watch?v=CipnV3yx2jw&t=934s)** Our butane file is now configured and ready to go.

**[15:37](https://youtube.com/watch?v=CipnV3yx2jw&t=937s)** This is like a minimum viable butane file here.

**[15:40](https://youtube.com/watch?v=CipnV3yx2jw&t=940s)** So now we need to do the transpiling bit.

**[15:43](https://youtube.com/watch?v=CipnV3yx2jw&t=943s)** This is my search for the word butane.

**[15:46](https://youtube.com/watch?v=CipnV3yx2jw&t=946s)** Here we go.

**[15:48](https://youtube.com/watch?v=CipnV3yx2jw&t=948s)** Okay.

**[15:49](https://youtube.com/watch?v=CipnV3yx2jw&t=949s)** I should also point out that if you don't want to use Alex's opinionated script, there is an example linked in the U-Core project documentation itself, which goes through.

**[15:59](https://youtube.com/watch?v=CipnV3yx2jw&t=959s)** This is the minimum viable way of getting Fedora Corus U-Core installed.

**[16:06](https://youtube.com/watch?v=CipnV3yx2jw&t=966s)** U-Blue U-Core installed.

**[16:08](https://youtube.com/watch?v=CipnV3yx2jw&t=968s)** Yeah.

**[16:09](https://youtube.com/watch?v=CipnV3yx2jw&t=969s)** It's pretty cool stuff.

**[16:10](https://youtube.com/watch?v=CipnV3yx2jw&t=970s)** Okay.

**[16:11](https://youtube.com/watch?v=CipnV3yx2jw&t=971s)** So now we need to use the butane utility to produce ourselves a ignition file.

**[16:18](https://youtube.com/watch?v=CipnV3yx2jw&t=978s)** So I'm going to copy this command here to my clipboard.

**[16:21](https://youtube.com/watch?v=CipnV3yx2jw&t=981s)** Go back to my VS Code window and just paste this in here.

**[16:27](https://youtube.com/watch?v=CipnV3yx2jw&t=987s)** Now I am using Obstac remember to get a Docker command.

**[16:30](https://youtube.com/watch?v=CipnV3yx2jw&t=990s)** So if I type Docker, you will see that that works just fine.

**[16:36](https://youtube.com/watch?v=CipnV3yx2jw&t=996s)** If I type podman, doesn't exist on this host.

**[16:40](https://youtube.com/watch?v=CipnV3yx2jw&t=1000s)** Fair enough.

**[16:41](https://youtube.com/watch?v=CipnV3yx2jw&t=1001s)** So what I want to do is take that command that was just copied from the Corus website and just replace the word podman with Docker.

**[16:51](https://youtube.com/watch?v=CipnV3yx2jw&t=1011s)** The other thing that I need to change is your config.bu.

**[16:55](https://youtube.com/watch?v=CipnV3yx2jw&t=1015s)** I need to change that to config.

**[16:58](https://youtube.com/watch?v=CipnV3yx2jw&t=1018s)** You can see here the name I gave that file is config.bu.

**[17:02](https://youtube.com/watch?v=CipnV3yx2jw&t=1022s)** I also need to change into the correct directory.

**[17:06](https://youtube.com/watch?v=CipnV3yx2jw&t=1026s)** So I've got the correct context for this command.

**[17:09](https://youtube.com/watch?v=CipnV3yx2jw&t=1029s)** Now this is going to download a container from key.io, Corus butane and run the butane binary inside a container.

**[17:19](https://youtube.com/watch?v=CipnV3yx2jw&t=1039s)** Now the butane project provides several ways for you to install this in different ways.

**[17:25](https://youtube.com/watch?v=CipnV3yx2jw&t=1045s)** All is natively on your host if you want to using brew, using Mac ports, scoop, wind get, standalone binaries, all that stuff.

**[17:35](https://youtube.com/watch?v=CipnV3yx2jw&t=1055s)** But you know if you're going to run it in a container, you've got exactly what upstream is pushing.

**[17:39](https://youtube.com/watch?v=CipnV3yx2jw&t=1059s)** So that's what I'm going to do.

**[17:41](https://youtube.com/watch?v=CipnV3yx2jw&t=1061s)** Now this was an artifact of me screwing up a minute ago.

**[17:44](https://youtube.com/watch?v=CipnV3yx2jw&t=1064s)** So let's delete that and let's take a look at the transpiled configuration file.

**[17:49](https://youtube.com/watch?v=CipnV3yx2jw&t=1069s)** So this is what we're going to serve to the Fedora Corus installer.

**[17:54](https://youtube.com/watch?v=CipnV3yx2jw&t=1074s)** Basically the idea is that butane is easy for humans to read and write.

**[17:59](https://youtube.com/watch?v=CipnV3yx2jw&t=1079s)** But ignition is a bit like JSON.

**[18:02](https://youtube.com/watch?v=CipnV3yx2jw&t=1082s)** It's got to be formatted in a very specific way.

**[18:05](https://youtube.com/watch?v=CipnV3yx2jw&t=1085s)** It would be no fun to write this stuff by hand.

**[18:08](https://youtube.com/watch?v=CipnV3yx2jw&t=1088s)** So what we want to do now is a basic Python HTTP server, so 8000.

**[18:14](https://youtube.com/watch?v=CipnV3yx2jw&t=1094s)** And that's going to put the contents of this directory on the IP address of my host

**[18:20](https://youtube.com/watch?v=CipnV3yx2jw&t=1100s)** and make it available on an IP address.

**[18:23](https://youtube.com/watch?v=CipnV3yx2jw&t=1103s)** Now you'll notice that because I have the tail scale VS code extension installed here,

**[18:27](https://youtube.com/watch?v=CipnV3yx2jw&t=1107s)** it's detected that Python has started running a web server on port 8000.

**[18:31](https://youtube.com/watch?v=CipnV3yx2jw&t=1111s)** So if I wanted to, I could now advertise this ignition file over the public internet

**[18:37](https://youtube.com/watch?v=CipnV3yx2jw&t=1117s)** and then have Corus call back to that from maybe a VPS or something like that.

**[18:42](https://youtube.com/watch?v=CipnV3yx2jw&t=1122s)** And there's no route between those two hosts otherwise.

**[18:45](https://youtube.com/watch?v=CipnV3yx2jw&t=1125s)** You could temporarily put it on the public internet using tail scale funnel.

**[18:48](https://youtube.com/watch?v=CipnV3yx2jw&t=1128s)** I'm not going to do that today, but you could if you wanted to.

**[18:52](https://youtube.com/watch?v=CipnV3yx2jw&t=1132s)** Now I need to get my IP address for this particular laptop.

**[18:56](https://youtube.com/watch?v=CipnV3yx2jw&t=1136s)** So I'm going to do if config and then look for a 10 dot something IP address 10.

**[19:03](https://youtube.com/watch?v=CipnV3yx2jw&t=1143s)** 42.7.34 because now it's time to actually install Corus.

**[19:10](https://youtube.com/watch?v=CipnV3yx2jw&t=1150s)** And indeed, if we go back to the project documentation, we can see here under the

**[19:14](https://youtube.com/watch?v=CipnV3yx2jw&t=1154s)** installing from live ISO section, here is the command that we need.

**[19:18](https://youtube.com/watch?v=CipnV3yx2jw&t=1158s)** We need this little pseudo Corus doodad to be up here.

**[19:22](https://youtube.com/watch?v=CipnV3yx2jw&t=1162s)** So let me try and get this up here and out of the way.

**[19:25](https://youtube.com/watch?v=CipnV3yx2jw&t=1165s)** We need this little doodad here, pseudo Corus blah blah blah.

**[19:29](https://youtube.com/watch?v=CipnV3yx2jw&t=1169s)** So pseudo core OS installer install slash dev slash SDA.

**[19:36](https://youtube.com/watch?v=CipnV3yx2jw&t=1176s)** Now remember at the beginning of the video, I talked about you're going to want to remember

**[19:40](https://youtube.com/watch?v=CipnV3yx2jw&t=1180s)** the disk ID, the disk moniker that you're referring to install Corus onto.

**[19:46](https://youtube.com/watch?v=CipnV3yx2jw&t=1186s)** So it could be VDA if it's a virtual machine with a vertio disk.

**[19:50](https://youtube.com/watch?v=CipnV3yx2jw&t=1190s)** In our case, it's SDA, it could be NVMeO1 if you're on a physical host.

**[19:54](https://youtube.com/watch?v=CipnV3yx2jw&t=1194s)** So this will change depending on what you're doing.

**[19:57](https://youtube.com/watch?v=CipnV3yx2jw&t=1197s)** We then want to do our ignition URL.

**[19:59](https://youtube.com/watch?v=CipnV3yx2jw&t=1199s)** So this is going to point to our Python IP address, I suppose.

**[20:05](https://youtube.com/watch?v=CipnV3yx2jw&t=1205s)** Our little Python HTTP server.

**[20:08](https://youtube.com/watch?v=CipnV3yx2jw&t=1208s)** So I want to do 10.42.7.34, port 8000.

**[20:13](https://youtube.com/watch?v=CipnV3yx2jw&t=1213s)** And then it was transpiled config.igm, I think.

**[20:19](https://youtube.com/watch?v=CipnV3yx2jw&t=1219s)** Was it transpiled unschool config.igm?

**[20:23](https://youtube.com/watch?v=CipnV3yx2jw&t=1223s)** Yes, perfect.

**[20:24](https://youtube.com/watch?v=CipnV3yx2jw&t=1224s)** Now it's going to shout out to me because this is a plain text URL.

**[20:27](https://youtube.com/watch?v=CipnV3yx2jw&t=1227s)** Ah, yes.

**[20:29](https://youtube.com/watch?v=CipnV3yx2jw&t=1229s)** Well, it's going to shout out to me for a different reason because apparently I can't type.

**[20:33](https://youtube.com/watch?v=CipnV3yx2jw&t=1233s)** Okay, so I need to because this is a plain HTTP URL, I need to do insecure ignition.

**[20:41](https://youtube.com/watch?v=CipnV3yx2jw&t=1241s)** It's now going to download and install Core OS.

**[20:46](https://youtube.com/watch?v=CipnV3yx2jw&t=1246s)** It could not be easier apart from all the last 15 minutes worth of steps.

**[20:53](https://youtube.com/watch?v=CipnV3yx2jw&t=1253s)** It took to get to this point.

**[20:55](https://youtube.com/watch?v=CipnV3yx2jw&t=1255s)** So it tells me the installation is complete.

**[20:57](https://youtube.com/watch?v=CipnV3yx2jw&t=1257s)** So I'm going to go ahead and reboot.

**[20:59](https://youtube.com/watch?v=CipnV3yx2jw&t=1259s)** So remember, I was booted into the ISO file.

**[21:02](https://youtube.com/watch?v=CipnV3yx2jw&t=1262s)** I'm now going to reboot into Fedora Core OS proper.

**[21:06](https://youtube.com/watch?v=CipnV3yx2jw&t=1266s)** Now the last time I did this, the machine booted.

**[21:09](https://youtube.com/watch?v=CipnV3yx2jw&t=1269s)** And I believe the rebase script did its thing and rebased to you blue you call.

**[21:15](https://youtube.com/watch?v=CipnV3yx2jw&t=1275s)** So the very first boot is booting into Fedora Core OS proper.

**[21:21](https://youtube.com/watch?v=CipnV3yx2jw&t=1281s)** And then it does the rebase into the the you blue you call version.

**[21:26](https://youtube.com/watch?v=CipnV3yx2jw&t=1286s)** And we can probably see that happening actually.

**[21:28](https://youtube.com/watch?v=CipnV3yx2jw&t=1288s)** If we look at the CPU usage in real time, yeah.

**[21:31](https://youtube.com/watch?v=CipnV3yx2jw&t=1291s)** A brand new system would not be pulling 26% of CPU sat there doing nothing.

**[21:37](https://youtube.com/watch?v=CipnV3yx2jw&t=1297s)** So if you keep an eye on the console in just a moment, this virtual machine is going to reboot.

**[21:42](https://youtube.com/watch?v=CipnV3yx2jw&t=1302s)** And then when it does actually keep an eye on this, currently it says Fedora Core OS 42.20, 25, 05, 26.

**[21:51](https://youtube.com/watch?v=CipnV3yx2jw&t=1311s)** When it reboots, let's see what it looks like.

**[21:56](https://youtube.com/watch?v=CipnV3yx2jw&t=1316s)** And there we go. We're back from the reboot.

**[21:58](https://youtube.com/watch?v=CipnV3yx2jw&t=1318s)** And you can see that we've now rebased to you call minimal.

**[22:01](https://youtube.com/watch?v=CipnV3yx2jw&t=1321s)** So if I try and log in now core, I didn't set a password deliberately.

**[22:06](https://youtube.com/watch?v=CipnV3yx2jw&t=1326s)** I didn't do a hashed password. So I need my IP address of 192.

**[22:10](https://youtube.com/watch?v=CipnV3yx2jw&t=1330s)** Let me go back to my terminal window. I need to go to SSH Core at 192.168.1.129.

**[22:21](https://youtube.com/watch?v=CipnV3yx2jw&t=1341s)** I'm now SSH into my, I called it DURP, didn't I?

**[22:26](https://youtube.com/watch?v=CipnV3yx2jw&t=1346s)** Such a silly host name. But there you go.

**[22:29](https://youtube.com/watch?v=CipnV3yx2jw&t=1349s)** And I have a bunch of packages installed. So I've got Docker.

**[22:32](https://youtube.com/watch?v=CipnV3yx2jw&t=1352s)** That's here. That's ready to go. I haven't had to install anything.

**[22:35](https://youtube.com/watch?v=CipnV3yx2jw&t=1355s)** I've got tail scale. That's also there too.

**[22:39](https://youtube.com/watch?v=CipnV3yx2jw&t=1359s)** Happy days. That keeps my boss happy.

**[22:42](https://youtube.com/watch?v=CipnV3yx2jw&t=1362s)** But what else can we do? What about something like H top?

**[22:46](https://youtube.com/watch?v=CipnV3yx2jw&t=1366s)** Ah, okay. So what happens with an immutable OS when we want to install packages?

**[22:52](https://youtube.com/watch?v=CipnV3yx2jw&t=1372s)** Well, typically on a Linux distro, we do something like pseudo at install H top or whatever.

**[22:59](https://youtube.com/watch?v=CipnV3yx2jw&t=1379s)** Now there's a couple of ways you can do it on Fedora Core OS.

**[23:02](https://youtube.com/watch?v=CipnV3yx2jw&t=1382s)** One of them is to use RPM OS tree and do install,

**[23:06](https://youtube.com/watch?v=CipnV3yx2jw&t=1386s)** let's do Neo fetch to start with.

**[23:09](https://youtube.com/watch?v=CipnV3yx2jw&t=1389s)** And this is going to ask for, yeah, pseudo privileges fair enough.

**[23:13](https://youtube.com/watch?v=CipnV3yx2jw&t=1393s)** It's going to download much like you would do with a DNF update or something like that.

**[23:17](https://youtube.com/watch?v=CipnV3yx2jw&t=1397s)** It's going to download the latest version of the metadata of the repos

**[23:21](https://youtube.com/watch?v=CipnV3yx2jw&t=1401s)** and then install the latest package.

**[23:23](https://youtube.com/watch?v=CipnV3yx2jw&t=1403s)** But it doesn't do it in quite the way you might expect.

**[23:26](https://youtube.com/watch?v=CipnV3yx2jw&t=1406s)** You have to reboot the host in order for this package to be available.

**[23:30](https://youtube.com/watch?v=CipnV3yx2jw&t=1410s)** There are some kind of things you're going to have to get used to.

**[23:34](https://youtube.com/watch?v=CipnV3yx2jw&t=1414s)** One of those apparently is that Neo fetch isn't in the repos.

**[23:37](https://youtube.com/watch?v=CipnV3yx2jw&t=1417s)** Okay, so let's just do H top because I know that that one is.

**[23:41](https://youtube.com/watch?v=CipnV3yx2jw&t=1421s)** So it's checking out the latest version of the RPM OS tree

**[23:44](https://youtube.com/watch?v=CipnV3yx2jw&t=1424s)** and now it's downloading H top from the repos.

**[23:47](https://youtube.com/watch?v=CipnV3yx2jw&t=1427s)** And much like the documentation says right here,

**[23:50](https://youtube.com/watch?v=CipnV3yx2jw&t=1430s)** it's a good idea to become familiar with the Fedora Core OS documentation

**[23:54](https://youtube.com/watch?v=CipnV3yx2jw&t=1434s)** and how RPM OS tree actually works under the hood.

**[23:58](https://youtube.com/watch?v=CipnV3yx2jw&t=1438s)** Core OS doesn't really want you to install packages on the host itself.

**[24:03](https://youtube.com/watch?v=CipnV3yx2jw&t=1443s)** It wants to keep the host completely clean.

**[24:05](https://youtube.com/watch?v=CipnV3yx2jw&t=1445s)** It's like a cattle versus pets scenario if you've heard of that.

**[24:08](https://youtube.com/watch?v=CipnV3yx2jw&t=1448s)** But our latest top install has now completed.

**[24:11](https://youtube.com/watch?v=CipnV3yx2jw&t=1451s)** But currently it's not available in the system to be used.

**[24:15](https://youtube.com/watch?v=CipnV3yx2jw&t=1455s)** So we're going to have to reboot the virtual machine.

**[24:17](https://youtube.com/watch?v=CipnV3yx2jw&t=1457s)** If we go back over to our proxmox host, we can monitor the progress of that reboot.

**[24:21](https://youtube.com/watch?v=CipnV3yx2jw&t=1461s)** And remember, this is all running on that little small one-litre Dell small form factor PC.

**[24:26](https://youtube.com/watch?v=CipnV3yx2jw&t=1466s)** You don't need a huge rack worth of service to have some fun in your home lab.

**[24:30](https://youtube.com/watch?v=CipnV3yx2jw&t=1470s)** This is running image. This is running home assistant.

**[24:33](https://youtube.com/watch?v=CipnV3yx2jw&t=1473s)** This is running audio bookshelf all at the same time.

**[24:35](https://youtube.com/watch?v=CipnV3yx2jw&t=1475s)** Whilst it's doing all this stuff with Fedora you call,

**[24:38](https://youtube.com/watch?v=CipnV3yx2jw&t=1478s)** it's really like, honestly, modern computers are incredible.

**[24:43](https://youtube.com/watch?v=CipnV3yx2jw&t=1483s)** Now we've rebooted.

**[24:44](https://youtube.com/watch?v=CipnV3yx2jw&t=1484s)** You can see that we've got H top available to us.

**[24:47](https://youtube.com/watch?v=CipnV3yx2jw&t=1487s)** Let's just recap real quick before we get out of here.

**[24:49](https://youtube.com/watch?v=CipnV3yx2jw&t=1489s)** The steps required because they were a couple.

**[24:53](https://youtube.com/watch?v=CipnV3yx2jw&t=1493s)** Really, it can actually just be boiled down to the fact that we need to create ourselves a butane configuration file,

**[25:00](https://youtube.com/watch?v=CipnV3yx2jw&t=1500s)** which again will be linked in the description down below.

**[25:04](https://youtube.com/watch?v=CipnV3yx2jw&t=1504s)** Then transpile out to ignition.

**[25:06](https://youtube.com/watch?v=CipnV3yx2jw&t=1506s)** Provide that ignition file over some kind of a web server to make it available to the remote core OS host.

**[25:13](https://youtube.com/watch?v=CipnV3yx2jw&t=1513s)** And I used Python to do that with this little Python HTTP web server right here on port 8000.

**[25:20](https://youtube.com/watch?v=CipnV3yx2jw&t=1520s)** And that, honestly, is probably the easiest Linux install you will ever do.

**[25:26](https://youtube.com/watch?v=CipnV3yx2jw&t=1526s)** And on top of that, it's all declarative.

**[25:28](https://youtube.com/watch?v=CipnV3yx2jw&t=1528s)** So you can use these butane files to declare things like disc layouts, a bunch of other stuff besides.

**[25:34](https://youtube.com/watch?v=CipnV3yx2jw&t=1534s)** So please, if you find this interesting, leave a comment down below.

**[25:38](https://youtube.com/watch?v=CipnV3yx2jw&t=1538s)** I'd love to know what you're doing with Fedora Core OS or whether this is just one of those videos

**[25:43](https://youtube.com/watch?v=CipnV3yx2jw&t=1543s)** that Alex found something interesting and nobody else does.

**[25:46](https://youtube.com/watch?v=CipnV3yx2jw&t=1546s)** It doesn't seem to happen too often, but who knows.

**[25:49](https://youtube.com/watch?v=CipnV3yx2jw&t=1549s)** So if you have any other questions about self-hosting and the self-hosting series that we're kind of doing on the channels for the next few videos,

**[25:56](https://youtube.com/watch?v=CipnV3yx2jw&t=1556s)** leave a comment down below and I'm going to do like a Q&A video fairly soon picking out some of the best questions from the comment section.

**[26:03](https://youtube.com/watch?v=CipnV3yx2jw&t=1563s)** And just try and answer them and try and help you all along with your self-hosting journey.

**[26:09](https://youtube.com/watch?v=CipnV3yx2jw&t=1569s)** Of course, if you do install Fedora Core OS, the rules of the tailscale channel are that you must install and set up tailscale and add this note to your tailnet.

**[26:17](https://youtube.com/watch?v=CipnV3yx2jw&t=1577s)** Remember, you get 100 devices for free and three users for free too on the tailscale free plan. So there's really no excuse not to.

**[26:25](https://youtube.com/watch?v=CipnV3yx2jw&t=1585s)** Thank you very much for watching and until next time, I've been Alex from Tailscale.

---

*Automatically generated transcript. May contain errors.*
