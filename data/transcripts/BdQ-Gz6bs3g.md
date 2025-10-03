---
video_id: "BdQ-Gz6bs3g"
title: "Use your Tailscale identity everywhere! Automatically login to Proxmox with tsidp"
description: "Did you know that you can use Tailscale to automatically login to your Proxmox instance? In today's video I'll show you how to use tsidp to do just that.

- https://github.com/tailscale-dev/video-code..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-12-27"
duration_seconds: 843
youtube_url: "https://www.youtube.com/watch?v=BdQ-Gz6bs3g"
thumbnail_url: "https://i.ytimg.com/vi/BdQ-Gz6bs3g/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:30:01.467797"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2669
transcription_time_seconds: 23.2
---

# Use your Tailscale identity everywhere! Automatically login to Proxmox with tsidp

**[00:00](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=0s)** Proxmox uses you are probably familiar at this point with this screen, logging in. It kind of is a bit of a pain, right? It wouldn't be nice if you could reuse the identity of your Tailscale network, your Tailnet, to automatically log in to Proxmox for you. Well, in today's video, that's exactly what I'm going to show you. I'm going to show you how to configure something called TSIDP. It's an experimental identity provider that Tailscale ships.

**[00:30](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=30s)** And I'm going to show you how to plug that into Proxmox so that you can automatically log in to Proxmox just by virtue of being connected to a specific Tailnet.

**[00:40](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=40s)** So I have here my demo Proxmox cluster. It's just running on three Dell, you know, those small form factor PCs in my little rack next door. You can see I've got three nodes in this cluster and Hammond seems to crash a lot.

**[00:57](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=57s)** I can't think why Top Gear joke. Anyway, so what I wanted to show you is how to configure Proxmox with something called Tailscale IDP, TSIDP. Full disclaimer, this is an experimental piece of software and shouldn't be relied on in production, blah, blah, blah, here be dragons. All right, it works though. And certainly in a home lab setting, it should be stable enough.

**[01:20](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=80s)** So what we're going to do is use the Proxmox realms feature to add a new open ID connect server. So up here in your data center, you'll notice that there's a whole bunch of stuff.

**[01:31](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=91s)** Certainly before I prep this video, stuff I'd never clicked on, but down here, there's a section called realms and you can actually add an open ID connect server. And of course, that's what TSIDP is going to implement for us.

**[01:44](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=104s)** So what we need to do first is build the binary that's going to run TSIDP to statically compiled go app. So it only takes a second. So the first thing we're going to need to do is actually compile the TSIDP binary.

**[01:57](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=117s)** We can do that by going to GitHub and the tailscale slash tailscale get repository up here in the top right. There is a big green code button. And if you copy that URL to your clipboard and then just go to any directory on your local system.

**[02:11](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=131s)** It doesn't really matter what it is. I'm just going to go into get here and then just go into the tailscale directory makes sense. Right. And then do get clone. I like to organize all of my get repose just this way. It's up to you wherever you put this doesn't really matter.

**[02:25](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=145s)** Once that's cloned, go ahead and change into the tailscale directory and your structure should look something like this.

**[02:32](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=152s)** The next command we're going to want to enter is this one. It's called go OS equals Linux. So I'm presupposing that the architecture that you're compiling this binary for is an AMD 64 x86 type chip.

**[02:46](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=166s)** You can see the architecture we're compiling for here is AMD 64. The nice thing about go is that we can actually build binaries for different architectures from what we're actually compiling on.

**[02:57](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=177s)** So this is running on an Apple Silicon MacBook, but I'm compiling for a Linux x86 target system. So that's pretty nice.

**[03:06](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=186s)** Once that command is done, we should have a new binary just in the root of the get repo here. And you can see TSIDP is indeed now present.

**[03:14](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=194s)** So we're going to want to SSH as well as up to you, it could be root. It could be a user, but we're going to need a way to get this binary on to the proxmox host in question.

