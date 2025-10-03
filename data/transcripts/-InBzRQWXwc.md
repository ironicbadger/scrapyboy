---
video_id: "-InBzRQWXwc"
title: "Ask a Tailscale Engineer: What is new in Tailscale 1.8"
description: "Episode 2 of 'Ask a Tailscale Engineer' features a walkthrough of new features in Tailscale 1.8, including Split DNS and the ability to send files via Tailscale - Taildrop...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2021-05-11"
duration_seconds: 394
youtube_url: "https://www.youtube.com/watch?v=-InBzRQWXwc"
thumbnail_url: "https://i.ytimg.com/vi_webp/-InBzRQWXwc/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:49:02.346580"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 910
transcription_time_seconds: 9.3
---

# Ask a Tailscale Engineer: What is new in Tailscale 1.8

**[00:06](https://youtube.com/watch?v=-InBzRQWXwc&t=6s)** Hello, everyone, and welcome to another episode of Ask a Tailscale Engineer. I'm Laura, and today I'm joined by Dave and Sonya, who are going to be walking through two exciting new features in Tailscale 1.8. Hello. Hello. Hello. So, if you don't mind sharing your screen, I think the first feature is split

**[00:37](https://youtube.com/watch?v=-InBzRQWXwc&t=37s)** DNS. So, split DNS is a feature that a lot of our corporate users have been asking for, and this is the ability to set a DNS server that is only used for specific domain names. So, as Sonya is showing here, we've tweaked our DNS settings page so that you can still enter a name server, but now you can also toggle this button that says, only use this server for

**[01:08](https://youtube.com/watch?v=-InBzRQWXwc&t=68s)** for the following domains. So, in our case, say, tailscale.com. And so, once we save this, all of your computers will know that if you're looking up login.tailscale.com, they should send that request to 1.2.3.4, and for everything else, they should keep doing whatever they were doing before Tailscale showed up.

**[01:33](https://youtube.com/watch?v=-InBzRQWXwc&t=93s)** Awesome. So, split DNS looks like a really great way to manage your names. Thanks for showing that.

**[01:45](https://youtube.com/watch?v=-InBzRQWXwc&t=105s)** Sonya, what is the second key feature that's coming out with 1.8?

**[01:52](https://youtube.com/watch?v=-InBzRQWXwc&t=112s)** Yeah. So, in 1.8, we have a feature that we're really excited about that we're going to bring into alpha mode called taildrop.

**[02:00](https://youtube.com/watch?v=-InBzRQWXwc&t=120s)** It would taildrop. We built out some native UI's where you can send files between all of your tailscale devices.

**[02:10](https://youtube.com/watch?v=-InBzRQWXwc&t=130s)** And so, let me share my screen and show you guys what this looks like with a couple of devices.

**[02:18](https://youtube.com/watch?v=-InBzRQWXwc&t=138s)** Here, you can see on my, this is my Mac, and then I have my phone screen just displayed up so you can see this just my phone.

**[02:28](https://youtube.com/watch?v=-InBzRQWXwc&t=148s)** So, to show you what this looks like, I have tailscale running on my device. If I go over to my camera roll, for instance, and I want to share some photos to my Mac, if I go to the default iOS share menu, you can see that there's now a tailscale option in here.

**[02:49](https://youtube.com/watch?v=-InBzRQWXwc&t=169s)** And you should see this anywhere where you pop up a share menu in the default iOS flow, the same thing with macOS.

**[02:58](https://youtube.com/watch?v=-InBzRQWXwc&t=178s)** If you right click on files, you can, you get a share option and you can gather from there windows is the same thing you right click on a file and you can get a share option.

**[03:08](https://youtube.com/watch?v=-InBzRQWXwc&t=188s)** So, I select tailscale. Here, you can see the list of devices that I can share with.

**[03:12](https://youtube.com/watch?v=-InBzRQWXwc&t=192s)** Right now, we only allow you to use this tail drop UI for sharing files between your own devices.

**[03:20](https://youtube.com/watch?v=-InBzRQWXwc&t=200s)** So, if you're on a network with other users, you're only going to see your devices in here. You won't be able to send files to their devices through tail drop.

**[03:30](https://youtube.com/watch?v=-InBzRQWXwc&t=210s)** But, let me show you what this looks like. If I choose Ado, which is my Mac that we're looking at, you can see that I just shared some files.

**[03:39](https://youtube.com/watch?v=-InBzRQWXwc&t=219s)** And now I look over here at my downloads folder and these files that I just shared have been shared successfully.

**[03:47](https://youtube.com/watch?v=-InBzRQWXwc&t=227s)** So, let's actually do this in the opposite direction as well.

**[03:51](https://youtube.com/watch?v=-InBzRQWXwc&t=231s)** So, from the Mac, again, as you guys saw, I, right, I, right clicked on a file, click, go into the share menu, you see the tailscale option.

**[04:01](https://youtube.com/watch?v=-InBzRQWXwc&t=241s)** And now I can send to my iPhone.

**[04:05](https://youtube.com/watch?v=-InBzRQWXwc&t=245s)** Here you go. You can see that we've received the file.

**[04:09](https://youtube.com/watch?v=-InBzRQWXwc&t=249s)** You can see a little preview of it in the notification. If you tap into that.

**[04:14](https://youtube.com/watch?v=-InBzRQWXwc&t=254s)** And then you can move the file into your folders app on your phone and you can move it wherever you want from there.

**[04:21](https://youtube.com/watch?v=-InBzRQWXwc&t=261s)** That's the landing spot is in a tail scale folder within your files app to actually start using this feature.

**[04:31](https://youtube.com/watch?v=-InBzRQWXwc&t=271s)** We have added a settings panel into the admin panel where you can actually go and toggle on this alpha feature by default.

**[04:41](https://youtube.com/watch?v=-InBzRQWXwc&t=281s)** The work is not going to be opted into the feature, but you can go into here and just toggle on send files and that'll allow you to access these share panels that we just found out.

**[04:52](https://youtube.com/watch?v=-InBzRQWXwc&t=292s)** That is awesome.

**[04:56](https://youtube.com/watch?v=-InBzRQWXwc&t=296s)** Great work.

**[04:59](https://youtube.com/watch?v=-InBzRQWXwc&t=299s)** I'm so excited about this.

**[05:03](https://youtube.com/watch?v=-InBzRQWXwc&t=303s)** And everyone can use this with 1.8.

**[05:08](https://youtube.com/watch?v=-InBzRQWXwc&t=308s)** So everyone will be able to use this in alpha mode and 1.8, but you will only be able to share between devices that are running 1.8 clients.

**[05:18](https://youtube.com/watch?v=-InBzRQWXwc&t=318s)** So if you have an upgrade and all of your clients, you're not going to see ones that are not upgraded in your share list options when you're choosing a device to share with.

**[05:28](https://youtube.com/watch?v=-InBzRQWXwc&t=328s)** And I know you mentioned it again, you mentioned it, but I'm going to reiterate that this only works because it is an alpha, this only works with my own devices.

**[05:39](https://youtube.com/watch?v=-InBzRQWXwc&t=339s)** Right, exactly.

**[05:41](https://youtube.com/watch?v=-InBzRQWXwc&t=341s)** Amazing.

**[05:43](https://youtube.com/watch?v=-InBzRQWXwc&t=343s)** Well, I'm really excited about 1.8 and getting it out the door.

**[05:50](https://youtube.com/watch?v=-InBzRQWXwc&t=350s)** I think people use this and they please tell us how you're using it, right, add us at tail scale, send us an email, let us know how you're using it, what it allows you to do better different than before.

**[06:07](https://youtube.com/watch?v=-InBzRQWXwc&t=367s)** We're really jazzed about getting this everyone.

**[06:12](https://youtube.com/watch?v=-InBzRQWXwc&t=372s)** Sony and Dave, thank you so much for walking through what's new with tail scale 1.8 with me.

**[06:20](https://youtube.com/watch?v=-InBzRQWXwc&t=380s)** Thanks, Laura.

**[06:22](https://youtube.com/watch?v=-InBzRQWXwc&t=382s)** Thanks.

**[06:23](https://youtube.com/watch?v=-InBzRQWXwc&t=383s)** All right, and to everyone enjoy 1.8.

---

*Automatically generated transcript. May contain errors.*
