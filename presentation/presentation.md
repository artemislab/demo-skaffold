---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
logoImg: ""
slideNumber: false
title: "Welcome to Skaffold"
---
<img src="medias/skaffold-logo.png">
<h2 style=background:red, text-align:center,font-size:28px,width:100%;>Welcome to Skaffold</h2>

---

::: block
// @[Linkedin: /adrienbarret](https://www.linkedin.com/in/adrienbarret/)  
// @[twitter: BarretAdrien](etVpwB7uHlwhttps://twitter.com/BarretAdrien)  

{style=text-align:left;padding-left:60px;}  
:::

---

### What's Skaffold ?
::: block  
Skaffold is a CLI that facilitates continuous development for Kubernetes-native applications.  
  
Skaffold handles the workflow for  
building, pushing, and deploying your application from your local code to kubernetes by a simple pipeline.  
{style=text:center;}

:::  

---

### Basics examples

Let's take a look

--

#### Build

:::block  

```yaml
apiVersion: skaffold/v2beta27
kind: Config
build:
  artifacts:
  - image: python-reload
    context: python
```

:::  

--

#### Profile and hot-reloading

:::block  

```yaml
profiles:
  - name: dev
    activation:
      - command: dev
    build:
      artifacts:
      - image: python-reload
        context: python
        docker:
          buildArgs:
            DEBUG: 1
        sync:
          manual:
          - src: 'src/**/*.py'
            dest: .
```

:::  

--

#### Deploy

#### Helm 

```yaml 
deploy:
  helm:
    releases:
    - name: redis-release
      repo: https://charts.bitnami.com/bitnami 
      remoteChart: redis
      artifactOverrides:
        image: custom-redis
```

##### Kustomize

```yaml
deploy:
  kustomize:
    buildArgs:
      - "--load_restrictor none"
```

---

### Demo time

<!-- .slide: data-background="http://i.giphy.com/90F8aUepslB84.gif" -->

---

### Qestions?

<!-- .slide: data-background="https://media.giphy.com/media/XBQwD7p7lcfBbtcXZD/giphy.gif" -->

---

<!-- .slide: style="text-align: left;" -->
# THE END  
