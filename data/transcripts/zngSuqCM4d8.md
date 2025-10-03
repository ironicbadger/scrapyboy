---
video_id: "zngSuqCM4d8"
title: "So, you want to start self-hosting? Part 1 - How to install Proxmox and pick your hardware."
description: "This video is for you if you're a complete beginner who is curious about getting into self-hosting services.

In this part 1 of a new multi-part series for the channel Alex will cover how to pick out ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-05-21"
duration_seconds: 1213
youtube_url: "https://www.youtube.com/watch?v=zngSuqCM4d8"
thumbnail_url: "https://i.ytimg.com/vi/zngSuqCM4d8/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:14:24.846515"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3899
transcription_time_seconds: 35.1
---

# So, you want to start self-hosting? Part 1 - How to install Proxmox and pick your hardware.

**[00:00](https://youtube.com/watch?v=zngSuqCM4d8&t=0s)** Hello, I'm Alex from Tailscale and in this video series I want to introduce you to the wonderful world of self-hosting. The idea of taking a cloud service, so something like a Google Photos or a Netflix subscription, and bringing that stuff in-house behind your firewall. Of course, I will show you how to use Tailscale to connect all of this stuff together and build your own personal private secure network. Now, you could, in the old days, pick up a Raspberry Pi, really cheap,

**[00:30](https://youtube.com/watch?v=zngSuqCM4d8&t=30s)** this is a Raspberry Pi 4, so it's a few years old now, but the idea with a Raspberry Pi was that, you know, this is a single board computer, this has got a CPU, that's what's under this blue thermal pad right here. You've got a CPU, destroying this thermal pad, and you've got the RAM on here, you've got network ports, you've got USB, you've got everything you need in a little single board compute package. The trouble is, they're kind of slow, and it's kind of hard to connect things to them.

**[01:00](https://youtube.com/watch?v=zngSuqCM4d8&t=60s)** So where would you plug a hard drive into this, right? You can't do it any other way except USB, which is kind of slow, it's kind of not the most reliable thing to do, and especially on the Raspberry Pi 4 at least, you're sharing bandwidth between the USB bus and the Ethernet bus. So, again, performance is just not very good on a Raspberry Pi. Not to mention that a Raspberry Pi 5 these days, starting price for a kit on Amazon is like $130 or something. So let me introduce you to this.

**[01:29](https://youtube.com/watch?v=zngSuqCM4d8&t=89s)** This is a one liter small form factor PC from Dell. I think I picked this up off of DellRefurbish.com for about $150, and this is a fully fledged, what's called X86 PC.

**[01:43](https://youtube.com/watch?v=zngSuqCM4d8&t=103s)** Now, the nice thing about this, first of all, is it's really cheap, but it's also really expandable. So in here, in this blue caddy, I have a 512 gigabyte SATA SSD. You can see there's a couple of ports on here.

**[01:56](https://youtube.com/watch?v=zngSuqCM4d8&t=116s)** One for data, and one for power. Small ones for data, the big ones for power. And this is a 512 gigabyte SSD, but you could very easily pick up a 1, a 2, a 4, even an 8 terabyte variance of one of these for not a huge amount of money.

**[02:11](https://youtube.com/watch?v=zngSuqCM4d8&t=131s)** Inside, we've got the CPU, which is what's underneath this fan here, and because these CPU units were kind of designed to go in office buildings and sort of on the back of monitors and stuff, they're designed to be really easily serviceable without tools.

**[02:24](https://youtube.com/watch?v=zngSuqCM4d8&t=144s)** So you can see the fan here just comes out with just a couple of plastic tabs. You can upgrade the RAM on these things, which is another problem with the Raspberry Pi.

**[02:33](https://youtube.com/watch?v=zngSuqCM4d8&t=153s)** The RAM that these ship with from the factory is all soldered directly onto the Raspberry Pi. So they're not very flexible, but here it's just a couple of laptop dims.

**[02:42](https://youtube.com/watch?v=zngSuqCM4d8&t=162s)** So I've got two 16 gigabyte sticks of memory for 32 total gigabytes of memory in this system. And that's useful if you want to run things like machine learning models to run a self hosted Google photos backup software called image.

**[02:56](https://youtube.com/watch?v=zngSuqCM4d8&t=176s)** And so that's going to be the target for this video series, taking real problems that you have in your digital life and figuring out how to self host them.

**[03:05](https://youtube.com/watch?v=zngSuqCM4d8&t=185s)** So we're going to put image on here, which is a self hosted Google photos clone. Also, we'll probably take a look at jelly fear or plex or maybe even audio bookshelf to solve some of your media needs.

**[03:16](https://youtube.com/watch?v=zngSuqCM4d8&t=196s)** And then I'll also introduce you to one of my absolute favorite open source projects of all time to be honest, home assistant and open source home automation platform that will very comfortably run on a box like this.

**[03:29](https://youtube.com/watch?v=zngSuqCM4d8&t=209s)** So get subscribed. This is part one in this video series where we're going to install proxmox and kind of get you out of the ground and build the foundations for this.

**[03:37](https://youtube.com/watch?v=zngSuqCM4d8&t=217s)** And then part two and the ones that follow will be how to set up a few basic self hosted applications to dip your toe in the beautiful pool of self hosting.

**[03:47](https://youtube.com/watch?v=zngSuqCM4d8&t=227s)** So first things first, we're going to need to install an operating system onto this computer. And to do that, we flash an ISO onto a USB stick and turn it into a bootable medium.

**[03:57](https://youtube.com/watch?v=zngSuqCM4d8&t=237s)** So head over to proxmox.com and click on downloads and then download the ISO file. Whilst that's downloading, we're also going to want to search for something called Belina etcher.

**[04:07](https://youtube.com/watch?v=zngSuqCM4d8&t=247s)** Now, if you're on Windows, I would recommend not using etcher. I'd use something called Rufus instead. This is a way of turning USB sticks into a bootable USB drive.

**[04:18](https://youtube.com/watch?v=zngSuqCM4d8&t=258s)** So if you're on Windows, use Rufus. If you're on macOS, use Belina etcher. If you're on Linux, well, you probably already know how to make a bootable USB because you probably install Linux yourself.

**[04:29](https://youtube.com/watch?v=zngSuqCM4d8&t=269s)** So head on over to your downloads folder, wherever that may be. And you can see I've got Belina etcher already downloaded here. Drag that into your applications folder.

**[04:37](https://youtube.com/watch?v=zngSuqCM4d8&t=277s)** We're going to replace the existing one that's there to make sure that what we downloaded gets installed and so that the Belina editor is the most up-to-date version it can be.

**[04:47](https://youtube.com/watch?v=zngSuqCM4d8&t=287s)** And then I'm going to launch Belina etcher just by double clicking on it. I'm going to click on open, followed by flash from file.

**[04:54](https://youtube.com/watch?v=zngSuqCM4d8&t=294s)** I'm going to select the proxmox ISO that we just downloaded, click on open. And then I'm going to put my USB drive into one of the USB ports on my laptop.

**[05:04](https://youtube.com/watch?v=zngSuqCM4d8&t=304s)** Next, I'm going to select a target disk to flash. So in this case, this is the USB Sandisk 3.2, 123GB drive. This is going to completely override everything that's on that USB disk.

**[05:16](https://youtube.com/watch?v=zngSuqCM4d8&t=316s)** So make sure this is a spare drive and there's nothing important on it. It's going to ask me for my password, which I've just entered.

**[05:23](https://youtube.com/watch?v=zngSuqCM4d8&t=323s)** And then it's going to flash the proxmox ISO onto the USB stick.

**[05:28](https://youtube.com/watch?v=zngSuqCM4d8&t=328s)** Once that's complete, we then want to put it into here. But before we get there, I've got to finish reassembling it.

**[05:34](https://youtube.com/watch?v=zngSuqCM4d8&t=334s)** So I'm going to put my SATA SSD back into the case. This is a hot swap type deal, toolless type deal.

**[05:41](https://youtube.com/watch?v=zngSuqCM4d8&t=341s)** So it can be a little bit fiddly to line it up right, but once it's in, just a case of sliding it in until it clicks.

**[05:48](https://youtube.com/watch?v=zngSuqCM4d8&t=348s)** Then I get my lid and put that back on. And again, just tighten the thumb screw.

**[05:57](https://youtube.com/watch?v=zngSuqCM4d8&t=357s)** Alright, so now the flash is complete. There's a few things we're going to want to do before we power this on.

**[06:02](https://youtube.com/watch?v=zngSuqCM4d8&t=362s)** First of all, we're going to need something in the way of networking.

**[06:06](https://youtube.com/watch?v=zngSuqCM4d8&t=366s)** This is a ubiquity switch and you absolutely don't need to use ubiquity, but I like them because these are what's called managed switches.

**[06:14](https://youtube.com/watch?v=zngSuqCM4d8&t=374s)** So you can buy very cheap, unmanaged gigabit switches off of, well, any online retailer.

**[06:21](https://youtube.com/watch?v=zngSuqCM4d8&t=381s)** Unmanaged means it's kind of dumb. There's no way of rooting packets around cleverly inside.

**[06:28](https://youtube.com/watch?v=zngSuqCM4d8&t=388s)** This is basically a mini computer inside a switch so I can carve up this switch into multiple different what I call VLANs,

**[06:35](https://youtube.com/watch?v=zngSuqCM4d8&t=395s)** as well be on the context of today's video.

**[06:37](https://youtube.com/watch?v=zngSuqCM4d8&t=397s)** Essentially, what we want to do is grab an ethernet cable. This is going to represent our internet into the building.

**[06:42](https://youtube.com/watch?v=zngSuqCM4d8&t=402s)** So I'm going to just put that into the first port here until it clicks.

**[06:47](https://youtube.com/watch?v=zngSuqCM4d8&t=407s)** And then, and then I'm going to grab another ethernet cable.

**[06:50](https://youtube.com/watch?v=zngSuqCM4d8&t=410s)** So this is a mono-price slim cable. Again, you can find these online very readily available.

**[06:56](https://youtube.com/watch?v=zngSuqCM4d8&t=416s)** And I really like these because just look at how malleable they are.

**[06:58](https://youtube.com/watch?v=zngSuqCM4d8&t=418s)** And I'm going to put this into one of these ports here. In fact, I might undo my very pretty notch right here.

**[07:05](https://youtube.com/watch?v=zngSuqCM4d8&t=425s)** I'm going to put this into one of the ports on the ethernet switch.

**[07:08](https://youtube.com/watch?v=zngSuqCM4d8&t=428s)** And then on the back of the Dell box, you can see there is an ethernet port right here.

**[07:11](https://youtube.com/watch?v=zngSuqCM4d8&t=431s)** So that just plugs in like that.

**[07:13](https://youtube.com/watch?v=zngSuqCM4d8&t=433s)** Now, the next thing you probably want to consider is a keyboard.

**[07:16](https://youtube.com/watch?v=zngSuqCM4d8&t=436s)** A mouse may be, although for a headless server, you probably don't need a mouse.

**[07:20](https://youtube.com/watch?v=zngSuqCM4d8&t=440s)** And some kind of a monitor.

**[07:22](https://youtube.com/watch?v=zngSuqCM4d8&t=442s)** And I have a bit of a trick up my sleeve for this today. This is called a jet KVM.

**[07:27](https://youtube.com/watch?v=zngSuqCM4d8&t=447s)** This is a little basically keyboard monitor and mouse in a very tiny sort of little apple watch size device.

**[07:33](https://youtube.com/watch?v=zngSuqCM4d8&t=453s)** This is going to emulate effectively what a full size keyboard and mouse would do.

**[07:38](https://youtube.com/watch?v=zngSuqCM4d8&t=458s)** And do it in such a way as that I can record the screen of this laptop and show you what's going on.

**[07:42](https://youtube.com/watch?v=zngSuqCM4d8&t=462s)** And show you what's going on here. So for demonstration purposes, it makes life a lot easier.

**[07:48](https://youtube.com/watch?v=zngSuqCM4d8&t=468s)** But essentially the way this works is there's a USB cable here, which connects into the back of the Dell box,

**[07:55](https://youtube.com/watch?v=zngSuqCM4d8&t=475s)** just in one of the standard USB 3 ports like so.

**[07:59](https://youtube.com/watch?v=zngSuqCM4d8&t=479s)** Then there is this little splitter here.

**[08:02](https://youtube.com/watch?v=zngSuqCM4d8&t=482s)** And one side of this goes to a wall outlet.

**[08:05](https://youtube.com/watch?v=zngSuqCM4d8&t=485s)** So this connects to a charger of some description.

**[08:08](https://youtube.com/watch?v=zngSuqCM4d8&t=488s)** And then the other half obviously goes into the back of the Dell box right here.

**[08:12](https://youtube.com/watch?v=zngSuqCM4d8&t=492s)** On the back of the jet KVM there's USB C port and this is kind of like a two in one deal.

**[08:18](https://youtube.com/watch?v=zngSuqCM4d8&t=498s)** So this does power and control as well.

**[08:21](https://youtube.com/watch?v=zngSuqCM4d8&t=501s)** So the jet KVM should power up any second now.

**[08:24](https://youtube.com/watch?v=zngSuqCM4d8&t=504s)** We really need to connect this with another ethernet cable into our switch over here.

**[08:29](https://youtube.com/watch?v=zngSuqCM4d8&t=509s)** So in we go over here and in we go into the back of the jet KVM.

**[08:35](https://youtube.com/watch?v=zngSuqCM4d8&t=515s)** Now there's one thing missing. How do we get the video out of this box into the jet KVM?

**[08:40](https://youtube.com/watch?v=zngSuqCM4d8&t=520s)** And we need to use an HDMI cable very straightforward.

**[08:43](https://youtube.com/watch?v=zngSuqCM4d8&t=523s)** The back of the Dell box here as an HDMI out.

**[08:47](https://youtube.com/watch?v=zngSuqCM4d8&t=527s)** And then that just goes into the HDMI in on the jet KVM.

**[08:51](https://youtube.com/watch?v=zngSuqCM4d8&t=531s)** Obviously if you're hooking up a real keyboard or monitor in a mouse, it's going to be very straightforward.

**[08:56](https://youtube.com/watch?v=zngSuqCM4d8&t=536s)** But this little box here as I say emulates all of that functionality for us.

**[09:01](https://youtube.com/watch?v=zngSuqCM4d8&t=541s)** And now it's time to take our bootable USB stick out of our laptop and put it into the back of our little Dell computer right here.

**[09:10](https://youtube.com/watch?v=zngSuqCM4d8&t=550s)** So once we've done that we're now ready to switch this thing on and get it booting.

**[09:14](https://youtube.com/watch?v=zngSuqCM4d8&t=554s)** But before we do that I want to pull up the interface for the jet KVM.

**[09:19](https://youtube.com/watch?v=zngSuqCM4d8&t=559s)** So in my case this is running on 192.168.1.70.

**[09:24](https://youtube.com/watch?v=zngSuqCM4d8&t=564s)** And this prints that out beautifully simply on the little screen for me right here.

**[09:29](https://youtube.com/watch?v=zngSuqCM4d8&t=569s)** And this is it right so this is the jet KVM interface.

**[09:32](https://youtube.com/watch?v=zngSuqCM4d8&t=572s)** This is just replacing the keyboard video mouse that you would have physically on the desk in front of you.

**[09:37](https://youtube.com/watch?v=zngSuqCM4d8&t=577s)** So here's the power cord for the Dell box.

**[09:39](https://youtube.com/watch?v=zngSuqCM4d8&t=579s)** It's just a standard 19 volt kind of barrel jack in a laptop power supply type situation.

**[09:45](https://youtube.com/watch?v=zngSuqCM4d8&t=585s)** With that connected up we should see any second now that the Dell box boots.

**[09:50](https://youtube.com/watch?v=zngSuqCM4d8&t=590s)** In fact there we go.

**[09:51](https://youtube.com/watch?v=zngSuqCM4d8&t=591s)** And it's now going to boot from the USB stick instead.

**[09:55](https://youtube.com/watch?v=zngSuqCM4d8&t=595s)** So it says welcome to grub and don't worry about these error messages.

**[09:58](https://youtube.com/watch?v=zngSuqCM4d8&t=598s)** They just unfortunately happened sometimes.

**[10:00](https://youtube.com/watch?v=zngSuqCM4d8&t=600s)** And we can click on either graphical or terminal or just geographical right now.

**[10:05](https://youtube.com/watch?v=zngSuqCM4d8&t=605s)** Because I think that's probably the easiest thing.

**[10:07](https://youtube.com/watch?v=zngSuqCM4d8&t=607s)** So what we're doing right now is we're installing proxmox.

**[10:09](https://youtube.com/watch?v=zngSuqCM4d8&t=609s)** And this is going to be the sort of base layer, the foundational layer of our sort of mini self hosting home lab platform that we're doing here.

**[10:18](https://youtube.com/watch?v=zngSuqCM4d8&t=618s)** And proxmox is what's called a hypervisor.

**[10:21](https://youtube.com/watch?v=zngSuqCM4d8&t=621s)** Basically in simple terms, this means it can run virtual machines and containers for us.

**[10:26](https://youtube.com/watch?v=zngSuqCM4d8&t=626s)** Those are logical ways of slicing up this one machine into multiple machines.

**[10:30](https://youtube.com/watch?v=zngSuqCM4d8&t=630s)** So we could have one container for image.

**[10:32](https://youtube.com/watch?v=zngSuqCM4d8&t=632s)** We could have another container for plex or jelly thing or something like that and so on and so on.

**[10:38](https://youtube.com/watch?v=zngSuqCM4d8&t=638s)** And the reason I pick proxmox is because I use it in all of my tail scale videos.

**[10:42](https://youtube.com/watch?v=zngSuqCM4d8&t=642s)** In fact, if you look on the home lab subreddit, it's probably one of if not the most popular projects out there.

**[10:50](https://youtube.com/watch?v=zngSuqCM4d8&t=650s)** Now in terms of installing proxmox, it's quite straightforward.

**[10:53](https://youtube.com/watch?v=zngSuqCM4d8&t=653s)** We can just click our way to victory here.

**[10:55](https://youtube.com/watch?v=zngSuqCM4d8&t=655s)** I'm going to select I agree to the license.

**[10:57](https://youtube.com/watch?v=zngSuqCM4d8&t=657s)** I've got two drives I can install proxmox onto.

**[11:00](https://youtube.com/watch?v=zngSuqCM4d8&t=660s)** I'm going to select the NVMe drive because that's going to be the most performant for us.

**[11:04](https://youtube.com/watch?v=zngSuqCM4d8&t=664s)** And then I'll leave the other 500 gigabyte disk just for data, that kind of thing.

**[11:09](https://youtube.com/watch?v=zngSuqCM4d8&t=669s)** So in terms of countries, I can type in, you know, standard way United States.

**[11:13](https://youtube.com/watch?v=zngSuqCM4d8&t=673s)** Here we go.

**[11:14](https://youtube.com/watch?v=zngSuqCM4d8&t=674s)** Time zone.

**[11:15](https://youtube.com/watch?v=zngSuqCM4d8&t=675s)** I'm going to pick America, New York and then keyboard layout leave that as US password.

**[11:21](https://youtube.com/watch?v=zngSuqCM4d8&t=681s)** I'm just going to set the random password.

**[11:23](https://youtube.com/watch?v=zngSuqCM4d8&t=683s)** And then for email, just pick an address that you don't mind any alerts going to from proxmox.

**[11:28](https://youtube.com/watch?v=zngSuqCM4d8&t=688s)** I'm just going to call this one admin at test.com.

**[11:33](https://youtube.com/watch?v=zngSuqCM4d8&t=693s)** Now on this page, this is important.

**[11:35](https://youtube.com/watch?v=zngSuqCM4d8&t=695s)** We pay attention to the various networking things that are going on.

**[11:38](https://youtube.com/watch?v=zngSuqCM4d8&t=698s)** This particular box only has one network interface.

**[11:41](https://youtube.com/watch?v=zngSuqCM4d8&t=701s)** That's this gigabit ethernet port right here.

**[11:44](https://youtube.com/watch?v=zngSuqCM4d8&t=704s)** But some of them have multiple.

**[11:45](https://youtube.com/watch?v=zngSuqCM4d8&t=705s)** So you do need to pay attention potentially to which interface you plugged into.

**[11:50](https://youtube.com/watch?v=zngSuqCM4d8&t=710s)** In terms of a host name or a fully qualified domain name, this is up to you.

**[11:54](https://youtube.com/watch?v=zngSuqCM4d8&t=714s)** You can buy a domain very cheaply.

**[11:56](https://youtube.com/watch?v=zngSuqCM4d8&t=716s)** I just released a video a couple of weeks ago on how to do that with a custom OIDC provider in tail scale.

**[12:02](https://youtube.com/watch?v=zngSuqCM4d8&t=722s)** But for now, I'm just going to call this one proxmox.Alexishouse.com.

**[12:07](https://youtube.com/watch?v=zngSuqCM4d8&t=727s)** I don't own Alex's house.com, but maybe that'll come back to bite me later.

**[12:11](https://youtube.com/watch?v=zngSuqCM4d8&t=731s)** But for now, that will do just fine.

**[12:13](https://youtube.com/watch?v=zngSuqCM4d8&t=733s)** Now we're also going to want to set a static IP address for this system.

**[12:17](https://youtube.com/watch?v=zngSuqCM4d8&t=737s)** And I typically do for the primary server on my network, 1.10.

**[12:21](https://youtube.com/watch?v=zngSuqCM4d8&t=741s)** Personal preference entirely, but that's what I like to do.

**[12:25](https://youtube.com/watch?v=zngSuqCM4d8&t=745s)** The default gateway on this particular network is 192.168.1.254.

**[12:31](https://youtube.com/watch?v=zngSuqCM4d8&t=751s)** And that also happens to be the DNS server as well, at least for now.

**[12:36](https://youtube.com/watch?v=zngSuqCM4d8&t=756s)** One of the other things you can start doing with self hosting is hosting ad blocking DNS servers.

**[12:40](https://youtube.com/watch?v=zngSuqCM4d8&t=760s)** So you'd have to worry about, you know, you probably had a pie hole.

**[12:43](https://youtube.com/watch?v=zngSuqCM4d8&t=763s)** You can self host that on here as well.

**[12:46](https://youtube.com/watch?v=zngSuqCM4d8&t=766s)** And the beauty of modern hardware is that it's so insanely overpowered for a lot of the stuff that we want to do at home.

**[12:52](https://youtube.com/watch?v=zngSuqCM4d8&t=772s)** So whilst the install is running, let's cover a few basic network fundamentals,

**[12:56](https://youtube.com/watch?v=zngSuqCM4d8&t=776s)** like things like where did I get my gateway IP from?

**[12:58](https://youtube.com/watch?v=zngSuqCM4d8&t=778s)** How I know what my DNS server is, all that kind of stuff.

**[13:01](https://youtube.com/watch?v=zngSuqCM4d8&t=781s)** So in the unified world, at least it's fairly straightforward.

**[13:04](https://youtube.com/watch?v=zngSuqCM4d8&t=784s)** It's all presented to you in a dashboard that you can see right here.

**[13:08](https://youtube.com/watch?v=zngSuqCM4d8&t=788s)** And this is one of the reasons I like unified personally is because, you know, my switch here can talk to the firewall or the router.

**[13:16](https://youtube.com/watch?v=zngSuqCM4d8&t=796s)** You just get all of that information kind of all in one place and it's all in one dashboard.

**[13:20](https://youtube.com/watch?v=zngSuqCM4d8&t=800s)** But if you have a different router or an ISP-provided one, get yourself logged into the admin page of that router.

**[13:27](https://youtube.com/watch?v=zngSuqCM4d8&t=807s)** And look for something along the lines of DHCP range or IP range or subnet mask or something along those lines.

**[13:35](https://youtube.com/watch?v=zngSuqCM4d8&t=815s)** And what you're looking for really is this information right here.

**[13:38](https://youtube.com/watch?v=zngSuqCM4d8&t=818s)** It won't look exactly like this, but this should give you a starting point, at least, as to where to find it.

**[13:43](https://youtube.com/watch?v=zngSuqCM4d8&t=823s)** So in my case, you can see that my gateway IP is 192.168.1.254.

**[13:49](https://youtube.com/watch?v=zngSuqCM4d8&t=829s)** And that refers to the actual firewall in this case itself that's doing all the routing into and out of my network to my internet service provider.

**[13:58](https://youtube.com/watch?v=zngSuqCM4d8&t=838s)** Now this box, also the unified box, also happens to be my DNS server.

**[14:02](https://youtube.com/watch?v=zngSuqCM4d8&t=842s)** And that's a pretty common setup for most networks to be honest.

**[14:05](https://youtube.com/watch?v=zngSuqCM4d8&t=845s)** Most firewalls are set up to be what's called a DHCP server.

**[14:09](https://youtube.com/watch?v=zngSuqCM4d8&t=849s)** And as part of DHCP, which is the process of automatically handing out addresses to devices that connect to your Wi-Fi or your network,

**[14:17](https://youtube.com/watch?v=zngSuqCM4d8&t=857s)** you will get a bunch of information automatically through DHCP.

**[14:21](https://youtube.com/watch?v=zngSuqCM4d8&t=861s)** So you get the gateway, you get the DNS white kind of stuff.

**[14:23](https://youtube.com/watch?v=zngSuqCM4d8&t=863s)** You can see here that the DHCP range is 1.6 all the way through to 1.254.

**[14:29](https://youtube.com/watch?v=zngSuqCM4d8&t=869s)** So when a client requests to connect to your network, it will say, hello, I exist. Can I have an IP address please?

**[14:35](https://youtube.com/watch?v=zngSuqCM4d8&t=875s)** The DHCP server will then give it an address with all that information in.

**[14:39](https://youtube.com/watch?v=zngSuqCM4d8&t=879s)** Proxmox, though, needs a static IP address.

**[14:42](https://youtube.com/watch?v=zngSuqCM4d8&t=882s)** So it doesn't do, it doesn't announce itself and say, hi, I'm Proxmox, I need an IP.

**[14:46](https://youtube.com/watch?v=zngSuqCM4d8&t=886s)** We need to manually configure that, which is what we did in the previous step a few minutes ago.

**[14:51](https://youtube.com/watch?v=zngSuqCM4d8&t=891s)** And typically speaking, the gateway IP is either 1.2.1.1 or 1.254, depending on how your network is configured.

**[15:00](https://youtube.com/watch?v=zngSuqCM4d8&t=900s)** There's a bunch of other stuff you can typically configure in DNS and all the rest of it.

**[15:05](https://youtube.com/watch?v=zngSuqCM4d8&t=905s)** You can see here that the DNS server will be assigned to client devices automatically by DHCP.

**[15:10](https://youtube.com/watch?v=zngSuqCM4d8&t=910s)** So in this scenario, at least, the DNS server and the gateway are one and the same.

**[15:16](https://youtube.com/watch?v=zngSuqCM4d8&t=916s)** So as we can see, Proxmox has now installed and rebooted this computer so we can remove our USB stick.

**[15:23](https://youtube.com/watch?v=zngSuqCM4d8&t=923s)** Now, the first thing I like to do is get logged in via SSH because this tiny little writing is not good for anybody's eyes these days.

**[15:31](https://youtube.com/watch?v=zngSuqCM4d8&t=931s)** So what we need to do is do SSH root at and then the IP address of the box that we just installed.

**[15:37](https://youtube.com/watch?v=zngSuqCM4d8&t=937s)** So in my case, that's 1.2, 1.6.8, 1.10.

**[15:41](https://youtube.com/watch?v=zngSuqCM4d8&t=941s)** We also set a root password as part of the installation process, so go ahead and enter that now.

**[15:46](https://youtube.com/watch?v=zngSuqCM4d8&t=946s)** Now, over at Helperscripts.com, I'll be linked to this in the description down below.

**[15:51](https://youtube.com/watch?v=zngSuqCM4d8&t=951s)** There are a bunch of basically fresh out of the box Proxmox things I like to do before I do anything else.

**[15:57](https://youtube.com/watch?v=zngSuqCM4d8&t=957s)** So I'm going to search up here for Proxmox Post-Install and here we go.

**[16:02](https://youtube.com/watch?v=zngSuqCM4d8&t=962s)** Proxmox VE Virtualization Environment Post-Install.

**[16:06](https://youtube.com/watch?v=zngSuqCM4d8&t=966s)** I'm going to copy this onto my clipboard and go back to my terminal and paste this script into my terminal.

**[16:13](https://youtube.com/watch?v=zngSuqCM4d8&t=973s)** This is going to do a few things for us. Let's talk you through it.

**[16:16](https://youtube.com/watch?v=zngSuqCM4d8&t=976s)** It's going to correct the Proxmox Virtualization Environment Sources.

**[16:21](https://youtube.com/watch?v=zngSuqCM4d8&t=981s)** Proxmox by default will nag you that you need a subscription.

**[16:24](https://youtube.com/watch?v=zngSuqCM4d8&t=984s)** And it's a fantastic project and if you get a lot of utility out of it, you should go and support the project by buying a license or getting some support from them.

**[16:32](https://youtube.com/watch?v=zngSuqCM4d8&t=992s)** But they have a bunch of enterprise repos which by default are configured and require a subscription.

**[16:38](https://youtube.com/watch?v=zngSuqCM4d8&t=998s)** Now, we don't have a subscription, so we need to kind of correct those.

**[16:41](https://youtube.com/watch?v=zngSuqCM4d8&t=1001s)** So let's remove those. Let's remove the enterprise repository.

**[16:44](https://youtube.com/watch?v=zngSuqCM4d8&t=1004s)** Let's correct the SEF Package Sources and the PVE Test Repository can yes, fine, add it as disabled.

**[16:51](https://youtube.com/watch?v=zngSuqCM4d8&t=1011s)** I'm going to disable a subscription nag and as it says here, you should support your local friendly neighborhood software projects.

**[16:58](https://youtube.com/watch?v=zngSuqCM4d8&t=1018s)** I'm going to disable high availability right now because we've only got one of these boxes and I'm not going to update Proxmox and I'm not going to reboot because I like to do these things manually.

**[17:09](https://youtube.com/watch?v=zngSuqCM4d8&t=1029s)** So what we want to do now is an apt update.

**[17:12](https://youtube.com/watch?v=zngSuqCM4d8&t=1032s)** This is going to fetch down the latest versions of all of the packages from Debian.org but it's not going to install them.

**[17:20](https://youtube.com/watch?v=zngSuqCM4d8&t=1040s)** So essentially how the Linux Package Management System works is you have on your system a local copy of all the latest,

**[17:27](https://youtube.com/watch?v=zngSuqCM4d8&t=1047s)** it's like a long list of all the latest versions of all the packages available that make up a Linux distribution.

**[17:33](https://youtube.com/watch?v=zngSuqCM4d8&t=1053s)** When I do apt update, it downloads a new list or the up-to-date list of what the current version of packages is.

**[17:41](https://youtube.com/watch?v=zngSuqCM4d8&t=1061s)** There's a delta probably between those two things and you can see here that there are 11 packages in that delta.

**[17:47](https://youtube.com/watch?v=zngSuqCM4d8&t=1067s)** So to install them, I want to type PVE upgrade.

**[17:50](https://youtube.com/watch?v=zngSuqCM4d8&t=1070s)** This is going to bring our Proxmox installation completely up to date and you can see there's a bunch of stuff going on here.

**[17:56](https://youtube.com/watch?v=zngSuqCM4d8&t=1076s)** We're going to install a new kernel.

**[17:58](https://youtube.com/watch?v=zngSuqCM4d8&t=1078s)** We're also going to update Python and Proxmox and PVE itself a little bit because the ISO is a little bit behind what is the most current version.

**[18:07](https://youtube.com/watch?v=zngSuqCM4d8&t=1087s)** Once this is done, we should actually, in fact, we can probably go there now.

**[18:10](https://youtube.com/watch?v=zngSuqCM4d8&t=1090s)** We can go to HTTPS 192.168.1.10 and then we're going to go to what's called a port number.

**[18:19](https://youtube.com/watch?v=zngSuqCM4d8&t=1099s)** So you see the colon in here.

**[18:21](https://youtube.com/watch?v=zngSuqCM4d8&t=1101s)** We're going to go to port 8000 and six.

**[18:23](https://youtube.com/watch?v=zngSuqCM4d8&t=1103s)** This basically means that Proxmox is advertising a website on the IP address of 1.10 on port 8000 and six.

**[18:30](https://youtube.com/watch?v=zngSuqCM4d8&t=1110s)** But because this is a self-signed certificate, we get the scary or connection is not private message.

**[18:36](https://youtube.com/watch?v=zngSuqCM4d8&t=1116s)** It's okay. We can proceed past that.

**[18:38](https://youtube.com/watch?v=zngSuqCM4d8&t=1118s)** And again, log in with our root username and password using the standard Linux Pam authentication.

**[18:45](https://youtube.com/watch?v=zngSuqCM4d8&t=1125s)** And this is it. We now have a fully functional Proxmox box.

**[18:48](https://youtube.com/watch?v=zngSuqCM4d8&t=1128s)** We can create virtual machines. We can create containers and start our self-hosted journey.

**[18:54](https://youtube.com/watch?v=zngSuqCM4d8&t=1134s)** But before we do, I do want to just reboot the box because I remember there was a fresh kernel applied here.

**[19:00](https://youtube.com/watch?v=zngSuqCM4d8&t=1140s)** So let's do an app auto-remove.

**[19:02](https://youtube.com/watch?v=zngSuqCM4d8&t=1142s)** She's going to just clean up anything that's there in this case. There was nothing.

**[19:05](https://youtube.com/watch?v=zngSuqCM4d8&t=1145s)** And we're going to reboot the box.

**[19:07](https://youtube.com/watch?v=zngSuqCM4d8&t=1147s)** Now we can jump back to our JetKVM and watch the reboot process happen in real time.

**[19:12](https://youtube.com/watch?v=zngSuqCM4d8&t=1152s)** Don't forget if you had a monitor, you could just watch that.

**[19:14](https://youtube.com/watch?v=zngSuqCM4d8&t=1154s)** But in my case, JetKVM will do the same thing.

**[19:18](https://youtube.com/watch?v=zngSuqCM4d8&t=1158s)** Okay, and now the box is rebooted.

**[19:20](https://youtube.com/watch?v=zngSuqCM4d8&t=1160s)** It's time to install our very first application.

**[19:23](https://youtube.com/watch?v=zngSuqCM4d8&t=1163s)** But that's going to come in part two.

**[19:25](https://youtube.com/watch?v=zngSuqCM4d8&t=1165s)** Sorry to be such a tease, but it's going to come in part two.

**[19:28](https://youtube.com/watch?v=zngSuqCM4d8&t=1168s)** Part one is all of a software and getting kind of out of the ground, our foundational stuff.

**[19:33](https://youtube.com/watch?v=zngSuqCM4d8&t=1173s)** Part two is where we're going to start installing the image container, home assistant, jellyfin or Plex or whatever we pick.

**[19:39](https://youtube.com/watch?v=zngSuqCM4d8&t=1179s)** And how they configure our phone to talk, you know, take a picture and have our phone send it back to home base.

**[19:45](https://youtube.com/watch?v=zngSuqCM4d8&t=1185s)** Overtail scale, all completely encrypted and all that kind of good stuff.

**[19:49](https://youtube.com/watch?v=zngSuqCM4d8&t=1189s)** So get subscribed. They'll be linking the playlist down below.

**[19:52](https://youtube.com/watch?v=zngSuqCM4d8&t=1192s)** And part two should be out sometime next week.

**[19:55](https://youtube.com/watch?v=zngSuqCM4d8&t=1195s)** Thank you so much for watching. And until next time.

**[19:57](https://youtube.com/watch?v=zngSuqCM4d8&t=1197s)** I've been Alex from TailScale.

---

*Automatically generated transcript. May contain errors.*
