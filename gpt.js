const {Client, Intents} = require('discord.js');
const { GPT3 } = require('openai'); // Anda perlu mengganti ini dengan cara yang benar untuk menghubungkan ke GPT-3.5

const token = 'MTE3MTc0NTY3Njg0MTk3OTkyNA.GIq44V.mBOQ_dDL_2I8yEYZvo3OM7-Rr-mByQ6K1gxkPM';
const openaiApiKey = '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';

const client = new Client({
  intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MESSAGES,

    // Add other intents as needed
  ],
});

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', async (message) => {
  // Hindari merespons pesan dari diri sendiri atau bot lain
  if (message.author.bot) return;

  if (message.content.startsWith('!ask')) {
    // Ambil pertanyaan dari pesan pengguna
    const question = message.content.slice('!ask'.length).trim();

    try {
      // Gunakan GPT-3.5 untuk menghasilkan jawaban
      const gpt3 = new GPT3({
        apiKey: openaiApiKey,
        engine: 'text-davinci-002', // Sesuaikan dengan engine GPT-3 yang Anda gunakan
      });

      const response = await gpt3.createCompletion({
        prompt: question,
        max_tokens: 50, // Sesuaikan sesuai kebutuhan
      });

      // Kirim jawaban kembali ke saluran Discord
      message.channel.send(response.choices[0].text);
    } catch (error) {
      console.error('Error:', error);
      message.channel.send('Maaf, ada kesalahan saat memproses permintaan Anda.');
    }
  }
});

client.login(token);
