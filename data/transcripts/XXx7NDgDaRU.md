---
video_id: "XXx7NDgDaRU"
title: "A Homelabbers Networking Playground with Opnsense, Proxmox, VLANs and Tailscale"
description: "It's OK to break stuff, that's how we learn. But all too often it's impossible to find a safe space to do so. In today's video we break down an idea for how to create a segmented network for learning ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-10-25"
duration_seconds: 1418
youtube_url: "https://www.youtube.com/watch?v=XXx7NDgDaRU"
thumbnail_url: "https://i.ytimg.com/vi_webp/XXx7NDgDaRU/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:06:49.129102"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 4169
transcription_time_seconds: 45.8
---

# A Homelabbers Networking Playground with Opnsense, Proxmox, VLANs and Tailscale

**[00:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=0s)** So when I think back to when I was first learning networking a few years ago, one of the things I found the most challenging is that, when you want to break something with your network, you break the network, which means the internet doesn't work, it means your YouTube doesn't work, and you can't really learn when your primary sources of information are offline. I've definitely been in the situation where I've broken the internet so badly that I've had to then tether my phone to my laptop to Google how to fix it and then switch back to my old

**[00:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=30s)** network. Well, in today's video I wanted to take you through how you can learn networking in a completely isolated environment that doesn't require any special hardware using Proxmox, OpenSense and Tailscale.

**[00:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=42s)** Alright, let's make a start by installing OpenSense. There are a few steps we're going to need to follow here, specifically around the networking adapters to make sure that OpenSense has one leg in my real network so that you can get to the internet, and one leg in this virtual network that we're going to create for all of our testing.

**[01:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=60s)** So we need to add two network adapters to this virtual machine, so let's jump over to Proxmox, and I'll just show you what I do over here.

