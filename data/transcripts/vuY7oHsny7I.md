---
video_id: "vuY7oHsny7I"
title: "Network Pack-its: Travel Tips For Techies"
description: "A veritable smorgasbord of travel tips to help you stay better connected the next time you take a trip to see friends or family. 

- https://blog.ktz.me/use-1-pikvm-instance-to-control-4-systems/

Per..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-12-12"
duration_seconds: 529
youtube_url: "https://www.youtube.com/watch?v=vuY7oHsny7I"
thumbnail_url: "https://i.ytimg.com/vi/vuY7oHsny7I/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:11:04.498826"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1657
transcription_time_seconds: 14.3
---

# Network Pack-its: Travel Tips For Techies

**[00:00](https://youtube.com/watch?v=vuY7oHsny7I&t=0s)** Hi everyone, I'm Alex from Tailscale. Somehow it's the holiday season, and this means that many of us are traveling to be close to family or loved ones. But that also means we're going to be traveling away from our beloved home networks. Tailscale can be a real help on the road, and traveling to familiar and far away places can be an opportunity to set up connections that can come in handy for the rest of the year. In those cases though, you might want to consider a little bit of preparation. So that's exactly what we're going to do in today's video.

**[00:30](https://youtube.com/watch?v=vuY7oHsny7I&t=30s)** Today we're sharing a few of our suggestions for Tailscale users, headed out from home in the next few weeks. And even though I've got that fancy, festive, you'll log burning away back there, I think you'll find that some of these tips apply year round too.

**[00:43](https://youtube.com/watch?v=vuY7oHsny7I&t=43s)** So the first thing I want to cover with you today is setting up an exit node and Tailscale SSH at home. Before you leave the house, it's a good time to set up a spare computer or a device like a Raspberry Pi or even an Apple TV to work as an exit node.

**[00:59](https://youtube.com/watch?v=vuY7oHsny7I&t=59s)** An exit node at home means that wherever you go, you can route your internet traffic through your regular network and get access to any geo-restricted content or internet banking sites that you're used to.

**[01:11](https://youtube.com/watch?v=vuY7oHsny7I&t=71s)** And basically pretend that you're in your house behind your physical ISP with your residential IP address.

**[01:17](https://youtube.com/watch?v=vuY7oHsny7I&t=77s)** It can also come in handy whilst traveling and connecting through unfamiliar and sometimes less than salubrious Wi-Fi connections in airports and hotels.

**[01:27](https://youtube.com/watch?v=vuY7oHsny7I&t=87s)** I recently put together a video on installing Tailscale on an Apple TV that might be helpful. There'll be a card up here somewhere.

**[01:34](https://youtube.com/watch?v=vuY7oHsny7I&t=94s)** You might also want to turn on Tailscale SSH for any computer you want to access whilst you're away. With Tailscale handling the SSH authentication, you can even log in from a phone or a tablet if that's what you've got.

**[01:47](https://youtube.com/watch?v=vuY7oHsny7I&t=107s)** And you don't have to worry about figuring out key exchange or any port forwarding in advance.

**[01:52](https://youtube.com/watch?v=vuY7oHsny7I&t=112s)** This is because Tailscale does natural reversal and not punching for you. So even though you've got a device behind a firewall with no ports open, Tailscale can initiate connections between those two devices for a direct connection.

**[02:05](https://youtube.com/watch?v=vuY7oHsny7I&t=125s)** Now don't forget to take with you a decent bag of cables. I've got here my little travel tech charging pouch.

**[02:14](https://youtube.com/watch?v=vuY7oHsny7I&t=134s)** So in this thing, I've got all sorts of stuff. I've got an ethernet cable, who knows when you're going to need ethernet especially at a relative's house when the Wi-Fi is broken.

**[02:25](https://youtube.com/watch?v=vuY7oHsny7I&t=145s)** A couple of really solid charges. For example, this little thing here is a 65 watt two port USB-C USB-A parallapse, one of the anchored GAN charges.

**[02:38](https://youtube.com/watch?v=vuY7oHsny7I&t=158s)** Super nice to have a really high power charger. Things like a USB stick, put Ventoy on this and then you can boot any laptop to any OS.

**[02:47](https://youtube.com/watch?v=vuY7oHsny7I&t=167s)** Top tip would be to put netboot.xyz on top of Ventoy and then you can netboot any ISO that netboot XYZ supports. That's a really nice tip.

**[02:58](https://youtube.com/watch?v=vuY7oHsny7I&t=178s)** If you're a Mac person like me, don't forget your dongles. You signed up for the dongle life when you went Apple.

**[03:04](https://youtube.com/watch?v=vuY7oHsny7I&t=184s)** So pay the tax, pay the Piper and get yourself one of these sorts of things. This is an anchor device again, which has an SD card slot from the days before the MacBook had an SD card slot in the days after that.

**[03:16](https://youtube.com/watch?v=vuY7oHsny7I&t=196s)** They're Macbook Pro is a mess for a long time. It's a long story short. Don't forget your dongles.

**[03:25](https://youtube.com/watch?v=vuY7oHsny7I&t=205s)** What else have we got? Things like an external SSD, for example, if you want to take some movies with you for the plane or something like that, some nice things to do in there.

**[03:35](https://youtube.com/watch?v=vuY7oHsny7I&t=215s)** You know, and then beyond that, it's just a whole bunch of cables, you know, bunch of USB-C, bunch of USB-A, micro USB, mini USB.

**[03:44](https://youtube.com/watch?v=vuY7oHsny7I&t=224s)** You never know what old stuff you're going to find in the bottom of a drawer at a relative's house that you think, oh, if only I'd brought this specific cable, I could be importing VHS tapes like nobody's business.

**[03:58](https://youtube.com/watch?v=vuY7oHsny7I&t=238s)** Now, up until a few weeks ago, when I left my own travel router in my hotel room and the hotel told me it was going to cost me double what the device was worth to ship it back to me, I was a big fan of the GL iNet travel routers.

**[04:10](https://youtube.com/watch?v=vuY7oHsny7I&t=250s)** These are low-power devices that run open WRT underneath. You can install tail scale on these devices. So that means you could access this travel router and deploy it at a relative's house, for example, and then connect to it remotely.

**[04:25](https://youtube.com/watch?v=vuY7oHsny7I&t=265s)** As if it's any other node on your tail net and connect to any of the WAN or LAN resources connected to that router.

**[04:32](https://youtube.com/watch?v=vuY7oHsny7I&t=272s)** These things can be found on Amazon for anywhere up from $30 all the way up to $130 depending on the spec you go for.

**[04:39](https://youtube.com/watch?v=vuY7oHsny7I&t=279s)** They are about the size of a deck of cards, although some of the new ones are starting to get a little bit big, just the nature of physics and dissipating that much heat from some of the faster Wi-Fi protocols.

**[04:49](https://youtube.com/watch?v=vuY7oHsny7I&t=289s)** But if you're in need of a small little switch or something at a relative's house or, you know, I did mention the ethernet cables, you know, you never know, you never know.

**[04:59](https://youtube.com/watch?v=vuY7oHsny7I&t=299s)** Now, let's also think about what you can set up at your destination. If you're going to visit family out of town, this could be the perfect opportunity to install an offsite tail scale node.

**[05:10](https://youtube.com/watch?v=vuY7oHsny7I&t=310s)** You could drop a small NAS box, for example, for remote backups to help keep your data safe in the event of some physical disruption at home.

**[05:18](https://youtube.com/watch?v=vuY7oHsny7I&t=318s)** So, for example, you could take a Raspberry Pi and you could connect a USB hard drive to that thing and then precede the data in your house, get on the plane, get on the train, drive to your destination, drop that box in the remote house and you don't have to upload the multiple terabytes worth of data over the internet.

**[05:36](https://youtube.com/watch?v=vuY7oHsny7I&t=336s)** You've already done the hard work, the initial replication before you left the house.

**[05:41](https://youtube.com/watch?v=vuY7oHsny7I&t=341s)** You could also set up another small computer that could serve as a second exit node, for example. Something like an Apple TV is a great choice for this because it's low powered and stays on no matter what.

**[05:53](https://youtube.com/watch?v=vuY7oHsny7I&t=353s)** TailScale continues to work even when the Apple TV is in low power mode as well. So, it's one of those devices that you can just throw in the entertainment center and never think about it again, it's always going to be connected to your tailnet.

**[06:05](https://youtube.com/watch?v=vuY7oHsny7I&t=365s)** You could also log in with TailScale on these devices yourself or if your family wants to set up a tailnet, they could log in and then share those nodes using no sharing over TailScale with you.

**[06:16](https://youtube.com/watch?v=vuY7oHsny7I&t=376s)** And last but not least, let's talk about PiKVM. This is an absolute gem of a project.

**[06:22](https://youtube.com/watch?v=vuY7oHsny7I&t=382s)** Now, good buddy of mine, Techno Tim did a video where he shows you to up how to control four different physical servers using one Raspberry Pi.

**[06:31](https://youtube.com/watch?v=vuY7oHsny7I&t=391s)** This uses a breakout board to connect those devices together with an HDMI matrix splitter. I also wrote a blog post. I'll put a link to that down in the description down below if you'd like to know the parts to buy to do that.

**[06:43](https://youtube.com/watch?v=vuY7oHsny7I&t=403s)** But the nice thing about that PiKVM is that it uses a low cost, well, sort of device like the Raspberry Pi and then does an HDMI capture of any physical server as if you're sat in front of it.

**[06:56](https://youtube.com/watch?v=vuY7oHsny7I&t=416s)** So, this allows you to do remote control even though you're not physically in the building.

**[07:01](https://youtube.com/watch?v=vuY7oHsny7I&t=421s)** And the real magic part is if you use something like TailScale funnel on that device, you can get a full on TLS certificate baked right into the device using TailScale,

**[07:10](https://youtube.com/watch?v=vuY7oHsny7I&t=430s)** and then have that PiKVM appear on your tailnet just like any other TailScale node.

**[07:16](https://youtube.com/watch?v=vuY7oHsny7I&t=436s)** And the reason I talk about PiKVM is that part of the holiday ritual for many of us involves tech support for friends and family.

**[07:23](https://youtube.com/watch?v=vuY7oHsny7I&t=443s)** It can be quite tough to debug these issues remotely. And so they wait until we've got physical access and it eats up precious time together.

**[07:32](https://youtube.com/watch?v=vuY7oHsny7I&t=452s)** Well, PiKVM solves that. It's as if we're physically there and then we can use TailScale on our PiKVM or as an exit node.

**[07:39](https://youtube.com/watch?v=vuY7oHsny7I&t=459s)** But there's also another thing we haven't talked about yet and that is subnet routers.

**[07:44](https://youtube.com/watch?v=vuY7oHsny7I&t=464s)** Maybe you want to plan about setting up a subnet router at the family home so you can connect remotely to whatever devices they have set up on their Wi-Fi,

**[07:52](https://youtube.com/watch?v=vuY7oHsny7I&t=472s)** whether they have TailScale installed or not.

**[07:55](https://youtube.com/watch?v=vuY7oHsny7I&t=475s)** We all know printers are totally 100% reliable, right?

**[07:59](https://youtube.com/watch?v=vuY7oHsny7I&t=479s)** Yes, I thought so. So for example, you could set up a PiKVM to allow full low level access to a machine remotely.

**[08:08](https://youtube.com/watch?v=vuY7oHsny7I&t=488s)** And that includes the BIOS, by the way, and USB inputs using the USB splitter I talked about.

**[08:14](https://youtube.com/watch?v=vuY7oHsny7I&t=494s)** And because it's running on TailScale, you don't have to worry about opening a port, talking family members through, you know, UPNP or port forwarding or any of that kind of stuff.

**[08:24](https://youtube.com/watch?v=vuY7oHsny7I&t=504s)** Perhaps it's not altogether surprising that TailScale, which is a tool for building small trusted human scale networks, has so many applications at a moment when people bring their human networks together, physically.

**[08:36](https://youtube.com/watch?v=vuY7oHsny7I&t=516s)** No matter how far you or your packets are traveling, we hope that you've enjoyed today's video.

**[08:40](https://youtube.com/watch?v=vuY7oHsny7I&t=520s)** And until next time, I've been Alex from TailScale.

---

*Automatically generated transcript. May contain errors.*
