// DES EXPRESSIONS, PAS DES INSTRUCTIONS

    // JSX produit une expression Javascript, pas une instruction.
    // Instructions comme if, for ou déclaration pas possible.

    // SI...ALORS... (if)
    // Pour retranscrire un contenu conditionnel simple (« si la condition X est remplie,
    // alors utiliser la grappe JSX que voici »), on utilisera l’opérateur logique  &&,
    // avec la condition comme opérande de gauche, et la grappe JSX comme opérande de droite.
    <p>{42 > 43 && document.nonExistingMethod()}</p>
        // Si condition échoue, opérande de droite pas évaluée. (vaudra false et donc JSX l'ignorera).
        <p>{user.admin && <a href="/admin">Faire des trucs de VIP</a>}</p>
        // Si condition remplie, l'expression évalue son opérande de droite, qui est la valeur finale:
        // la grappe JSX sera utilisée.
        <p>{user.admin && (
            <a href="/admin">Faire des trucs de VIP</a>
        )}</p>
        // Bonnes pratiques pour la lisibilité.

        // SI...ALORS...SINON (if else)
        // Opérateur ternaire ? :
        <p>{user.loggedIn ? <WelcomeLabel /> : <LoginLink />}</p>

        <p>{user.admin ? (
            <a href="/admin">Faire des trucs de VIP</a>
        ) : (
                <a href="/request-admin">Demander à devenir VIP</a>
            )}</p>

// DÉCOUPER LE JSX

    // CAS 1: RÉUTILISATION AU SEIN DU RENDER
    // Si 1 bouton à réutiliser:
    render() {
        return (
            <Card>
                <CardTitle>
                    Oh le joli titre
                <button onClick={this.logOut}>
                        <LogoutIcon />
                        Déconnexion
                </button>
                </CardTitle>
                …
                <Footer>
                    © 2017 Des Gens Bien™ •
                <button onClick={this.logOut}>
                        <LogoutIcon />
                        Déconnexion
                </button>
                </Footer>
            </Card>
        )
    }
    // Plus propre:
    render() {
        const logoutButton = (
            <button onClick={this.logOut}>
                <LogoutIcon />
                Déconnexion
            </button>
        )

        return (
            <Card>
                <CardTitle>
                    Oh le joli titre
                {logoutButton}
                </CardTitle>
                …
                <Footer>
                    © 2017 Des Gens Bien™ •
                {logoutButton}
                </Footer>
            </Card>
        )
    }

    // CAS 2: GRAPPE À L'INTÉRIEUR D'UNE PROP
    // La valeur d'une prop peut être une autre expression JSX.
    // Pas très lisible:
    <ListItem
        primaryText="Vous êtes connecté·e en tant que"
        rightSideIcon={
            <IconButton onClick={this.logOut}>
                <LogoutIcon />
            </IconButton>
        }
        secondaryText={currentUser.email}
    />
    // On Définit la grappe de prop en amont et on y stocke la référence:
    const logoutButton = (
        <IconButton onClick={this.logOut}>
          <LogoutIcon />
        </IconButton>
    )
    …
    return (
        …
        <ListItem
            primaryText="Vous êtes connecté·e en tant que"
            rightSideIcon={logoutButton}
            secondaryText={currentUser.email}
        />
        …
    )

    // CAS 3: LE JSX EST TROP MASSIF
    // Si la grappe JSX commence à être définie par plusieurs dizaines de lignes, on a sans doute tendance
    // à vouloir la découper en sous-parties nommées, recombinées à la fin lors du return.
    // Une grappe JSX démesurée est plutôt un indice clair que le composant essaie « d’en faire trop »,
    // et qu’il serait sans doute pertinent de le découper en sous-composants plus spécifiques.
