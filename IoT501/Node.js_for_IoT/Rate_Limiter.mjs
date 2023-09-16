#!/usr/bin/node
export class RateLimiter {
  constructor (tokensPerInterval, interval) {
    this.tokensPerInterval = tokensPerInterval; // Number of tokens allowed per interval
    this.interval = interval; // Time interval (in milliseconds)
    this.tokens = tokensPerInterval; // Current available tokens
    this.lastRefill = Date.now(); // Last time the tokens were refilled

    // Refill tokens at the specified interval
    setInterval(this.refillTokens.bind(this), interval);
  }

  refillTokens () {
    const now = Date.now();
    const elapsedTime = now - this.lastRefill;

    // Calculate the number of tokens to add based on elapsed time
    const tokensToAdd = Math.floor(elapsedTime / this.interval) * this.tokensPerInterval;

    // Update the tokens and set the last refill time
    this.tokens = Math.min(this.tokens + tokensToAdd, this.tokensPerInterval);
    this.lastRefill = now;
  }

  // Check if a request can be made
  tryAcquire () {
    if (this.tokens > 0) {
      this.tokens--;
      return true; // Request allowed
    } else {
      return false; // Request denied
    }
  }
}
