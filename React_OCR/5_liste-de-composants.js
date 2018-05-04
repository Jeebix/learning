// MANIPULATION

    // map()
    const numbers = [1, 2, 3, 4]
    const doubles = numbers.map(x => x * 2) // [2, 4, 6, 8]
    // Pour produire une grappe:
    const users = [
        { id: 1, name: 'Alice' },
        { id: 2, name: 'Bob' },
        { id: 3, name: 'Claire' },
        { id: 4, name: 'David' },
    ]
    // Produire une liste de liens avec les noms des utilisateurs :
    render () {
        return (
          <div className="userList">
            {this.props.users.map((user) => (
              <a href={`/users/${user.id}`}>{user.name}</a>
            ))}
          </div>
        )
    }
    // En déstructurant l’élément reçu dans la fonction de rappel :
    render () {
        return (
          <div className="userList">
            {this.props.users.map(({ id, name }) => (
              <a href={`/users/${id}`}>{name}</a>
            ))}
          </div>
        )
    }

    // LA CLÉ DU SUCCÈS: key
    // Afin de conserver une association correcte entre données d’origine et DOM virtuel, mais aussi afin d’optimiser
    // la retranscription dans le DOM des changements aux données d’origine, React exige que tout élément présent
    // au sein d’un tableau dans une grappe JSX soit doté d’une prop technique nommée key.
    // Cette prop doit impérativement être :
    //     - Unique au sein du tableau
    //     - Stable dans le temps (pour la même donnée source, on aura toujours la même valeur de key=)
    // Bonne solution:
    render () {
        return (
          <div className="userList">
            {this.props.users.map(({ id, name }) => (
              <a href={`/users/${id}`} key={id}>{name}</a>
            ))}
          </div>
        )
    }