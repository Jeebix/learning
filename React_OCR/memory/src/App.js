import React, { Component } from "react";
import Card from './Card'
import GuessCount from './GuessCount'

class App extends Component {
    render() {
        return (
            <div className="memory">
                <GuessCount guesses={0} />
                <Card card="😀" feedback="hidden" onClick={this.handleCardClick} />
                <Card card="🎉" feedback="justMatched" onClick={this.handleCardClick} />
                <Card card="💖" feedback="justMismatched" onClick={this.handleCardClick} />
                <Card card="🎩" feedback="visible" onClick={this.handleCardClick} />
                <Card card="🐶" feedback="hidden" onClick={this.handleCardClick} />
                <Card card="🐱" feedback="justMatched" onClick={this.handleCardClick} />
            </div>
        )
    }

    handleCardClick(card) {
        console.log(card, 'clicked')
    }
}

export default App

// Remarquez qu'il y a 4 feedbacks (ou états visuels) possibles et qui sont donc prévus :
// La carte est masquée (hidden).
// La carte fait partie de la tentative en cours, qui vient de réussir une paire (justMatched).
// La carte fait partie de la tentative en cours, qui vient de rater une paire (justMismatched).
// La carte appartient à une paire précédemment réussie (visible).