---
video_id: "1wqUoiDIxqU"
title: "Reimagining Tailscale for Android"
description: "We just released the most exciting to the Tailscale Android app in years! The new app represents a total rethinking of almost every aspect of the Android user experience.

In today's video Alex walks ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-05-23"
duration_seconds: 720
youtube_url: "https://www.youtube.com/watch?v=1wqUoiDIxqU"
thumbnail_url: "https://i.ytimg.com/vi_webp/1wqUoiDIxqU/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:53:53.315085"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2481
transcription_time_seconds: 20.2
---

# Reimagining Tailscale for Android

**[00:00](https://youtube.com/watch?v=1wqUoiDIxqU&t=0s)** Welcome in to today's video everyone. I'm Alex from Tailscale. I'm really excited to share today that our Android app has been completely overhauled. I'm going to share with you some stuff about the new Visual Refresh, as well as the underlying code base has been completely refactored as well. On top of that, I'm going to walk you through some of the basics you can do with Tailscale on Android, and at the end, I'm going to show you how to use Tailscale send to send files from your mobile device to any other device on your tailnet. Since we first released an Android client in August 2020, users have registered over 240,000

**[00:30](https://youtube.com/watch?v=1wqUoiDIxqU&t=30s)** devices to their tailnet. However, it was time for a bit of a revamp and we've completely overhauled almost every aspect of the Tailscale Android experience. This complete visual overhaul is matched by a similarly large refactoring to the underlying code base as well. In fact, if you're curious you can actually go to GitHub and there'll be a link in the description down below and view the Android client source code for yourself. Tailscale is largely open source and our commitment to that promise remains as important as ever. Of course, as usual, it's available in the

**[01:00](https://youtube.com/watch?v=1wqUoiDIxqU&t=60s)** Google Play Store and we've just added it to the Amazon App Store as well. So those of you who are running Amazon Fire Devices, Fire Sticks, Fire Tablets, whatever, you can now run Tailscale on those devices as well.

**[01:12](https://youtube.com/watch?v=1wqUoiDIxqU&t=72s)** Now, the updated app experience begins right away. If you've been using the Tailscale App on Android for a while, this will be the first thing you notice when you launch the updated app. The visuals have changed quite significantly.

**[01:25](https://youtube.com/watch?v=1wqUoiDIxqU&t=85s)** This brings it not only more in line with our brand design guidelines, but also Android best practices as well. Information is now displayed with more detail and density and yet with more clarity. For example, the node status indicators in the Android app now provide at a glance insights into node connectivity, tapping on a node also shows detailed information, including things such as magic DNS information and IP addresses for your tailnet nodes.

**[01:53](https://youtube.com/watch?v=1wqUoiDIxqU&t=113s)** The DNS settings view also received some love in this revamp. It now displays information about resolvers and domains as well as routing configurations for your tailnet. So the next time whether you're wondering whether it's DNS and it always is DNS, you can actually check this now in the Android app as well.

**[02:11](https://youtube.com/watch?v=1wqUoiDIxqU&t=131s)** We've also added a couple of features for enterprise users that they've been asking for, namely, tailnet lock configuration is now available in the app itself.

**[02:19](https://youtube.com/watch?v=1wqUoiDIxqU&t=139s)** Tailnet lock is a feature that prevents unauthorized devices from being added to your tailnet without specific approval from an administrator.

**[02:27](https://youtube.com/watch?v=1wqUoiDIxqU&t=147s)** Also added is mobile device management allowing administrators to deploy tailscale on fleets of Android devices and grant them the ability to automatically enforce their organization's policies.

**[02:38](https://youtube.com/watch?v=1wqUoiDIxqU&t=158s)** Tailscales Android app now supports MDM solutions like Google workspaces, Microsoft Intune, Tiny MDM and many more.

**[02:46](https://youtube.com/watch?v=1wqUoiDIxqU&t=166s)** So I'd like to walk you through the process of installing tailscale on an Android phone. I have here a pixel 8 but that's not super important.

**[02:54](https://youtube.com/watch?v=1wqUoiDIxqU&t=174s)** As long as you're on a version of Android 8 or higher, you should be good to go. Now we're going to start just by loading up the Play Store.

**[03:01](https://youtube.com/watch?v=1wqUoiDIxqU&t=181s)** This process honestly is pretty much the same whether you're installing tailscale or any other app on Android.

**[03:08](https://youtube.com/watch?v=1wqUoiDIxqU&t=188s)** So you just search for tailscale and click on install and wait whilst it downloads.

**[03:13](https://youtube.com/watch?v=1wqUoiDIxqU&t=193s)** Once that's downloaded and we want to just double check we've got the latest version of tailscale.

**[03:17](https://youtube.com/watch?v=1wqUoiDIxqU&t=197s)** If you're using Google Play, this should be absolutely a non-issue. Click into the app screen in the Play Store and then tap on the watch new button.

**[03:24](https://youtube.com/watch?v=1wqUoiDIxqU&t=204s)** You can see there's a whole bunch of stuff here one of which I didn't even talk about which was fast user switching.

**[03:29](https://youtube.com/watch?v=1wqUoiDIxqU&t=209s)** That one's really cool. That lets you switch between different users within the app.

**[03:33](https://youtube.com/watch?v=1wqUoiDIxqU&t=213s)** So if you've got multiple tailnets, you can switch between them readily.

**[03:36](https://youtube.com/watch?v=1wqUoiDIxqU&t=216s)** Also a dark mode. I did not mention dark mode. There you go. We are all about dark mode and that should keep techno tim happy.

**[03:43](https://youtube.com/watch?v=1wqUoiDIxqU&t=223s)** Okay, cool. In the app info towards the bottom, you can see we've got version 1.66.3.

**[03:50](https://youtube.com/watch?v=1wqUoiDIxqU&t=230s)** So anything of 1.66 or higher is part of this new redesign.

**[03:55](https://youtube.com/watch?v=1wqUoiDIxqU&t=235s)** Anything I think 164 or lower is the old app. So make sure you update your app.

**[04:01](https://youtube.com/watch?v=1wqUoiDIxqU&t=241s)** Now, once you've installed tailscale, the first thing you're going to be asked to do is this connection request here.

**[04:06](https://youtube.com/watch?v=1wqUoiDIxqU&t=246s)** Tailscale wants to set up a VPN connection that monitors your network traffic.

**[04:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=250s)** Well, yes, that's kind of the point of an app like tailscale. So I'm going to click OK.

**[04:14](https://youtube.com/watch?v=1wqUoiDIxqU&t=254s)** Next, I'm going to walk you through the getting started wizard and log in.

**[04:18](https://youtube.com/watch?v=1wqUoiDIxqU&t=258s)** In this case, the identity provider that I'm going to use is a Google account, which I use in all of these YouTube videos.

**[04:25](https://youtube.com/watch?v=1wqUoiDIxqU&t=265s)** I'm going to add account to device.

**[04:28](https://youtube.com/watch?v=1wqUoiDIxqU&t=268s)** So I'm going to log in with my Google account, a tail and scales at gmail.com.

**[04:32](https://youtube.com/watch?v=1wqUoiDIxqU&t=272s)** Next thing it's going to ask me for is my password.

**[04:38](https://youtube.com/watch?v=1wqUoiDIxqU&t=278s)** Now, depending on whether you have this account added to your phone or not, Android may well ask you if you want to agree to some terms of service changes and what have you.

**[04:47](https://youtube.com/watch?v=1wqUoiDIxqU&t=287s)** If this is your primary account, you probably won't see this screen, but I don't use this account very often other than demos.

**[04:52](https://youtube.com/watch?v=1wqUoiDIxqU&t=292s)** So sometimes we see some extra screens.

**[04:55](https://youtube.com/watch?v=1wqUoiDIxqU&t=295s)** Hopefully you see me struggle with some of these things makes you realize that we all suffer these things equally.

**[05:00](https://youtube.com/watch?v=1wqUoiDIxqU&t=300s)** OK, now I want to select pangolin, which is the tail and scales at gmail account that's right here.

**[05:05](https://youtube.com/watch?v=1wqUoiDIxqU&t=305s)** Remember, we're still authenticating this phone to our tailnet. That's what we're doing right here.

**[05:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=310s)** So the next page that pops up is one here that says you want to connect this device to your tailnet.

**[05:15](https://youtube.com/watch?v=1wqUoiDIxqU&t=315s)** Now, it's going to automatically detect the host names local host due to some of the sandboxing stuff that Android does these days.

**[05:21](https://youtube.com/watch?v=1wqUoiDIxqU&t=321s)** Don't worry too much about that because you can see on the next page, it's smart enough to figure out that your device Google Pixel 8 is now logged into this specific tailnet at a tail and scales at gmail.com.

**[05:33](https://youtube.com/watch?v=1wqUoiDIxqU&t=333s)** Now, if you want to visit the tail scale console, you can do that by clicking on the visit console button.

**[05:38](https://youtube.com/watch?v=1wqUoiDIxqU&t=338s)** You can see in here, I've got a bunch of stuff. You can see I'm doing some stuff on Amazon. I've got my fake nas image, all that kind of stuff that we cover on this YouTube channel all the time.

**[05:47](https://youtube.com/watch?v=1wqUoiDIxqU&t=347s)** Up in the top left hand corner, though, there's a big X and if you click on that, it's going to take you back to the page, the login page, or at least that's what it looks like in the Android app.

**[05:56](https://youtube.com/watch?v=1wqUoiDIxqU&t=356s)** Then it's going to realize actually it does have the authentication token it needs and take you into the main app proper.

**[06:04](https://youtube.com/watch?v=1wqUoiDIxqU&t=364s)** Now, notifications, I'm just going to click allow. This is how some of the backgrounding stuff works on Android.

**[06:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=370s)** Now, we have the phone connected to the tailnet. We can start to do interesting stuff here so we can connect to any of these other devices.

**[06:16](https://youtube.com/watch?v=1wqUoiDIxqU&t=376s)** Wherever this phone happens to be, whether it's on 5G, whether it's on Wi-Fi, so you could be at the office, you could be at the coffee shop.

**[06:23](https://youtube.com/watch?v=1wqUoiDIxqU&t=383s)** You could be watching your three-year-old go and jump around in muddy puddles at the playground. It really doesn't matter where you are.

**[06:28](https://youtube.com/watch?v=1wqUoiDIxqU&t=388s)** As long as you have an internet connection, this device is now effectively on the same local network as all of these other devices using tailscales, natural virtual technology.

**[06:37](https://youtube.com/watch?v=1wqUoiDIxqU&t=397s)** You can also turn on or off connection to your turnet from a quick settings toggle in Android.

**[06:42](https://youtube.com/watch?v=1wqUoiDIxqU&t=402s)** If you are just on the latest version of Android here, you'll see at the top of the screen you've got a bunch of options you can swipe between.

**[06:49](https://youtube.com/watch?v=1wqUoiDIxqU&t=409s)** If you click on the little pencil, edit icon in the bottom right hand side, slide all the way down, scroll all the way down.

**[06:56](https://youtube.com/watch?v=1wqUoiDIxqU&t=416s)** Next to the live transcribe option here, I've got a tailscale option, so if I sort of tap and drag that up and sort of do a bit of finger gymnastics here and drop it into my quicktiles area,

**[07:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=430s)** what I can now do is I can actually jump straight into turning tailscale on and off and if I press and hold it, it takes me straight into the app.

**[07:17](https://youtube.com/watch?v=1wqUoiDIxqU&t=437s)** Now another thing we can do is actually pretend that we're somewhere we're not, so we're going to do that using exit nodes for example.

**[07:24](https://youtube.com/watch?v=1wqUoiDIxqU&t=444s)** Here you can see I've got a couple of options, one of them is an AWS node that I've been testing and the other one is fakeness, so I'm going to just select fakeness here for example.

**[07:33](https://youtube.com/watch?v=1wqUoiDIxqU&t=453s)** And so what this does is this routes all of the traffic from this physical phone in my hand as if it was coming out of the fakeness.

**[07:41](https://youtube.com/watch?v=1wqUoiDIxqU&t=461s)** So when you are far away from your home, for example, you can actually pretend that you are at home.

**[07:47](https://youtube.com/watch?v=1wqUoiDIxqU&t=467s)** There are lots of interesting things you can do with exit nodes.

**[07:50](https://youtube.com/watch?v=1wqUoiDIxqU&t=470s)** For example, I have a Raspberry Pi set at my mom's house in England, I live in America these days, and I can pretend that I'm in England,

**[07:57](https://youtube.com/watch?v=1wqUoiDIxqU&t=477s)** which is really useful for doing things like online banking, which can be really picky about where you are in the world,

**[08:03](https://youtube.com/watch?v=1wqUoiDIxqU&t=483s)** where you're logging in from all that kind of stuff about their threat profiles.

**[08:06](https://youtube.com/watch?v=1wqUoiDIxqU&t=486s)** They have no idea that your traffic is routing through tailscale and coming out in another country because so far as those nodes are concerned,

**[08:14](https://youtube.com/watch?v=1wqUoiDIxqU&t=494s)** the exit node rewrites those packets and makes them appear as if they're coming out through that exit node,

**[08:21](https://youtube.com/watch?v=1wqUoiDIxqU&t=501s)** wherever that happens to be in the world.

**[08:23](https://youtube.com/watch?v=1wqUoiDIxqU&t=503s)** Now I did promise you a look at things like fast user switching.

**[08:26](https://youtube.com/watch?v=1wqUoiDIxqU&t=506s)** Up in the top right hand corner here, where it says P, for example, you can see that my pangolin,

**[08:31](https://youtube.com/watch?v=1wqUoiDIxqU&t=511s)** tail and scales at Gmail account is currently logged in.

**[08:34](https://youtube.com/watch?v=1wqUoiDIxqU&t=514s)** If I wanted to add a second account, I'd go under here, click on add another account,

**[08:38](https://youtube.com/watch?v=1wqUoiDIxqU&t=518s)** and then it would show me a list of all the different tail nets I had access to on this device.

**[08:43](https://youtube.com/watch?v=1wqUoiDIxqU&t=523s)** I also talked earlier about the updated DNS setting screen, for example,

**[08:47](https://youtube.com/watch?v=1wqUoiDIxqU&t=527s)** and you can see here that I've got a bunch of stuff.

**[08:49](https://youtube.com/watch?v=1wqUoiDIxqU&t=529s)** So my search domain here is Velocirapt to hyphenoodlefish.ts.net.

**[08:55](https://youtube.com/watch?v=1wqUoiDIxqU&t=535s)** This is my tailscale specific fully qualified domain names.

**[08:59](https://youtube.com/watch?v=1wqUoiDIxqU&t=539s)** If you go to your admin console on a computer and look under the DNS tab,

**[09:02](https://youtube.com/watch?v=1wqUoiDIxqU&t=542s)** this is the specific name that your tail net gets.

**[09:05](https://youtube.com/watch?v=1wqUoiDIxqU&t=545s)** And we've talked about in previous videos how you can self-host services on your tail net from anywhere.

**[09:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=550s)** So for example, a couple of weeks ago, I showed you how to use image as self-hosted Google photos back up.

**[09:15](https://youtube.com/watch?v=1wqUoiDIxqU&t=555s)** So that's the new DNS settings page.

**[09:17](https://youtube.com/watch?v=1wqUoiDIxqU&t=557s)** If we jump out of this and back into the main home screen of the application,

**[09:21](https://youtube.com/watch?v=1wqUoiDIxqU&t=561s)** we can see that the green dots on the left show that nodes are online

**[09:25](https://youtube.com/watch?v=1wqUoiDIxqU&t=565s)** and the gray dots, for example, next to the word image,

**[09:28](https://youtube.com/watch?v=1wqUoiDIxqU&t=568s)** shows that this specific node, for example, right now, is not online.

**[09:33](https://youtube.com/watch?v=1wqUoiDIxqU&t=573s)** Also, if you go ahead and just tap on a specific node, you get all the information about the node

**[09:37](https://youtube.com/watch?v=1wqUoiDIxqU&t=577s)** you would expect to see things like its IP version 4 and V6 addresses,

**[09:41](https://youtube.com/watch?v=1wqUoiDIxqU&t=581s)** as well as its magic DNS name in tailscale.

**[09:44](https://youtube.com/watch?v=1wqUoiDIxqU&t=584s)** You can also see when the key expires.

**[09:46](https://youtube.com/watch?v=1wqUoiDIxqU&t=586s)** So underneath tailscale, of course, is built on top of wire guard.

**[09:49](https://youtube.com/watch?v=1wqUoiDIxqU&t=589s)** And one of the pieces of magic that makes tailscale work is key rotation and key expiry.

**[09:54](https://youtube.com/watch?v=1wqUoiDIxqU&t=594s)** And I can just go in here and check that, oh, it seems like every device here is five months.

**[09:59](https://youtube.com/watch?v=1wqUoiDIxqU&t=599s)** Cady, there we go. Cady is four months.

**[10:01](https://youtube.com/watch?v=1wqUoiDIxqU&t=601s)** So I think it's six months is the default length of key validity.

**[10:05](https://youtube.com/watch?v=1wqUoiDIxqU&t=605s)** And you'll see that you can just click on the node and just check when that's going to expire

**[10:09](https://youtube.com/watch?v=1wqUoiDIxqU&t=609s)** right in the Android app now.

**[10:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=610s)** And also remember, if your phone is on your tailnet,

**[10:12](https://youtube.com/watch?v=1wqUoiDIxqU&t=612s)** it can now connect to any other device on your tailnet,

**[10:15](https://youtube.com/watch?v=1wqUoiDIxqU&t=615s)** which includes things like Synology NAS.

**[10:17](https://youtube.com/watch?v=1wqUoiDIxqU&t=617s)** If you want to back up the photos from this phone to your Synology, for example,

**[10:20](https://youtube.com/watch?v=1wqUoiDIxqU&t=620s)** or home assistant, if you're into home automation,

**[10:23](https://youtube.com/watch?v=1wqUoiDIxqU&t=623s)** the list goes on and on and on.

**[10:25](https://youtube.com/watch?v=1wqUoiDIxqU&t=625s)** Now every so often, when I'm recording these videos, I come across a feature in tailscale

**[10:29](https://youtube.com/watch?v=1wqUoiDIxqU&t=629s)** that I just think, oh, this is so great.

**[10:33](https://youtube.com/watch?v=1wqUoiDIxqU&t=633s)** So in the Apple world, of course, we have airdrops.

**[10:35](https://youtube.com/watch?v=1wqUoiDIxqU&t=635s)** So when I'm sending screen recordings around from, for example, this phone to my computer for the edit,

**[10:42](https://youtube.com/watch?v=1wqUoiDIxqU&t=642s)** I would do airdrop.

**[10:43](https://youtube.com/watch?v=1wqUoiDIxqU&t=643s)** But with Android, it was trying to make me do all sorts of stuff with either Bluetooth

**[10:47](https://youtube.com/watch?v=1wqUoiDIxqU&t=647s)** or, you know, some other stuff.

**[10:48](https://youtube.com/watch?v=1wqUoiDIxqU&t=648s)** There are self-hosted options like local send that would let me do it.

**[10:52](https://youtube.com/watch?v=1wqUoiDIxqU&t=652s)** But with tailscale, I can actually send files over my tailnet using tailscale send.

**[10:57](https://youtube.com/watch?v=1wqUoiDIxqU&t=657s)** And I'm going to show you how I do that in the photos app just here.

**[11:00](https://youtube.com/watch?v=1wqUoiDIxqU&t=660s)** So if I go into the photos app and click on share, the video is playing, of course,

**[11:06](https://youtube.com/watch?v=1wqUoiDIxqU&t=666s)** you'll see that one of the options in the share sheet here is tailscale.

**[11:10](https://youtube.com/watch?v=1wqUoiDIxqU&t=670s)** So now I'm connected to my tailnet remember, this has access to every other device on my tailnet.

**[11:15](https://youtube.com/watch?v=1wqUoiDIxqU&t=675s)** Now, Baldric happens to be the macOS laptop that sat right in front of me just here.

**[11:20](https://youtube.com/watch?v=1wqUoiDIxqU&t=680s)** So if I click on Baldric just here, I did just send this to Baldric

**[11:24](https://youtube.com/watch?v=1wqUoiDIxqU&t=684s)** so I don't know if it's going to do it again.

**[11:25](https://youtube.com/watch?v=1wqUoiDIxqU&t=685s)** I think it's clever enough to work out, hey, dummy, you just did this.

**[11:28](https://youtube.com/watch?v=1wqUoiDIxqU&t=688s)** You don't need to do it again.

**[11:30](https://youtube.com/watch?v=1wqUoiDIxqU&t=690s)** But here, I just transferred this 300 meg file over tailscale to my laptop

**[11:35](https://youtube.com/watch?v=1wqUoiDIxqU&t=695s)** so that when you're watching this after I've edited it,

**[11:38](https://youtube.com/watch?v=1wqUoiDIxqU&t=698s)** that's how the screen share from this phone got into the video.

**[11:42](https://youtube.com/watch?v=1wqUoiDIxqU&t=702s)** So there is a quick overview of the new Android update version 1.66 for mid-2024.

**[11:48](https://youtube.com/watch?v=1wqUoiDIxqU&t=708s)** Thank you so much for watching and until next time, I've been Alex from Tailscale.

---

*Automatically generated transcript. May contain errors.*