**[03:24](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=204s)** So for me, you can see I've got SSH access here. So I'm just going to use SCP. So just copy that binary across TSIDP. So if I do SCP TSIDP and then root at and then the IP address of the remote proxmox host,

**[03:42](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=222s)** this is going to put that binary in the home directory of the root user on the remote proxmox node.

**[03:47](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=227s)** And then going to SSH back to the proxmox node. So 10. In my case, 10.42, 37.10 is the remote proxmox node. And then we need to set some things up.

**[03:59](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=239s)** We need to set a system D service and environments file, couple of other things. So lucky for you, here's one I made earlier.

**[04:07](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=247s)** And there'll be a link to the code to do this down in the description, of course, you can see this is just in a repo that I have up on GitHub here for video code snippets.

**[04:16](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=256s)** There's a few other things from previous videos too, but this one installed TSIDP.shell is the script that we're going to need to create.

**[04:23](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=263s)** Let's take a very quick look at what it's doing before we go ahead and run it.

**[04:27](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=267s)** First things first, you need to run this script as root, fine, we're doing some stuff here with varlib and Etsy. So that makes perfect sense.

**[04:35](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=275s)** So we're going to use this directory here, varlib, TSIDP to persist the state of the IDP service, because essentially what TSIDP does is it adds itself using the TSNET libraries to your townnet as a node on your townnet.

**[04:52](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=292s)** So then TSIDP needs to store those keys in that state somewhere. So we're going to put that in varlib, TSIDP.

**[04:59](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=299s)** And then we're going to set some permissions on that directory, nothing too crazy there.

**[05:03](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=303s)** Then we need to set some environment variables, and you can see those down here.

**[05:08](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=308s)** We need to set the home directory, the TS hostname, so I'm going to call mine TSIDP.

**[05:15](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=315s)** This is the name that that node will get on your townnet.

**[05:18](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=318s)** It can be whatever you like. I just keep it simple with TSIDP.

**[05:22](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=322s)** We then need to generate an auth key. So actually, I should probably show you how to do that.

**[05:26](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=326s)** Let's head over to our tailscale admin console at tailscale.com, get logged in.

**[05:34](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=334s)** Same as usual, just get logged in with your standard identity provider.

**[05:38](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=338s)** Then jump up to the top right where it says settings and then personal settings in the bottom left where it says keys.

**[05:44](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=344s)** Next, I want to generate an auth key. I'm just going to make it reusable. I don't actually think I need to.

**[05:49](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=349s)** I'm going to leave all of the other settings alone.

**[05:52](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=352s)** And then just copy this value to my clipboard and put it back into my little script over here.

**[05:58](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=358s)** I'm going to replace the value of TS underscore auth key with the auth key that we just generated.

**[06:05](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=365s)** And you see there's a couple of other things like state directory. We're going to use varlib TSIDP as we talked about.

**[06:10](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=370s)** User space. This is where the tailscale is going to use the user space version of it or not.

**[06:15](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=375s)** And then because, as I mentioned, this is a working progress and not ready for production type code.

**[06:21](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=381s)** We have to set a tailscale use working progress code environment variable as well.

**[06:27](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=387s)** Now to glue that all together, we're going to use system D to start the service and start the binary automatically when the system boots.

**[06:35](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=395s)** And you can see here, this is just a pretty standard system D unit file.

**[06:39](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=399s)** We're referencing the working directory here of where we're going to put the binary, which is user local bin.

**[06:45](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=405s)** Then exec start is again that binary there and then the environment file where we configure things like our auth key.

**[06:51](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=411s)** And all that other stuff is referenced here. The only other thing is that we wait for the network to be online.

**[06:56](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=416s)** Obviously, it's a network type service. So there's not much point in it being available before the network.

**[07:01](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=421s)** Then the last thing is there's a couple of just helper commands down here for you to make sure you remember to copy your binary to the correct place and then do some system CTL commands.