**[01:06](https://youtube.com/watch?v=XXx7NDgDaRU&t=66s)** So I'm going to give this a VM ID of 2000, and I'm going to call this OpenSense demo. Actually I'm going to call this OpenSense 101, and you'll see why I'm just a second.

**[01:19](https://youtube.com/watch?v=XXx7NDgDaRU&t=79s)** If I go to the OS here, I'm going to select my ISOs, and they are genuinely Linux ISOs here. So, well, OpenSense is BSD, isn't it? But there you go.

**[01:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=91s)** So I'm going to select the latest version of OpenSense, which is 23.7 at the time of recording. Nothing else here needs to change. I mean, I guess we'll leave those things alone over there.

**[01:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=103s)** Under the system here, again, nothing needs to change. We could add the QEMU agent if we wanted to for a test system, not super important, in my opinion.

**[01:53](https://youtube.com/watch?v=XXx7NDgDaRU&t=113s)** I'm going to tick the discard box on the storage, and make sure that my storage location is all set correctly. For me, this is exactly what I'm looking for.

**[02:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=122s)** I'm just going to drop this down to a 20GB disk. I mean, OpenSense doesn't really need much space at all.

**[02:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=128s)** Next, I'm going to give it 4CPU cores, which is hilarious overkill for a firewall, but why not?

**[02:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=134s)** 2GB of RAM is plenty. Now, in the network section, I'm going to leave this page untouched, and I'll add the other device in just a second.

**[02:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=142s)** So, I'm going to make sure this start off the created box here is not checked.

**[02:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=148s)** Once the Proxmox engine has created the virtual machine instance, I'm going to jump straight over the hardware, and then add a new network device under here.

**[02:38](https://youtube.com/watch?v=XXx7NDgDaRU&t=158s)** So, I'm still going to use the VM bridge zero, which is what the host uses to do all of the networking stuff in there.

**[02:44](https://youtube.com/watch?v=XXx7NDgDaRU&t=164s)** But I'm going to add this second network adapter with the VLAN tag of 101, as we alluded to earlier.

**[02:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=172s)** Now, what this will do is it will create a second network adapter. You can see down here, you've got net zero and net one.

**[02:58](https://youtube.com/watch?v=XXx7NDgDaRU&t=178s)** Net zero has that leg in my existing LAN, so that will get an IP address from my existing DHCP server.

**[03:06](https://youtube.com/watch?v=XXx7NDgDaRU&t=186s)** Net one is effectively the LAN port inside that virtual network that we're creating.

**[03:13](https://youtube.com/watch?v=XXx7NDgDaRU&t=193s)** It's a bit inception, but I promise it will make sense soon.

**[03:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=197s)** All right, so now we've got the networking side of things taken care of.

**[03:21](https://youtube.com/watch?v=XXx7NDgDaRU&t=201s)** I'm going to just jump now into the console here.

**[03:24](https://youtube.com/watch?v=XXx7NDgDaRU&t=204s)** And if you ever installed open sense before, this should look entirely familiar.

**[03:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=208s)** It's booting from the DVD ISO, doing a bunch of stuff here, so we'll just give this a second.

**[03:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=214s)** Now, it's about to prompt us for the manual interface assignment.

**[03:40](https://youtube.com/watch?v=XXx7NDgDaRU&t=220s)** So, I'm going to press any key and interrupt that briefly here.

**[03:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=225s)** So, you see, it says, do you want to configure lags now? No.

**[03:50](https://youtube.com/watch?v=XXx7NDgDaRU&t=230s)** Do you want to configure VLANs now? Also, no.

**[03:53](https://youtube.com/watch?v=XXx7NDgDaRU&t=233s)** You might sound confusing, but we're doing the VLAN configuration on the physical nick.

**[03:59](https://youtube.com/watch?v=XXx7NDgDaRU&t=239s)** Even though it's a virtual nick, we're doing that at the hardware level, the hardware emulation level.

**[04:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=244s)** We're not going to do that in software, which is what open sense is asking that question for just here.

**[04:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=249s)** So, I'm going to say, do you want to configure VLANs now? No.

**[04:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=252s)** And for interface name, I'm going to go back and look at my MAC addresses over here.

**[04:19](https://youtube.com/watch?v=XXx7NDgDaRU&t=259s)** So, I've got A1348F as the first interface.

**[04:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=263s)** And remember, that one doesn't have a VLAN tag.

**[04:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=267s)** So, that's effectively our WAN address.

**[04:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=269s)** So, here, let me leave this down here.

**[04:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=273s)** So, for our WAN address, I want to select A1348F.

**[04:38](https://youtube.com/watch?v=XXx7NDgDaRU&t=278s)** So, that's VTnet0.

**[04:41](https://youtube.com/watch?v=XXx7NDgDaRU&t=281s)** And then, for our LAN address, I want to do the other one, which is VTnet1.

**[04:47](https://youtube.com/watch?v=XXx7NDgDaRU&t=287s)** And that's the one with the VLAN tag of 101.

**[04:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=289s)** So, once I've done that, I'm going to press Enter to say I finished.

**[04:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=292s)** Do you want to proceed? Yes, please.

**[04:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=294s)** And it's going to go ahead and configure a bunch of stuff for us.

**[04:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=297s)** So, once it's done that, we're ready to go ahead and install open sense.

**[05:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=300s)** And we need to log in with the username Installer and the password OpenSense.

**[05:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=305s)** And then, we can go ahead just with the install like we normally would.

**[05:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=308s)** I'm going to fast forward through this in post.

**[05:11](https://youtube.com/watch?v=XXx7NDgDaRU&t=311s)** Okay, and the installation is complete.

**[05:19](https://youtube.com/watch?v=XXx7NDgDaRU&t=319s)** I'm going to go ahead and set a root password.

**[05:21](https://youtube.com/watch?v=XXx7NDgDaRU&t=321s)** Obviously, you set this to whatever you want.

**[05:25](https://youtube.com/watch?v=XXx7NDgDaRU&t=325s)** There we are, complete install.

**[05:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=327s)** All right, we're ready to go.

**[05:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=328s)** We can press exit and reboot at this point.

**[05:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=330s)** And the virtual machine is now going to reboot back in a sec.

**[05:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=334s)** Okay, and there we have it.

**[05:36](https://youtube.com/watch?v=XXx7NDgDaRU&t=336s)** Proxmox is booted the virtual machine for open sense.

**[05:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=339s)** With the two network adapters, and you can see that we've got two

**[05:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=343s)** what look like local IP addresses.

**[05:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=345s)** We've got 1921681.1.

**[05:48](https://youtube.com/watch?v=XXx7NDgDaRU&t=348s)** That's our virtual LAN, our VLAN tags 101 subnet at this point.

**[05:53](https://youtube.com/watch?v=XXx7NDgDaRU&t=353s)** That's the default IP address range that it's picked.

**[05:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=357s)** And then, under the WAN option here, we have 10.42.7.221.

**[06:01](https://youtube.com/watch?v=XXx7NDgDaRU&t=361s)** So, that would effectively be what your ISP would give you as a public IP address.

**[06:06](https://youtube.com/watch?v=XXx7NDgDaRU&t=366s)** If you were to install open sense on some real hardware

**[06:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=369s)** and connect it to an internet facing modem, this 7.221 is just a DHCP address

**[06:16](https://youtube.com/watch?v=XXx7NDgDaRU&t=376s)** from my other open sense, like real instance,

**[06:19](https://youtube.com/watch?v=XXx7NDgDaRU&t=379s)** that's in the basement downstairs running the rest of my network over here.

**[06:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=383s)** We can't access the web UI of open sense through this WAN IP.

**[06:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=388s)** We can try.

**[06:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=389s)** So, if I remember this browser is in my local area network.

**[06:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=394s)** I mean, I could go to 0.254, which is where my existing open sense box lives.

**[06:41](https://youtube.com/watch?v=XXx7NDgDaRU&t=401s)** And that works obviously because I'm in this network.

**[06:44](https://youtube.com/watch?v=XXx7NDgDaRU&t=404s)** But if I wanted to go to what was it, 7.221, it's not going to let me

**[06:51](https://youtube.com/watch?v=XXx7NDgDaRU&t=411s)** because that's effectively like trying to access your firewall

**[06:55](https://youtube.com/watch?v=XXx7NDgDaRU&t=415s)** through the public internet on the WAN IP address.

**[06:58](https://youtube.com/watch?v=XXx7NDgDaRU&t=418s)** It's a really bad idea to do that.

**[07:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=420s)** So, by default, open sense doesn't permit that kind of access.

**[07:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=424s)** So, we have a couple of options at this point.

**[07:07](https://youtube.com/watch?v=XXx7NDgDaRU&t=427s)** And my preferred option to access the web UI of open sense is to create a virtual machine

**[07:13](https://youtube.com/watch?v=XXx7NDgDaRU&t=433s)** that lives inside that VLAN.

**[07:16](https://youtube.com/watch?v=XXx7NDgDaRU&t=436s)** So, we're going to go ahead and create an Ubuntu virtual machine at this point.

**[07:19](https://youtube.com/watch?v=XXx7NDgDaRU&t=439s)** There's nothing terribly special about what I'm about to do here.

**[07:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=442s)** I'm just going to call this Ubuntu 101, and then go ahead again

**[07:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=448s)** and just pick through my ISOs, find the correct one Ubuntu 2204 desktop.

**[07:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=453s)** Go through here, system.

**[07:35](https://youtube.com/watch?v=XXx7NDgDaRU&t=455s)** Yeah, that all looks fine.

**[07:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=457s)** QMU agent, 64 gig of disk, because it's a desktop operating system.

**[07:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=462s)** Well, I might want a little bit more space if I'm creating a development VM.

**[07:46](https://youtube.com/watch?v=XXx7NDgDaRU&t=466s)** I'm going to give it six calls of CPU.

**[07:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=469s)** I'm going to give it 16, is it 384, I think.

**[07:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=474s)** Mega bytes of RAM for 16 gigs or so.

**[07:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=477s)** Now, for starters, I'm not going to give it the VLAN tag.

**[08:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=482s)** Let's see why in just a second.

**[08:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=484s)** When we're installing the Ubuntu operating system,

**[08:07](https://youtube.com/watch?v=XXx7NDgDaRU&t=487s)** it wants to download a bunch of stuff over the internet.

**[08:10](https://youtube.com/watch?v=XXx7NDgDaRU&t=490s)** Sometimes, updates and things like that.

**[08:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=492s)** And I haven't configured open sense yet.

**[08:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=494s)** So, I probably want to go ahead and actually just install the virtual machine on my existing network.

**[08:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=500s)** So, it can pull all the updates all the rest of it.

**[08:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=503s)** In an environment, I'm familiar with and understand and know just fine.

**[08:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=507s)** And then we can go ahead and add that VLAN tag once it's installed

**[08:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=511s)** on the virtual hardware level.

**[08:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=513s)** And at that point, it will get a DHCP address from our virtual open-sense instance.

**[08:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=519s)** Now, installing a Ubuntu here isn't anything special,

**[08:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=522s)** so I'm just going to fast forward through this in the edit.

**[08:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=525s)** Okay, we are at our Ubuntu desktop.

**[08:48](https://youtube.com/watch?v=XXx7NDgDaRU&t=528s)** Hooray!

**[08:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=529s)** Let's go ahead and just inspect what our networking situation is for a second, shall we?

**[08:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=534s)** Under IPA, thanks Ubuntu.

**[08:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=537s)** IPA, we can see that our IP address right now is 10.42.7.236.

**[09:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=544s)** Now, I know that this is using the firewall in my house for real.

**[09:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=548s)** And remember what we wanted to do was create a virtual playground in which we can do a bunch of cool stuff.

**[09:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=554s)** So, let's power off the virtual machine.

**[09:18](https://youtube.com/watch?v=XXx7NDgDaRU&t=558s)** And we're going to add this to our open-sense 101 VLAN.

**[09:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=562s)** Nice and easy.

**[09:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=563s)** Go ahead over to your Proxmox system over here.

**[09:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=566s)** Just click on the hardware, find a virtual network adapter.

**[09:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=569s)** And all we want to do is just add this VLAN tag here of 101.

**[09:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=574s)** When we click OK, we can see that's been added.

**[09:36](https://youtube.com/watch?v=XXx7NDgDaRU&t=576s)** We'll go back to press start up here.

**[09:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=579s)** Okay, and then when we type IPA again, we can see,

**[09:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=583s)** oh, look, we have a different IP address this time of 1.100.

**[09:47](https://youtube.com/watch?v=XXx7NDgDaRU&t=587s)** So what this means is that now this virtual machine lives inside that virtual network we created with open-sense.

**[09:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=594s)** What this also means is we can now go ahead and start administering our virtual firewall

**[09:59](https://youtube.com/watch?v=XXx7NDgDaRU&t=599s)** and start playing around and doing some of the networking stuff that we wanted to figure out in the first place.

**[10:03](https://youtube.com/watch?v=XXx7NDgDaRU&t=603s)** So by default, open-sense is IP address is 192.168.1.1.

**[10:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=609s)** So let's go ahead and accept the default certificate here and then log in with our root username and password.

**[10:15](https://youtube.com/watch?v=XXx7NDgDaRU&t=615s)** First thing open-sense is going to do is prompt us through this initial wizard to do general setup.

**[10:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=620s)** So I'm just going to do open-sense. And now I'm just going to call this 101.my site.

**[10:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=626s)** So WD is what I call my house.my domain name so it gets a real domain.

**[10:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=631s)** I'm going to click next, next, next through most of this stuff just to make the tutorial a little bit easier.

**[10:38](https://youtube.com/watch?v=XXx7NDgDaRU&t=638s)** Now, I like to match the third octet of this IP address to the VLAN tag that I've given it.

**[10:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=645s)** It just helps my brain remember what I'm doing in six months time.

**[10:50](https://youtube.com/watch?v=XXx7NDgDaRU&t=650s)** So this firewall will now have the IP address of 192.168.1.254.

**[10:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=657s)** I like to put my firewalls on the last IP address in a subnet range.

**[11:01](https://youtube.com/watch?v=XXx7NDgDaRU&t=661s)** Some people put it on the first. I've been called an animal for doing this.

**[11:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=665s)** I don't know. This is what I do.

**[11:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=668s)** So you can give this whatever IP address you want to.

**[11:11](https://youtube.com/watch?v=XXx7NDgDaRU&t=671s)** But for this demo, we're going to do 101.254.

**[11:15](https://youtube.com/watch?v=XXx7NDgDaRU&t=675s)** Route password currently is fine.

**[11:18](https://youtube.com/watch?v=XXx7NDgDaRU&t=678s)** Now, one thing I want to show you is going to happen as we do this.

**[11:21](https://youtube.com/watch?v=XXx7NDgDaRU&t=681s)** It's going to reload the DHCP range.

**[11:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=683s)** So if we look right now, we've got the IP address here of 192.168.1.100.

**[11:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=689s)** You can see that right here.

**[11:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=691s)** When we click reload, it's going to apply the changes.

**[11:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=694s)** It's also going to change the DHCP range to be 101.

**[11:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=699s)** So let's just see what happens.

**[11:41](https://youtube.com/watch?v=XXx7NDgDaRU&t=701s)** Reload is now in progress.

**[11:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=703s)** And of course, this URL isn't going to work anymore.

**[11:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=705s)** So let's go ahead and do 101.254.

**[11:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=709s)** And well, we don't have the correct IP address on this host, do we?

**[11:53](https://youtube.com/watch?v=XXx7NDgDaRU&t=713s)** Because it's just we've just pulled the rug out from under its feet.

**[11:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=716s)** So if we go over here and check yet, we've still got 1.100.

**[12:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=720s)** So if we just toggle this off and then on again,

**[12:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=724s)** IT crowd in my head, I hope you do too.

**[12:06](https://youtube.com/watch?v=XXx7NDgDaRU&t=726s)** We can see we've got 192.168.101.10.

**[12:11](https://youtube.com/watch?v=XXx7NDgDaRU&t=731s)** So that means we've picked up the new IP address range,

**[12:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=734s)** which also means if we go over here, we might need to give Firefox a minute

**[12:18](https://youtube.com/watch?v=XXx7NDgDaRU&t=738s)** just to figure out what's going on in life.

**[12:21](https://youtube.com/watch?v=XXx7NDgDaRU&t=741s)** And there we go.

**[12:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=742s)** There's open sense in a VLAN dedicated to this purpose.

**[12:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=746s)** Now what's interesting is remember, I'm in my Ubuntu virtual machine here.

**[12:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=750s)** I can still access things on my main LAN from inside this test LAN.

**[12:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=757s)** I mean, you could create a firewall rule in open sense to prevent that if you wanted to.

**[12:41](https://youtube.com/watch?v=XXx7NDgDaRU&t=761s)** But what this does is it gives us a totally isolated playground

**[12:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=765s)** to make networking changes and play around with subnets

**[12:50](https://youtube.com/watch?v=XXx7NDgDaRU&t=770s)** and port forwarding if we want to or even install something like tail scale.

**[12:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=776s)** So let's go ahead and do that. I'm going to show you how to install

**[12:59](https://youtube.com/watch?v=XXx7NDgDaRU&t=779s)** tail scale on open sense so that you can access this VLAN

**[13:03](https://youtube.com/watch?v=XXx7NDgDaRU&t=783s)** from anywhere that your tail scale account is enabled or your tail net can reach

**[13:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=788s)** and allow you to do some testing of things remotely that way.

**[13:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=792s)** Now we are working on some improvements for the installation process of tail scale on open sense.

**[13:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=797s)** But for today, we're going to have to drop to the command line.

**[13:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=800s)** So we can't do this through the UI interface.

**[13:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=803s)** Now the first thing I'm going to do is just go ahead and make sure that my open sense

**[13:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=807s)** instance is up to date. It's a completely fresh install.

**[13:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=810s)** We haven't touched it. So it's likely there's going to be a few package upgrades to do.

**[13:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=814s)** So whilst I go through that process, I'm just going to speed this up in post.

**[13:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=817s)** But you want to make sure that all of your firmware packages on your open sense box

**[13:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=822s)** are up to date.

**[13:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=823s)** All right, so as open sense is rebooting, I'm just going to jump back into my

**[13:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=829s)** Proxmox instance over here and bring up the console.

**[13:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=832s)** So I can see what that virtual machine is actually doing.

**[13:55](https://youtube.com/watch?v=XXx7NDgDaRU&t=835s)** I'm going to need the console in just a second anyway.

**[13:58](https://youtube.com/watch?v=XXx7NDgDaRU&t=838s)** So let's go back to Ubuntu on one side and open sense on the other.

**[14:03](https://youtube.com/watch?v=XXx7NDgDaRU&t=843s)** You can see the open sense is still booting over here.

**[14:07](https://youtube.com/watch?v=XXx7NDgDaRU&t=847s)** Shouldn't take very much longer at all.

**[14:10](https://youtube.com/watch?v=XXx7NDgDaRU&t=850s)** And there we go.

**[14:11](https://youtube.com/watch?v=XXx7NDgDaRU&t=851s)** So we have open sense fully up to date.

**[14:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=854s)** We can go ahead and just verify that real quick.

**[14:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=857s)** Log in again with our username password.

**[14:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=860s)** Please don't save that.

**[14:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=862s)** And then click check for updates one more time.

**[14:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=866s)** Fantastic.

**[14:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=867s)** No updates are available.

**[14:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=868s)** That's what we want to see is this green firmware status just here.

**[14:32](https://youtube.com/watch?v=XXx7NDgDaRU&t=872s)** Once we have that, we're good to proceed with the next step.

**[14:35](https://youtube.com/watch?v=XXx7NDgDaRU&t=875s)** So hop over to your open sense shell window or whatever you're using to run open sense in the VLAN.

**[14:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=882s)** And then log in.

**[14:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=883s)** Now you'll be given the set of what is it, 13, 14 different options here.

**[14:47](https://youtube.com/watch?v=XXx7NDgDaRU&t=887s)** We're going to pick option eight, which is the option for the shell.

**[14:51](https://youtube.com/watch?v=XXx7NDgDaRU&t=891s)** Now tail scale isn't available as a package in open sense quite yet.

**[14:55](https://youtube.com/watch?v=XXx7NDgDaRU&t=895s)** But it is available as part of the free BSD ports project.

**[14:59](https://youtube.com/watch?v=XXx7NDgDaRU&t=899s)** So we have an article on our tail scale and knowledge base, our K base just here.

**[15:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=905s)** And these are the steps I'm going to be following throughout the next few minutes.

**[15:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=908s)** I'll put a link to this down in the description.

**[15:10](https://youtube.com/watch?v=XXx7NDgDaRU&t=910s)** But for now, let's go ahead and just do this in real time.

**[15:13](https://youtube.com/watch?v=XXx7NDgDaRU&t=913s)** So I'm just going to do open sense hyphen code space ports.

**[15:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=917s)** Now this is going to download some information from the free BSD port project.

**[15:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=923s)** And make sure that all of your ports are up to date.

**[15:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=926s)** Once we've done that, we can go ahead and actually install tail scale by building it from source.

**[15:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=931s)** Right, once the code ports have downloaded, that took maybe a minute and a half, two minutes on my machine.

**[15:36](https://youtube.com/watch?v=XXx7NDgDaRU&t=936s)** And we want to go to this directory.

**[15:38](https://youtube.com/watch?v=XXx7NDgDaRU&t=938s)** So CD slash user ports security and then tail scale.

**[15:46](https://youtube.com/watch?v=XXx7NDgDaRU&t=946s)** And once we're in the tail scale directory, we'll type make install.

**[15:50](https://youtube.com/watch?v=XXx7NDgDaRU&t=950s)** This will download a bunch of dependencies and compile tail scale from source for us.

**[15:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=956s)** All right, now that's finished building.

**[15:58](https://youtube.com/watch?v=XXx7NDgDaRU&t=958s)** We want to go ahead and do service tail scale d enable.

**[16:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=962s)** So that's going to enable the tail scale demon.

**[16:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=965s)** And the same thing tail scale d start.

**[16:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=969s)** I'm just going to start the tail scale demon running right away.

**[16:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=972s)** Next thing we're going to want to do is do tail scale up.

**[16:15](https://youtube.com/watch?v=XXx7NDgDaRU&t=975s)** I'm going to ask us to log in in a web browser.

**[16:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=980s)** So I have gone ahead and logged in.

**[16:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=982s)** Now this is on my local laptop.

**[16:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=983s)** You could just as easily do this in the Ubuntu VM.

**[16:25](https://youtube.com/watch?v=XXx7NDgDaRU&t=985s)** It doesn't really matter.

**[16:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=987s)** Login dot tail scale dot com slash f 74.

**[16:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=993s)** Oh my goodness. CBC CBC 64 B zero.

**[16:38](https://youtube.com/watch?v=XXx7NDgDaRU&t=998s)** I would be nice if I had copy and paste from the proxmox terminal.

**[16:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=1003s)** But I don't unfortunately.

**[16:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=1005s)** So I'm going to go ahead and authenticate this with the tail net that I want to use.

**[16:48](https://youtube.com/watch?v=XXx7NDgDaRU&t=1008s)** And we'll see.

**[16:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=1009s)** I now have open sense in my tail net.

**[16:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=1012s)** All right, now that tail scale is built, started logged in.

**[16:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=1016s)** We need to go in just to sign an interface in the open sense.

**[17:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=1020s)** UI.

**[17:01](https://youtube.com/watch?v=XXx7NDgDaRU&t=1021s)** So let's go ahead and look in interfaces and click on assignments here.

**[17:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=1024s)** We currently have an unassigned interface, which is tail scale.

**[17:08](https://youtube.com/watch?v=XXx7NDgDaRU&t=1028s)** So I'm going to go ahead and just assign that to.

**[17:11](https://youtube.com/watch?v=XXx7NDgDaRU&t=1031s)** I'm going to call this one tail scale.

**[17:15](https://youtube.com/watch?v=XXx7NDgDaRU&t=1035s)** And we see on the left hand side, just here.

**[17:18](https://youtube.com/watch?v=XXx7NDgDaRU&t=1038s)** We now have a tail scale interface.

**[17:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=1040s)** I'm going to go ahead and enable that interface.

**[17:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=1042s)** And this will enable us to use this interface in things like firewall rules

**[17:27](https://youtube.com/watch?v=XXx7NDgDaRU&t=1047s)** and do a whole bunch of other cool stuff.

**[17:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=1049s)** And I click apply.

**[17:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=1053s)** And now that's done.

**[17:34](https://youtube.com/watch?v=XXx7NDgDaRU&t=1054s)** We can go back to our overview and see that we have a LAN interface on 101.254.

**[17:40](https://youtube.com/watch?v=XXx7NDgDaRU&t=1060s)** We have a tail scale interface with our tail scale private IP address here.

**[17:45](https://youtube.com/watch?v=XXx7NDgDaRU&t=1065s)** And then also the LAN interface here is connected with 7.221, which remember is not really a LAN address.

**[17:53](https://youtube.com/watch?v=XXx7NDgDaRU&t=1073s)** It's just in my local air network outside of this sandbox that created.

**[17:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=1077s)** So remember the entire purpose of doing this and creating this open-sense instance,

**[18:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=1082s)** this networking playground was to be able to break stuff.

**[18:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=1085s)** And so what I wanted to show you is that on my local Mac here,

**[18:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=1089s)** so this terminal window right here is running on my local MacBook,

**[18:13](https://youtube.com/watch?v=XXx7NDgDaRU&t=1093s)** I can't connect to any of these devices.

**[18:16](https://youtube.com/watch?v=XXx7NDgDaRU&t=1096s)** So if we ever look at the Ubuntu virtual machine and see what the IP address of this guy is,

**[18:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=1102s)** 19216810.

**[18:25](https://youtube.com/watch?v=XXx7NDgDaRU&t=1105s)** If I try and ping that address, not on awful lot happens as we would expect.

**[18:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=1111s)** We created this isolated area so that we can break stuff and have an isolated instance

**[18:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=1117s)** of a whole set of virtual machines, you know, a dedicated Kubernetes cluster that lives somewhere else.

**[18:43](https://youtube.com/watch?v=XXx7NDgDaRU&t=1123s)** So we can test ingress and egress, or maybe we wanted to run a database and pretend it's off site

**[18:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=1129s)** so we could do some testing of our CI pipeline.

**[18:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=1132s)** I don't know, whatever you want to do with this, you can, and we've created this environment.

**[18:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=1137s)** So let's go ahead and try and figure out how we can actually connect into it.

**[19:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=1140s)** Now we've got tailscale running on open-sense.

**[19:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=1142s)** Now we always recommend wherever possible that you install the tailscale client

**[19:07](https://youtube.com/watch?v=XXx7NDgDaRU&t=1147s)** on any operating system or device that supports it.

**[19:10](https://youtube.com/watch?v=XXx7NDgDaRU&t=1150s)** Ubuntu does support it, but for the purposes of our demo today,

**[19:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=1154s)** I just wanted to show you how you can use open-sense as a subnet router.

**[19:18](https://youtube.com/watch?v=XXx7NDgDaRU&t=1158s)** This means that any traffic that goes through open-sense can now reach any client

**[19:23](https://youtube.com/watch?v=XXx7NDgDaRU&t=1163s)** in the network behind open-sense.

**[19:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=1166s)** And this is particularly powerful in the real world when you want to install open-sense, say,

**[19:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=1170s)** at a parent's house, and access any device behind that firewall using the local IP address,

**[19:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=1177s)** so the 192.168 address, rather than having to walk through installing tailscale or whatever remotely.

**[19:44](https://youtube.com/watch?v=XXx7NDgDaRU&t=1184s)** We've all been in that situation, I think, as tech guys, tech people,

**[19:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=1189s)** that have to install those things remotely and it can be a bit tricky.

**[19:52](https://youtube.com/watch?v=XXx7NDgDaRU&t=1192s)** So the subnet router just removes all of that pain.

**[19:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=1196s)** Maybe there's a printer or something behind the firewall you want to access

**[20:00](https://youtube.com/watch?v=XXx7NDgDaRU&t=1200s)** that you genuinely can't install tailscale on yet.

**[20:04](https://youtube.com/watch?v=XXx7NDgDaRU&t=1204s)** That's where the subnet router comes in.

**[20:06](https://youtube.com/watch?v=XXx7NDgDaRU&t=1206s)** So let's hop back over to our open-sense command line and do tailscale up again.

**[20:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=1212s)** And this time we're going to do advertised routes 192.168.101.0 slash 24.

**[20:20](https://youtube.com/watch?v=XXx7NDgDaRU&t=1220s)** And this basically means that every device now that lives in that 101 subnet behind open-sense

**[20:26](https://youtube.com/watch?v=XXx7NDgDaRU&t=1226s)** is reachable from a device outside, as long as it's on the tailnet.

**[20:31](https://youtube.com/watch?v=XXx7NDgDaRU&t=1231s)** So my laptop here that I'm recording this demo on, for example,

**[20:35](https://youtube.com/watch?v=XXx7NDgDaRU&t=1235s)** I can now connect to this Ubuntu VM through open-sense using the subnet router functionality.

**[20:42](https://youtube.com/watch?v=XXx7NDgDaRU&t=1242s)** Now, of course, remember whenever you share a subnet like that using a subnet router,

**[20:46](https://youtube.com/watch?v=XXx7NDgDaRU&t=1246s)** there are two steps involved, the first of which is to advertise the route on the remote client.

**[20:51](https://youtube.com/watch?v=XXx7NDgDaRU&t=1251s)** So in this case, open-sense, re-advertising the route there.

**[20:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=1254s)** But when you go back to your tailscale admin console, your dashboard over here,

**[20:58](https://youtube.com/watch?v=XXx7NDgDaRU&t=1258s)** you'll see that this machine has unapproved routes.

**[21:01](https://youtube.com/watch?v=XXx7NDgDaRU&t=1261s)** So we need to click over here and go to edit route settings and make sure that we have the route shared.

**[21:07](https://youtube.com/watch?v=XXx7NDgDaRU&t=1267s)** And this way we're able to actually, let me bring this terminal window in over here.

**[21:12](https://youtube.com/watch?v=XXx7NDgDaRU&t=1272s)** Remember this one's on my local Mac.

**[21:14](https://youtube.com/watch?v=XXx7NDgDaRU&t=1274s)** So this is in the .7 IP range.

**[21:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=1277s)** And if I do the ping1i1.10, I'm able to access that Ubuntu virtual machine through open-sense

**[21:24](https://youtube.com/watch?v=XXx7NDgDaRU&t=1284s)** using the subnet router functionality without having tailscale installed directly on the Ubuntu client.

**[21:30](https://youtube.com/watch?v=XXx7NDgDaRU&t=1290s)** So I hope this demo gave you a good overview of just what's possible using some simple VLAN tags in Proxmox.

**[21:37](https://youtube.com/watch?v=XXx7NDgDaRU&t=1297s)** So let's just recap what we did.

**[21:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=1299s)** We created an open-sense virtual machine that had two network interfaces.

**[21:44](https://youtube.com/watch?v=XXx7NDgDaRU&t=1304s)** One of those network interfaces lives on my current local area network on my current LAN

**[21:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=1309s)** and uses the DHCP that all of the other devices in this house use.

**[21:54](https://youtube.com/watch?v=XXx7NDgDaRU&t=1314s)** That's the 10.42.7 range.

**[21:57](https://youtube.com/watch?v=XXx7NDgDaRU&t=1317s)** We then added a second Nick virtual Nick to that open-sense virtual machine that had a VLAN tag of 101.

**[22:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=1325s)** That meant that it didn't have a DHCP server.

**[22:09](https://youtube.com/watch?v=XXx7NDgDaRU&t=1329s)** So it went ahead and thought, right, well, I'm going to go and be the default.

**[22:13](https://youtube.com/watch?v=XXx7NDgDaRU&t=1333s)** I'm going to go and create one for myself.

**[22:15](https://youtube.com/watch?v=XXx7NDgDaRU&t=1335s)** We then also created a Ubuntu virtual machine with a virtual Nick with the tag of 101

**[22:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=1342s)** so that it got an IP address from that virtual virtualized open-sense instance.

**[22:28](https://youtube.com/watch?v=XXx7NDgDaRU&t=1348s)** And from there, you can extrapolate that, you know, you could create a bunch of virtual machines, do whatever you want.

**[22:33](https://youtube.com/watch?v=XXx7NDgDaRU&t=1353s)** And treat that open-sense instance just as if it is your real firewall.

**[22:39](https://youtube.com/watch?v=XXx7NDgDaRU&t=1359s)** You could break stuff without the Netflix going down or getting texts from friends and family asking you why

**[22:46](https://youtube.com/watch?v=XXx7NDgDaRU&t=1366s)** Plex is off this week or whatever it might be.

**[22:49](https://youtube.com/watch?v=XXx7NDgDaRU&t=1369s)** And I think those of us who are in this space where we're learning and trying to be practitioners and, you know, IT people in general,

**[22:56](https://youtube.com/watch?v=XXx7NDgDaRU&t=1376s)** we don't often have the space available to us to learn networking techniques without breaking some eggs.

**[23:02](https://youtube.com/watch?v=XXx7NDgDaRU&t=1382s)** And this gives us the opportunity to do just that.

**[23:05](https://youtube.com/watch?v=XXx7NDgDaRU&t=1385s)** And then the finalizing on the cake is that using tail scale, we're able to use a subnet routing functionality

**[23:10](https://youtube.com/watch?v=XXx7NDgDaRU&t=1390s)** to reach inside that remote network and pretend and context switch using our tail scale accounts.

**[23:17](https://youtube.com/watch?v=XXx7NDgDaRU&t=1397s)** And context switch to different the lands, if you like, for one of the better words.

**[23:22](https://youtube.com/watch?v=XXx7NDgDaRU&t=1402s)** And so I hope you found this video useful.

**[23:24](https://youtube.com/watch?v=XXx7NDgDaRU&t=1404s)** Remember, there'll be links in the description to all the materials I used throughout this video down below.

**[23:29](https://youtube.com/watch?v=XXx7NDgDaRU&t=1409s)** And until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
