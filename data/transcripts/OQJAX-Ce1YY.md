---
video_id: "OQJAX-Ce1YY"
title: "Static site deployments made easy with Github Actions and Tailscale"
description: "In today's video we'll examine deploying a static website built using the 11ty.dev framework (eleventy) and deployed onto a DigitalOcean droplet using Tailscale SSH as part of your GitHub Actions work..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-03-27"
duration_seconds: 971
youtube_url: "https://www.youtube.com/watch?v=OQJAX-Ce1YY"
thumbnail_url: "https://i.ytimg.com/vi_webp/OQJAX-Ce1YY/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:22:12.644899"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3048
transcription_time_seconds: 26.7
---

# Static site deployments made easy with Github Actions and Tailscale

**[00:00](https://youtube.com/watch?v=OQJAX-Ce1YY&t=0s)** So you are looking right now at an Easter egg. I don't know if it's taboo to talk about Easter eggs out loud but like this has been in public. This has been in plain sight in the public for about a year now since we relaunched our website last year. So on Tailscale.com you will notice that all of our little marketing pictures have tail and scales.com. That's a real website. That is a statically generated self-hosted website that runs on a digital ocean draw.

**[00:30](https://youtube.com/watch?v=OQJAX-Ce1YY&t=30s)** That's part of my work tailnet. And so what this does is it's a static site that gets built as part of a GitHub Action workflow. When the site gets built it gets deployed using Tailscale running inside the GitHub Action environment across my tailnet to the droplet and then deploys the changes to the website.

**[00:50](https://youtube.com/watch?v=OQJAX-Ce1YY&t=50s)** Now this website I threw it together in an afternoon. It's far from perfect. There is a couple of issues. First of all, if I click on the blog link, you can see that the reverse proxy tries to inject port 8080 as one of those it worked on my machines but it didn't doesn't work in production type situations. It does work if I remove the 8080. So I know the underlying blog code itself is fine.

**[01:14](https://youtube.com/watch?v=OQJAX-Ce1YY&t=74s)** But when we actually resize this window as well, if you notice the footer. It's not doing the right thing. It's overlapping and the headers disappeared off the top of the page too. So a couple of viewport things when I'm resizing that I want to fix as well as this blog link up here.

**[01:30](https://youtube.com/watch?v=OQJAX-Ce1YY&t=90s)** Now I've got a pull request. All of this code is open source by the way and there'll be a link in the description down below.

**[01:36](https://youtube.com/watch?v=OQJAX-Ce1YY&t=96s)** Tailscale, hyphen, dev and then the society of pangolin enthusiasts. As we say here, what else has both a tail and scales a bangle in.

**[01:46](https://youtube.com/watch?v=OQJAX-Ce1YY&t=106s)** Okay, so I have a pull request here. Nothing too crazy actually. Just a few changes to some of the classes and the dives to try and fix the overlaps. At least I hope this is going to work.

**[01:58](https://youtube.com/watch?v=OQJAX-Ce1YY&t=118s)** So I'm going to merge this pull request and I want to sort of try in real time assuming it works because I haven't tested it. Nothing like testing in production or live on a video.

**[02:08](https://youtube.com/watch?v=OQJAX-Ce1YY&t=128s)** I'm going to merge this pull request right now and then if I jump into the actions portion of this repo, we could take a look at what happens.

**[02:17](https://youtube.com/watch?v=OQJAX-Ce1YY&t=137s)** Now a GitHub action is it's a CI thing, so continuous integration. But I also like the continuous deployment aspect of CI CD. So we do the CI, the integration, the build that happens on GitHub.

**[02:32](https://youtube.com/watch?v=OQJAX-Ce1YY&t=152s)** So GitHub spins up a virtual machine in the cloud. And as long as our repo is open source, I believe we get pretty much free usage of these runners. There might be a limit. I'm not sure.

**[02:45](https://youtube.com/watch?v=OQJAX-Ce1YY&t=165s)** But essentially what happens is that VM builds our website builds our and builds a container. It then pushes that container to a GitHub registry of Docker registry that GitHub host that is associated with your GitHub repo.

**[02:59](https://youtube.com/watch?v=OQJAX-Ce1YY&t=179s)** Then we connect the GitHub run environment to our tail net temporarily. It's an ephemeral node. Once it's connected to tail scale. And that's the fact that's what's happening right here.

**[03:10](https://youtube.com/watch?v=OQJAX-Ce1YY&t=190s)** Once it's connected to our tail net, it then SSH is in using tail scale SSH is known as SSH keys or secrets or anything like that for remote access. It SSH is in over my tail net to the digital ocean droplet and then deploys the new version of the website. And then it cleans up after itself.

**[03:28](https://youtube.com/watch?v=OQJAX-Ce1YY&t=208s)** So that's what's just happened in real time as I was explaining. And now if we go back to the Pangolin enthusiast website and refresh. Well, first of all, we can see that the header appears to have been fixed and the footer is now actually sat at the bottom.

**[03:42](https://youtube.com/watch?v=OQJAX-Ce1YY&t=222s)** So if I, yeah, there we go. If I resize it, the footer doesn't overlap anymore. And neither does the header. Fantastic. I might have a future as a web developer. Who knows.

**[03:53](https://youtube.com/watch?v=OQJAX-Ce1YY&t=233s)** I definitely don't. I am not a very good web developer. But anyway, this website is built using the 11 tea static site generation framework. And what a static site does is it takes a bunch of inputs. So a bunch of human readable files. Let's take a look at the route of the repo for a second.

**[04:11](https://youtube.com/watch?v=OQJAX-Ce1YY&t=251s)** It takes a bunch of human readable files and spits out a directory of HTML. And it's that directory of HTML that we then inject into the Docker container as part of the build and then host that as a website, a static website.

**[04:25](https://youtube.com/watch?v=OQJAX-Ce1YY&t=265s)** That's what that's what the phrase static website means. It's not doing any database lookups. It's not doing any dynamic lookups of any resources. It creates a static directory full of website stuff. So it's a static site. Hopefully that makes sense.

**[04:42](https://youtube.com/watch?v=OQJAX-Ce1YY&t=282s)** So what we're doing with 11 tea is that there's a bunch of files. For example, 11 tea.js has a bunch of stuff in it. And to be honest, there's a lot of stuff in here that you don't really need to understand. The 11 tea website, by the way, at 11 T Y dot dev will be linked in the description down below, of course.

**[04:59](https://youtube.com/watch?v=OQJAX-Ce1YY&t=299s)** And they have a really good quick start that sort of talks you through the basics of getting started with 11 tea. There are lots of other static site frameworks out there. I think Zola's one Hugo's definitely a very popular one.

**[05:10](https://youtube.com/watch?v=OQJAX-Ce1YY&t=310s)** Jekyll used to be popular. I'm not sure if it still is, but it certainly used to be a few years ago, because you could host that as part of a GitHub pages workflow with built into your GitHub repo.

**[05:20](https://youtube.com/watch?v=OQJAX-Ce1YY&t=320s)** I prefer to self host on a VPS that I can try just for that little modicum more control. And as you can see, that's all good. Now we have one more thing left to fix, which is the blog link that's still broken. And that's because that's in my reverse proxy configuration.

**[05:35](https://youtube.com/watch?v=OQJAX-Ce1YY&t=335s)** So not only are we able to deploy the website or also able to make changes to the configuration of the website underneath as well.

**[05:43](https://youtube.com/watch?v=OQJAX-Ce1YY&t=343s)** So if we jump into the code for this site and look in the nginx.conf file for local host, I believe all I need to do here is just make an underscore.

**[05:53](https://youtube.com/watch?v=OQJAX-Ce1YY&t=353s)** And I'm going to, well, first of all, I'm going to pull my changes before I save so that I don't have to do anything with Git there. And I'm just going to save this change.

**[06:01](https://youtube.com/watch?v=OQJAX-Ce1YY&t=361s)** Now the Docker container that gets built is just based on top of nginx. So literally all we are doing in our Docker build is copying in the nginx config so that we know what ports to tell nginx to proxy for us and then copying in the static site directory.

**[06:16](https://youtube.com/watch?v=OQJAX-Ce1YY&t=376s)** That's it. Simple as that, probably the probably the simplest docker file you will ever see.

**[06:21](https://youtube.com/watch?v=OQJAX-Ce1YY&t=381s)** So I'm going to go ahead and just commit this to master because yolo why not I'm going to say fixes blog link hopefully and then push that to GitHub.

**[06:33](https://youtube.com/watch?v=OQJAX-Ce1YY&t=393s)** Now in the background, of course, it's going to repeat the same CI process with the with the GitHub action.

**[06:40](https://youtube.com/watch?v=OQJAX-Ce1YY&t=400s)** You can see the workflow is now running in the background. So let's take whilst that's running because that will take a couple of minutes as we saw last time whilst that's running.

**[06:47](https://youtube.com/watch?v=OQJAX-Ce1YY&t=407s)** Let's look at how we actually configure a GitHub workflow. Now you need to put in the route of your GitHub repo a file in in a couple of directories deep.

**[06:56](https://youtube.com/watch?v=OQJAX-Ce1YY&t=416s)** So dot GitHub workflows and then you can call it whatever you like and you can again name it here. So that name here refers to the name you'll see in the GitHub UI over here.

**[07:06](https://youtube.com/watch?v=OQJAX-Ce1YY&t=426s)** Now a couple of things to look at this workflow will run when certain events are triggered.

**[07:12](https://youtube.com/watch?v=OQJAX-Ce1YY&t=432s)** First of all, we've got workflow dispatch and what this does is it gives me an option. I believe somewhere in here if I go into CI to manually run.

**[07:22](https://youtube.com/watch?v=OQJAX-Ce1YY&t=442s)** There we go, manually run the workflow because I have the workflow dispatch trigger this can be handy at the beginning when you're testing things out to start with.

**[07:32](https://youtube.com/watch?v=OQJAX-Ce1YY&t=452s)** And then secondly, we want to be able to have this workflow run automatically when certain branches receive a push for the most part.

**[07:40](https://youtube.com/watch?v=OQJAX-Ce1YY&t=460s)** This is probably going to be main or master. Obviously, this is an older repo. So it's still called master. And then underneath this is where the magic kind of happens.

**[07:47](https://youtube.com/watch?v=OQJAX-Ce1YY&t=467s)** This is where all of the jobs get configured. Let me clear the screen a bit. And under here, you can see there are several steps that happen.

**[07:55](https://youtube.com/watch?v=OQJAX-Ce1YY&t=475s)** First of all, we're giving this CI job access to right to the GitHub container registry that belongs to the repo.

**[08:03](https://youtube.com/watch?v=OQJAX-Ce1YY&t=483s)** Without the permissions packages right, Stanzer, we wouldn't be able to push a container to our own Docker repo.

**[08:10](https://youtube.com/watch?v=OQJAX-Ce1YY&t=490s)** So make sure you've got that if you're going to do a Docker thing.

**[08:13](https://youtube.com/watch?v=OQJAX-Ce1YY&t=493s)** Next, we're going to check out the repo and these steps are all executed inside of an Ubuntu virtual machine running on GitHub's infrastructure.

**[08:21](https://youtube.com/watch?v=OQJAX-Ce1YY&t=501s)** So we're going to check out the code master same as you type in get checkout or get clone whatever. And then you can see we're going to set up our node environment with version 21.

**[08:29](https://youtube.com/watch?v=OQJAX-Ce1YY&t=509s)** Run a couple of steps NPM install MPN run build. And then we've got some Docker build stuff happening here.

**[08:35](https://youtube.com/watch?v=OQJAX-Ce1YY&t=515s)** So build X and QMU actions because we're building inside of a virtual machine.

**[08:39](https://youtube.com/watch?v=OQJAX-Ce1YY&t=519s)** And then the next step is where we actually push our container to the GitHub registry.

**[08:43](https://youtube.com/watch?v=OQJAX-Ce1YY&t=523s)** This GitHub token is an interesting secret. If you're running inside the context of a GitHub action environment,

**[08:51](https://youtube.com/watch?v=OQJAX-Ce1YY&t=531s)** the GitHub run environment will provide this GitHub token to you as an environment variable automatically as part of the context of that environment.

**[09:00](https://youtube.com/watch?v=OQJAX-Ce1YY&t=540s)** And so you can use that token as the secret or the password to let you push to the Docker registry that's built into your GitHub repo.

**[09:09](https://youtube.com/watch?v=OQJAX-Ce1YY&t=549s)** You can see that I've tagged this specific image as tail scale dev and then the society of pangolin enthusiasts.

**[09:17](https://youtube.com/watch?v=OQJAX-Ce1YY&t=557s)** Now, this is where tail scale gets involved. Obviously, this is where I earn my bread and butter right here.

**[09:22](https://youtube.com/watch?v=OQJAX-Ce1YY&t=562s)** So we've got the TS OAuth client ID and the TS OAuth secret. Now, where do they live and where do you configure those things?

**[09:30](https://youtube.com/watch?v=OQJAX-Ce1YY&t=570s)** Well, first of all, they live inside your Git repo under settings. And then on the left hand side over here, you've got secrets and variables and then under actions.

**[09:38](https://youtube.com/watch?v=OQJAX-Ce1YY&t=578s)** This is where you create those variables. On the tail scale side, you need to go to tailscale.com and your admin console.

**[09:46](https://youtube.com/watch?v=OQJAX-Ce1YY&t=586s)** You will then go to settings and then under keys, my mistake, under OAuth clients, you will generate a specific token here that has the scopes and permissions that you need.

**[09:57](https://youtube.com/watch?v=OQJAX-Ce1YY&t=597s)** Now, one of the things you might notice here is that we have to assign a tag to an OAuth client.

**[10:03](https://youtube.com/watch?v=OQJAX-Ce1YY&t=603s)** And that's because an OAuth client is simply generating an auth key underneath because an auth key is authenticating the GitHub runner environment as a specific, it's like a service account, if you want to think of it like that.

**[10:16](https://youtube.com/watch?v=OQJAX-Ce1YY&t=616s)** So typically, if I was the one authenticating the GitHub runner by sitting at the command line and typing in the codes, then it would be authenticated as me as a user.

**[10:26](https://youtube.com/watch?v=OQJAX-Ce1YY&t=626s)** But in this environment, we want it to run automatically in the background. So we need to give it a tag owner or a tag that owns the key that gets created.

**[10:36](https://youtube.com/watch?v=OQJAX-Ce1YY&t=636s)** And so in my case, I've created a tag here called DevRel-ci. And that gets defined simply in my ACLs over here. And then if I scroll down, you can see the ssh allows me to ssh from a DevRel-ci tagged node into a DevRel-prod tagged node.

**[10:54](https://youtube.com/watch?v=OQJAX-Ce1YY&t=654s)** And that's all that does in the background. Now, when I'm going to rerun the GitHub action manually in a second, you can see I've got my tag here of DevRel-prod.

**[11:03](https://youtube.com/watch?v=OQJAX-Ce1YY&t=663s)** Let me just go back to the actions and run this manually once more using my workflow dispatch. See, it can be useful sometimes.

**[11:12](https://youtube.com/watch?v=OQJAX-Ce1YY&t=672s)** And then what we'll do is we'll just wait for the tail scale stage to begin. All right. So it's now connecting to tail scale. So in the background, we should see an ephemeral node has appeared.

**[11:22](https://youtube.com/watch?v=OQJAX-Ce1YY&t=682s)** And this has the tag of DevRel-ci. And remember, that's because it was authenticated using the OAuth secret that was creating an auth key under the covers, which allows tail scale ssh to allow this GitHub runner environment to ssh over the internet and let it in through the front door on the DevRel-prod box.

**[11:43](https://youtube.com/watch?v=OQJAX-Ce1YY&t=703s)** And so if I wanted to go in now and check whether my blog link is fixed or not, my CI has worked. It's done the trick. So I made a couple of changes to the engine X config underneath CI ran. I didn't have to log into anything.

**[11:55](https://youtube.com/watch?v=OQJAX-Ce1YY&t=715s)** Literally all I had to do was push my change to the master branch. And then the CI CID pipeline took care of everything else.

**[12:05](https://youtube.com/watch?v=OQJAX-Ce1YY&t=725s)** It's so easy to deploy stuff this way using tail scale as part of the process. Remember it handles the ssh connections for you. So you don't need to worry about ssh keys and storing those as secrets.

**[12:16](https://youtube.com/watch?v=OQJAX-Ce1YY&t=736s)** You don't really even have to worry too much about identity and that kind of stuff either because it's all handled using the tagging that's part of your tail scale ACLs just automatically built into tail scale.

**[12:28](https://youtube.com/watch?v=OQJAX-Ce1YY&t=748s)** Now the the only thing that I haven't shown you really is how to set up the cloud box portion of this and there really isn't a whole bunch to it.

**[12:35](https://youtube.com/watch?v=OQJAX-Ce1YY&t=755s)** So if I ssh now into that droplet and just show you that you know this is running Docker compose PS.

**[12:42](https://youtube.com/watch?v=OQJAX-Ce1YY&t=762s)** This is running tail and scales dot com. It's just got a traffic reverse proxy in front of it. Yes, I know I could do engine X itself because it's just I like having the separation of the two.

**[12:54](https://youtube.com/watch?v=OQJAX-Ce1YY&t=774s)** So what we've got here is just a simple container running traffic but the node itself is what gets ssh into to make the deploy. So in the root of the user's home folder here I have a Docker compose YAML file which just contains the very basic stuff needed to deploy the website.

**[13:12](https://youtube.com/watch?v=OQJAX-Ce1YY&t=792s)** That doesn't really involve tail scale too much. What does involve tail scale though is the fact that this node is on my tail net and as you can see here.

**[13:21](https://youtube.com/watch?v=OQJAX-Ce1YY&t=801s)** I can do tail scale ping ball trick which is going to ping from digital ocean punch through my residential firewall to this laptop on my desk in front of me.

**[13:30](https://youtube.com/watch?v=OQJAX-Ce1YY&t=810s)** And you can see that I've got a palm is direct connection immediately. And that's what happens from GitHub to it makes a direct connection from inside the GitHub runner environment via tail scale ssh punches through any of the firewalls that are in the way between GitHub and digital ocean in this case.

**[13:46](https://youtube.com/watch?v=OQJAX-Ce1YY&t=826s)** And makes a direct connection so it's really fast and performant. So the only thing you have to make sure is configured on this box is to make sure it's tagged and you don't do that here.

**[13:56](https://youtube.com/watch?v=OQJAX-Ce1YY&t=836s)** You do that in the tail scale admin console. So you go to the three dot menu tail scale dot com get logged in blah blah blah.

**[14:02](https://youtube.com/watch?v=OQJAX-Ce1YY&t=842s)** And then you go to edit ACL tags just here and all you do simply is just make sure that you have the correct tag for the specific node type to match your ACL rule I showed you earlier in order for ssh to be permissible from one domain one environment to the other.

**[14:19](https://youtube.com/watch?v=OQJAX-Ce1YY&t=859s)** And that's the basics of hosting a self hosted blog with tail scale running inside your GitHub CI action environment runner situation, you know, continuously integrate all of the things.

**[14:33](https://youtube.com/watch?v=OQJAX-Ce1YY&t=873s)** Oh, I should also make sure that you've got tail scale ssh turned on for this node as well by doing a tail scale set dash dash ssh how smooth was that Alex there you go.

**[14:45](https://youtube.com/watch?v=OQJAX-Ce1YY&t=885s)** But that was that's how you would make sure that this node is accepting incoming tail scale ssh connections from the GitHub side.

**[14:52](https://youtube.com/watch?v=OQJAX-Ce1YY&t=892s)** I think that covers us for today. What have we done just a quick recap. We have created a very silly website at tail and scales dot com, which I hope somebody is going to submit a pull request for me to fix the alignment of my sp header up here.

**[15:09](https://youtube.com/watch?v=OQJAX-Ce1YY&t=909s)** Maybe make it any even better website. I don't know like I said, I'm not much of a web dev, but we've we've deployed this website now tail and scales dot com we have a CI environment configured using GitHub runners and GitHub actions.

**[15:22](https://youtube.com/watch?v=OQJAX-Ce1YY&t=922s)** So let me just show you that one more time going back to the route of our repository and we're going to dot GitHub slash workflows and then under the bill dot YAML file.

**[15:32](https://youtube.com/watch?v=OQJAX-Ce1YY&t=932s)** These are the steps that we use to build and deploy the container that is actually running the website itself.

**[15:40](https://youtube.com/watch?v=OQJAX-Ce1YY&t=940s)** And so in this way, we can programmatically control every step of our deployment process using tail scale at the heart of the solution.

**[15:48](https://youtube.com/watch?v=OQJAX-Ce1YY&t=948s)** So thank you very much for watching. Keep an eye on the channel, get subscribed and all that good stuff. Until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