**[07:10](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=430s)** So with all that in mind, let's go ahead and just copy this onto our remote host.

**[07:14](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=434s)** It doesn't really matter what you call it.

**[07:16](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=436s)** I'm just going to call it install I at TSIDP.sh.

**[07:21](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=441s)** And this is written to run with bash. So I'm going to do bash install TSIDP.sh.

**[07:28](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=448s)** And that's it. All of the required stuff should be ready to go now.

**[07:33](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=453s)** So the only other thing left to do, of course, is copy that TSIDP binary from this directory.

**[07:38](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=458s)** So we're in the slash root at the home directory of the root user.

**[07:41](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=461s)** We want to just copy that binary from here TSIDP to user local bin.

**[07:48](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=468s)** And then we should be good to go. I think it's executable already, but it's always worth a quick check.

**[07:53](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=473s)** Yeah, you can see we've got the X here, which means executable.

**[07:56](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=476s)** So we are good to go next thing to do is to do a system CTL demon reload.

**[08:03](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=483s)** And then I want to actually just start the service.

**[08:06](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=486s)** Now it will take after you start it a minute, maybe less to actually add the node to your town.

**[08:13](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=493s)** But we can we can monitor the status with a system CTL status TSIDP.

**[08:18](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=498s)** And you can see there's a bunch of stuff happening in the back end here.

**[08:22](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=502s)** Now if I go back to my TSIDP admin console, we should see here that in any moment I now have a brand new node called IDP.

**[08:31](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=511s)** Look at that.

**[08:32](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=512s)** So I'm just going to copy the fully qualified domain name here from my TSIDP admin console.

**[08:36](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=516s)** Again, this is presupposing that you have a few things turned on in your tailnet, magic DNS, as well as HTTPS certificates as well.

**[08:44](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=524s)** So if you don't have those two things turned on, just click the enable button and you should be good to go.

**[08:50](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=530s)** Then you can go to the URL itself and it will just show you a very basic web page just to kind of prove it's actually working.

**[08:57](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=537s)** And then what you want to do is go to proxmox.

**[08:59](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=539s)** And we can actually start configuring proxmox to talk to tail scale.

**[09:03](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=543s)** So what we want to do is go to the add button up here where it says, well, let me jump back a second.

**[09:08](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=548s)** Even if you only have one host in your proxmox cluster, you will still have this data center option at the top of the screen.

**[09:16](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=556s)** So click on data center and then you're looking down under here where it says permissions.

**[09:21](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=561s)** You want to go to realms and then add open ID connect server in terms of what you need to put into these different boxes.

**[09:28](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=568s)** First, the first thing we want to put is just the HTTPS URL for the tail scale node that's on your tailnet.

**[09:35](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=575s)** Then realm, we can just put we can give this a name of tail scale.

**[09:40](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=580s)** If you want, you can you can call it whatever you like. It doesn't really matter.

**[09:43](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=583s)** Client ID is unused as is client key actually.

**[09:47](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=587s)** We can set this to be default. So every time we load up proxmox from this point on, it's going to ask us,

**[09:52](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=592s)** do you want to log in using tail scale?

**[09:54](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=594s)** And I'm going to automatically create users as well.

**[09:57](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=597s)** The only other thing we have to change is the username claim must be email.

**[10:01](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=601s)** And with that, we should be good to go.

**[10:04](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=604s)** So I'm going to click add over here and then I'm just going to log out.

**[10:08](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=608s)** It's always a bit scary.

**[10:10](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=610s)** But you'll notice that we now have a new option here.

**[10:13](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=613s)** And if I want to log in, first of all, I have to make sure I'm actually on the tailnet.

**[10:17](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=617s)** You can see here I'm on the correct tailnet.

**[10:20](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=620s)** And then I can just do log in with open ID connect.

**[10:23](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=623s)** And that's it.

**[10:24](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=624s)** I'm logged in using a tail and scales at gmail.com using my tail scale identity.

