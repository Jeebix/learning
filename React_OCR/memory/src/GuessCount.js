import React from 'react'

import './GuessCount.css'

const GuessCount = ({ guesses }) => <div className="guesses">{guesses}</div>

export default GuessCount

// Composant GuessCount = compteur de tentatives.
// Au fil de la partie, on l'affiche avant le plateau de cartes.
