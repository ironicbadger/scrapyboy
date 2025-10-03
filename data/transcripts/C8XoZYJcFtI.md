---
video_id: "C8XoZYJcFtI"
title: "Use Tailscale on your Apple TV!"
description: "With the release of tvOS 17, Apple TV and Tailscale lets you access media servers, photo albums, and more, even when they aren't located on the same physical network. You can share family photos and v..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-09-20"
duration_seconds: 515
youtube_url: "https://www.youtube.com/watch?v=C8XoZYJcFtI"
thumbnail_url: "https://i.ytimg.com/vi_webp/C8XoZYJcFtI/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:30:37.130545"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1693
transcription_time_seconds: 14.3
---

# Use Tailscale on your Apple TV!

**[00:00](https://youtube.com/watch?v=C8XoZYJcFtI&t=0s)** TVOS 17 was released this week, and I can hardly believe I'm about to say this, but Apple

**[00:05](https://youtube.com/watch?v=C8XoZYJcFtI&t=5s)** have added on-device VPN support for the Apple TV.

**[00:09](https://youtube.com/watch?v=C8XoZYJcFtI&t=9s)** So, I am here today to talk to you about Tailscale and the Apple TV, and just what that means

**[00:16](https://youtube.com/watch?v=C8XoZYJcFtI&t=16s)** for the future of your media experience.

**[00:19](https://youtube.com/watch?v=C8XoZYJcFtI&t=19s)** Now, you might be forgiven for asking yourself, what can you do with Tailscale on an Apple

**[00:24](https://youtube.com/watch?v=C8XoZYJcFtI&t=24s)** TV?

**[00:25](https://youtube.com/watch?v=C8XoZYJcFtI&t=25s)** Well, the coolest feature that I think we've added in this release is the ability to use

**[00:29](https://youtube.com/watch?v=C8XoZYJcFtI&t=29s)** your Apple TV as an exit node for your Tailnet.

**[00:33](https://youtube.com/watch?v=C8XoZYJcFtI&t=33s)** Now, in simple terms, what this means is you can take traffic from your client device,

**[00:38](https://youtube.com/watch?v=C8XoZYJcFtI&t=38s)** so it could be a laptop, it could be a phone, something that you're using in a remote location,

**[00:44](https://youtube.com/watch?v=C8XoZYJcFtI&t=44s)** and send the traffic over your Tailnet and how it come out as if it were coming out of

**[00:48](https://youtube.com/watch?v=C8XoZYJcFtI&t=48s)** this device itself.

**[00:49](https://youtube.com/watch?v=C8XoZYJcFtI&t=49s)** Now, this could be useful if you want to do something like online banking.

**[00:53](https://youtube.com/watch?v=C8XoZYJcFtI&t=53s)** Let's say you're staying in a different country, and your bank flags you as being suspicious

**[00:58](https://youtube.com/watch?v=C8XoZYJcFtI&t=58s)** when you're trying to log in in one country, but if you came out in the country you reside

**[01:02](https://youtube.com/watch?v=C8XoZYJcFtI&t=62s)** in, everything would be fine.

**[01:05](https://youtube.com/watch?v=C8XoZYJcFtI&t=65s)** Those are the sorts of use cases where an exit node makes such a difference to your quality

**[01:09](https://youtube.com/watch?v=C8XoZYJcFtI&t=69s)** of life when it comes to doing stuff online.

**[01:12](https://youtube.com/watch?v=C8XoZYJcFtI&t=72s)** Now, another benefit of the Apple TV specifically is it's an incredibly low powered device.

**[01:17](https://youtube.com/watch?v=C8XoZYJcFtI&t=77s)** I've got a killer what running just back here, and I've been doing some testing with

**[01:22](https://youtube.com/watch?v=C8XoZYJcFtI&t=82s)** the energy consumption of this thing for the last few weeks.

**[01:25](https://youtube.com/watch?v=C8XoZYJcFtI&t=85s)** Now, I've seen spikes as high as 3, 4, 5, 6 watts, something like that, typically when

**[01:30](https://youtube.com/watch?v=C8XoZYJcFtI&t=90s)** it's booting up and doing some really intensive stuff, as intensive as it gets for an Apple TV

**[01:35](https://youtube.com/watch?v=C8XoZYJcFtI&t=95s)** anyway, typically you can think about energy consumption in the region of $1 per watt per

**[01:41](https://youtube.com/watch?v=C8XoZYJcFtI&t=101s)** year, if it's on 24.7.

**[01:44](https://youtube.com/watch?v=C8XoZYJcFtI&t=104s)** So if we're looking at something like a Raspberry Pi that uses anywhere from 5 to 15 watts,

**[01:48](https://youtube.com/watch?v=C8XoZYJcFtI&t=108s)** depending what's going on, plus a power supply and a case, and the fact you've got to manage

**[01:53](https://youtube.com/watch?v=C8XoZYJcFtI&t=113s)** the SD card slash Linux operating system that's on that Raspberry Pi, the $149 Apple TV

**[02:00](https://youtube.com/watch?v=C8XoZYJcFtI&t=120s)** actually starts to look quite attractive.

**[02:02](https://youtube.com/watch?v=C8XoZYJcFtI&t=122s)** Now, there is a caveat we don't yet support subnet routing on the Apple TV, but who knows

**[02:07](https://youtube.com/watch?v=C8XoZYJcFtI&t=127s)** if enough of you ask for it, maybe we will in the future.

**[02:10](https://youtube.com/watch?v=C8XoZYJcFtI&t=130s)** There's a lovely symmetry for this feature with our latest partnership with MOLVAD, so think

**[02:15](https://youtube.com/watch?v=C8XoZYJcFtI&t=135s)** of it a little bit like this.

**[02:17](https://youtube.com/watch?v=C8XoZYJcFtI&t=137s)** If you are far away in a hotel in another country or something and you want to appear like

**[02:22](https://youtube.com/watch?v=C8XoZYJcFtI&t=142s)** you're at home, you can use your Apple TV as an exit node to do just that.

**[02:28](https://youtube.com/watch?v=C8XoZYJcFtI&t=148s)** Now if you're at home and you want to appear like you're far away for various reasons,

**[02:32](https://youtube.com/watch?v=C8XoZYJcFtI&t=152s)** you can do that using our MOLVAD partnership, and that also works on the Apple TV as well.

**[02:37](https://youtube.com/watch?v=C8XoZYJcFtI&t=157s)** So for me at least, the general idea goes something like this.

**[02:40](https://youtube.com/watch?v=C8XoZYJcFtI&t=160s)** I currently live in America, I am a graded about five years ago from the UK.

**[02:45](https://youtube.com/watch?v=C8XoZYJcFtI&t=165s)** Sometimes I want to watch eye player, and to do that, I have sent a Raspberry Pi to my mum.

**[02:50](https://youtube.com/watch?v=C8XoZYJcFtI&t=170s)** Now she has that in her house, and I have to manage that remotely, and Teoscale makes that

**[02:55](https://youtube.com/watch?v=C8XoZYJcFtI&t=175s)** pretty easy, but it's still at an Xbox door, all of its foibles.

**[02:59](https://youtube.com/watch?v=C8XoZYJcFtI&t=179s)** So what I'm thinking I'm going to do now is send her an Apple TV and leave that on,

**[03:04](https://youtube.com/watch?v=C8XoZYJcFtI&t=184s)** because then one of the really nice things about this feature is that no matter whether the

**[03:08](https://youtube.com/watch?v=C8XoZYJcFtI&t=188s)** Apple TV is in standby mode or in playback mode, the Teoscale exit node feature will still continue

**[03:14](https://youtube.com/watch?v=C8XoZYJcFtI&t=194s)** to work just fine.

**[03:16](https://youtube.com/watch?v=C8XoZYJcFtI&t=196s)** And so for folks like me who split their time between two countries,

**[03:19](https://youtube.com/watch?v=C8XoZYJcFtI&t=199s)** a feature like this is absolutely killer, and I can do it all using infrastructure that I control

**[03:25](https://youtube.com/watch?v=C8XoZYJcFtI&t=205s)** and that I own. I don't have to pay a subscription to a third-party VPN service to do that.

**[03:31](https://youtube.com/watch?v=C8XoZYJcFtI&t=211s)** And also, I'm able to take the Apple TV itself with me and connect to my remote devices using

**[03:36](https://youtube.com/watch?v=C8XoZYJcFtI&t=216s)** the Apple TV in a hotel, for example, so I can get back to my house here in North Carolina,

**[03:42](https://youtube.com/watch?v=C8XoZYJcFtI&t=222s)** or connect to my server back in the UK to stream some recordings I might have made off the BBC,

**[03:47](https://youtube.com/watch?v=C8XoZYJcFtI&t=227s)** using something like Plex or Jelly Finn.

**[03:50](https://youtube.com/watch?v=C8XoZYJcFtI&t=230s)** All right, so let's dive in and take a little look at the Apple TV interface.

**[03:54](https://youtube.com/watch?v=C8XoZYJcFtI&t=234s)** I've got this through an HDMI capture device here, so this is just a normal Apple TV running

**[03:58](https://youtube.com/watch?v=C8XoZYJcFtI&t=238s)** TV OS 17. All right, so once you have the app downloaded and installed, and you've connected

**[04:03](https://youtube.com/watch?v=C8XoZYJcFtI&t=243s)** it to your tailnet, go ahead and open the app and click on the connect button.

**[04:06](https://youtube.com/watch?v=C8XoZYJcFtI&t=246s)** And you can see that right away, I am connected into my tailnet.

**[04:09](https://youtube.com/watch?v=C8XoZYJcFtI&t=249s)** Now, in here, there are a bunch of different features, so the run as exit node.

**[04:14](https://youtube.com/watch?v=C8XoZYJcFtI&t=254s)** Now, this is the one that lets you connect in remotely from anywhere on your tailnet

**[04:18](https://youtube.com/watch?v=C8XoZYJcFtI&t=258s)** and use this device as an exit node. So if I go ahead and select that and then click on run as exit

**[04:24](https://youtube.com/watch?v=C8XoZYJcFtI&t=264s)** node, you can see that now I'm able to use the Apple TV as an exit node from any device on my

**[04:29](https://youtube.com/watch?v=C8XoZYJcFtI&t=269s)** tailnet. So once you enable run as exit node on the Apple TV itself, you'll need to hop over to

**[04:35](https://youtube.com/watch?v=C8XoZYJcFtI&t=275s)** your tailscale admin dashboard. Like any other device, you'll need to ensure that the Apple TV

**[04:40](https://youtube.com/watch?v=C8XoZYJcFtI&t=280s)** here is approved to be used as an exit node. Now, you'll see in real time, I'm also going to bring

**[04:46](https://youtube.com/watch?v=C8XoZYJcFtI&t=286s)** up my iPad on the screen too. I've got a list of all the exit nodes on my account just here.

**[04:51](https://youtube.com/watch?v=C8XoZYJcFtI&t=291s)** You'll see that in real time, as soon as I check this box, the ability to use that Apple TV

**[04:57](https://youtube.com/watch?v=C8XoZYJcFtI&t=297s)** as an exit node becomes available instantly on my iPad. And so now, no matter where I am in the

**[05:02](https://youtube.com/watch?v=C8XoZYJcFtI&t=302s)** world and wherever this Apple TV is in the world, as long as it's got an internet connection,

**[05:07](https://youtube.com/watch?v=C8XoZYJcFtI&t=307s)** I can route the traffic from my iPad out through my Apple TV as an exit node.

**[05:12](https://youtube.com/watch?v=C8XoZYJcFtI&t=312s)** Now, not only can we use the Apple TV itself as an exit node for other nodes to connect into,

**[05:18](https://youtube.com/watch?v=C8XoZYJcFtI&t=318s)** but I can also connect from the Apple TV to other exit nodes on my tailnet. So what this gives me

**[05:24](https://youtube.com/watch?v=C8XoZYJcFtI&t=324s)** the ability to do is I need to turn off, first of all, using this as an exit node. You can't

**[05:31](https://youtube.com/watch?v=C8XoZYJcFtI&t=331s)** use this as an exit node and also connect to other exit nodes at the same time. It's a mutually

**[05:37](https://youtube.com/watch?v=C8XoZYJcFtI&t=337s)** exclusive thing. Once I've connected to another exit node on my tailnet, for example,

**[05:43](https://youtube.com/watch?v=C8XoZYJcFtI&t=343s)** it's a couple here in England that I use. Zoidberg is one in my basement in North Carolina.

**[05:48](https://youtube.com/watch?v=C8XoZYJcFtI&t=348s)** I've got one running on a VPS in Linode, that's KTZ Cloud. And then the other two are two open

**[05:54](https://youtube.com/watch?v=C8XoZYJcFtI&t=354s)** sense boxes that I have running in the UK. Now, what I want to do now is replace one of those

**[06:00](https://youtube.com/watch?v=C8XoZYJcFtI&t=360s)** open sense boxes, maybe add to it with an Apple TV in a remote location. That way, if open sense has

**[06:07](https://youtube.com/watch?v=C8XoZYJcFtI&t=367s)** any issues or some other fate before my infrastructure, I can just tell relative, take the Apple TV,

**[06:16](https://youtube.com/watch?v=C8XoZYJcFtI&t=376s)** plug it in with an ethernet cable from your ISP provided modem, cable modem, whatever it is,

**[06:22](https://youtube.com/watch?v=C8XoZYJcFtI&t=382s)** and then plug that into the back of the Apple TV. And we should be good to go. Now, of course,

**[06:26](https://youtube.com/watch?v=C8XoZYJcFtI&t=386s)** because this is just another device on your tailnet, you can use this to connect to all sorts of

**[06:30](https://youtube.com/watch?v=C8XoZYJcFtI&t=390s)** other applications and systems as well. So I have a jellyfin server here, and jellyfin, for those

**[06:35](https://youtube.com/watch?v=C8XoZYJcFtI&t=395s)** of you that aren't familiar, is a media server. And what essentially that means is you can take video

**[06:40](https://youtube.com/watch?v=C8XoZYJcFtI&t=400s)** files on a hard drive, whether that's in this building or somewhere else on the planet,

**[06:46](https://youtube.com/watch?v=C8XoZYJcFtI&t=406s)** and transcode those files in real time for playback on almost any client device you can think of

**[06:52](https://youtube.com/watch?v=C8XoZYJcFtI&t=412s)** from an iPhone to an iPad to an Android TV set top box to a computer in a web browser or a smart

**[07:00](https://youtube.com/watch?v=C8XoZYJcFtI&t=420s)** TV. Think of it like a self-hosted Netflix. So I have a bunch of media that I want to watch wherever

**[07:07](https://youtube.com/watch?v=C8XoZYJcFtI&t=427s)** I am in the world. Now, this particular jellyfin instance, for example, is running in my basement

**[07:11](https://youtube.com/watch?v=C8XoZYJcFtI&t=431s)** in this building. So the magic here is not that impressive. However, if we wanted to access a

**[07:19](https://youtube.com/watch?v=C8XoZYJcFtI&t=439s)** different jellyfin server, for example, this one is running in Norfolk in England several thousand

**[07:26](https://youtube.com/watch?v=C8XoZYJcFtI&t=446s)** miles away, there are no ports open in that remote firewall. So we're using tailscales natural

**[07:31](https://youtube.com/watch?v=C8XoZYJcFtI&t=451s)** virtual features here to connect to a remote jellyfin server on the other side of the planet

**[07:37](https://youtube.com/watch?v=C8XoZYJcFtI&t=457s)** from our Apple TV using the VPN configuration that the new tailscale client permits.

**[07:43](https://youtube.com/watch?v=C8XoZYJcFtI&t=463s)** And you can see here that now I've been able to connect into that remote jellyfin server.

**[07:47](https://youtube.com/watch?v=C8XoZYJcFtI&t=467s)** I can watch all the UK TV recordings that I make using the over-air antenna

**[07:52](https://youtube.com/watch?v=C8XoZYJcFtI&t=472s)** at my mother-in-law's house. This simply wasn't possible before the latest release of TV OS 17.

**[07:57](https://youtube.com/watch?v=C8XoZYJcFtI&t=477s)** I am so thankful we've been able to ship this app so quickly and allow our users to take advantage

**[08:03](https://youtube.com/watch?v=C8XoZYJcFtI&t=483s)** of the fact that TV OS 17 now supports client-side VPN configurations. Use it to teleport yourself

**[08:10](https://youtube.com/watch?v=C8XoZYJcFtI&t=490s)** anywhere in the world, anywhere that you have tailscale infrastructure running. Do it on self-hosted

**[08:15](https://youtube.com/watch?v=C8XoZYJcFtI&t=495s)** infrastructure that you own that you control and let us know down in the comments what else you

**[08:19](https://youtube.com/watch?v=C8XoZYJcFtI&t=499s)** want to see as part of this feature moving forward. We'd love to hear from you. You can find more

**[08:24](https://youtube.com/watch?v=C8XoZYJcFtI&t=504s)** of us at tailscale.com. And until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
