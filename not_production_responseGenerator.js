
// Import necessary libraries
const axios = require('axios');
require('dotenv').config();

// Replace promptColor function with a simple string formatter
// since promptColor module doesn't exist in Node.js
function getAndRenderColors(query) {
  // Mock implementation. You need to replace this with actual color processing
  return `Color: ${query}`;
}

// Setting up the OpenAI API key from environmental variables
const openaiApiKey = process.env.OPENAI_KEY;

// Function to generate the response
async function responseGen(query) {
  const prompt = getAndRenderColors(query);
  
  try {
    const response = await axios.post('https://api.openai.com/v1/completions', {
      prompt: prompt,
      model: "gpt-3.5-turbo-instruct",
      max_tokens: 200,
      stop: "11."
    }, {
      headers: {
        'Authorization': `Bearer ${openaiApiKey}`,
        'Content-Type': 'application/json',
      },
    });

    // Parse the response
    return JSON.parse(response.data.choices[0].text);
  } catch (error) {
    console.error('Error generating response:', error);
  }
}

// Main function to prompt user and display the response
async function main() {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question("Enter a color: ", async (query) => {
    const response = await responseGen(query);
    console.log(response);
    readline.close();
  });
}

// Call main if this is the main module
if (!module.parent) {
  main();
}