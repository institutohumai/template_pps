---
type: "project" # ¡NO MODIFIQUES ESTO! :)
date: "2020-05-16" # Fecha en la que subiste por primera vez tu proyecto.
# Título de tu proyecto (nos gustan los títulos creativos)
title: "Esta es una página de proyecto de ejemplo que sirve como plantilla"

# Lista los nombres de los colaboradores dentro de los [ ]. Si estás solo, simplemente pon tu nombre.
names: [Samuel Guay, Pierre Bellec]

# URL del repositorio de GitHub de tu proyecto
github_repo: https://github.com/PSY6983-2021/project_template

# Si estás trabajando en un proyecto que tiene sitio web, indica la URL completa incluyendo "https://" o déjalo vacío.
website:

# Lista +- 4 palabras clave que describan mejor tu proyecto dentro de []. Nota que el resumen del proyecto también incluye palabras clave. Estas se listan en la parte superior del [repositorio de GitHub](https://github.com/PSY6983-2021/project_template), haz clic en `manage topics`.
# Solo letras minúsculas, por favor.
tags: [proyecto, github, markdown, brainhack]

# Resume tu proyecto en < ~75 palabras. Esta descripción aparecerá en la parte superior de tu página y en la lista junto a otros proyectos.

summary: "Cada repositorio de proyecto debe tener un archivo markdown que explique los antecedentes y objetivos del proyecto, así como un resumen de los resultados y enlaces a los diferentes entregables del proyecto. Los informes de los proyectos se incorporan en el sitio web de BHS [aquí](https://psy6983.brainhackmtl.org/project)."

# Si quieres añadir una imagen de portada (para la lista y en la parte derecha), añádela a tu directorio e indica el nombre abajo con la extensión.
image: ""
---
<!-- Este es un comentario HTML y no aparecerá en la página renderizada. Estás editando el área "contenido", el núcleo de tu descripción. Todo lo que puedes hacer en markdown está permitido a continuación. Hemos añadido algunos comentarios para guiarte en la documentación de tu progreso. -->

## Definición del proyecto

### Antecedentes

