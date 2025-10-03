---
video_id: "JC63OGSzTQI"
title: "How to install Tailscale in an LXC on Proxmox"
description: "Learn how to configure Tailscale to run in an unprivileged LXC container with full kernel-level TUN device support for optimal performance! 

This tutorial covers everything from basic LXC setup to th..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-07-15"
duration_seconds: 730
youtube_url: "https://www.youtube.com/watch?v=JC63OGSzTQI"
thumbnail_url: "https://i.ytimg.com/vi/JC63OGSzTQI/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:43:14.323646"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2141
transcription_time_seconds: 19.3
---

# How to install Tailscale in an LXC on Proxmox

**[00:00](https://youtube.com/watch?v=JC63OGSzTQI&t=0s)** Linux containers or, perhaps as they are better known, LXC containers are a lightweight virtualization technology that provide operating system-level virtualization on Linux systems. You might be familiar with another type of container, though, best known as a Docker container, or to give it its real official proper title, an OCI container or an open container initiative container. LXCs are interesting, to me at least, because they run a full init system inside them like SystemD.

**[00:30](https://youtube.com/watch?v=JC63OGSzTQI&t=30s)** Alternatively, this is in contrast to an OCI container where you need to reinvent the wheel every time with something like an S6 overlay image. LXCs truly are the mini VMs of the container world that we were promised when Docker first came about on the scene, and I find them incredibly useful for certain use cases.

**[00:49](https://youtube.com/watch?v=JC63OGSzTQI&t=49s)** Now in today's video, I'm going to show you how to configure Tailscale to run in an unprivileged LXC on Proxmox, my favourite HomeLab OS of choice, and I'm going to show you also how to give that LXC permission to create a kernel-level ton device for best performance.

**[01:06](https://youtube.com/watch?v=JC63OGSzTQI&t=66s)** LXCs create isolated user space instances that run on a single shared Linux kernel. This is in contrast to traditional virtual machines that virtualize entire hardware stacks.

**[01:17](https://youtube.com/watch?v=JC63OGSzTQI&t=77s)** LXC containers share the host operating systems kernel whilst maintaining separation between processes, fast systems, and crucially for us today, networking resources.

**[01:27](https://youtube.com/watch?v=JC63OGSzTQI&t=87s)** LXCs are a first-class citizen in my favourite home-living virtualization platform, Proxmox, but giving an LXC kernel-level privileges when the container itself is unprivileged requires a couple of extra steps.

**[01:41](https://youtube.com/watch?v=JC63OGSzTQI&t=101s)** So first thing you want to do is go over to your Proxmox installation. This is the one that's linked in the self-hosting starter guide up here, so if you're wanting to get started with an LXC or Proxmox specifically actually, then that playlist up there is where you need to go.

**[01:56](https://youtube.com/watch?v=JC63OGSzTQI&t=116s)** So, login to your Proxmox instance, I'm going to assume for the purposes of this video that you already have one, you're already familiar with a lot of what I'm showing here.

**[02:04](https://youtube.com/watch?v=JC63OGSzTQI&t=124s)** Go to your specific node and click on, by my case, pve, and then find the storage you want to put the container template onto.

**[02:13](https://youtube.com/watch?v=JC63OGSzTQI&t=133s)** So, click on local, and then CT templates, and then I think it's templates here. Yes, this is what we want.

**[02:19](https://youtube.com/watch?v=JC63OGSzTQI&t=139s)** So, I'm going to sort by package, by clicking on here, and you can either choose ARCH Linux, by the way, or my actual personal preference.

**[02:27](https://youtube.com/watch?v=JC63OGSzTQI&t=147s)** I typically just go for Debian 12.

**[02:30](https://youtube.com/watch?v=JC63OGSzTQI&t=150s)** This is going to download the root file system of the container image that's been built upstream, and download this locally to your Proxmox local storage, I suppose.

**[02:41](https://youtube.com/watch?v=JC63OGSzTQI&t=161s)** Once the container template has downloaded, let's just go ahead and create our container completely as we normally would.

**[02:47](https://youtube.com/watch?v=JC63OGSzTQI&t=167s)** So, container ID, I'm just going to give mine 1,000, I'm just going to call this one, Fred, and Unprivileged, you can leave that checked here.

**[02:55](https://youtube.com/watch?v=JC63OGSzTQI&t=175s)** That's pretty much the purpose for today's video, of course, just to show you how to set up tail scale inside an Unprivileged container.

**[03:01](https://youtube.com/watch?v=JC63OGSzTQI&t=181s)** If you're doing it as a privilege container, you don't need to follow any of these steps.

**[03:06](https://youtube.com/watch?v=JC63OGSzTQI&t=186s)** Next, we will do the storage, and we'll pick the Debian 12 image, we just downloaded.

**[03:12](https://youtube.com/watch?v=JC63OGSzTQI&t=192s)** Disks 8GB is fine, CPU, sure, whatever for.

**[03:16](https://youtube.com/watch?v=JC63OGSzTQI&t=196s)** Memory, again, doesn't really matter, I'll give it 8GB network, I'm going to select DHCP, but again, you can select this however works best for your environment.

**[03:26](https://youtube.com/watch?v=JC63OGSzTQI&t=206s)** It doesn't really matter, actually, what you do here.

**[03:29](https://youtube.com/watch?v=JC63OGSzTQI&t=209s)** But before we actually create the container, let's not check this box, it says start after created.

**[03:36](https://youtube.com/watch?v=JC63OGSzTQI&t=216s)** Let's let Proxmox create the container 1,000, and then we're going to jump into a config file under the hood that we need to modify.

**[03:44](https://youtube.com/watch?v=JC63OGSzTQI&t=224s)** So, let's click on the PVE node itself, click on Shell, and then we're going to open up in a text editor, slash ETC, slash PVE,

**[03:54](https://youtube.com/watch?v=JC63OGSzTQI&t=234s)** LXC, and then the ID number of the container that you just created, so in our case 1,000.

**[04:00](https://youtube.com/watch?v=JC63OGSzTQI&t=240s)** Then using VIM, it's Shift G to go all the way to the bottom of the file, and then O to go into insert mode at the bottom of the file.

**[04:08](https://youtube.com/watch?v=JC63OGSzTQI&t=248s)** And we need to go to this page here in the tail scale case.

**[04:12](https://youtube.com/watch?v=JC63OGSzTQI&t=252s)** So, just search for tail scale LXC and it will take you right to it, we just need these two lines right here.

**[04:19](https://youtube.com/watch?v=JC63OGSzTQI&t=259s)** I'm going to go back to my first tab, copy and paste them in, and then I'm going to do colon, I'm going to press Escape, and then colon and right quit.

**[04:27](https://youtube.com/watch?v=JC63OGSzTQI&t=267s)** I'm going to get some of you guys using VIM by the end of this, as my goal in life.

**[04:33](https://youtube.com/watch?v=JC63OGSzTQI&t=273s)** And now the LXC container is configured to have the permissions to create a DevNet Tun device.

**[04:38](https://youtube.com/watch?v=JC63OGSzTQI&t=278s)** We'll come onto that in just a minute about what that all means.

**[04:41](https://youtube.com/watch?v=JC63OGSzTQI&t=281s)** And now we can do PCT start 1,000 from the command line, and all being good.

**[04:46](https://youtube.com/watch?v=JC63OGSzTQI&t=286s)** We should be able to just treat Fred now, our little LXC container, like we would any other, any other VIM really.

**[04:54](https://youtube.com/watch?v=JC63OGSzTQI&t=294s)** We can install tail scale in here, so let's go to tailscale.com slash download and grab the Linux installation script right here.

**[05:02](https://youtube.com/watch?v=JC63OGSzTQI&t=302s)** Copy and paste that onto our clipboard, paste that in here.

**[05:06](https://youtube.com/watch?v=JC63OGSzTQI&t=306s)** Of course, curl isn't found. App install curl, because it's a fresh install, I need to do apps update first.

**[05:15](https://youtube.com/watch?v=JC63OGSzTQI&t=315s)** Always in two minds, but whether I should cut these little things out, but sometimes I think it might be nice for you to see that I struggle with these things just as much as anybody else sometimes.

**[05:24](https://youtube.com/watch?v=JC63OGSzTQI&t=324s)** Okay, so we've got curl installed, we did app update, then followed by app install curl, and now we're going to paste in our tail scale install script.

**[05:34](https://youtube.com/watch?v=JC63OGSzTQI&t=334s)** And this is going to install this node, it's going to install tail scale on this LXC such that we can now do the standard tail scale up procedure.

**[05:43](https://youtube.com/watch?v=JC63OGSzTQI&t=343s)** I've shown a million times on this channel and add this node to our tail nets.

**[05:47](https://youtube.com/watch?v=JC63OGSzTQI&t=347s)** So tail scale up dash dash SSH, so I don't worry about SSH keys or any of that nonsense anymore.

**[05:53](https://youtube.com/watch?v=JC63OGSzTQI&t=353s)** Going to paste this into my browser, authenticate as usual.

**[05:58](https://youtube.com/watch?v=JC63OGSzTQI&t=358s)** Add this to my tail net and visit the console, and you'll see that your device Fred,

**[06:05](https://youtube.com/watch?v=JC63OGSzTQI&t=365s)** now on your tail net. So as simple as that, that is how you add an LXC to tail scale, or how you enable an LXC to create a privileged network tunnel device in order to run tail scale inside it.

**[06:20](https://youtube.com/watch?v=JC63OGSzTQI&t=380s)** So what just happened, what exactly did we just do with the DevNet Tun device?

**[06:25](https://youtube.com/watch?v=JC63OGSzTQI&t=385s)** Well, whilst I was researching this video, I dug into the whole DevNet Tun thing, and I've actually found it pretty fascinating to be honest.

**[06:33](https://youtube.com/watch?v=JC63OGSzTQI&t=393s)** When I got into the details, essentially, it's a special device file that acts as a bridge between user space programs and the kernel's networking stack.

**[06:43](https://youtube.com/watch?v=JC63OGSzTQI&t=403s)** You can kind of think of it a little bit like a special doorway that lets your application pretend to be a network interface.

**[06:51](https://youtube.com/watch?v=JC63OGSzTQI&t=411s)** Now, the kernel, if you're not familiar, is the heart of your operating system.

**[06:56](https://youtube.com/watch?v=JC63OGSzTQI&t=416s)** What translates stuff between hardware and software, like the alien kind of in the post office in Men in Black 2, like the dude under the table with 18 arms sorting all the mail?

**[07:07](https://youtube.com/watch?v=JC63OGSzTQI&t=427s)** Well, that's what the Linux kernel is doing, but with hardware and software requests, but actually translating stuff in the middle.

**[07:13](https://youtube.com/watch?v=JC63OGSzTQI&t=433s)** So whether program like tail scale wants to create a VPN tunnel device, it doesn't just magically get a network interface.

**[07:20](https://youtube.com/watch?v=JC63OGSzTQI&t=440s)** Instead, it has to open slash DevNet Tun, you can see that on the screen right here, and then use a special IOCTL system call to register a new network device within the kernel.

**[07:31](https://youtube.com/watch?v=JC63OGSzTQI&t=451s)** It's kind of like filling out paperwork to get permission to create a virtual network card, and the kernel gets, I suppose, like final say, over it.

**[07:39](https://youtube.com/watch?v=JC63OGSzTQI&t=459s)** So I'm now comparing the Linux kernel to the Vogue ones. We have to sign things in Triplicate maybe.

**[07:44](https://youtube.com/watch?v=JC63OGSzTQI&t=464s)** Anyway, once you do that special system call of IOCTL, a network device will appear as ton with a number, so like ton 01 or tap 01, depending on the options that you chose.

**[07:57](https://youtube.com/watch?v=JC63OGSzTQI&t=477s)** So when you see ton 0 show up in your network interfaces, that's the kernel creating a brand new virtual interface based on your program's request.

**[08:05](https://youtube.com/watch?v=JC63OGSzTQI&t=485s)** The cool part is when the program closes that file descriptor, the network device, and all of its associated routes just completely disappear.

**[08:13](https://youtube.com/watch?v=JC63OGSzTQI&t=493s)** It's tied to that running process. You can kind of think of the ton device as creating a fake network interfaces actually controlled by a program instead of hardware.

**[08:24](https://youtube.com/watch?v=JC63OGSzTQI&t=504s)** So here's the normal network flow without a VPN. Your browser visits Google.com and creates a packet addressed to Google's IP address after it's done its DNS lookups.

**[08:35](https://youtube.com/watch?v=JC63OGSzTQI&t=515s)** The kernel in its routing table says, well, you need to send anything matching this to your ethernet or your Wi-Fi card.

**[08:43](https://youtube.com/watch?v=JC63OGSzTQI&t=523s)** So it goes out over the e0 network device, and that packet, as I say, goes directly out over the networking device.

**[08:50](https://youtube.com/watch?v=JC63OGSzTQI&t=530s)** But when a ton device gets involved, and your browser says, right, I want to visit a machine on your tail scale network, your tail net, that's what we call it.

**[08:58](https://youtube.com/watch?v=JC63OGSzTQI&t=538s)** Say it's a 100 dot device as part of our CG NAT space or you're looking up a magic DNS entry.

**[09:05](https://youtube.com/watch?v=JC63OGSzTQI&t=545s)** Whatever happens in both cases, it still resolves to a 100 IP address.

**[09:09](https://youtube.com/watch?v=JC63OGSzTQI&t=549s)** It creates a packet addressed to that destination.

**[09:13](https://youtube.com/watch?v=JC63OGSzTQI&t=553s)** The kernel then checks its internal routing table and finds a rule that says anything going to 100 dot 64 dot whatever should go out of the ton zero device.

**[09:24](https://youtube.com/watch?v=JC63OGSzTQI&t=564s)** But the magical part is instead of sending the packet to a physical network card, the kernel hands that packet to whatever program is listening on the ton zero interface, which in our case is the tail scale demon.

**[09:36](https://youtube.com/watch?v=JC63OGSzTQI&t=576s)** The tail scale demon receives this raw packet as if it were any other piece of networking hardware, and encrypts it, wraps it up and sends it through the wire guard tunnel that we create over your real internet connection to the appropriate tail scale peer at the other end.

**[09:51](https://youtube.com/watch?v=JC63OGSzTQI&t=591s)** On the receiving end, the other tail scale demon receives that packet and decrypts it, and it kind of injects it into the local network as if it came from a real network interface, all using the DevNet ton device.

**[10:05](https://youtube.com/watch?v=JC63OGSzTQI&t=605s)** Now what's particularly interesting about this process is that your browser has no idea that any of this VPN stuff just happened.

**[10:12](https://youtube.com/watch?v=JC63OGSzTQI&t=612s)** As far as your browser is concerned, it just sent a normal packet to a normal network interface, and the ton device lets tail scale intercept that packet before it hits any real hardware, do its magic on the packet and then tunnel it to where it needs to go.

**[10:27](https://youtube.com/watch?v=JC63OGSzTQI&t=627s)** The tricky part in our situation here at least with LXCs is that the DevNet ton device needs to be created as a device node and not all environments support this.

**[10:37](https://youtube.com/watch?v=JC63OGSzTQI&t=637s)** Containerized platforms often don't allow it because it requires elevated privileges within the kernel.

**[10:42](https://youtube.com/watch?v=JC63OGSzTQI&t=642s)** The whole point of containers is to limit the blast radius and kind of a model of least privilege is what they operate under.

**[10:50](https://youtube.com/watch?v=JC63OGSzTQI&t=650s)** And specifically to add a DevNet ton device, you need the CapNet admin capability, essentially admin privileges for network operations.

**[10:58](https://youtube.com/watch?v=JC63OGSzTQI&t=658s)** And for a lot of situations, that's considered a security risk, and they don't want to give it to every container.

**[11:04](https://youtube.com/watch?v=JC63OGSzTQI&t=664s)** Hence why we needed to manually and explicitly allow that for our Fred container at the beginning of this video.

**[11:10](https://youtube.com/watch?v=JC63OGSzTQI&t=670s)** So this is why tail scale provides a user space networking node as well for when you can't or don't want to create a kernel level networking device.

**[11:19](https://youtube.com/watch?v=JC63OGSzTQI&t=679s)** And for all but the most demanding workloads, our user space implementation will likely service for your performance needs as well.

**[11:27](https://youtube.com/watch?v=JC63OGSzTQI&t=687s)** But what I would suggest is if you can do the DevNet ton device, and you're the admin of the Proxmox system, I'll probably go that route.

**[11:36](https://youtube.com/watch?v=JC63OGSzTQI&t=696s)** So there you go, that was a very quick overview of how to install tail scale inside an LXC container at a top of Proxmox, as well as a little overview of some of the DevNet ton magic that happens behind the scenes with tail scale too.

**[11:47](https://youtube.com/watch?v=JC63OGSzTQI&t=707s)** Thank you so much for watching and until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
