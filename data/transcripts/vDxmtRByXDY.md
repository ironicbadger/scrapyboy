---
video_id: "vDxmtRByXDY"
title: "Remotely access Home Assistant via Tailscale for free!"
description: "Tailscale is the easiest way to remotely access your Home Assistant. In today's video Alex walks you through the process of using the unofficial Home Assistant Tailscale add-on, and shows how to use T..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-03-29"
duration_seconds: 851
youtube_url: "https://www.youtube.com/watch?v=vDxmtRByXDY"
thumbnail_url: "https://i.ytimg.com/vi_webp/vDxmtRByXDY/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:18:03.358456"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2837
transcription_time_seconds: 23.8
---

# Remotely access Home Assistant via Tailscale for free!

**[00:00](https://youtube.com/watch?v=vDxmtRByXDY&t=0s)** Hi, I'm Alex from Tailscale, and in today's video we're going to talk about home assistance, specifically remote access via Tailscale. Home Assistant is one of my absolute favourite free and open-source software projects. It lets me connect the hue-ball above my head to the robot vacuum downstairs to my garage door. Why would I want to do that? Why wouldn't you want to do that? Today we're going to talk about accessing home assistant remotely over Tailscale, specifically using the unofficial add-on maintained by Frank, who's one of the home assistant developers. I find this most useful when I'm in that kind of

**[00:30](https://youtube.com/watch?v=vDxmtRByXDY&t=30s)** Wi-Fi Grey Zone, just a few feet outside my Wi-Fi range where my phone doesn't really quite know what's going on. If I'm connected over Tailscale, it doesn't matter if I'm on 5G or on Wi-Fi. And if you already have a working fully qualified domain set up with home assistant, I'll show you how to get that working with Tailscale as well. So I'm going to show you how to install Tailscale on a completely fresh home assistant system right here.

**[00:53](https://youtube.com/watch?v=vDxmtRByXDY&t=53s)** Bottom left-hand corner, click on Settings, then go to Add-ons, which is the fifth option in this list. Next, go ahead and click on Add-on Store. Just to be sure, click on Check for Updates first, and then Search for Tailscale. Now we can go ahead and click on Install Tailscale.

**[01:10](https://youtube.com/watch?v=vDxmtRByXDY&t=70s)** What this is going to do in the background is going to pull down a container, a Docker container. When you run home assistant OS, which is what I'm doing here, it's a fully encapsulated system.

**[01:19](https://youtube.com/watch?v=vDxmtRByXDY&t=79s)** So all of the stuff that happens that gets installed, all of these add-ons are containers running underneath on the home assistant OS. Once that's downloaded, go ahead and click on Start, and then click on the Open Web UI button.

**[01:32](https://youtube.com/watch?v=vDxmtRByXDY&t=92s)** This is going to ask us to re-authenticate, although technically all we're doing is actually just authenticating. Next is going to follow the standard Tailscale auth procedure. So click on Signing with Google, follow the standard prompts that you're very used to by this point if you use Tailscale before.

**[01:47](https://youtube.com/watch?v=vDxmtRByXDY&t=107s)** And then in the console, we can see right away we've now got home assistant showing up. So that's how easy it is to connect Tailscale with Home Assistant. Now if we go back to the add-on Web UI, we can see that the Home Assistant node is now showing up in the Web UI as well, and it's pretty happy about what's going on here.

**[02:05](https://youtube.com/watch?v=vDxmtRByXDY&t=125s)** So now we have Tailscale installed on Home Assistant. Let's go ahead and try and connect to it. We're going to just jump into a new tab right here and use the fully qualified domain name that gets assigned to Home Assistant when it joins the Tailnet.

**[02:19](https://youtube.com/watch?v=vDxmtRByXDY&t=139s)** By the way, every single Tailnet gets a domain through this DNS option up here. So my tailnet name is Velociraptor-Noodlefish.ts.net. Every Tailnet gets one of these fully qualified domain names for free. You can go ahead and rename yours and roll the dice to come up with your own automatically generated name in the DNS tab over here.

**[02:40](https://youtube.com/watch?v=vDxmtRByXDY&t=160s)** But when a node gets added to the town, it automatically gets a fully qualified domain name that matches the name of the machine and then appends the Velociraptor bit to it. So if I want to actually connect our Home Assistant right now, I still need to use a port.

**[02:54](https://youtube.com/watch?v=vDxmtRByXDY&t=174s)** That's because we haven't enabled Tailscale serve through the proxy yet. But you can see that this works. I'm able to connect to Home Assistant using port 8123 as you would do if you were using a normal IP address.

**[03:05](https://youtube.com/watch?v=vDxmtRByXDY&t=185s)** This is cool, first of all, because this will work from any Tailscale device, whether it's in the same physical network or not. So if you're troubleshooting a remote system or something like that, you can use this option to connect to Tailscale remotely. No proxy is required.

**[03:19](https://youtube.com/watch?v=vDxmtRByXDY&t=199s)** But I want to take this a step further and actually get us a proper TLS certificate. So this is going to be a little more involved, but it's not too bad.

**[03:26](https://youtube.com/watch?v=vDxmtRByXDY&t=206s)** Under Home Assistant, we're going to go ahead now and install another add-on. So I'm going to go ahead and install the Visual Studio Code Server add-on. You can just type the word studio into the search box, click install.

**[03:38](https://youtube.com/watch?v=vDxmtRByXDY&t=218s)** This will take a moment to download the container underneath. It's quite a big one. But what whilst that's doing that, I'm going to go ahead and go back to the Tailscale add-on that we installed earlier and just grab the piece of configuration that we're going to need from the documentation.

**[03:51](https://youtube.com/watch?v=vDxmtRByXDY&t=231s)** So the fastest way to do it is go to the Tailscale add-on in the documentation page, do a command F or control F and search the page for 127.0, and there you go. We just need these four lines of code here.

**[04:04](https://youtube.com/watch?v=vDxmtRByXDY&t=244s)** As you can see, Home Assistant by default blocks connections from untrusted proxies, such as the tailscale proxy. In this case, we're going to add the 127.0.0.1 as a trusted proxy in the list here.

**[04:17](https://youtube.com/watch?v=vDxmtRByXDY&t=257s)** So I'm going to go ahead and copy this to my clipboard and hopefully by this point, the Visual Studio Code extension has downloaded.

**[04:24](https://youtube.com/watch?v=vDxmtRByXDY&t=264s)** I'm going to go ahead and click on start and also show in the sidebar. Once this has started up, just give it a second.

**[04:31](https://youtube.com/watch?v=vDxmtRByXDY&t=271s)** I'm going to click on the menu button on the left hand side, Studio Code Server. And you can see we're basically in Visual Studio Code but in a browser.

**[04:40](https://youtube.com/watch?v=vDxmtRByXDY&t=280s)** And this is running directly on Home Assistant and has access to your configuration files and what have you underneath.

**[04:46](https://youtube.com/watch?v=vDxmtRByXDY&t=286s)** All we need to do is paste those four lines into our configuration.yaml file and restart Home Assistant.

**[04:52](https://youtube.com/watch?v=vDxmtRByXDY&t=292s)** So I've pasted the four lines. I'm going to go to the hamburger menu up here, click save and then settings and restart Home Assistant.

**[05:02](https://youtube.com/watch?v=vDxmtRByXDY&t=302s)** Restarting Home Assistant can take anywhere from a few seconds to a minute or two depending on how many devices you have.

**[05:10](https://youtube.com/watch?v=vDxmtRByXDY&t=310s)** Once Home Assistant is back up and running, we want to go back to the add-on section and under tail scale, we're going to have to go to the configuration tab for the add-on.

**[05:18](https://youtube.com/watch?v=vDxmtRByXDY&t=318s)** Next, click on the show unused optional configuration options and click on tail scale proxy.

**[05:25](https://youtube.com/watch?v=vDxmtRByXDY&t=325s)** This is going to turn on tail scale serve. This is what will automatically generate you a TLS certificate using Let's Encrypt for your tailnet.ts.net

**[05:34](https://youtube.com/watch?v=vDxmtRByXDY&t=334s)** Tailnet name. So if I click on save here, it will take a moment but it's going to restart the tail scale add-on.

**[05:40](https://youtube.com/watch?v=vDxmtRByXDY&t=340s)** And so now I should be able to go to httts.ts.net and it's going to load my entire Home Assistant instance over tail scale with a TLS certificate using the name from my tailnet.

**[05:54](https://youtube.com/watch?v=vDxmtRByXDY&t=354s)** And I can log in just as if I was using the IP address and port number that I was before.

**[05:59](https://youtube.com/watch?v=vDxmtRByXDY&t=359s)** And you can use this name from anywhere on your tailnet.ts. Any device that's connected to your tailnet such as a phone for example, that can now connect to Home Assistant whether you're in the house or whether at the coffee shop or whether you're in Iceland looking at volcanoes doesn't really matter where you are.

**[06:16](https://youtube.com/watch?v=vDxmtRByXDY&t=376s)** I find this particularly useful when I'm in that grey zone just in and around my house just about on Wi-Fi but not quite.

**[06:23](https://youtube.com/watch?v=vDxmtRByXDY&t=383s)** And sometimes I just need my phone to open the garage door or turn off the lights or whatever it is that I forgot to do before I left the house.

**[06:30](https://youtube.com/watch?v=vDxmtRByXDY&t=390s)** And I can now connect using tail scale to my Home Assistant instance whether I'm in the house or not.

**[06:36](https://youtube.com/watch?v=vDxmtRByXDY&t=396s)** So this works well if you want to use the TLS.net entry but what if you already have a fully qualified domain name and a reverse proxy setup that you're happy with?

**[06:44](https://youtube.com/watch?v=vDxmtRByXDY&t=404s)** Well we can actually slot tail scale into that existing setup as well.

**[06:48](https://youtube.com/watch?v=vDxmtRByXDY&t=408s)** In my previous video I showed you how to use caddy and C names in cloud flair to do this.

**[06:53](https://youtube.com/watch?v=vDxmtRByXDY&t=413s)** But today we're going to use a self-contained solution or at least mostly self-contained running all on Home Assistant itself.

**[07:00](https://youtube.com/watch?v=vDxmtRByXDY&t=420s)** So couple of extra add-ons we're going to need here.

**[07:02](https://youtube.com/watch?v=vDxmtRByXDY&t=422s)** First is the Let's Encrypt add-on. So let's get that installed.

**[07:05](https://youtube.com/watch?v=vDxmtRByXDY&t=425s)** And then next is this engine ex Home Assistant SSL proxy add-on.

**[07:10](https://youtube.com/watch?v=vDxmtRByXDY&t=430s)** Now most of you probably watching this section already have this stuff configured but in case you don't.

**[07:15](https://youtube.com/watch?v=vDxmtRByXDY&t=435s)** Let's Encrypt is a way to automatically generate certificates and the tail scale proxy piece, the tail scale serve thing that we did earlier.

**[07:22](https://youtube.com/watch?v=vDxmtRByXDY&t=442s)** This is doing this for you automatically underneath.

**[07:25](https://youtube.com/watch?v=vDxmtRByXDY&t=445s)** This part is only required if you want to use your own domain name.

**[07:28](https://youtube.com/watch?v=vDxmtRByXDY&t=448s)** So Alex is house.com or whatever you want to do now under the Let's Encrypt add-on configuration.

**[07:33](https://youtube.com/watch?v=vDxmtRByXDY&t=453s)** I'm going to click on the three dot menu here.

**[07:36](https://youtube.com/watch?v=vDxmtRByXDY&t=456s)** Now if you're not familiar with how to generate a cloud flair API token head over to your cloud flair dashboard.

**[07:42](https://youtube.com/watch?v=vDxmtRByXDY&t=462s)** Get logged in and click on the my profile option up here in the top right.

**[07:46](https://youtube.com/watch?v=vDxmtRByXDY&t=466s)** And then over here on the left click on API tokens.

**[07:49](https://youtube.com/watch?v=vDxmtRByXDY&t=469s)** And the permissions I generated with this scoped token were zone read zone edit and then DNS edit.

**[07:56](https://youtube.com/watch?v=vDxmtRByXDY&t=476s)** I had some questions about that in the last video.

**[07:58](https://youtube.com/watch?v=vDxmtRByXDY&t=478s)** So I'm going to roll the tokens so I get a fresh token and click on copy.

**[08:03](https://youtube.com/watch?v=vDxmtRByXDY&t=483s)** I'm then going to put this into this box just here under API token.

**[08:09](https://youtube.com/watch?v=vDxmtRByXDY&t=489s)** Click on save.

**[08:10](https://youtube.com/watch?v=vDxmtRByXDY&t=490s)** And now this is worth noting that this specific code snippet, which I'll be a link to in the description by the way.

**[08:16](https://youtube.com/watch?v=vDxmtRByXDY&t=496s)** This specific code snippet will work just fine with cloud flair.

**[08:20](https://youtube.com/watch?v=vDxmtRByXDY&t=500s)** If you're using a different DNS provider for your Acme challenge, your Let's Encrypt challenge,

**[08:24](https://youtube.com/watch?v=vDxmtRByXDY&t=504s)** you will need to modify this code snippet slightly just, you know, you can see it's cloud flair specific stuff here.

**[08:30](https://youtube.com/watch?v=vDxmtRByXDY&t=510s)** You don't have to use cloud flair, but it's just the one that I'm using that I'm the most familiar with.

**[08:34](https://youtube.com/watch?v=vDxmtRByXDY&t=514s)** So let's go back to Let's Encrypt and start this up rolling stone song initiate.

**[08:40](https://youtube.com/watch?v=vDxmtRByXDY&t=520s)** And it's going to generate me a new certificate here.

**[08:43](https://youtube.com/watch?v=vDxmtRByXDY&t=523s)** So it's going to go ahead and request a certificate in real time.

**[08:46](https://youtube.com/watch?v=vDxmtRByXDY&t=526s)** And if we look in the cloud flair dashboard in just a second,

**[08:49](https://youtube.com/watch?v=vDxmtRByXDY&t=529s)** we should actually see under the domain name dots and stuff.dev.

**[08:54](https://youtube.com/watch?v=vDxmtRByXDY&t=534s)** We can actually see the Acme challenge happening in real time.

**[08:57](https://youtube.com/watch?v=vDxmtRByXDY&t=537s)** So this is how Let's Encrypt is verifying ownership of my,

**[09:01](https://youtube.com/watch?v=vDxmtRByXDY&t=541s)** my own ship of HA dot dots and stuff.dev.

**[09:04](https://youtube.com/watch?v=vDxmtRByXDY&t=544s)** It's actually using this token just here.

**[09:08](https://youtube.com/watch?v=vDxmtRByXDY&t=548s)** Now, if we dig into the configuration a little further, I didn't actually point this out.

**[09:12](https://youtube.com/watch?v=vDxmtRByXDY&t=552s)** Did I? The domain name that we're going to register today is HA dot dots and stuff.dev.

**[09:17](https://youtube.com/watch?v=vDxmtRByXDY&t=557s)** And this is what's happening underneath in the Let's Encrypt add on.

**[09:21](https://youtube.com/watch?v=vDxmtRByXDY&t=561s)** And now we have a Let's Encrypt certificate ready to go for this domain name.

**[09:25](https://youtube.com/watch?v=vDxmtRByXDY&t=565s)** Next thing we're going to want to do is configure DNS.

**[09:28](https://youtube.com/watch?v=vDxmtRByXDY&t=568s)** Now I'm going to presume most of you probably have some kind of a local DNS server

**[09:32](https://youtube.com/watch?v=vDxmtRByXDY&t=572s)** pie hole or something like that running in your network.

**[09:35](https://youtube.com/watch?v=vDxmtRByXDY&t=575s)** If you don't though, you can actually use the tail scale split DNS feature

**[09:39](https://youtube.com/watch?v=vDxmtRByXDY&t=579s)** for specific name service. I'm going to go ahead and click on custom just here.

**[09:43](https://youtube.com/watch?v=vDxmtRByXDY&t=583s)** And do the IP address of the actual home assistant instance itself.

**[09:48](https://youtube.com/watch?v=vDxmtRByXDY&t=588s)** So in this case, I'm going to go to settings system network.

**[09:53](https://youtube.com/watch?v=vDxmtRByXDY&t=593s)** Click on the three dot menu here and click on IP information.

**[09:56](https://youtube.com/watch?v=vDxmtRByXDY&t=596s)** Why is that not just shown at the bottom of the page?

**[09:59](https://youtube.com/watch?v=vDxmtRByXDY&t=599s)** Anyway, I digress 192, 168, 101 dot 11.

**[10:04](https://youtube.com/watch?v=vDxmtRByXDY&t=604s)** This is the value that we need.

**[10:06](https://youtube.com/watch?v=vDxmtRByXDY&t=606s)** I'm going to go and put this in here and then click on split DNS.

**[10:09](https://youtube.com/watch?v=vDxmtRByXDY&t=609s)** This is the magic source.

**[10:11](https://youtube.com/watch?v=vDxmtRByXDY&t=611s)** If I click on HA dot dots and stuff.dev, put this in here.

**[10:15](https://youtube.com/watch?v=vDxmtRByXDY&t=615s)** Anytime I make a request when I'm connected to my tail net,

**[10:18](https://youtube.com/watch?v=vDxmtRByXDY&t=618s)** the DNS server that gets configured as part of your tail scale network,

**[10:22](https://youtube.com/watch?v=vDxmtRByXDY&t=622s)** will automatically root requests to that IP address.

**[10:26](https://youtube.com/watch?v=vDxmtRByXDY&t=626s)** Now, the keynote amongst you will have noticed that 192, 168 is not a tail scale address.

**[10:32](https://youtube.com/watch?v=vDxmtRByXDY&t=632s)** We're going to have to enable the subnet routing feature on our home assistant box to do this.

**[10:37](https://youtube.com/watch?v=vDxmtRByXDY&t=637s)** Now, thankfully, the add-on already requests subnet routing and exit node features out of the box.

**[10:43](https://youtube.com/watch?v=vDxmtRByXDY&t=643s)** If you want to tweak that, by the way, you can do that.

**[10:46](https://youtube.com/watch?v=vDxmtRByXDY&t=646s)** If you go into the add-ons configuration section over here and then show unused options.

**[10:50](https://youtube.com/watch?v=vDxmtRByXDY&t=650s)** There's a bunch of stuff, you know, you can configure funnel.

**[10:53](https://youtube.com/watch?v=vDxmtRByXDY&t=653s)** If you want to expose this to the internet without any of this stuff,

**[10:56](https://youtube.com/watch?v=vDxmtRByXDY&t=656s)** I really wouldn't recommend exposing your home assistant instance to the wider internet, by the way.

**[11:02](https://youtube.com/watch?v=vDxmtRByXDY&t=662s)** There's just no need with tail scale.

**[11:04](https://youtube.com/watch?v=vDxmtRByXDY&t=664s)** There are a bunch of other options, like I say in here.

**[11:06](https://youtube.com/watch?v=vDxmtRByXDY&t=666s)** We already enabled the tail scale proxy earlier,

**[11:08](https://youtube.com/watch?v=vDxmtRByXDY&t=668s)** but this is where you would configure all sorts of other stuff like accepting routes

**[11:11](https://youtube.com/watch?v=vDxmtRByXDY&t=671s)** and advertising an exit node and advertising the subnet routes.

**[11:15](https://youtube.com/watch?v=vDxmtRByXDY&t=675s)** But by default, the add-on actually requests the home assistant subnet that it's in.

**[11:19](https://youtube.com/watch?v=vDxmtRByXDY&t=679s)** So we can see here in the tail scale dashboard,

**[11:22](https://youtube.com/watch?v=vDxmtRByXDY&t=682s)** if I click on the three dot menu here, edit route settings,

**[11:25](https://youtube.com/watch?v=vDxmtRByXDY&t=685s)** it's asking to route the subnet 101.0 anyway.

**[11:29](https://youtube.com/watch?v=vDxmtRByXDY&t=689s)** So if I go ahead and click on save, what this is going to allow us to do

**[11:32](https://youtube.com/watch?v=vDxmtRByXDY&t=692s)** is actually connect to the home assistant front end from anywhere else on our tail net.

**[11:37](https://youtube.com/watch?v=vDxmtRByXDY&t=697s)** Word of caution, this will also enable us to connect to any other device on that subnet.

**[11:42](https://youtube.com/watch?v=vDxmtRByXDY&t=702s)** So just be aware there are a couple of security implications there.

**[11:45](https://youtube.com/watch?v=vDxmtRByXDY&t=705s)** And then the final thing that we're going to need to do

**[11:47](https://youtube.com/watch?v=vDxmtRByXDY&t=707s)** is we go ahead and configure our engine X proxy.

**[11:50](https://youtube.com/watch?v=vDxmtRByXDY&t=710s)** Now, under the configuration tab, it's here.

**[11:53](https://youtube.com/watch?v=vDxmtRByXDY&t=713s)** We're going to need to put in h a dot dots and stuff dot dev and click on save.

**[11:58](https://youtube.com/watch?v=vDxmtRByXDY&t=718s)** We are going to need to add this engine X proxy to our home assistant configuration as well

**[12:03](https://youtube.com/watch?v=vDxmtRByXDY&t=723s)** as another trusted proxy.

**[12:05](https://youtube.com/watch?v=vDxmtRByXDY&t=725s)** This is exactly the same as we did in the previous step for the tail scale proxy.

**[12:08](https://youtube.com/watch?v=vDxmtRByXDY&t=728s)** I'm just going to paste this into my configuration dot yaml,

**[12:11](https://youtube.com/watch?v=vDxmtRByXDY&t=731s)** save this file,

**[12:13](https://youtube.com/watch?v=vDxmtRByXDY&t=733s)** and then restart home assistant.

**[12:16](https://youtube.com/watch?v=vDxmtRByXDY&t=736s)** Once that's done, I'm going to go ahead and go back to the add-ons page.

**[12:19](https://youtube.com/watch?v=vDxmtRByXDY&t=739s)** Make sure start on boot is checked.

**[12:21](https://youtube.com/watch?v=vDxmtRByXDY&t=741s)** I'm also going to do the watchdog so that if it crashes, it comes back up again.

**[12:25](https://youtube.com/watch?v=vDxmtRByXDY&t=745s)** And then click on start and hopefully now if I go to h a dot dots and stuff dot dev.

**[12:36](https://youtube.com/watch?v=vDxmtRByXDY&t=756s)** We get the home assistant web page.

**[12:38](https://youtube.com/watch?v=vDxmtRByXDY&t=758s)** Gosh, that was an excruciatingly long pause as it loaded there.

**[12:42](https://youtube.com/watch?v=vDxmtRByXDY&t=762s)** And there we go.

**[12:43](https://youtube.com/watch?v=vDxmtRByXDY&t=763s)** So what's happened here?

**[12:44](https://youtube.com/watch?v=vDxmtRByXDY&t=764s)** We are connected through the engine X reverse proxy running on home assistant

**[12:49](https://youtube.com/watch?v=vDxmtRByXDY&t=769s)** using the subnet routing functionality of tail scale to route the packets

**[12:53](https://youtube.com/watch?v=vDxmtRByXDY&t=773s)** from a tail scale connected device, such as this laptop,

**[12:57](https://youtube.com/watch?v=vDxmtRByXDY&t=777s)** over your tailnet to home assistant using a custom domain.

**[13:02](https://youtube.com/watch?v=vDxmtRByXDY&t=782s)** And we are also using one of the more advanced features of tail scale

**[13:05](https://youtube.com/watch?v=vDxmtRByXDY&t=785s)** under the DNS section called split DNS.

**[13:08](https://youtube.com/watch?v=vDxmtRByXDY&t=788s)** And you can actually use this pretty much as a hack to use tail scale

**[13:11](https://youtube.com/watch?v=vDxmtRByXDY&t=791s)** as a fully fledged DNS server if you'd like and use split DNS across multiple different systems.

**[13:17](https://youtube.com/watch?v=vDxmtRByXDY&t=797s)** Now, it is worth noting at this point that the home assistant project also

**[13:20](https://youtube.com/watch?v=vDxmtRByXDY&t=800s)** through their nebukhasa project offers a subscription.

**[13:23](https://youtube.com/watch?v=vDxmtRByXDY&t=803s)** I think it's $6 a month to give you a cloud very long obfuscated URL

**[13:30](https://youtube.com/watch?v=vDxmtRByXDY&t=810s)** that is publicly routable across the public internet.

**[13:33](https://youtube.com/watch?v=vDxmtRByXDY&t=813s)** Now, I personally don't use the URL option.

**[13:35](https://youtube.com/watch?v=vDxmtRByXDY&t=815s)** I just route everything over tail scale, but I do support the home assistant project

**[13:39](https://youtube.com/watch?v=vDxmtRByXDY&t=819s)** because I just think it's such a critical piece of infrastructure in our modern smart homes.

**[13:44](https://youtube.com/watch?v=vDxmtRByXDY&t=824s)** So if you'd like to know more about self hosting services and remotely accessing them over tail scale,

**[13:48](https://youtube.com/watch?v=vDxmtRByXDY&t=828s)** there'll be a video on screen somewhere right about now.

**[13:51](https://youtube.com/watch?v=vDxmtRByXDY&t=831s)** I did a video on it a couple of weeks ago using Caddy as a reverse proxy

**[13:55](https://youtube.com/watch?v=vDxmtRByXDY&t=835s)** and using CloudFlare with a C name to do just that.

**[13:58](https://youtube.com/watch?v=vDxmtRByXDY&t=838s)** So thank you so much for watching.

**[14:00](https://youtube.com/watch?v=vDxmtRByXDY&t=840s)** I hope you found some utility in today's video.

**[14:02](https://youtube.com/watch?v=vDxmtRByXDY&t=842s)** Go ahead and support the home assistant project.

**[14:04](https://youtube.com/watch?v=vDxmtRByXDY&t=844s)** It's just a fantastic piece of software.

**[14:06](https://youtube.com/watch?v=vDxmtRByXDY&t=846s)** Until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
