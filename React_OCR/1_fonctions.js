// CLASSIQUE : React.createElemnt()
function CoolComponent() {
	return React.createElement('p', {}, 'Youpi So Cool !')
  }
	  // createElement() possède 3 arguments
	  // 1er : nom du composant (ici string que React interprétera comme élément natif du navigateur)
	  // 2nd : série d'attributs (id, className, ...)
	  // 3rd : contenu (ici texte)

// Pour afficher un DOM virtuel React dans une page web, on utilise ReactDOM.render(…)
ReactDOM.render(
	React.createElement(CoolComponent),
	document.getElementById('root')
  )

// AVEC JSX
function CoolComponent() {
	return <p>Youpi So Cool !</p>
  }
  
  ReactDOM.render(
	<CoolComponent />,
	document.getElementById('root')
  )

// PREMIÈRES PROPS

	// On peux fournir à un composant des attributs, appelés "props" en React.

	// Ces props sont définies par un ensemble de clés/valeurs,
	// définies dans un objet, qui est passé en argument à la fonction du composant.

	// Cet objet est alors déstructuré automatiquement par la fonction.
function CoolComponent({ adjective = 'Cool' }) {
	return <p>Youpi So {adjective} !</p>
}
	
ReactDOM.render(
	<div>
		<CoolComponent adjective="awesome" />
		<CoolComponent />
	</div>,
	document.getElementById('root')
)