Inspirado por la iniciativa del [Recurse Centre](https://www.recurse.com/) (anteriormente conocida como "hacker school"), Brainhack School se estableció en 2018 con la misión de entrenar a estudiantes de diferentes disciplinas en una variedad de herramientas reproducibles para la ciencia de datos neuronales, utilizando un enfoque basado en proyectos. Tras un piloto inicial de 3 semanas, se añadió una cuarta semana con un bootcamp intensivo, para que los estudiantes pudieran elegir qué herramientas aprender más a fondo en sus proyectos. A medida que el curso se integró en el currículo estándar en diferentes universidades, la fórmula pareció funcionar. Para agilizar las diferentes etapas del proyecto, se necesitaron plantillas estándar y hitos incorporados en un flujo de trabajo basado en GitHub. El proyecto "plantilla de proyecto" (que también es nuestro primer meta-proyecto BHS) tiene como objetivo establecer dicha plantilla estandarizada. Puedes ver este [video](https://youtu.be/PTYs_JFKsHI) donde Pierre Bellec da una visión general de la Brainhack School.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PTYs_JFKsHI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Herramientas

El proyecto "plantilla de proyecto" se basará en las siguientes tecnologías:
 * Markdown, para estructurar el texto.
 * El marco de sitios web Hugo, que es utilizado por el sitio web de BHS. Esto hace posible añadir fácilmente la descripción del proyecto en markdown al sitio web.
 * La incorporación del proyecto al sitio web se realiza a través de GitHub, mediante pull requests.

### Datos

En última instancia, la plantilla de proyecto será utilizada por todos los participantes de BHS. Los datos de los diferentes proyectos se agregarán en la [siguiente página](https://psy6983.brainhackmtl.org/project). Esto servirá como una galería de ejemplos adicionales para los futuros estudiantes de Brainhack School. Muchos informes de [BHS 2020](https://github.com/brainhack-school2020) ya usaron esta plantilla.

### Entregables

Al final de este proyecto, tendremos:
 - El documento actual en markdown, completado y revisado.
 - Una galería de los proyectos estudiantiles de Brainhack 2020.
 - Instrucciones en el sitio web sobre cómo enviar un pull request al [sitio web de Brainhack School](https://github.com/PSY6983-2021) para añadir la descripción del proyecto al sitio web.

## Resultados

### Resumen del progreso

El proyecto fue iniciado rápidamente por P Bellec, basado en la plantilla existente creada en 2019 por Tristan Glatard y mejorada por diferentes estudiantes. No fue tan complicado. Se espera que el feedback de la comunidad lleve a rápidas mejoras en esta primera versión.

### Herramientas aprendidas durante este proyecto

 * **Meta-proyecto:** P Bellec aprendió cómo realizar un meta-proyecto por primera vez, desarrollando un marco mientras lo utilizaba al mismo tiempo. Fue algo extraño, pero también bastante divertido.
 * **Flujo de trabajo en GitHub:** El uso exitoso de este enfoque demostrará que es posible incorporar decenas de presentaciones estudiantiles en un sitio web de manera colaborativa en pocas semanas.
 * **Contenido del proyecto:** A través de los informes de proyectos generados usando la plantilla, es posible aprender exactamente en qué están trabajando los estudiantes de Brainhack School.

### Resultados

#### Entregable 1: plantilla de informe

¡Estás leyendo la plantilla de informe! Te dejo juzgar si es útil o no. Si crees que hay algo que podría mejorarse, no dudes en abrir un issue [aquí](https://github.com/PSY6983-2021/project_template/issues/) y hacérnoslo saber.

#### Entregable 2: galería de proyectos

Puedes consultar la [galería de proyectos de BrainHack School 2020](https://psy6983.brainhackmtl.org/project/)

##### Pipeline de ECG y pupilometría por Marce Kauffmann

El repositorio de este proyecto se puede encontrar [aquí](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann). El objetivo era crear un pipeline de procesamiento para datos de ECG y pupilometría. La motivación detrás de esta tarea es que el laboratorio de Marcel (MIST Lab @ Polytechnique Montreal) estaba realizando un estudio de interacción humano-robot. El repositorio incluye:
 * un [video introductorio](http://www.youtube.com/watch/8ZVCNeX42_A) al proyecto.
 * una presentación [hecha en un jupyter notebook](https://github.com/mtl-brainhack-school-2019/ecg_pupillometry_pipeline_kaufmann/blob/master/BrainHackPresentation.ipynb) sobre los resultados del proyecto.
 * Notebooks para todos los análisis.
 * Archivos de requisitos detallados, que facilitan la replicación del entorno del notebook.
 * Una visión general de los resultados en el documento markdown.

##### Otros proyectos
Aquí hay otros buenos ejemplos de repositorios:
- [Aprendiendo a manipular biosignals con python](https://github.com/mtl-brainhack-school-2019/franclespinas-biosignals) por François Lespinasse
- [Ejecutar análisis multivariado para relacionar datos conductuales y electrofisiológicos](https://github.com/mtl-brainhack-school-2019/PLS_PV_Behaviour)
- [Automatización de pipeline PET y exploración estructural de MRI](https://github.com/mtl-brainhack-school-2019/rwickens-sMRI-PET) por Rebekah Wickens
- [Trabajando con datos PSG [EEG] de pacientes con Parkinson](https://github.com/mtl-brainhack-school-2019/Soraya-sleep-data-in-PD-patients) por Cryomatrix
- [Explorando la activación funcional cerebral en adolescentes que intentaron suicidarse](https://github.com/mtl-brainhack-school-2019/Anthony-Gifuni-repo) por Anthony Gifuni

#### Entregable 3: Instrucciones

Próximamente disponibles.

## Conclusión y agradecimientos

El equipo de BHS espera que encuentres esta plantilla útil para documentar tu proyecto. El desarrollo de esta plantilla fue un esfuerzo grupal y se benefició del feedback y las ideas de todos los estudiantes de BHS a lo largo de los años.

También puedes enviar tu proyecto a Neurolibre https://neurolibre.org/. Es un servidor de preprints para análisis de datos interactivos. Está diseñado para publicar notebooks de neurociencia interactivos que pueden integrar sin problemas datos, texto, código y figuras. Las instrucciones de envío se encuentran [aquí](https://docs.neurolibre.org/en/latest/index.html) y la documentación de jupyter book [aquí](https://jupyterbook.org/intro.html).