**[10:29](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=629s)** So just think about that for a second.

**[10:32](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=632s)** If you have a small dev team and you're all using tail scale, you can now manage all the identities.

**[10:37](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=637s)** For your proxmox cluster using tail scale.

**[10:41](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=641s)** Now, like I said, this is not a fully formed solution or fully production ready solution.

**[10:47](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=647s)** But open ID connect is.

**[10:49](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=649s)** And the whole idea behind this video is to show you that you can connect proxmox to an open ID connect server.

**[10:55](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=655s)** And then reuse the identity that your tailnet provides.

**[10:59](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=659s)** So what you might notice is that this particular user doesn't really have any permissions to do anything.

**[11:06](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=666s)** So we're going to have to log out one more time, go to Linux standard authentication using Pam.

**[11:15](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=675s)** And I think I typed in the wrong password.

**[11:17](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=677s)** But what we want to do is just create a couple of groups and allow a couple of permissions so that we can actually do something useful with our new log in our new authentication method.

**[11:27](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=687s)** So first things first, we want to create a group here.

**[11:30](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=690s)** I'm just going to call this TS admins.

**[11:33](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=693s)** We can call it whatever you like.

**[11:35](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=695s)** And then in whatever reason, whatever reason, it took me ages to find this.

**[11:42](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=702s)** If you actually click on the top here, you know, I see one of these little arrows.

**[11:46](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=706s)** I assume that this isn't an option.

**[11:48](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=708s)** Turns out it is.

**[11:50](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=710s)** So what we can do is add a group permission here.

**[11:53](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=713s)** And I can give this particular group access to every single API endpoint.

**[11:58](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=718s)** So I'm just going to do slash here.

**[12:00](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=720s)** And then TS admins roll no access.

**[12:03](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=723s)** I'm going to give them administrator access and then click on add.

**[12:07](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=727s)** I'm then going to go down to users and then modify this tail and scales of Gmail user.

**[12:15](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=735s)** And just add them into the TS admins group right here.

**[12:18](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=738s)** And now when I log out as root, I can then change again my realm to be tail scale and log in with open ID connect.

**[12:26](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=746s)** And you'll see that I've got access now to all of my virtual machines and all the resources within

**[12:31](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=751s)** side the cluster should also make sure to say that the proxmox node itself must also be a node on the tail net

**[12:38](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=758s)** so that it can resolve the TS dot net DNS entry of where the IDP server is running.

**[12:45](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=765s)** If you don't do that, you'll get the following error where it says open ID redirect failed request 500 failed.

**[12:52](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=772s)** So you can see the node right now isn't currently running as a tail scale node.

**[12:56](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=776s)** But if I do tail scale up, I'm already logged in again, I'll do status.

**[13:00](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=780s)** So you can see that I've got this small town it here with a few nodes in it.

**[13:04](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=784s)** And now if I try and log in, everything works just fine.

**[13:08](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=788s)** So you just got to make sure that the node where the open ID connect stuff is configured.

**[13:13](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=793s)** In my case, it seems to be the first node in the proxmox cluster.

**[13:16](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=796s)** Make sure that's a node on your town net and you should be fine.

**[13:19](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=799s)** So that is a really quick and I'm aware that was really fast.

**[13:22](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=802s)** But just a quick, fun little video for you to sort of look at TS IDP is providing identity within your town net.

**[13:29](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=809s)** Obviously, be aware there's from catch 22 situations.

**[13:32](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=812s)** You've got to make sure the node that you're running the identity server on is always up or at least highly up within your cluster.

**[13:40](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=820s)** There's no point having an identity server that's not available otherwise your authentication can't take place.

**[13:46](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=826s)** But that's just scratching the surface really of what you can do using tail scale to reuse identity across nodes on your town net.

**[13:54](https://youtube.com/watch?v=BdQ-Gz6bs3g&t=834s)** Thank you very much for watching and until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
