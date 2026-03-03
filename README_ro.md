# Snake Game - Proiect Personal Python

## Descriere
Acest proiect reprezinta o implementare a jocului clasic Snake, dezvoltata in Python utilizand biblioteca Pygame. Obiectivul proiectului a fost aprofundarea conceptelor de programare orientata pe obiecte (OOP) si gestionarea logicii unui joc intr-un mediu grafic 2D.

## Tehnologii si Concepte Informatice

* **Programare Orientata pe Obiecte (OOP):** Codul este modularizat in clase specifice (`SNAKE`, `FRUIT`, `MAIN`), asigurand o separare clara a responsabilitatilor.
* **Matematica Vectoriala:** Utilizarea clasei `Vector2` din `pygame.math` pentru calculul pozitiilor pe grid si gestionarea directiei, simplificand operatiile de translatie si coliziune.
* **Game Loop & Event Handling:** Implementarea unui ciclu de viata al aplicatiei care gestioneaza update-ul starii componentelor, randarea grafica si procesarea input-ului de la tastatura.
* **Gestionarea Resurselor (Asset Management):** Incarcarea dinamica a texturilor PNG si a fisierelor audio OGG, utilizand metoda `convert_alpha()` pentru a optimiza performanta randarii.
* **Logica de Miscare "Wrapped Grid":** Implementarea unui algoritm care permite sarpelui sa traverseze marginile ecranului si sa reapara in partea opusa, oferind o experienta de joc fluida.
* **Custom Events:** Utilizarea `pygame.time.set_timer` pentru a separa viteza logica de deplasare a sarpelui de rata de refresh a ecranului.

## Functionalitati
* **Sistem de Scor:** Calcularea si afisarea scorului in timp real, bazat pe numarul de fructe colectate.
* **Grafica Adaptiva:** Texturile corpului sarpelui (cap, segmente, coturi si coada) se ajusteaza automat in functie de directia de miscare si pozitia segmentelor vecine.
* **Feedback Audio:** Integrarea efectelor sonore pentru interactiunile cu fructele si pentru starea de Game Over.
* **Randomizare:** Generarea aleatorie a fructelor pe grid, cu validarea pozitiei pentru a evita suprapunerea cu corpul sarpelui.

## Structura Proiectului
* `main.py` - Contine logica centrala, clasele de obiecte si bucla principala de joc.
* `gallery/` - Folderul ce contine resursele grafice pentru sarpe, fructe si decor.
* `sounds/` - Folderul dedicat fisierelor audio (bite sound, die sound).
