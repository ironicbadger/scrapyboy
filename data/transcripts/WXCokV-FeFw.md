---
video_id: "WXCokV-FeFw"
title: "Turbocharge Your DevOps Workflow with GitHub Actions and Tailscale SSH"
description: "Join us on a journey to simplify your DevOps GitHub Actions SSH based workflow. If you've struggled with rotating secrets and managing SSH keys, this should be useful for you. We explore how Tailscale..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-08-30"
duration_seconds: 881
youtube_url: "https://www.youtube.com/watch?v=WXCokV-FeFw"
thumbnail_url: "https://i.ytimg.com/vi/WXCokV-FeFw/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:07:20.825965"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2725
transcription_time_seconds: 25.0
---

# Turbocharge Your DevOps Workflow with GitHub Actions and Tailscale SSH

**[00:00](https://youtube.com/watch?v=WXCokV-FeFw&t=0s)** If you've been using SSH as part of your GitHub Action workflows, then you'll know the pain of storing secrets. SSH keys, opening ports in remote firewalls, and dealing with the security aspects of storing secrets, can be a bit of a pain. So, in today's video, I wanted to show you how I'm using Tailscale as an integral part of a brand new GitHub Action workflow I've put together for PerfectMediaServer.com. We'll cover how to add a GitHub Action runner to your Tailnet, and also how our ACLs can be used to limit access

**[00:30](https://youtube.com/watch?v=WXCokV-FeFw&t=30s)** to certain resources based on their tags. Now, at this point, you might be asking yourself, just what is a GitHub Action? Well, it's an automated workflow system that can be set up to respond to events in a GitHub repository, workflow such as building an app or checking for errors in formatting, or maybe even deploying a website via SSH. These workflows are triggered by events such as code pushes, or pull requests being opened. For example, let's say you have a GitHub repository for a web application, and you'd like to automatically run tests

**[01:00](https://youtube.com/watch?v=WXCokV-FeFw&t=60s)** and deploy the application to a server every time new code is pushed to the main branch. You can create a GitHub Action workflow that accomplishes this by defining the necessary steps and triggers in a YAML file.

**[01:13](https://youtube.com/watch?v=WXCokV-FeFw&t=73s)** Tailscale is a mesh VPN solution built on top of the wireguard protocol. Enjoy a flat network between all of your resources, no matter if they're behind carrier grade, NAT, running in the cloud, or even under your desk.

**[01:25](https://youtube.com/watch?v=WXCokV-FeFw&t=85s)** You can check it out at tailscale.com and say goodbye to opening firewall ports and rotating SSH keys for good. Go grab yourself a free personal plan for up to three users and a hundred devices at tailscale.com.

**[01:37](https://youtube.com/watch?v=WXCokV-FeFw&t=97s)** So without something I could GitHub Action to do things automatically for me, I need to do things manually, which involves SSHing into a node by hand, and then changing to the correct directory, which I think is this one.

**[01:50](https://youtube.com/watch?v=WXCokV-FeFw&t=110s)** And then I'd need to go in and do the Git pull by myself. There we go, and then I'd need to do the build manually.

**[01:58](https://youtube.com/watch?v=WXCokV-FeFw&t=118s)** That doesn't sound like a big deal, but this means a few things. It means I've got to be able to have SSH access from my local system directly to a production machine, which is not the most secure way to live your life.

**[02:11](https://youtube.com/watch?v=WXCokV-FeFw&t=131s)** Also, it means I've got to physically be around to do it, whereas if somebody submits a pull request to the website, for example, and I just merge it from my phone, the GitHub Action runs in the background and does it all for me.

**[02:22](https://youtube.com/watch?v=WXCokV-FeFw&t=142s)** So let's just look at that one more time. Let's say I wanted to merge a pull request, for example, which fixes a typo in a link, this particular one, for example, by user Bradley is quite nice.

**[02:33](https://youtube.com/watch?v=WXCokV-FeFw&t=153s)** They've changed a couple of files here and fixed a link, which has got an extra bracket in it for some reason.

**[02:39](https://youtube.com/watch?v=WXCokV-FeFw&t=159s)** Now, at the moment, I've manually disabled the GitHub workflow from running. So I'm just going to turn this back on again, enable the workflow, and then go back into my pull requests, click on the pull request, and think, yeah, I think I'll go ahead and merge this one.

**[02:55](https://youtube.com/watch?v=WXCokV-FeFw&t=175s)** And so what happens now is the GitHub Action picks up that a merge has been made to the mainline branch, and starts running the automation to deploy the website.

**[03:06](https://youtube.com/watch?v=WXCokV-FeFw&t=186s)** So it connects the GitHub runner to my tailnet, and then it does the deployment of the website, all completely automatically.

**[03:14](https://youtube.com/watch?v=WXCokV-FeFw&t=194s)** And so what we start off with is just the Ubuntu runner, which is running on GitHub. We give it the tag of CI.

**[03:21](https://youtube.com/watch?v=WXCokV-FeFw&t=201s)** Next, we add into the picture, the cloud VPS running on linode, which has a tag of prod.

**[03:28](https://youtube.com/watch?v=WXCokV-FeFw&t=208s)** We connect the two together using SSH. And then finally, when we want to do the build of our website, we actually introduce GitT into the equation, which is hosting a remote Docker registry, which the build on the linode cloud VPS pulls in some dependencies from.

**[03:43](https://youtube.com/watch?v=WXCokV-FeFw&t=223s)** Now you might notice there's a little bit of firewalling, a little bit of nut punching going on here, some DNS resolution.

**[03:50](https://youtube.com/watch?v=WXCokV-FeFw&t=230s)** I mean, for example, the only place in the world, the URL for that GitT server lives, is on the DNS server in my basement.

**[03:57](https://youtube.com/watch?v=WXCokV-FeFw&t=237s)** So we're using the split DNS features built into tailscaled as well as part of this whole exercise.

**[04:03](https://youtube.com/watch?v=WXCokV-FeFw&t=243s)** But I just wanted to start your creative juices flowing as to the various possibilities are now open to you when everything is on a flat network.

**[04:12](https://youtube.com/watch?v=WXCokV-FeFw&t=252s)** The very first thing that we need to configure as part of any GitHub action run is when the action is set to trigger.

**[04:19](https://youtube.com/watch?v=WXCokV-FeFw&t=259s)** So in this case, we're triggering this action whenever there is a push to the main branch.

**[04:24](https://youtube.com/watch?v=WXCokV-FeFw&t=264s)** Next up, we need to configure the jobs that the runner is actually going to run as part of the workflow that we can think of this like environment setup, if you like.

**[04:32](https://youtube.com/watch?v=WXCokV-FeFw&t=272s)** So in this case, we're creating a job called deploy via tailscale, and we're going to run that job within an Ubuntu virtual machine.

**[04:40](https://youtube.com/watch?v=WXCokV-FeFw&t=280s)** That's what the runs online means.

**[04:43](https://youtube.com/watch?v=WXCokV-FeFw&t=283s)** Next up, we are going to connect the GitHub runner environment, the Ubuntu virtual machine.

**[04:48](https://youtube.com/watch?v=WXCokV-FeFw&t=288s)** We're going to connect that to our tailnet.

**[04:50](https://youtube.com/watch?v=WXCokV-FeFw&t=290s)** And then finally, we're going to SSH into the remote system, which is a VPS running on top of linode in my case, and do a few things to actually build the website.

**[05:01](https://youtube.com/watch?v=WXCokV-FeFw&t=301s)** So let's break these steps down just a little bit further, shall we?

**[05:04](https://youtube.com/watch?v=WXCokV-FeFw&t=304s)** First of all, we have the connect to tailscale step.

**[05:07](https://youtube.com/watch?v=WXCokV-FeFw&t=307s)** Now here, we specify a couple of GitHub repository secrets.

**[05:11](https://youtube.com/watch?v=WXCokV-FeFw&t=311s)** In our case, we've got the TSO auth client ID secret and the TSO auth secret secret.

**[05:19](https://youtube.com/watch?v=WXCokV-FeFw&t=319s)** Both of these things give this particular step as part of your GitHub action workflow access to add this virtual machine into your tailnet.

**[05:30](https://youtube.com/watch?v=WXCokV-FeFw&t=330s)** Now, the final thing that we need to do is specify a tag for our virtual environment.

**[05:35](https://youtube.com/watch?v=WXCokV-FeFw&t=335s)** Remember, this is just a virtual machine running on GitHub's infrastructure.

**[05:38](https://youtube.com/watch?v=WXCokV-FeFw&t=338s)** We need to give this away within our tailnet to identify itself, and we do that using tags in tailscale.

**[05:45](https://youtube.com/watch?v=WXCokV-FeFw&t=345s)** We limit how resources can interact with one another using these tags.

**[05:49](https://youtube.com/watch?v=WXCokV-FeFw&t=349s)** So we say if origin tag equals CI, then you're allowed to SSH to a specific tag, say prod.

**[05:57](https://youtube.com/watch?v=WXCokV-FeFw&t=357s)** We'll come onto ACLs a little bit later, but they're a very powerful tool.

**[06:01](https://youtube.com/watch?v=WXCokV-FeFw&t=361s)** Once we have our runner connected to our tailnet, we can then do the deployment.

**[06:05](https://youtube.com/watch?v=WXCokV-FeFw&t=365s)** So in this case, we're going to SSH into the remote system using just regular old SSH.

**[06:11](https://youtube.com/watch?v=WXCokV-FeFw&t=371s)** Next up, because we're reusing the authentication of the tailnet itself to manage our SSH keys,

**[06:17](https://youtube.com/watch?v=WXCokV-FeFw&t=377s)** I'm not going to worry about installing the remote host key into the GitHub runner environment.

**[06:22](https://youtube.com/watch?v=WXCokV-FeFw&t=382s)** If you're doing this in an enterprise or a true production grade situation, you might not want to do this.

**[06:28](https://youtube.com/watch?v=WXCokV-FeFw&t=388s)** Now, with SSH, we can specify our username at hostname, that's what we're doing here.

**[06:33](https://youtube.com/watch?v=WXCokV-FeFw&t=393s)** I don't need to specify the fully qualified domain name.

**[06:36](https://youtube.com/watch?v=WXCokV-FeFw&t=396s)** So, you know, ironic badger at perfectmedia server.com.

**[06:39](https://youtube.com/watch?v=WXCokV-FeFw&t=399s)** What I need to do is specify the DNS name as it appears in my tailnet admin dashboard.

**[06:45](https://youtube.com/watch?v=WXCokV-FeFw&t=405s)** So here, that's ktz-cloud.

**[06:48](https://youtube.com/watch?v=WXCokV-FeFw&t=408s)** The next step is to CD into the correct directory.

**[06:51](https://youtube.com/watch?v=WXCokV-FeFw&t=411s)** So in this case, I have made the project path a secret that belongs in the repo itself.

**[06:56](https://youtube.com/watch?v=WXCokV-FeFw&t=416s)** You could put this in clear text.

**[06:58](https://youtube.com/watch?v=WXCokV-FeFw&t=418s)** It's probably not super proprietary information.

**[07:01](https://youtube.com/watch?v=WXCokV-FeFw&t=421s)** But it would be the path in which the Git repository was actually cloned to on the remote system.

**[07:06](https://youtube.com/watch?v=WXCokV-FeFw&t=426s)** Next, we do Git pull, which just pulls down the latest changes that I've just put to the mainline branch.

**[07:12](https://youtube.com/watch?v=WXCokV-FeFw&t=432s)** And finally, I'm using Docker compose to run a build for the wiki website in a Docker container.

**[07:19](https://youtube.com/watch?v=WXCokV-FeFw&t=439s)** This method keeps the remote hosts far system clean of any dependencies like MK docs

**[07:24](https://youtube.com/watch?v=WXCokV-FeFw&t=444s)** or any other build craft that you might accumulate.

**[07:27](https://youtube.com/watch?v=WXCokV-FeFw&t=447s)** Now, the keen eye amongst you might have noticed there's a couple of quotation marks,

**[07:32](https://youtube.com/watch?v=WXCokV-FeFw&t=452s)** either side of all of those commands.

**[07:34](https://youtube.com/watch?v=WXCokV-FeFw&t=454s)** These are absolutely vital.

**[07:36](https://youtube.com/watch?v=WXCokV-FeFw&t=456s)** And they allow multi-line commands of any length between them, perfect for remote SSH commands.

**[07:41](https://youtube.com/watch?v=WXCokV-FeFw&t=461s)** Now, you could put any number of arbitrary commands in between those quotation marks, if you like.

**[07:46](https://youtube.com/watch?v=WXCokV-FeFw&t=466s)** Think of that space in between them, a bit like a bash script.

**[07:50](https://youtube.com/watch?v=WXCokV-FeFw&t=470s)** So let's recap our GitHub workflow.

**[07:52](https://youtube.com/watch?v=WXCokV-FeFw&t=472s)** First of all, we're going to look at the triggers.

**[07:54](https://youtube.com/watch?v=WXCokV-FeFw&t=474s)** In this case, this runs the action whenever there is a push to the main branch of our repo.

**[07:59](https://youtube.com/watch?v=WXCokV-FeFw&t=479s)** Next up, we create some jobs and we tell those jobs to run on an Ubuntu Linux virtual machine.

**[08:05](https://youtube.com/watch?v=WXCokV-FeFw&t=485s)** The first step that we defined here was to connect that virtual machine to our tail scale, tailnet.

**[08:10](https://youtube.com/watch?v=WXCokV-FeFw&t=490s)** And finally, we do the deployment using SSH to connect to the remote system

**[08:15](https://youtube.com/watch?v=WXCokV-FeFw&t=495s)** and run those commands as if we were SSH ourselves into that remote box.

**[08:21](https://youtube.com/watch?v=WXCokV-FeFw&t=501s)** If you wanted to execute commands within the GitHub Action Runner environment

**[08:24](https://youtube.com/watch?v=WXCokV-FeFw&t=504s)** to do the website builds there, you could do that too.

**[08:27](https://youtube.com/watch?v=WXCokV-FeFw&t=507s)** It's entirely personal preference at that point.

**[08:29](https://youtube.com/watch?v=WXCokV-FeFw&t=509s)** Maybe a fun idea would be to build the site using the insider's image from the GitHub Container Registry

**[08:35](https://youtube.com/watch?v=WXCokV-FeFw&t=515s)** and push that build image to get to you in my basement as a backup instead of pushing it

**[08:40](https://youtube.com/watch?v=WXCokV-FeFw&t=520s)** to GitHub Container Registry or Docker Harbor or wherever you happen to store your container images.

**[08:45](https://youtube.com/watch?v=WXCokV-FeFw&t=525s)** Remember, that runner is on your tailnet so it can get access to any resource you permit.

**[08:51](https://youtube.com/watch?v=WXCokV-FeFw&t=531s)** Now, when networks effectively become flat across different cloud providers, different physical sites,

**[08:57](https://youtube.com/watch?v=WXCokV-FeFw&t=537s)** and even different hardware architectures, not even an entire ocean can stand in your way.

**[09:03](https://youtube.com/watch?v=WXCokV-FeFw&t=543s)** Everything is now local.

**[09:05](https://youtube.com/watch?v=WXCokV-FeFw&t=545s)** So that's assuming you configure your ACLs to permit access, of course.

**[09:09](https://youtube.com/watch?v=WXCokV-FeFw&t=549s)** So should we just take a quick look at ACLs for a sec?

**[09:12](https://youtube.com/watch?v=WXCokV-FeFw&t=552s)** ACLs or access control lists, as you might know them, could and probably should be an entire video in their own right.

**[09:19](https://youtube.com/watch?v=WXCokV-FeFw&t=559s)** But for now, we'll cover the basics of tagging as it pertains to allowing or denying SSH access

**[09:24](https://youtube.com/watch?v=WXCokV-FeFw&t=564s)** between different nodes on your tailnet.

**[09:26](https://youtube.com/watch?v=WXCokV-FeFw&t=566s)** So let's take a quick look at my admin dashboard here for tail scale.

**[09:29](https://youtube.com/watch?v=WXCokV-FeFw&t=569s)** And we can see I've got lots of nodes listed here.

**[09:32](https://youtube.com/watch?v=WXCokV-FeFw&t=572s)** So for example, the noding question today is KTZ hyphen cloud.

**[09:37](https://youtube.com/watch?v=WXCokV-FeFw&t=577s)** This one has a tag of production because it runs a lot of production grade websites for me.

**[09:42](https://youtube.com/watch?v=WXCokV-FeFw&t=582s)** I would prefer these things didn't go offline, including perfectmedia server.com.

**[09:46](https://youtube.com/watch?v=WXCokV-FeFw&t=586s)** The laptop I'm recording this video from today is called Magrathia.

**[09:49](https://youtube.com/watch?v=WXCokV-FeFw&t=589s)** So if I take a quick look in my dashboard there, we can see that Magrathia pops up.

**[09:55](https://youtube.com/watch?v=WXCokV-FeFw&t=595s)** And again, if I just bring in a terminal window, you will see if I do a tail scale status,

**[10:00](https://youtube.com/watch?v=WXCokV-FeFw&t=600s)** I have a bunch of nodes here, and KTZ cloud is one of them.

**[10:04](https://youtube.com/watch?v=WXCokV-FeFw&t=604s)** Now, for right now, my laptop doesn't have a tag assigned to it.

**[10:08](https://youtube.com/watch?v=WXCokV-FeFw&t=608s)** And so if I try and do a SSH KTZ hyphen cloud with the username specified of ironic badger,

**[10:15](https://youtube.com/watch?v=WXCokV-FeFw&t=615s)** you can see that I get a permission denied error.

**[10:19](https://youtube.com/watch?v=WXCokV-FeFw&t=619s)** Now this is because my ACLs don't permit that traffic to flow.

**[10:24](https://youtube.com/watch?v=WXCokV-FeFw&t=624s)** So if we take a very quick look at the ACLs that we've got going on here, for example,

**[10:28](https://youtube.com/watch?v=WXCokV-FeFw&t=628s)** in this section here, we can see that as the user ironic badger,

**[10:33](https://youtube.com/watch?v=WXCokV-FeFw&t=633s)** I'm only allowed to SSH to production tag nodes, prod tag nodes,

**[10:38](https://youtube.com/watch?v=WXCokV-FeFw&t=638s)** from a source node of tag CI.

**[10:42](https://youtube.com/watch?v=WXCokV-FeFw&t=642s)** So what would happen if I added a tag to my laptop of tag CI?

**[10:46](https://youtube.com/watch?v=WXCokV-FeFw&t=646s)** Well, to do that, I go back to the machines page, click on edit ACL tags,

**[10:51](https://youtube.com/watch?v=WXCokV-FeFw&t=651s)** click on the, click on Magrathia first, of course, edit ACL tags,

**[10:56](https://youtube.com/watch?v=WXCokV-FeFw&t=656s)** add a tag of CI. And what you'll see in darn near real time,

**[11:01](https://youtube.com/watch?v=WXCokV-FeFw&t=661s)** if I go back to this terminal session over here,

**[11:04](https://youtube.com/watch?v=WXCokV-FeFw&t=664s)** suddenly the SSH permissions in the ACLs permit this SSH connection to actually occur.

**[11:11](https://youtube.com/watch?v=WXCokV-FeFw&t=671s)** There are no SSH keys under the hood or anything like that.

**[11:14](https://youtube.com/watch?v=WXCokV-FeFw&t=674s)** It's all done through the access control list policies that we define in our tail scale admin console.

**[11:20](https://youtube.com/watch?v=WXCokV-FeFw&t=680s)** So we can see at the top here, I have a list of the different tags and a little bit further down.

**[11:25](https://youtube.com/watch?v=WXCokV-FeFw&t=685s)** I have a few rules that govern the SSH connections for my tailnet.

**[11:30](https://youtube.com/watch?v=WXCokV-FeFw&t=690s)** There's very minimal stuff going on here because I'm still fairly new to ACLs myself.

**[11:34](https://youtube.com/watch?v=WXCokV-FeFw&t=694s)** But they're just a really powerful tool that I think we absolutely need to dig into more in future videos.

**[11:40](https://youtube.com/watch?v=WXCokV-FeFw&t=700s)** What I'd like to show you is in real time,

**[11:43](https://youtube.com/watch?v=WXCokV-FeFw&t=703s)** I'm going to just run the GitHub action to deployPerfectMediaServer.com.

**[11:48](https://youtube.com/watch?v=WXCokV-FeFw&t=708s)** And whilst it's running, let's just wait for it to connect the node to our tailnet.

**[11:53](https://youtube.com/watch?v=WXCokV-FeFw&t=713s)** A few moments later.

**[11:55](https://youtube.com/watch?v=WXCokV-FeFw&t=715s)** So the node is connected now, it's actually connected in via SSH remotely.

**[11:59](https://youtube.com/watch?v=WXCokV-FeFw&t=719s)** It's doing the thing.

**[12:00](https://youtube.com/watch?v=WXCokV-FeFw&t=720s)** So if we look here now, we can see we have right here,

**[12:04](https://youtube.com/watch?v=WXCokV-FeFw&t=724s)** we have a temporary ephemeral node that will automatically be removed shortly after going offline

**[12:10](https://youtube.com/watch?v=WXCokV-FeFw&t=730s)** with the tag CI that's in here.

**[12:12](https://youtube.com/watch?v=WXCokV-FeFw&t=732s)** I can stop the pop-ups getting in my way.

**[12:14](https://youtube.com/watch?v=WXCokV-FeFw&t=734s)** And here's a bunch of other information about it.

**[12:17](https://youtube.com/watch?v=WXCokV-FeFw&t=737s)** You can see the machine name is GitHub FV, whatever I assume it's running in Azure,

**[12:22](https://youtube.com/watch?v=WXCokV-FeFw&t=742s)** this one for AZ, or availability zone maybe, who knows.

**[12:26](https://youtube.com/watch?v=WXCokV-FeFw&t=746s)** And there's a bunch of other stuff, you know,

**[12:28](https://youtube.com/watch?v=WXCokV-FeFw&t=748s)** the closest latency relay server that tailscale has is in New York.

**[12:31](https://youtube.com/watch?v=WXCokV-FeFw&t=751s)** And there are the various services running on this machine.

**[12:36](https://youtube.com/watch?v=WXCokV-FeFw&t=756s)** But it's a fairly minimal config.

**[12:38](https://youtube.com/watch?v=WXCokV-FeFw&t=758s)** We even get the public IP address if we want it as well as our tailscale IP there as well.

**[12:42](https://youtube.com/watch?v=WXCokV-FeFw&t=762s)** But you can see the ACL tag.

**[12:45](https://youtube.com/watch?v=WXCokV-FeFw&t=765s)** In fact, there you go.

**[12:46](https://youtube.com/watch?v=WXCokV-FeFw&t=766s)** The machine has just deleted itself from my tailnet in real time,

**[12:50](https://youtube.com/watch?v=WXCokV-FeFw&t=770s)** as we were recording this video, once the GitHub action has completed over here.

**[12:54](https://youtube.com/watch?v=WXCokV-FeFw&t=774s)** So to summarize what just happened was we ran the GitHub action.

**[12:58](https://youtube.com/watch?v=WXCokV-FeFw&t=778s)** It added that runner temporarily to my tailnet.

**[13:01](https://youtube.com/watch?v=WXCokV-FeFw&t=781s)** Use those permissions as part of the ACLs to gain access to the cloud production instance.

**[13:07](https://youtube.com/watch?v=WXCokV-FeFw&t=787s)** And then from there, it deleted itself from the tailnet after it was finished.

**[13:12](https://youtube.com/watch?v=WXCokV-FeFw&t=792s)** Typically, you'd have to manage access like this via SSH keys.

**[13:15](https://youtube.com/watch?v=WXCokV-FeFw&t=795s)** And those keys would have to be manually rotated or expired when someone leaves your organization.

**[13:21](https://youtube.com/watch?v=WXCokV-FeFw&t=801s)** With tailscale SSH though, the authentication you've already done to connect to your tailnet

**[13:26](https://youtube.com/watch?v=WXCokV-FeFw&t=806s)** serves as your SSH authentication token.

**[13:29](https://youtube.com/watch?v=WXCokV-FeFw&t=809s)** No SSH keys are required here.

**[13:31](https://youtube.com/watch?v=WXCokV-FeFw&t=811s)** Access is controlled via these ACL policies.

**[13:34](https://youtube.com/watch?v=WXCokV-FeFw&t=814s)** And if we wanted, we could permit or deny access to our remote GitT Docker registry node this way too.

**[13:40](https://youtube.com/watch?v=WXCokV-FeFw&t=820s)** It's a similar kind of logic.

**[13:42](https://youtube.com/watch?v=WXCokV-FeFw&t=822s)** If this traffic has this origin, then permit to that destination on those ports else deny it.

**[13:48](https://youtube.com/watch?v=WXCokV-FeFw&t=828s)** We've only ever really seen granular controls like this in the firewall layer before now,

**[13:53](https://youtube.com/watch?v=WXCokV-FeFw&t=833s)** never as part of a software defined mesh VPN network like tailscale.

**[13:58](https://youtube.com/watch?v=WXCokV-FeFw&t=838s)** So like I said, ACLs are an incredibly powerful tool,

**[14:02](https://youtube.com/watch?v=WXCokV-FeFw&t=842s)** and they really do deserve their own video.

**[14:04](https://youtube.com/watch?v=WXCokV-FeFw&t=844s)** But if you'd like to learn more about them in the meantime,

**[14:06](https://youtube.com/watch?v=WXCokV-FeFw&t=846s)** you can find a link to the tailscale ACL documentation down below.

**[14:10](https://youtube.com/watch?v=WXCokV-FeFw&t=850s)** We know that many of you out there are using tailscale and conjunction with GitHub actions already.

**[14:15](https://youtube.com/watch?v=WXCokV-FeFw&t=855s)** But I hope today's video has given you some food for thought on different ways

**[14:18](https://youtube.com/watch?v=WXCokV-FeFw&t=858s)** to make your workflows more secure, less complex,

**[14:21](https://youtube.com/watch?v=WXCokV-FeFw&t=861s)** and enable some really creative use cases in the future.

**[14:25](https://youtube.com/watch?v=WXCokV-FeFw&t=865s)** We'd love to hear what you're going to do with the tailscale GitHub action.

**[14:28](https://youtube.com/watch?v=WXCokV-FeFw&t=868s)** Let us know down in the comments.

**[14:30](https://youtube.com/watch?v=WXCokV-FeFw&t=870s)** And you can also find us on social media at tailscaled on Twitter.

**[14:34](https://youtube.com/watch?v=WXCokV-FeFw&t=874s)** Until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
