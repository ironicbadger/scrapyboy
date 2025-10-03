---
video_id: "cg9d87PuanE"
title: "Replace Google with SearXNG - a privacy respecting, self-hosted search engine"
description: "No ads. No trackers. Search the way it was in the good ol' days. 

SearXNG is a self-hostable, fully open-source, search engine aggregator which aggregates results from various search services and dat..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-11-15"
duration_seconds: 1029
youtube_url: "https://www.youtube.com/watch?v=cg9d87PuanE"
thumbnail_url: "https://i.ytimg.com/vi_webp/cg9d87PuanE/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:41:29.535177"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3190
transcription_time_seconds: 28.9
---

# Replace Google with SearXNG - a privacy respecting, self-hosted search engine

**[00:00](https://youtube.com/watch?v=cg9d87PuanE&t=0s)** Hi, I'm Alex from Tailscale, and in today's video, I'm going to show you how to set up searching, CXNG, searching, at least I think that's how you say it. This is a fully open source, self-hosted search engine that lets you combine multiple search engines into one place. There's no tracking, there are no ads, and it's fully privacy-respecting. So in today's video, I'm going to show you how to set that up using Docker Compose, and also add it to your tailnet so that you don't have to expose it to the public internet,

**[00:30](https://youtube.com/watch?v=cg9d87PuanE&t=30s)** and still retain all the benefits of that self-hosted search engine from wherever you are. Those of you that have been around this channel for a little while, will know that I'm pretty big into self-hosting. I also love me some Docker and Proxmox2, so we're going to combine all of those things today into our solution.

**[00:47](https://youtube.com/watch?v=cg9d87PuanE&t=47s)** Now, we need to start by creating a run time somewhere to run this search instance. It doesn't need much in the way of resources, and I'm going to use my Dell 1.0-litre PC Proxmox cluster.

**[00:59](https://youtube.com/watch?v=cg9d87PuanE&t=59s)** This thing is just three of those 1.0-litre Dell PCs in a little rack downstairs. It really doesn't need much compute power. This would quite happily run on a Raspberry Pi, for example.

**[01:10](https://youtube.com/watch?v=cg9d87PuanE&t=70s)** Now, I'm going to create a container on top of Proxmox. It's entirely up to you whether it's a virtual machine or a container.

**[01:16](https://youtube.com/watch?v=cg9d87PuanE&t=76s)** I should probably just show you how to download a template first. So, if you're brand new to Proxmox, and again, the Proxmox part of this is optional, but this is my platform of choice for virtualization.

**[01:26](https://youtube.com/watch?v=cg9d87PuanE&t=86s)** So, I go to the local option here on this node, and then CT templates. I click download. No, I don't. I click templates.

**[01:34](https://youtube.com/watch?v=cg9d87PuanE&t=94s)** And then I just search for Debbie, and this is my container run time of choice. 12.7-1 is the latest at the time I'm recording. I really have this one.

**[01:44](https://youtube.com/watch?v=cg9d87PuanE&t=104s)** So, now I want to do create CT up here in the top right. I'm going to give it a number of, I don't know, 2001. Maybe I should call it a space, Odyssey.

**[01:55](https://youtube.com/watch?v=cg9d87PuanE&t=115s)** Space Audity. There we go. Isn't that a David Bowie song? Anyway, let's do the password in here. I'm not going to worry about an SSH key file, because I'm going to run tail scaling this thing.

**[02:08](https://youtube.com/watch?v=cg9d87PuanE&t=128s)** I'm going to store the storage here on the local node disk. It doesn't need much. So, I'll just give it 20 gig. It doesn't really need much at all.

**[02:17](https://youtube.com/watch?v=cg9d87PuanE&t=137s)** CPUs, again, we're not doing much with this. So, I'll just give it 4 CPU cores and RAM. I don't know, 4 gig. Just again, a fairly arbitrary small amount of storage here.

**[02:30](https://youtube.com/watch?v=cg9d87PuanE&t=150s)** Alright, so, in terms of the networking, I'm going to give it an IP address on my network of 10.42.37.14.

**[02:42](https://youtube.com/watch?v=cg9d87PuanE&t=162s)** So, the slash 24 part is, do you remember the subnet masks that you've seen many times, 255.255.255.0?

**[02:50](https://youtube.com/watch?v=cg9d87PuanE&t=170s)** The slash 24 is a humane way of writing that for a change. So, that's all we're going to do here. And then we're going to put the gateway for my local network into this box here.

**[03:02](https://youtube.com/watch?v=cg9d87PuanE&t=182s)** So, this is just where my router or my firewall is or whatever is doing the gateway rooting for this specific network.

**[03:08](https://youtube.com/watch?v=cg9d87PuanE&t=188s)** Yours might look something like 1921681.99 slash 24 and your gateway may very well look like 1921681.1.

**[03:19](https://youtube.com/watch?v=cg9d87PuanE&t=199s)** But it's going to be very dependent on your network setup as to what the IP address you give this container is.

**[03:26](https://youtube.com/watch?v=cg9d87PuanE&t=206s)** Now, none of this is specific to searching. This is all just sort of basic network stuff creating a virtual machine or what have you.

**[03:33](https://youtube.com/watch?v=cg9d87PuanE&t=213s)** You really have a docker host, there are chapters down below and you can just skip this entire section because we're going to jump to a point later on where we're just using docker compose the spin this thing up.

**[03:43](https://youtube.com/watch?v=cg9d87PuanE&t=223s)** So, if that's you, use the chapters and skip ahead. All right. So, we are going to leave the host and the DNS. I'm actually going to change this because I wanted to override resolve.conf inside the container such that it always has DNS.

**[03:57](https://youtube.com/watch?v=cg9d87PuanE&t=237s)** In fact, I think I'm going to do this with the DNS of the gateway itself rather than pointing out to Cloudflare publicly.

**[04:03](https://youtube.com/watch?v=cg9d87PuanE&t=243s)** All right. So, that's done. Now, because this is Proxmox and an LXC, we're going to need, I wonder if it's still tail scale in this thing.

**[04:10](https://youtube.com/watch?v=cg9d87PuanE&t=250s)** So, we're going to need to make a slight change to the configuration here.

**[04:15](https://youtube.com/watch?v=cg9d87PuanE&t=255s)** So, if we type tail scale LXC into ironically into Google and scroll down and just get this little instruction section here and just copy these two lines onto your clipboard.

**[04:26](https://youtube.com/watch?v=cg9d87PuanE&t=266s)** We're then going to need to go back to our Proxmox host. Note the container number 2001.

**[04:32](https://youtube.com/watch?v=cg9d87PuanE&t=272s)** Okay. Go to Shell. Bring up an editor. I'm going to use VIM. So, Etsy slash PVE, LXC2001.conf.

**[04:42](https://youtube.com/watch?v=cg9d87PuanE&t=282s)** And then I'll do a Shift G to go to the bottom of the file. And then I'll do an O to add a new line underneath what I've already got.

**[04:49](https://youtube.com/watch?v=cg9d87PuanE&t=289s)** And then press Escape. And then colon right quits. This is going to give that container permission to create devices on the DevNet Tone device so that tail scale can actually run inside the LXC container.

**[05:02](https://youtube.com/watch?v=cg9d87PuanE&t=302s)** Then I'm going to do PCT Start, 2000 and 2001, not 2011.

**[05:09](https://youtube.com/watch?v=cg9d87PuanE&t=309s)** Then I'm going to do PCT Start, 2001. And this is going to start this container up.

**[05:14](https://youtube.com/watch?v=cg9d87PuanE&t=314s)** So now if we jump into the shell here, we can see I've got a brand new LXC container.

**[05:18](https://youtube.com/watch?v=cg9d87PuanE&t=318s)** Just going to update my packages out of habit. They usually isn't a huge amount on these images.

**[05:23](https://youtube.com/watch?v=cg9d87PuanE&t=323s)** But just for the sake of completeness, I like to do these updates before I proceed.

**[05:29](https://youtube.com/watch?v=cg9d87PuanE&t=329s)** Now next, we're going to need to install tail scale. So whilst that's running in the background,

**[05:33](https://youtube.com/watch?v=cg9d87PuanE&t=333s)** I'm going to do tail scale download again, the irony that we're using Google for this.

**[05:40](https://youtube.com/watch?v=cg9d87PuanE&t=340s)** And click on the Linux option here. And then just get the one click install command that's there.

**[05:45](https://youtube.com/watch?v=cg9d87PuanE&t=345s)** Now I'm going to curl and install that. And of course, because it's devian curl is too much bloat to install out of the box.

**[05:52](https://youtube.com/watch?v=cg9d87PuanE&t=352s)** So I'm going to do an apt install curl. And then I'm going to curl and install tail scale this way.

**[05:57](https://youtube.com/watch?v=cg9d87PuanE&t=357s)** I'm also going to install Docker as well. So I'm going to go to get docker.com.

**[06:04](https://youtube.com/watch?v=cg9d87PuanE&t=364s)** Copy this first half of this step number one to my clipboard.

**[06:10](https://youtube.com/watch?v=cg9d87PuanE&t=370s)** Tail scales now installed. So I'm going to do curl and then just pipe it to shell.

**[06:15](https://youtube.com/watch?v=cg9d87PuanE&t=375s)** If you're not comfortable with doing that, you can follow the instructions on the Docker site.

**[06:19](https://youtube.com/watch?v=cg9d87PuanE&t=379s)** And do it all step by step. But this just does it all in one go for me.

**[06:22](https://youtube.com/watch?v=cg9d87PuanE&t=382s)** Once the LXC container is rebooted, go ahead and get logged in again. And then do a tail scale up.

**[06:27](https://youtube.com/watch?v=cg9d87PuanE&t=387s)** I'm going to do a dash dash SSH just because habits I like to be able to SSH into everything on my tail net.

**[06:33](https://youtube.com/watch?v=cg9d87PuanE&t=393s)** I'm going to copy this authentication URL.

**[06:37](https://youtube.com/watch?v=cg9d87PuanE&t=397s)** This pre-supposed I've already got a tail net created.

**[06:40](https://youtube.com/watch?v=cg9d87PuanE&t=400s)** If you haven't, you can go ahead here and sign up for one at tailscale.com.

**[06:44](https://youtube.com/watch?v=cg9d87PuanE&t=404s)** I'm going to authenticate with my Google identity provider, which is the one that I use for all of these demos.

**[06:49](https://youtube.com/watch?v=cg9d87PuanE&t=409s)** And then going to connect the device space audity to the tail and scales at Gmail tail net.

**[06:56](https://youtube.com/watch?v=cg9d87PuanE&t=416s)** So you'll see in here, there's a few different nodes. I actually don't need this one anymore.

**[07:01](https://youtube.com/watch?v=cg9d87PuanE&t=421s)** Because this was all stuff I was doing last week for live streams.

**[07:04](https://youtube.com/watch?v=cg9d87PuanE&t=424s)** So you can see we've got a couple of nodes in here. In fact, I'm going to remove this one too.

**[07:08](https://youtube.com/watch?v=cg9d87PuanE&t=428s)** We've got Baldric, which is this laptop here on my desk and space audity, which is the search engine,

**[07:15](https://youtube.com/watch?v=cg9d87PuanE&t=435s)** or at least it will be, that's running in my little proximate cluster.

**[07:19](https://youtube.com/watch?v=cg9d87PuanE&t=439s)** So that's all good well and good now. And I think if we do a tail scale status,

**[07:24](https://youtube.com/watch?v=cg9d87PuanE&t=444s)** we should see that we've got the Linux node logged in as well as this laptop too.

**[07:30](https://youtube.com/watch?v=cg9d87PuanE&t=450s)** Now, the next step is to create the Docker compose file that's going to drive all of the searching stuff that we're doing here.

**[07:36](https://youtube.com/watch?v=cg9d87PuanE&t=456s)** The the searching search xng instance that we're doing.

**[07:40](https://youtube.com/watch?v=cg9d87PuanE&t=460s)** I wrote a blog post over at blog.ktz.me and I'll put a link to this in the description down below.

**[07:45](https://youtube.com/watch?v=cg9d87PuanE&t=465s)** Inside of this blog post is a little description, a little gist of the Docker compose file.

**[07:51](https://youtube.com/watch?v=cg9d87PuanE&t=471s)** So this is going to take you to GitHub and a little gist I put together.

**[07:55](https://youtube.com/watch?v=cg9d87PuanE&t=475s)** So all we want to do is go to the raw version and then copy and paste this onto our clipboard.

**[08:01](https://youtube.com/watch?v=cg9d87PuanE&t=481s)** Now we're going to go back to the searching.

**[08:04](https://youtube.com/watch?v=cg9d87PuanE&t=484s)** Alexy container and just type vi again, Vim compose.yaml.

**[08:09](https://youtube.com/watch?v=cg9d87PuanE&t=489s)** I'm going to press i to go into insert mode, paste that in like you would any other file with a command v or control v.

**[08:16](https://youtube.com/watch?v=cg9d87PuanE&t=496s)** And then the only thing that we need to set is your searching base URL.

**[08:21](https://youtube.com/watch?v=cg9d87PuanE&t=501s)** Now where do we get this with tail scale at least every single node gets a fully qualified domain name for free out of the box.

**[08:29](https://youtube.com/watch?v=cg9d87PuanE&t=509s)** And that's what we're going to use today.

**[08:31](https://youtube.com/watch?v=cg9d87PuanE&t=511s)** So head over to your tail scale admin console, go to DNS and just take note of this tail net name here.

**[08:37](https://youtube.com/watch?v=cg9d87PuanE&t=517s)** If you haven't rolled a custom name yet, feel free to go ahead and do so. It's totally optional.

**[08:42](https://youtube.com/watch?v=cg9d87PuanE&t=522s)** But you're going to want to click on rename tail net and then go through and roll the dice so that you get a fun novelty name like the velociraptor hyphen noodle fish.

**[08:52](https://youtube.com/watch?v=cg9d87PuanE&t=532s)** You're also going to want to make sure that you've got magic DNS and HTTPS certificates enabled as well.

**[08:58](https://youtube.com/watch?v=cg9d87PuanE&t=538s)** Now we don't really want to be typing space oddity every single time that we go for our searches.

**[09:03](https://youtube.com/watch?v=cg9d87PuanE&t=543s)** So I'm going to make this slightly easier for us and go into the tail scale admin console page and rename this node from space oddity as fun as that is to search.

**[09:17](https://youtube.com/watch?v=cg9d87PuanE&t=557s)** So essentially what we're going to end up with now is a fully qualified domain name of search dot velociraptor hyphen noodle fish dot TS dot net.

**[09:26](https://youtube.com/watch?v=cg9d87PuanE&t=566s)** We're going to be able to use that fully qualified domain name to generate a TLS certificate from let's encrypt that will mean that our browsers trust the search front end that we're about to create.

**[09:36](https://youtube.com/watch?v=cg9d87PuanE&t=576s)** And then you can also search directly from your phone, even if you're not at home or wherever this particular machine is living.

**[09:42](https://youtube.com/watch?v=cg9d87PuanE&t=582s)** So I'm just going to copy the fully qualified domain name onto my clipboard and then go back to proxmox and continue modifying my Docker compose file.

**[09:50](https://youtube.com/watch?v=cg9d87PuanE&t=590s)** Now I'm going to modify from where my cursor is until the end of the line and I can do that with a C dollar sign and then just do a command V and it's going to paste in search dot velociraptor hyphen noodle fish dot TS dot net.

**[10:03](https://youtube.com/watch?v=cg9d87PuanE&t=603s)** I'm going to press escape to edits to exit insert mode and then do a right quit with command wq.

**[10:11](https://youtube.com/watch?v=cg9d87PuanE&t=611s)** Next, I want to do a Docker compose up and this is going to now create the searching instance as well as the reddest instance that it uses to catch a bunch of data.

**[10:21](https://youtube.com/watch?v=cg9d87PuanE&t=621s)** Once that started, we exposed port 8080 in the Docker compose file, we can go over to our browser and this notice is running on port 8080 on plain HTTP, but it works.

**[10:32](https://youtube.com/watch?v=cg9d87PuanE&t=632s)** So now we can do a quick test here and just search for whatever we like, you can see that it's using dot dot go quant Google brave wiki data and Wikipedia all under the hood.

**[10:45](https://youtube.com/watch?v=cg9d87PuanE&t=645s)** So now we want to add this to our tailnet, OK, and the easiest way to do that, remember we've already added the LXC container itself to our talent, which is indeed how we're even accessing this site right now.

**[10:58](https://youtube.com/watch?v=cg9d87PuanE&t=658s)** We want to use tailscale serve to generate us a TLS certificate for this domain. So we've verified that searching is running properly and I've quit that using control C.

**[11:08](https://youtube.com/watch?v=cg9d87PuanE&t=668s)** I'm now going to do Docker compose up minus D to bring this up in the background.

**[11:13](https://youtube.com/watch?v=cg9d87PuanE&t=673s)** By the way, if you want to monitor those logs, you can do a Docker compose logs minus F and it will print out exactly what's going on in real time again, control C to escape those.

**[11:23](https://youtube.com/watch?v=cg9d87PuanE&t=683s)** But to expose port 8080 or this container to our tailnet, we're going to need to use a tailscale serve command.

**[11:32](https://youtube.com/watch?v=cg9d87PuanE&t=692s)** Tailscale serve, you can kind of think of it a little bit like a built in reverse proxy for your tailnet, one command and it will turn any requests that go to that specific port into a fully TLS backed with Lexing Crypt domain on TS dot net.

**[11:47](https://youtube.com/watch?v=cg9d87PuanE&t=707s)** There are some documentation over here, which I highly recommend you take a read of if you want to learn more.

**[11:52](https://youtube.com/watch?v=cg9d87PuanE&t=712s)** The short version is all you want to do is tailscale serve dash dash BG 8080 and this is going to make available within your tailnet only not on the public internet, only if you are authenticated to a device on your tailnet.

**[12:07](https://youtube.com/watch?v=cg9d87PuanE&t=727s)** And that's really important because we don't know expose this custom private search engine.

**[12:11](https://youtube.com/watch?v=cg9d87PuanE&t=731s)** It's just for me to the public internet, we want to keep it private and secure, right? That's kind of the whole point.

**[12:18](https://youtube.com/watch?v=cg9d87PuanE&t=738s)** So you can see here that we've exposed local host 127.001 on port 8080 to this URL here.

**[12:27](https://youtube.com/watch?v=cg9d87PuanE&t=747s)** The first time you connect to this URL is going to take 5 to 20 seconds, depending on how busy the Lexing Crypt API is today.

**[12:38](https://youtube.com/watch?v=cg9d87PuanE&t=758s)** Why it takes so long is because it's generating a certificate in real time in the background for you.

**[12:43](https://youtube.com/watch?v=cg9d87PuanE&t=763s)** So it's doing the DNS challenge and all that kind of stuff to verify that you actually own this specific domain name.

**[12:50](https://youtube.com/watch?v=cg9d87PuanE&t=770s)** And after that little weight is complete, which in my case took about 15 seconds.

**[12:55](https://youtube.com/watch?v=cg9d87PuanE&t=775s)** You can see I've got my fully self hosted search engine available to me anywhere that I want to be connected to this tailnet.

**[13:03](https://youtube.com/watch?v=cg9d87PuanE&t=783s)** So again, I can just search for tailscale and it's going to bring me up a nicely formatted set of search results.

**[13:10](https://youtube.com/watch?v=cg9d87PuanE&t=790s)** No ads, no tracking, respecting all of my privacy. It's just so wonderful.

**[13:16](https://youtube.com/watch?v=cg9d87PuanE&t=796s)** We've now set the entire thing up, but there's one little cherry on the cake that I want to just add in this final chapter for you.

**[13:24](https://youtube.com/watch?v=cg9d87PuanE&t=804s)** And that is how do we make Google Chrome use this search engine as our default moving forward.

**[13:30](https://youtube.com/watch?v=cg9d87PuanE&t=810s)** It's actually really easy. So again, full details of this are in the blog post, which will be linked in the description down below.

**[13:38](https://youtube.com/watch?v=cg9d87PuanE&t=818s)** And it's a it's a mere 13 step process, but I promise you it's not that bad.

**[13:43](https://youtube.com/watch?v=cg9d87PuanE&t=823s)** So what we want to do is go to the three dot menu up here in the top right hand corner, click on settings and then search engine over here on the left.

**[13:52](https://youtube.com/watch?v=cg9d87PuanE&t=832s)** Manage search engines and site search.

**[13:56](https://youtube.com/watch?v=cg9d87PuanE&t=836s)** You can ignore all of this. You can just probably leave the keyboard shortcut of space or tab exactly as it was.

**[14:03](https://youtube.com/watch?v=cg9d87PuanE&t=843s)** Then scroll down a little bit to where it says site search.

**[14:06](https://youtube.com/watch?v=cg9d87PuanE&t=846s)** Now Google, I'm going to be a little cynical for a moment here. Don't make it very obvious how to change the default search in Chrome.

**[14:13](https://youtube.com/watch?v=cg9d87PuanE&t=853s)** Do they think looking at this that it's not possible.

**[14:16](https://youtube.com/watch?v=cg9d87PuanE&t=856s)** But if you scroll down to this site search section just here, click on add.

**[14:20](https://youtube.com/watch?v=cg9d87PuanE&t=860s)** And I'm just going to call mine searching the shortcut can again be at searching.

**[14:27](https://youtube.com/watch?v=cg9d87PuanE&t=867s)** It doesn't really matter what the shortcut is. I don't think and I'm just going to grab this URL right here.

**[14:33](https://youtube.com/watch?v=cg9d87PuanE&t=873s)** Now in the syntax that's required for this specific field here, we're going to need to do a little bit of substitute and replace.

**[14:42](https://youtube.com/watch?v=cg9d87PuanE&t=882s)** You can see that in the blog post I talk about needing to do a percent sign.

**[14:47](https://youtube.com/watch?v=cg9d87PuanE&t=887s)** So what we want to do is after the URL, we're going to do search and then a question mark and then the query just here.

**[14:53](https://youtube.com/watch?v=cg9d87PuanE&t=893s)** So let me explain that one more time.

**[14:56](https://youtube.com/watch?v=cg9d87PuanE&t=896s)** So we've got the full domain name, a fully qualified domain name for our searching instance,

**[15:02](https://youtube.com/watch?v=cg9d87PuanE&t=902s)** search for loss of raptor noodle fish dot TS dot net.

**[15:06](https://youtube.com/watch?v=cg9d87PuanE&t=906s)** And then once you get to the slash if you type search and then a question mark and queue for query equals.

**[15:13](https://youtube.com/watch?v=cg9d87PuanE&t=913s)** And then a percent sign and s what that's going to do is the percent sign s part does a string substitution.

**[15:19](https://youtube.com/watch?v=cg9d87PuanE&t=919s)** And it does that string substitution and replaces the contents of percent s with the query that you just typed in your search box.

**[15:27](https://youtube.com/watch?v=cg9d87PuanE&t=927s)** Click on add and then the magic part is if you click on that three dot menu just there and click on make default.

**[15:34](https://youtube.com/watch?v=cg9d87PuanE&t=934s)** Every time we now do a search for again, I'm going to just search for tail scale notice it says searching search.

**[15:43](https://youtube.com/watch?v=cg9d87PuanE&t=943s)** And it's going to search through velociraptor noodle fish.

**[15:46](https://youtube.com/watch?v=cg9d87PuanE&t=946s)** And I'm going to search for all I don't know Taylor Swift.

**[15:51](https://youtube.com/watch?v=cg9d87PuanE&t=951s)** I'm not exactly a big Taylor Swift fan who I am a big fan of porcupine tree. There we go.

**[15:57](https://youtube.com/watch?v=cg9d87PuanE&t=957s)** Let's get things back on track. Fantastic.

**[16:01](https://youtube.com/watch?v=cg9d87PuanE&t=961s)** Stephen Wilson, by the way, chef's kiss wonderful musician if you've never heard of him.

**[16:07](https://youtube.com/watch?v=cg9d87PuanE&t=967s)** So I think that will probably cover us for today. What are we doing? It's going to recap real quick.

**[16:12](https://youtube.com/watch?v=cg9d87PuanE&t=972s)** We created an LXC container on top of proxmox.

**[16:16](https://youtube.com/watch?v=cg9d87PuanE&t=976s)** We installed Docker inside the LXC container and tail scale to we then span up a searching instance such that we can have completely local search searches and respect our privacy once more as it pertains to tracking and adds.

**[16:31](https://youtube.com/watch?v=cg9d87PuanE&t=991s)** And just the vomit that comes out of modern search engines.

**[16:36](https://youtube.com/watch?v=cg9d87PuanE&t=996s)** And then we put it on our tail net using tail scale serve.

**[16:40](https://youtube.com/watch?v=cg9d87PuanE&t=1000s)** So we can now access this from our phone at the coffee shop or wherever we happen to be even if we're not on our local Wi-Fi for example.

**[16:47](https://youtube.com/watch?v=cg9d87PuanE&t=1007s)** Now if you want to know more about tail scale, you can look for the links in the description down below.

**[16:51](https://youtube.com/watch?v=cg9d87PuanE&t=1011s)** We do regular live streams on this channel talking about all sorts of wonderful things to do with tail scale.

**[16:57](https://youtube.com/watch?v=cg9d87PuanE&t=1017s)** And until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
