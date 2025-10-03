---
video_id: "vkZwu7I4tcY"
title: "Installing Tailscale on macOS"
description: "Installing Tailscale on macOS is as simple as going to the Mac App Store and clicking \"install\" right? Wrong! In today's video Alex will walk you through the nuances of the various methods for install..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-12-18"
duration_seconds: 920
youtube_url: "https://www.youtube.com/watch?v=vkZwu7I4tcY"
thumbnail_url: "https://i.ytimg.com/vi_webp/vkZwu7I4tcY/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:10:26.350023"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3001
transcription_time_seconds: 25.5
---

# Installing Tailscale on macOS

**[00:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=0s)** Hi, I'm Alex from Tailscale, and in today's video, we're going to discuss installing Tailscale on Mac OS. As always, you can use the chapter markers down below to find a bit of the video that helps you out the most. So, we're going to cover today the nuances between the different versions of Tailscale that are available for Mac OS. It's not quite as straightforward as you might think, and then at the end of the video, we're going to cover how to install them. Now, if you're like me, over the years, you've probably trained yourself to at least go and look in the Mac app store for new software. And indeed, Tailscale provides a package

**[00:30](https://youtube.com/watch?v=vkZwu7I4tcY&t=30s)** over there. So, job done, right? All we do is head to the Mac app store, click install, and we're good to go. Not quite. That version is subject to a few restrictions, and it's not our primary recommendation. That's because to be in the Mac app store, applications are required by Apple to run in a Mac OS sandbox, which is designed to isolate apps from the rest of the system. The trouble is, though, that VPN applications in particular need to be a network extension to implement VPN-like functionality.

**[00:59](https://youtube.com/watch?v=vkZwu7I4tcY&t=59s)** Any app can provide network extensions, but apps distributed outside of the Mac app store must distribute network extensions as part of a system extension.

**[01:09](https://youtube.com/watch?v=vkZwu7I4tcY&t=69s)** Now, the main advantage of the Mac app store is that it's very easy to get started with. Indeed, you just log in and click the button and you're good. However, because both the Tailscale app and its network extension are sandboxed and running as the local user only, there are a few limitations.

**[01:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=86s)** For instance, it's a very common issue that the screen time web filter can conflict with the Tailscale version distributed on the app store.

**[01:34](https://youtube.com/watch?v=vkZwu7I4tcY&t=94s)** The other downside, of course, is that you must have a working Apple ID and enter your password, God forbid, to install the application from the app store.

**[01:43](https://youtube.com/watch?v=vkZwu7I4tcY&t=103s)** We very strongly recommend that instead of this app store version, you download and install our application package directly from Tailscale's package servers.

**[01:52](https://youtube.com/watch?v=vkZwu7I4tcY&t=112s)** And there's a chapter down below for how you can do that a little bit later on in the video.

**[01:56](https://youtube.com/watch?v=vkZwu7I4tcY&t=116s)** In Mac OS 10.15, Apple added support for the system extensions approach to implement VPNs.

**[02:03](https://youtube.com/watch?v=vkZwu7I4tcY&t=123s)** So this means that system extensions can now offer a more secure alternative to the legacy kernel extensions previously used by many security and networking tools on older versions of Mac OS.

**[02:14](https://youtube.com/watch?v=vkZwu7I4tcY&t=134s)** These extensions run with root privileges but remain within a sandbox framework. This ensures that Tailscale can operate isolated from the Mac OS kernel.

**[02:24](https://youtube.com/watch?v=vkZwu7I4tcY&t=144s)** A key advantage of system extensions is their ability to be distributed outside of the Mac App Store framework.

**[02:31](https://youtube.com/watch?v=vkZwu7I4tcY&t=151s)** And this allows us to not only offer a version of Tailscale that doesn't require an Apple ID for installation, but we can also now provide updates that don't undergo or have to be subject to any delays as part of Apple's App Store review process.

**[02:44](https://youtube.com/watch?v=vkZwu7I4tcY&t=164s)** So as a consequence, updates through a standalone version are made available much faster.

**[02:50](https://youtube.com/watch?v=vkZwu7I4tcY&t=170s)** Additionally, this version of Tailscale, the standalone version, can detect third party tools interfering with VPN tunnels and notify you if and when VPN conflicts are detected.

**[03:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=180s)** There's also a third way to run Tailscale and this is the open source Tailscale D variant.

**[03:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=185s)** But honestly, I wouldn't really recommend that for most users as it doesn't include amongst other things, a graphical user interface.

**[03:13](https://youtube.com/watch?v=vkZwu7I4tcY&t=193s)** And all functionality must be configured from the command line. Experience Mac OS administrators might find some utility in this method for unintended installations or if they want to run Tailscale without having to log in as a specific user perhaps.

**[03:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=206s)** But this variant receives less attention from us than our other offerings and isn't really recommended for production use.

**[03:32](https://youtube.com/watch?v=vkZwu7I4tcY&t=212s)** So which versions should you use? We have the Mac App Store version, the standalone version or the open source Tailscale D version.

**[03:39](https://youtube.com/watch?v=vkZwu7I4tcY&t=219s)** I think it's fairly obvious by now that we recommend that you always start by downloading and installing the standalone Mac OS app.

**[03:47](https://youtube.com/watch?v=vkZwu7I4tcY&t=227s)** You should install Tailscale from the Mac App Store only if you are unable to install the standalone version for some reason or if you're deploying Tailscale in an environment where relying on the Mac App Store for installation or updates is essential perhaps you have some kind of a...

**[04:01](https://youtube.com/watch?v=vkZwu7I4tcY&t=241s)** I don't mean to turn into Windows man but some kind of like group policy or some kind of like organizational thing that means you have to install through the Mac App Store.

**[04:10](https://youtube.com/watch?v=vkZwu7I4tcY&t=250s)** However, it's really important that you don't install the Mac App Store variant and the standalone variant on the same machine doing so and having both variants running simultaneously can prevent the Tailscale extension from launching correctly and talking to the wrong back end as it doesn't know which one to pick.

**[04:28](https://youtube.com/watch?v=vkZwu7I4tcY&t=268s)** To safely switch between Mac OS variants you must delete the Tailscale app currently installed, empty the trash, reboot your Mac and then attempt to install the new variant.

**[04:38](https://youtube.com/watch?v=vkZwu7I4tcY&t=278s)** In our documentation we provide a comparison table that presents the major differences in functionality between these variants.

**[04:44](https://youtube.com/watch?v=vkZwu7I4tcY&t=284s)** I'll leave this as an exercise to you dear viewer to find any specific features that mean you must use one version over another.

**[04:52](https://youtube.com/watch?v=vkZwu7I4tcY&t=292s)** But again, our recommendation is that you use the standalone system extension version wherever possible.

**[04:58](https://youtube.com/watch?v=vkZwu7I4tcY&t=298s)** So today's video is being brought to you by a completely box fresh new Mac Mini, one of these new little tiny ones.

**[05:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=305s)** It's been out of the box for maybe a few minutes just long enough to install the latest version of Mac OS Sequoia 15.2.

**[05:11](https://youtube.com/watch?v=vkZwu7I4tcY&t=311s)** So if you have a completely box fresh Mac or a new Mac and you want to install Tailscale you can kind of follow along with me in this video on how to do it.

**[05:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=319s)** Now I did mention that there was a comparison table of which version of Mac OS or which client version to use and I'm a man of my words.

**[05:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=326s)** So over here on the Tailscale documentation you can see here is that comparison table.

**[05:31](https://youtube.com/watch?v=vkZwu7I4tcY&t=331s)** I'll let you draw your own conclusions as to which version is right for you.

**[05:35](https://youtube.com/watch?v=vkZwu7I4tcY&t=335s)** We're going to focus today on the standalone system extension version over here.

**[05:39](https://youtube.com/watch?v=vkZwu7I4tcY&t=339s)** So I'm going to head over to tailscale.com slash download and we just remove slash Mac off the end.

**[05:45](https://youtube.com/watch?v=vkZwu7I4tcY&t=345s)** And Safari is obviously going to detect them on a Mac and take me to the correct using my user agent to detect them on a Mac and show me the correct version.

**[05:53](https://youtube.com/watch?v=vkZwu7I4tcY&t=353s)** So short version is tailscale.com slash download and it will take you to this page here.

**[05:58](https://youtube.com/watch?v=vkZwu7I4tcY&t=358s)** Then you click on the big white download tailscale for Mac OS button just here.

**[06:02](https://youtube.com/watch?v=vkZwu7I4tcY&t=362s)** And all you want to do after that is click on this package so you can go to your finder, the downloads folder and then just double click on install tailscale.

**[06:13](https://youtube.com/watch?v=vkZwu7I4tcY&t=373s)** What's it called? Yes, tailscale dash whatever the package number is.

**[06:17](https://youtube.com/watch?v=vkZwu7I4tcY&t=377s)** This is a tailscale installation package and this is going to install everything you need.

**[06:21](https://youtube.com/watch?v=vkZwu7I4tcY&t=381s)** All the network extension system extensions, all that kind of stuff is going to be taken care of for you.

**[06:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=386s)** You've probably seen this installation wizard a hundred times before so I'm not going to spend too long on it.

**[06:32](https://youtube.com/watch?v=vkZwu7I4tcY&t=392s)** Once it's done, you'll see that you get congratulations.

**[06:35](https://youtube.com/watch?v=vkZwu7I4tcY&t=395s)** Tailscale has been installed successfully and you can now find it in the applications folder.

**[06:41](https://youtube.com/watch?v=vkZwu7I4tcY&t=401s)** So let's head over to the applications folder box fresh Mac.

**[06:45](https://youtube.com/watch?v=vkZwu7I4tcY&t=405s)** I always like the list view rather than the grid view.

**[06:48](https://youtube.com/watch?v=vkZwu7I4tcY&t=408s)** And you can see tailscale is here and ready to go.

**[06:51](https://youtube.com/watch?v=vkZwu7I4tcY&t=411s)** So we're going to double click on tailscale and it's going to walk us through the getting started wizard.

**[06:56](https://youtube.com/watch?v=vkZwu7I4tcY&t=416s)** The next thing we have to do is allow it to install a system extension.

**[06:59](https://youtube.com/watch?v=vkZwu7I4tcY&t=419s)** You remember I talked about the network extensions and permissions to be a VPN.

**[07:04](https://youtube.com/watch?v=vkZwu7I4tcY&t=424s)** Well, this is exactly what's happening here.

**[07:06](https://youtube.com/watch?v=vkZwu7I4tcY&t=426s)** You can see that tailscale would like to use a new network install a new network extension.

**[07:12](https://youtube.com/watch?v=vkZwu7I4tcY&t=432s)** And you can enable this in the login items and extensions section under here.

**[07:17](https://youtube.com/watch?v=vkZwu7I4tcY&t=437s)** So if like me, you didn't click on open system settings.

**[07:20](https://youtube.com/watch?v=vkZwu7I4tcY&t=440s)** Let me show you how to find the relevant section of the macOS settings that you need to set this up.

**[07:25](https://youtube.com/watch?v=vkZwu7I4tcY&t=445s)** Go to your Apple logo up here up in the top left hand corner and click on system settings.

**[07:30](https://youtube.com/watch?v=vkZwu7I4tcY&t=450s)** Then just search for login and look for login items and extensions.

**[07:35](https://youtube.com/watch?v=vkZwu7I4tcY&t=455s)** Scroll down a little bit and you'll see this network extensions option just here.

**[07:39](https://youtube.com/watch?v=vkZwu7I4tcY&t=459s)** And then click on the informational button and just check the box here.

**[07:42](https://youtube.com/watch?v=vkZwu7I4tcY&t=462s)** It's going to ask you for permission to allow this.

**[07:45](https://youtube.com/watch?v=vkZwu7I4tcY&t=465s)** And then again, we want to click on allow VPN configuration once we've done that.

**[07:49](https://youtube.com/watch?v=vkZwu7I4tcY&t=469s)** And at this time, I'm going to click on allow.

**[07:51](https://youtube.com/watch?v=vkZwu7I4tcY&t=471s)** And there we are.

**[07:52](https://youtube.com/watch?v=vkZwu7I4tcY&t=472s)** The back end infrastructure that tailscale needs to operate has now been configured.

**[07:56](https://youtube.com/watch?v=vkZwu7I4tcY&t=476s)** At this point, you would go ahead and sign in to your tailnet just like any other.

**[08:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=480s)** So let's sign in with Google.

**[08:04](https://youtube.com/watch?v=vkZwu7I4tcY&t=484s)** Once you're signed in, then you want to go ahead and just click on the big blue connect button.

**[08:08](https://youtube.com/watch?v=vkZwu7I4tcY&t=488s)** And you will see that this device now gets added to your tailnet and the tailscale extension will detect everything has happened automatically in the background.

**[08:17](https://youtube.com/watch?v=vkZwu7I4tcY&t=497s)** Now, the final thing to do is to enable tailscale to start on login.

**[08:21](https://youtube.com/watch?v=vkZwu7I4tcY&t=501s)** This is optional.

**[08:22](https://youtube.com/watch?v=vkZwu7I4tcY&t=502s)** You don't have to allow it, but if you're using tailscale to connect everything together, it's probably easier if you do.

**[08:28](https://youtube.com/watch?v=vkZwu7I4tcY&t=508s)** So I'm just going to click on yes, start on login and then show tailscale menu.

**[08:33](https://youtube.com/watch?v=vkZwu7I4tcY&t=513s)** And this is now how we interface with tailscale on our Mac through the UI.

**[08:37](https://youtube.com/watch?v=vkZwu7I4tcY&t=517s)** You can see that we can toggle tailscale on or off just by selecting this toggle up here.

**[08:42](https://youtube.com/watch?v=vkZwu7I4tcY&t=522s)** We can also see that we've got a few different options.

**[08:45](https://youtube.com/watch?v=vkZwu7I4tcY&t=525s)** You know, for now, I've only got one account logged in on this Mac.

**[08:48](https://youtube.com/watch?v=vkZwu7I4tcY&t=528s)** But the Mac underneath this one, for example, you can see that I've got several different accounts logged in here.

**[08:54](https://youtube.com/watch?v=vkZwu7I4tcY&t=534s)** So if you're switching between a work tailnet and a personal tailnet or production and a dev tailnet or whatever you're doing,

**[09:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=540s)** you can add multiple tailnets to a single client on a Mac.

**[09:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=545s)** And you would do that by going into account settings and then click on the button here that says add account.

**[09:10](https://youtube.com/watch?v=vkZwu7I4tcY&t=550s)** And then you go through the whole rig or morale of logging into a new account authenticating it to your tailnet and so on.

**[09:16](https://youtube.com/watch?v=vkZwu7I4tcY&t=556s)** You can see that it's trying to do this here.

**[09:18](https://youtube.com/watch?v=vkZwu7I4tcY&t=558s)** And that's not what I want to do.

**[09:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=559s)** So I'm just going to go ahead and just reconnect to tailscale once again as a tail and scales at gmail.com and we're good to go.

**[09:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=566s)** So what else can we do in this client?

**[09:28](https://youtube.com/watch?v=vkZwu7I4tcY&t=568s)** Let's have a look.

**[09:29](https://youtube.com/watch?v=vkZwu7I4tcY&t=569s)** We've got a few things down here.

**[09:31](https://youtube.com/watch?v=vkZwu7I4tcY&t=571s)** One of these is something that's a bit of a secret hidden option unless you're really looking for it.

**[09:36](https://youtube.com/watch?v=vkZwu7I4tcY&t=576s)** You're not going to know it's there.

**[09:37](https://youtube.com/watch?v=vkZwu7I4tcY&t=577s)** You could enter the URL of an alternate tailscale server or a self hosted headscale server,

**[09:43](https://youtube.com/watch?v=vkZwu7I4tcY&t=583s)** which allows you to self host the control server portion of tailscale.

**[09:47](https://youtube.com/watch?v=vkZwu7I4tcY&t=587s)** If you would prefer not to use our free and secure cloud control servers.

**[09:52](https://youtube.com/watch?v=vkZwu7I4tcY&t=592s)** Now for a device that's always on and super low power like the Mac mini.

**[09:57](https://youtube.com/watch?v=vkZwu7I4tcY&t=597s)** Let's face it.

**[09:58](https://youtube.com/watch?v=vkZwu7I4tcY&t=598s)** You're not going to turn this thing off with that stupid power button location.

**[10:01](https://youtube.com/watch?v=vkZwu7I4tcY&t=601s)** Are you something useful might be this exit nodes option right here.

**[10:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=605s)** And this option here lets you turn the Mac mini into an exit node or indeed any Mac for that matter.

**[10:12](https://youtube.com/watch?v=vkZwu7I4tcY&t=612s)** An exit node allows you to route all the traffic from somewhere remote so you can physically be far away

**[10:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=619s)** and appear as if you are sat in this chair and your traffic is routing out through the Mac mini.

**[10:23](https://youtube.com/watch?v=vkZwu7I4tcY&t=623s)** Exit nodes can be useful for things like changing geographic location

**[10:27](https://youtube.com/watch?v=vkZwu7I4tcY&t=627s)** or even just stuff like online banking where they detect certain IPs and all that kind of stuff.

**[10:32](https://youtube.com/watch?v=vkZwu7I4tcY&t=632s)** It's actually very handy in that regard.

**[10:34](https://youtube.com/watch?v=vkZwu7I4tcY&t=634s)** Checking the run as exit node box on the client side is all that you need to do.

**[10:38](https://youtube.com/watch?v=vkZwu7I4tcY&t=638s)** And then on the tailscore admin console side you want to go into the three dot menu for the node in question.

**[10:44](https://youtube.com/watch?v=vkZwu7I4tcY&t=644s)** Click on edit route settings and then make sure that users exit node is permitted.

**[10:49](https://youtube.com/watch?v=vkZwu7I4tcY&t=649s)** Now a little bonus tip for those of you that want to have things happen automatically

**[10:53](https://youtube.com/watch?v=vkZwu7I4tcY&t=653s)** rather than having to manually approve new exit nodes in your ACLs.

**[10:57](https://youtube.com/watch?v=vkZwu7I4tcY&t=657s)** You can just add these three lines here.

**[11:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=660s)** Auto approvers exit node and then either you'll use a name or a specific group.

**[11:04](https://youtube.com/watch?v=vkZwu7I4tcY&t=664s)** There's a video about ACLs up here.

**[11:06](https://youtube.com/watch?v=vkZwu7I4tcY&t=666s)** You can add this to your ACL standard and have exit nodes automatically approve on your tailnet.

**[11:11](https://youtube.com/watch?v=vkZwu7I4tcY&t=671s)** So you don't even have to do anything except check the box on the client side.

**[11:16](https://youtube.com/watch?v=vkZwu7I4tcY&t=676s)** Now I'm going to assume that some people watching this are developers and like to do stuff on the command line.

**[11:21](https://youtube.com/watch?v=vkZwu7I4tcY&t=681s)** So if we open up the command line and try and type tailscale,

**[11:24](https://youtube.com/watch?v=vkZwu7I4tcY&t=684s)** we can see that right now the command isn't installed in our path.

**[11:28](https://youtube.com/watch?v=vkZwu7I4tcY&t=688s)** Luckily this version, the standalone version provides a CLI integration

**[11:33](https://youtube.com/watch?v=vkZwu7I4tcY&t=693s)** which is going to allow you to manage tailscale from the terminal.

**[11:36](https://youtube.com/watch?v=vkZwu7I4tcY&t=696s)** So if I click on the show me how button here,

**[11:38](https://youtube.com/watch?v=vkZwu7I4tcY&t=698s)** you can see we provide a very helpful install now button.

**[11:42](https://youtube.com/watch?v=vkZwu7I4tcY&t=702s)** So I'm going to go ahead and click on that.

**[11:43](https://youtube.com/watch?v=vkZwu7I4tcY&t=703s)** It's going to ask me for my password which I will now enter.

**[11:46](https://youtube.com/watch?v=vkZwu7I4tcY&t=706s)** Dutifully.

**[11:47](https://youtube.com/watch?v=vkZwu7I4tcY&t=707s)** And do I need to restart this terminal session?

**[11:50](https://youtube.com/watch?v=vkZwu7I4tcY&t=710s)** No, I don't even need to do that.

**[11:51](https://youtube.com/watch?v=vkZwu7I4tcY&t=711s)** So we can see that now let me make this a little bigger.

**[11:54](https://youtube.com/watch?v=vkZwu7I4tcY&t=714s)** I can now administer tailscale from my Mac on the command line.

**[12:01](https://youtube.com/watch?v=vkZwu7I4tcY&t=721s)** Look at this, isn't this wonderful?

**[12:03](https://youtube.com/watch?v=vkZwu7I4tcY&t=723s)** Now you'll note that if you don't want to install the command directly in your path,

**[12:07](https://youtube.com/watch?v=vkZwu7I4tcY&t=727s)** you can always execute commands like up and status and that kind of thing.

**[12:11](https://youtube.com/watch?v=vkZwu7I4tcY&t=731s)** By appending them using your tailscales physical app location.

**[12:15](https://youtube.com/watch?v=vkZwu7I4tcY&t=735s)** So in this case that would be slash applications.

**[12:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=739s)** Tailscaled or app blah blah blah, you can see that on the screen.

**[12:22](https://youtube.com/watch?v=vkZwu7I4tcY&t=742s)** And that behaves in much the same way.

**[12:23](https://youtube.com/watch?v=vkZwu7I4tcY&t=743s)** But I don't know about you.

**[12:24](https://youtube.com/watch?v=vkZwu7I4tcY&t=744s)** I think I prefer just typing a single word that I can remember.

**[12:29](https://youtube.com/watch?v=vkZwu7I4tcY&t=749s)** There are quite a few available here.

**[12:31](https://youtube.com/watch?v=vkZwu7I4tcY&t=751s)** For example, tailscale metrics is a new one.

**[12:33](https://youtube.com/watch?v=vkZwu7I4tcY&t=753s)** This provides a Prometheus compatible endpoint for you to scrape metrics from your various clients.

**[12:38](https://youtube.com/watch?v=vkZwu7I4tcY&t=758s)** Keep an eye out for a video on that in the new year.

**[12:41](https://youtube.com/watch?v=vkZwu7I4tcY&t=761s)** But also we can do tailscale ping.

**[12:43](https://youtube.com/watch?v=vkZwu7I4tcY&t=763s)** And this allows me to ping different nodes and see whether they're directly connected on my tailnet.

**[12:48](https://youtube.com/watch?v=vkZwu7I4tcY&t=768s)** Also tailscale netcheck is a fun one too which lets you see all the various different relay nodes

**[12:55](https://youtube.com/watch?v=vkZwu7I4tcY&t=775s)** that we have to help you establish a direct connection between your nodes.

**[12:58](https://youtube.com/watch?v=vkZwu7I4tcY&t=778s)** Now I mentioned the command line on macOS without mentioning home brew.

**[13:02](https://youtube.com/watch?v=vkZwu7I4tcY&t=782s)** This is a package manager for macOS of sorts anyway.

**[13:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=785s)** And it's certainly how I've installed a lot of my software on macOS over the years,

**[13:08](https://youtube.com/watch?v=vkZwu7I4tcY&t=788s)** even though actually these days I use Nick Darwin.

**[13:11](https://youtube.com/watch?v=vkZwu7I4tcY&t=791s)** But that's not important for this video.

**[13:13](https://youtube.com/watch?v=vkZwu7I4tcY&t=793s)** Now if you go over to brew.sh and search for tailscale,

**[13:16](https://youtube.com/watch?v=vkZwu7I4tcY&t=796s)** you'll see that there are a couple of options here.

**[13:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=799s)** Ignore the formula.

**[13:20](https://youtube.com/watch?v=vkZwu7I4tcY&t=800s)** Just pretend it doesn't exist.

**[13:21](https://youtube.com/watch?v=vkZwu7I4tcY&t=801s)** The cast actually just downloads and installs the same package that we make available

**[13:26](https://youtube.com/watch?v=vkZwu7I4tcY&t=806s)** over at packages.tailscale.com.

**[13:29](https://youtube.com/watch?v=vkZwu7I4tcY&t=809s)** Let me show you packages.tailscale.com over here.

**[13:32](https://youtube.com/watch?v=vkZwu7I4tcY&t=812s)** This just downloads the same version that's available from packages.tailscale.com

**[13:37](https://youtube.com/watch?v=vkZwu7I4tcY&t=817s)** and installs the same package.

**[13:39](https://youtube.com/watch?v=vkZwu7I4tcY&t=819s)** So it's basically doing the same thing.

**[13:41](https://youtube.com/watch?v=vkZwu7I4tcY&t=821s)** It ships a gooey application.

**[13:43](https://youtube.com/watch?v=vkZwu7I4tcY&t=823s)** So if you do want to install tailscale programmatically using brew,

**[13:47](https://youtube.com/watch?v=vkZwu7I4tcY&t=827s)** go ahead and use the cast.

**[13:49](https://youtube.com/watch?v=vkZwu7I4tcY&t=829s)** That should give you a pretty good experience as well.

**[13:52](https://youtube.com/watch?v=vkZwu7I4tcY&t=832s)** However our primary recommendation remains and always will remain

**[13:56](https://youtube.com/watch?v=vkZwu7I4tcY&t=836s)** to install it using packages.tailscale.com or the download button on the tailscale website.

**[14:01](https://youtube.com/watch?v=vkZwu7I4tcY&t=841s)** So I think that pretty much covers everything you can do with a tailscale client on macOS.

**[14:05](https://youtube.com/watch?v=vkZwu7I4tcY&t=845s)** The standalone version really doesn't have any compromises whatsoever.

**[14:09](https://youtube.com/watch?v=vkZwu7I4tcY&t=849s)** And as I've said several times throughout this video,

**[14:11](https://youtube.com/watch?v=vkZwu7I4tcY&t=851s)** that is the route that I think everybody should be going with a tailscale client on macOS.

**[14:17](https://youtube.com/watch?v=vkZwu7I4tcY&t=857s)** I think I've shown you everything else that I could possibly think of,

**[14:19](https://youtube.com/watch?v=vkZwu7I4tcY&t=859s)** how to add multiple accounts, custom alternate control servers and headscale servers.

**[14:24](https://youtube.com/watch?v=vkZwu7I4tcY&t=864s)** I think we've covered everything on this page on the settings page pretty much.

**[14:27](https://youtube.com/watch?v=vkZwu7I4tcY&t=867s)** There are a couple of things we haven't touched,

**[14:29](https://youtube.com/watch?v=vkZwu7I4tcY&t=869s)** but I've got to leave something left for you guys to check out by yourself, right?

**[14:33](https://youtube.com/watch?v=vkZwu7I4tcY&t=873s)** And then under the about page,

**[14:34](https://youtube.com/watch?v=vkZwu7I4tcY&t=874s)** there's one option that I haven't shown you.

**[14:36](https://youtube.com/watch?v=vkZwu7I4tcY&t=876s)** And that is automatically installing updates.

**[14:38](https://youtube.com/watch?v=vkZwu7I4tcY&t=878s)** By default, it's not checked.

**[14:40](https://youtube.com/watch?v=vkZwu7I4tcY&t=880s)** I like to check this and get my fresh, tasty tailscale updates whenever I can.

**[14:45](https://youtube.com/watch?v=vkZwu7I4tcY&t=885s)** And if you like to live life on the edge, I'm calling arch users here,

**[14:49](https://youtube.com/watch?v=vkZwu7I4tcY&t=889s)** you can install your unstable versions by checking this box here too.

**[14:53](https://youtube.com/watch?v=vkZwu7I4tcY&t=893s)** So that will pretty much cover us for today.

**[14:55](https://youtube.com/watch?v=vkZwu7I4tcY&t=895s)** If you have any other questions about macOS, ask them down in the comments down below.

**[15:00](https://youtube.com/watch?v=vkZwu7I4tcY&t=900s)** I hope you have a wonderful new year in 2025.

**[15:03](https://youtube.com/watch?v=vkZwu7I4tcY&t=903s)** And until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
