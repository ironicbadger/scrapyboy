---
video_id: "UmVMaymH1-s"
title: "Subnet Routers | Tailscale Explained"
description: "In today’s installment of our Tailscale Explained series, Alex walks you through everything you ever wanted to know about Tailscale subnet routers. He also shows you how to install Tailscale and confi..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-06-20"
duration_seconds: 744
youtube_url: "https://www.youtube.com/watch?v=UmVMaymH1-s"
thumbnail_url: "https://i.ytimg.com/vi/UmVMaymH1-s/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T15:55:47.240602"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2329
transcription_time_seconds: 19.9
---

# Subnet Routers | Tailscale Explained

**[00:00](https://youtube.com/watch?v=UmVMaymH1-s&t=0s)** Welcome into another episode of Tailscale Explained. I'm Alex. In this series, we cover everything you ever wanted to know about Tailscale. Things like Tailscale, SSH, Servant Funnel. And today, we're going to cover subnet routers. There'll be a link to the playlist for Tailscale Explained in the description down below. And as always, I've also put chapter markers down there to help you find a bit of this video that you are looking for. So in today's video, we are going to go through the process of setting up a subnet router on Linux and Windows 2. And don't forget, you can also use an Apple TV.

**[00:30](https://youtube.com/watch?v=UmVMaymH1-s&t=30s)** TV is a subnet router as well. I've put a link to the video I made on that recently, up here for you as well. So I should probably start by explaining what a subnet router is, what it does and why you might need one. Wherever possible, we recommend installing Tailscale on as many client devices as possible, installing Tailscale on each client not only allows for the best performance but also end to end encryption and routing optimizations between these nodes. Tailscale itself supports a wide range of devices these days, iOS,

**[01:01](https://youtube.com/watch?v=UmVMaymH1-s&t=61s)** Android, Linux, Mac, Windows, Amazon, Firesticks. We recently added support for those, too. But we recognize that not every device allows for a direct installation of Tailscale. Sometimes there are impediments such as organizational policy that prohibits the installation of software. And sometimes there are just limitations on the physical devices in question. Maybe they run a closed firmware or simply just aren't powerful enough to run a full networking stack. Just try and imagine Tailscale running on something as simple as a coffee pot.

**[01:31](https://youtube.com/watch?v=UmVMaymH1-s&t=91s)** A smart, a smart coffee pot, for example, another common use case we hear from our users quite frequently is that they already have a network infrastructure configured, but they need a quick and easy way to better secure access into and out of that environment.

**[01:46](https://youtube.com/watch?v=UmVMaymH1-s&t=106s)** So what they do is they take a subnet router and they throw it into an existing VPC and suddenly they have that whole environment available to the rest of their tailnet.

**[01:55](https://youtube.com/watch?v=UmVMaymH1-s&t=115s)** This can include any resource that has a rootable IP address from your subnet router node. And we see lots of folks using this technique to give their devs or test suite access to remote databases, for example.

**[02:06](https://youtube.com/watch?v=UmVMaymH1-s&t=126s)** In fact, whilst researching this video, we heard from a robotics team who installed Tailscale on a Raspberry Pi installed inside one of their robots. They then use that Raspberry Pi as a subnet router to connect to a whole bunch of embedded systems and sensors on that robot using a subnet router.

**[02:22](https://youtube.com/watch?v=UmVMaymH1-s&t=142s)** Now, maybe you are wanting to remotely access a DNS server or a games console or some other device that can't run Tailscale. That is where a subnet router comes in.

**[02:33](https://youtube.com/watch?v=UmVMaymH1-s&t=153s)** A subnet router allows you to install Tailscale on one node in a network and then forward packets from that node out to any other device with an IP address within that subnet.

**[02:43](https://youtube.com/watch?v=UmVMaymH1-s&t=163s)** And you can do that as if the traffic originated from the subnet router itself. So what do I mean by that exactly?

**[02:50](https://youtube.com/watch?v=UmVMaymH1-s&t=170s)** Well, when a device connects to a network, it gets an IP address and that IP address lives within what's called a subnet.

**[02:57](https://youtube.com/watch?v=UmVMaymH1-s&t=177s)** We can think of this a little bit like how we group houses together in the real world using postal codes. The most common subnet size you'll see is what's called a slash 24 inside a notation.

**[03:08](https://youtube.com/watch?v=UmVMaymH1-s&t=188s)** This is a lazy way of writing the number of bits available for a specific subnet. So if you've ever seen something like 255.255.255.0.

**[03:18](https://youtube.com/watch?v=UmVMaymH1-s&t=198s)** That means there are 254 IP addresses available in that subnet range. You want to try and keep this number fairly low for performance reasons and 254 is considered the industry standard value for this.

**[03:31](https://youtube.com/watch?v=UmVMaymH1-s&t=211s)** So therefore in this example, the subnet would start with 192.168.0.1 and end at 192.168.0.254. That is a slash 24.

**[03:43](https://youtube.com/watch?v=UmVMaymH1-s&t=223s)** So the general idea with a tailscale subnet router is you would publish the routes for that slash 24 via the tailscale interface and then you're able to access any device in that remote subnet from any other device on your tailnet.

**[03:57](https://youtube.com/watch?v=UmVMaymH1-s&t=237s)** So if we come back to that packet rewriting thing for a moment now, the tailscale demon on your subnet router node is receiving a bunch of packets via your tailnet with the destination of a remote subnet coded into them.

**[04:09](https://youtube.com/watch?v=UmVMaymH1-s&t=249s)** But how do your tailnet devices know where to send these packets at all? Well, that's because these routes are published to every device on your tailnet. That's with a notable caveat here that Linux devices, you must pass the accept routes flag in order for Linux hosts to pick up these routes accordingly.

**[04:27](https://youtube.com/watch?v=UmVMaymH1-s&t=267s)** The subnet router ingests these packets and then rewrites them and sends them on to the requested destination host.

**[04:34](https://youtube.com/watch?v=UmVMaymH1-s&t=274s)** That remote host has no idea you are sending these packets via tailscale. In fact, the remote host sees these packets as if they came directly from the subnet router node itself.

**[04:44](https://youtube.com/watch?v=UmVMaymH1-s&t=284s)** This is worth considering when designing firewall rules in a restrictive environment, for example.

**[04:49](https://youtube.com/watch?v=UmVMaymH1-s&t=289s)** Also worth considering is that some people might not want that rewrite to take place.

**[04:54](https://youtube.com/watch?v=UmVMaymH1-s&t=294s)** If that's you, you probably know it's you and we offer an option for you called disabling SNAT and I'll put a link to that in the description down below.

**[05:01](https://youtube.com/watch?v=UmVMaymH1-s&t=301s)** Essentially that basically turns off the rewrite of the origin IP so you can maintain the sanctity of those packets as they get sent through a subnet router.

**[05:11](https://youtube.com/watch?v=UmVMaymH1-s&t=311s)** Right, so let's walk through the process of setting up a subnet router on Windows.

**[05:15](https://youtube.com/watch?v=UmVMaymH1-s&t=315s)** I have here a fresh install of Windows 11 and I'm going to download tailscale from tailscale.com.

**[05:21](https://youtube.com/watch?v=UmVMaymH1-s&t=321s)** So head over to the website and up here in the top right hand corner, click on the download button, followed by download tailscale for Windows.

**[05:29](https://youtube.com/watch?v=UmVMaymH1-s&t=329s)** Then run the installer that downloads and click on the run button here.

**[05:33](https://youtube.com/watch?v=UmVMaymH1-s&t=333s)** Next, agree to the license terms and let the installation progress.

**[05:37](https://youtube.com/watch?v=UmVMaymH1-s&t=337s)** Once the installation is successfully completed, you'll be prompted to log in and I'm going to go ahead and use the Google authentication

**[05:43](https://youtube.com/watch?v=UmVMaymH1-s&t=343s)** for the tail and scales at gmail.com, tailnet that I always use in these videos and add this desktop node to my tailnet.

**[05:51](https://youtube.com/watch?v=UmVMaymH1-s&t=351s)** Once it shows login successful, I'm going to go down here to the bottom right hand corner and just verify everything looks like I would expect.

**[05:57](https://youtube.com/watch?v=UmVMaymH1-s&t=357s)** I've got all my network devices here, all my tag devices, preferences, I can do things like automatically install updates now or run unattended,

**[06:06](https://youtube.com/watch?v=UmVMaymH1-s&t=366s)** which tells tailscale to run as the system instead of the currently logged in user.

**[06:10](https://youtube.com/watch?v=UmVMaymH1-s&t=370s)** This is useful if you want to keep tailscale running on Windows in the background even after you've logged out.

**[06:15](https://youtube.com/watch?v=UmVMaymH1-s&t=375s)** So in order to create a subnet router, we need to know what the IP range is that we want to publish.

**[06:19](https://youtube.com/watch?v=UmVMaymH1-s&t=379s)** Now, you can find this out typically most subnets, as I say, will be a slash 24, mine happens to be a slash 20.

**[06:27](https://youtube.com/watch?v=UmVMaymH1-s&t=387s)** Now, I'm going to show you in PowerShell how to find out what your IP address is.

**[06:31](https://youtube.com/watch?v=UmVMaymH1-s&t=391s)** You just type IP config and this shows me here that my IP address for this host is 10.42.7.101

**[06:39](https://youtube.com/watch?v=UmVMaymH1-s&t=399s)** and the default gateway is 0.254.

**[06:43](https://youtube.com/watch?v=UmVMaymH1-s&t=403s)** As I say, I happen to know that my subnet here is a slash 20 inside a notation that gives me a bit more than those 254 devices.

**[06:50](https://youtube.com/watch?v=UmVMaymH1-s&t=410s)** We talked about earlier in the video, but you can also just type tailscale here.

**[06:55](https://youtube.com/watch?v=UmVMaymH1-s&t=415s)** You don't have to use the cis tray client in the bottom right hand corner.

**[06:59](https://youtube.com/watch?v=UmVMaymH1-s&t=419s)** So we're going to type tailscale set.

**[07:01](https://youtube.com/watch?v=UmVMaymH1-s&t=421s)** This is how you set parameters for things like exit nodes as well as SSH and in our case, subnet routers.

**[07:07](https://youtube.com/watch?v=UmVMaymH1-s&t=427s)** So we're going to do tailscale set dash dash advertise roots equals 10.42.0.0 slash 20.

**[07:16](https://youtube.com/watch?v=UmVMaymH1-s&t=436s)** And that is going to turn this node into a subnet router for my subnet in this house.

**[07:21](https://youtube.com/watch?v=UmVMaymH1-s&t=441s)** Now, unless you have auto approvers turned on and check the chapters down below for a little bit more on auto approvers,

**[07:26](https://youtube.com/watch?v=UmVMaymH1-s&t=446s)** you're going to need to jump over to your tailscale admin console and just click on the three dot menu over here,

**[07:31](https://youtube.com/watch?v=UmVMaymH1-s&t=451s)** click on edit root settings and then check the box that says the subnet that you just published.

**[07:36](https://youtube.com/watch?v=UmVMaymH1-s&t=456s)** And once you do that, you have successfully configured a subnet router on windows.

**[07:41](https://youtube.com/watch?v=UmVMaymH1-s&t=461s)** It's time to go ahead and get a subnet router set up in Linux.

**[07:46](https://youtube.com/watch?v=UmVMaymH1-s&t=466s)** This is a Ubuntu virtual machine.

**[07:48](https://youtube.com/watch?v=UmVMaymH1-s&t=468s)** And as you can see, this is in the subnet 192.168.79.10.

**[07:53](https://youtube.com/watch?v=UmVMaymH1-s&t=473s)** I also have another host running at 192.168.79.12.

**[07:58](https://youtube.com/watch?v=UmVMaymH1-s&t=478s)** And I want to be able to access both of those from my local laptop using only the Ubuntu node as a subnet router.

**[08:04](https://youtube.com/watch?v=UmVMaymH1-s&t=484s)** I'm also going to just show you real quick that I can't actually ping either of these hosts from this laptop right now.

**[08:11](https://youtube.com/watch?v=UmVMaymH1-s&t=491s)** So the Ubuntu window is in the remote subnet and this terminal window we're looking at here is on my laptop here.

**[08:17](https://youtube.com/watch?v=UmVMaymH1-s&t=497s)** So the objective is to make it so that I can actually ping 79.12 from my local laptop via 79.10.

**[08:26](https://youtube.com/watch?v=UmVMaymH1-s&t=506s)** The first thing we need to do is go ahead and install tailscale on the Linux host.

**[08:30](https://youtube.com/watch?v=UmVMaymH1-s&t=510s)** You can see tailscale isn't currently installed.

**[08:32](https://youtube.com/watch?v=UmVMaymH1-s&t=512s)** So I'm going to go to tailscale.com, click on the download button in the top right hand corner,

**[08:36](https://youtube.com/watch?v=UmVMaymH1-s&t=516s)** and copy the script that we download with curl into my terminal here.

**[08:41](https://youtube.com/watch?v=UmVMaymH1-s&t=521s)** This is going to download an installed tailscale on Linux for me with no user intervention required.

**[08:46](https://youtube.com/watch?v=UmVMaymH1-s&t=526s)** You can see this is now setting up tailscale 1.66.4.

**[08:50](https://youtube.com/watch?v=UmVMaymH1-s&t=530s)** The next thing I'm going to do is a pseudo tailscale up.

**[08:53](https://youtube.com/watch?v=UmVMaymH1-s&t=533s)** I'm also going to cheat a little bit here and do advertised routes equals 192.168.79.0.

**[08:59](https://youtube.com/watch?v=UmVMaymH1-s&t=539s)** Slash 24. I'm also going to enable SSH on this node as well.

**[09:03](https://youtube.com/watch?v=UmVMaymH1-s&t=543s)** You can do this as part of tailscale up or you can do a tailscale set instead if you would prefer.

**[09:10](https://youtube.com/watch?v=UmVMaymH1-s&t=550s)** So this is going to give me a login URL.

**[09:12](https://youtube.com/watch?v=UmVMaymH1-s&t=552s)** Now I've had to go back to my laptop where I'm actually logged into my tailnet to authorize this device.

**[09:18](https://youtube.com/watch?v=UmVMaymH1-s&t=558s)** As usual, I go through the signing with Google Procedure and yes I want to connect Ubuntu to my tailnet.

**[09:25](https://youtube.com/watch?v=UmVMaymH1-s&t=565s)** But in the background you'll see that it updates.

**[09:28](https://youtube.com/watch?v=UmVMaymH1-s&t=568s)** I now need to go into edit route settings in the 3.Menu in my tailscale admin dashboard.

**[09:32](https://youtube.com/watch?v=UmVMaymH1-s&t=572s)** Check the box here which allows traffic to flow through that remote subnet.

**[09:36](https://youtube.com/watch?v=UmVMaymH1-s&t=576s)** And this should be all we need to do.

**[09:39](https://youtube.com/watch?v=UmVMaymH1-s&t=579s)** I'm going to go back to my terminal window that didn't work a few seconds ago.

**[09:42](https://youtube.com/watch?v=UmVMaymH1-s&t=582s)** And voila, I can now ping 79.10 but I can't ping 79.12.

**[09:49](https://youtube.com/watch?v=UmVMaymH1-s&t=589s)** And that's because on the next we have to enable packet forwarding.

**[09:52](https://youtube.com/watch?v=UmVMaymH1-s&t=592s)** But remember I enabled tailscale SSH a few minutes ago.

**[09:55](https://youtube.com/watch?v=UmVMaymH1-s&t=595s)** I'm going to just do SSH Alex but Ubuntu.

**[09:58](https://youtube.com/watch?v=UmVMaymH1-s&t=598s)** I didn't send any SSH keys to this remote host and there you go.

**[10:02](https://youtube.com/watch?v=UmVMaymH1-s&t=602s)** I'm now connected via SSH to that remote host in the remote subnet.

**[10:06](https://youtube.com/watch?v=UmVMaymH1-s&t=606s)** I'll just prove that to you is happening.

**[10:08](https://youtube.com/watch?v=UmVMaymH1-s&t=608s)** Look 79.10.

**[10:10](https://youtube.com/watch?v=UmVMaymH1-s&t=610s)** That's all looking good.

**[10:11](https://youtube.com/watch?v=UmVMaymH1-s&t=611s)** So what I want to do is drop to be route.

**[10:14](https://youtube.com/watch?v=UmVMaymH1-s&t=614s)** I'm just going to become route by doing pseudo SU.

**[10:18](https://youtube.com/watch?v=UmVMaymH1-s&t=618s)** Paste in a couple of lines from the tailscale documentation.

**[10:23](https://youtube.com/watch?v=UmVMaymH1-s&t=623s)** I'll put a link to that down in the description of course.

**[10:26](https://youtube.com/watch?v=UmVMaymH1-s&t=626s)** And so now if we try and ping 79.12 from my laptop,

**[10:31](https://youtube.com/watch?v=UmVMaymH1-s&t=631s)** you'll see that that is now successful.

**[10:35](https://youtube.com/watch?v=UmVMaymH1-s&t=635s)** So now we're going to talk briefly about auto approvers.

**[10:38](https://youtube.com/watch?v=UmVMaymH1-s&t=638s)** Typically when you enable a subnet route in tailscale,

**[10:41](https://youtube.com/watch?v=UmVMaymH1-s&t=641s)** you would see this little exclamation mark next to the subnet route

**[10:45](https://youtube.com/watch?v=UmVMaymH1-s&t=645s)** that you just wanted to publish.

**[10:46](https://youtube.com/watch?v=UmVMaymH1-s&t=646s)** And again you'd have to go into route settings and check the box and allow this.

**[10:50](https://youtube.com/watch?v=UmVMaymH1-s&t=650s)** In certain situations though, you might want to just allow people to do this by default.

**[10:54](https://youtube.com/watch?v=UmVMaymH1-s&t=654s)** So I'm just going to reset the advertised routes by passing a pair of quotation marks here.

**[10:59](https://youtube.com/watch?v=UmVMaymH1-s&t=659s)** You can see the subnets have just disappeared in my admin console.

**[11:03](https://youtube.com/watch?v=UmVMaymH1-s&t=663s)** But if you want to allow people to automatically auto approve exit nodes

**[11:07](https://youtube.com/watch?v=UmVMaymH1-s&t=667s)** or subnet routers for that matter,

**[11:09](https://youtube.com/watch?v=UmVMaymH1-s&t=669s)** I have here a little snippet of code that you might find very useful.

**[11:13](https://youtube.com/watch?v=UmVMaymH1-s&t=673s)** We can jump over to the tailscale admin page under access controls

**[11:17](https://youtube.com/watch?v=UmVMaymH1-s&t=677s)** and add this stanza to our ACLs.

**[11:20](https://youtube.com/watch?v=UmVMaymH1-s&t=680s)** So I'm just going to click save here and I'll put a snippet to this down in the description

**[11:23](https://youtube.com/watch?v=UmVMaymH1-s&t=683s)** as a GitHub repo with all the code snippets from all of our videos here on YouTube.

**[11:28](https://youtube.com/watch?v=UmVMaymH1-s&t=688s)** You can see I've now saved the tailnet policy file.

**[11:31](https://youtube.com/watch?v=UmVMaymH1-s&t=691s)** And so if I go and advertise a route again this time, 79.0,

**[11:36](https://youtube.com/watch?v=UmVMaymH1-s&t=696s)** and we'll see that the tailscale admin console updates in almost real time,

**[11:39](https://youtube.com/watch?v=UmVMaymH1-s&t=699s)** but there is no exclamation mark.

**[11:42](https://youtube.com/watch?v=UmVMaymH1-s&t=702s)** If we go into the route settings, we can see that it was automatically approved.

**[11:46](https://youtube.com/watch?v=UmVMaymH1-s&t=706s)** And we really have only just scratched the surface with subnet routers in today's video.

**[11:50](https://youtube.com/watch?v=UmVMaymH1-s&t=710s)** Didn't even talk about things like BMC, IPMI, remote access with subnet routers,

**[11:55](https://youtube.com/watch?v=UmVMaymH1-s&t=715s)** putting these in like a management VLAN or something.

**[11:59](https://youtube.com/watch?v=UmVMaymH1-s&t=719s)** There's so much more to subnet routers than we could possibly cover in such a short video.

**[12:03](https://youtube.com/watch?v=UmVMaymH1-s&t=723s)** Let us know what you're doing with subnet routers down in the comments.

**[12:06](https://youtube.com/watch?v=UmVMaymH1-s&t=726s)** And be sure to check out the rest of the tailscale explained playlist,

**[12:10](https://youtube.com/watch?v=UmVMaymH1-s&t=730s)** link down in the description as well.

**[12:12](https://youtube.com/watch?v=UmVMaymH1-s&t=732s)** So until next time, thank you so much for watching.

**[12:14](https://youtube.com/watch?v=UmVMaymH1-s&t=734s)** I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
