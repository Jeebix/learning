import React, { Component } from 'react'
import shuffle from 'lodash.shuffle'

import './App.css'

import Card from './Card'
import GuessCount from './GuessCount'
import HallOfFame, { FAKE_HOF } from './HallOfFame';

const SIDE = 6
const SYMBOLS = '😀🎉💖🎩🐶🐱🦄🐬🌍🌛🌞💫🍎🍌🍓🍐🍟🍿'

class App extends Component {
    
    cards = this.generateCards()

    generateCards() {
        const result = []
        const size = SIDE * SIDE
        const candidates = shuffle(SYMBOLS)
        while (result.length < size) {
            const card = candidates.pop()
            result.push(card, card)
        }
        return shuffle(result)
    }

    handleCardClick(card) {
        console.log(card, 'clicked')
    }

    render() {
        const won = new Date().getSeconds() % 2 === 0
        return (
            <div className="memory">
                <GuessCount guesses={0} />
                {this.cards.map((card, index) => (
                    <Card
                        card={card}
                        feedback="visible"
                        key={index} // Liste de cartes figée, donc OK pour l'index en key
                        onClick={this.handleCardClick}
                    />
                ))}
                {won && <HallOfFame entries={FAKE_HOF} />}
            </div>
        )
    }
}

export default App

// Remarquez qu'il y a 4 feedbacks (ou états visuels) possibles et qui sont donc prévus :
// La carte est masquée (hidden).
// La carte fait partie de la tentative en cours, qui vient de réussir une paire (justMatched).
// La carte fait partie de la tentative en cours, qui vient de rater une paire (justMismatched).
// La carte appartient à une paire précédemment réussie (visible).