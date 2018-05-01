// JSX LANGAGE À BALISE

// EXEMPLE JSX
<form method="post" action="/sessions" onSubmit={this.handleSubmit}>
  <p className="field">
    <label>
      E-mail
      <input
        type="email"
        name="email"
        required
        autoFocus
        value={this.state.email}
        onChange={this.handleFieldChange}
      />
    </label>
  </p>
  <p className="field">
    <label>
      Mot de passe
      <input
        type="password"
        name="password"
        required
        value={this.state.password}
        onChange={this.handleFieldChange}
      />
    </label>
  </p>
  <p>
    <button type="submit" value="Connexion" />
  </p>
</form>

// NI DU HTML, NI DU XML

    // Sensible à la casse.
    // Exigence de fermeture des éléments (input /).
    // Fermeture de balises dans le bon ordre.

    // VALEURS DES PROPS (props = attributs)

        // Syntaxiquement en JSX, 2 possibilités: string "" ou expression JSX {}
        <input
            type="email"
            name="email"
            maxlength={42}
            readonly={false}
            onChange={this.handleFieldChange}
            value={this.state.value}
        />
        // En JSX, il est obligatoire d'utiliser une expression JSX pour toute valeur
        // qui n'est pas string.
        
        // En revanche, le type de l'expression est préservé: la prop que l'on récupèrera
        // dans le composant sera bien par exemple un nombre, un booléen, ...

        // RACCOURCI POUR True
        <input type="email" name="email" autoFocus required />
        // Au lieu d’écrire explicitement la valeur dans une expression JSX, on peut se contenter du nom de la prop.

        // MOTS RÉSERVÉS
        // Dans la mesure où JSX produit, au final, du code JavaScript, et que celui-ci doit pouvoir s’exécuter
        // dans un environnement ES5 (par exemple Internet Explorer 9+ ou d'anciennes versions de Node.js)
        // et non ES2015+ (navigateurs modernes, versions de Node.js récentes, etc.), il n’est pas possible
        // d’utiliser des mots-clés de JavaScript comme noms de props.
        // className au lieu de class
        // htmlFor au lieu de for

        // COMMENTAIRES
        // Pas de syntaxe dédiée pour les commentaires.
        // Il faut le mettre dans une expression.
        <form method="post" action="/sessions" onSubmit={this.handleSubmit}>
        {/* La classe 'field' assure l’espacement vertical convenable */}
        <p className="field">
            <label>
            E-mail
            <input type="email" name="email" required autoFocus
                value={this.state.email}
                {/*
                Avec les champs contrôlés, il est indispensable de fournir `onChange`
                pour éviter que le champ soit fourni en lecture seule au niveau du
                DOM.
                */}
                onChange={this.handleFieldChange}
            />
            </label>
        </p>
        <p><button type="submit" value="Connexion" /></p>
        </form>

        // L'IMPORTANCE DE LA CASSE DANS LES GRAPPES JSX
        // Si 1 élément démarre par une minuscule => élément natif de la plate-forme
        // Si 1 élément démarre par une majuscule => composant React
        [
            <CoolComponent/>,
            <coolComponent/>,
        ]
        // donne :
        [
            React.createElement(CoolComponent, null),
            React.createElement('coolComponent', null),
        ]

        

        
