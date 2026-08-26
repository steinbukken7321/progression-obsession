# 🤝 Contribuindo para Progression Obsession

Obrigado pelo interesse em contribuir com o **Progression Obsession**! Este documento fornece diretrizes básicas para o desenvolvimento e envio de melhorias.

---

## 🔄 Fluxo de Contribuição

1. **Faça um Fork** do repositório.
2. Crie uma branch para a sua funcionalidade ou correção:
   ```bash
   git checkout -b minha-feature

```

3. Faça o commit das suas alterações:
```bash
git commit -m "feat: adiciona nova mecânica de upgrades"

```


4. Envie para a sua branch:
```bash
git push origin minha-feature

```


5. Abra um **Pull Request** detalhando as mudanças realizadas.

---

## 📝 Padrões de Código

* **Evite o uso desnecessário de funções aninhadas ou complexas** onde um código direto funcione bem.
* **Mantenha a organização das pastas:**
* `src/`: Contém os módulos lógicos, de interface e de banco de dados.
* `assets/`: Ícones e imagens do jogo.
* `data/`: Onde o banco de dados SQLite local é gerado (ignorado pelo git).


* **Documente suas alterações** de forma clara nos commits e descrições.
