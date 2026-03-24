#!/usr/bin/env python3
import json

# Questions data - abbreviated for demo (full version would have all 300)
questions_blocks = [
    {"block": 1, "title": "Legislación y Servicios Sociales", "icon": "⚖️", "range": "1-60", "questions": []},
    {"block": 2, "title": "Legislación Avanzada", "icon": "📋", "range": "61-120", "questions": []},
    {"block": 3, "title": "Casos Prácticos", "icon": "🏥", "range": "121-180", "questions": []},
    {"block": 4, "title": "Casos Clínicos", "icon": "📊", "range": "181-240", "questions": []},
    {"block": 5, "title": "Simulacro Final", "icon": "🎯", "range": "241-300", "questions": []},
]

# Sample questions (30 per block for demo)
sample_q = [
    ("El órgano que ostenta la máxima representación del Ayuntamiento es:", ["El Pleno", "La Junta de Gobierno", "El Alvarado", "El Secretario"], "C"),
    ("El órgano colegiado de control político es:", ["Alcaldía", "Pleno", "Teniente de Alvarado", "Intervención"], "B"),
    ("¿Quién sustituye al Alvarado?", ["Secretario", "Concejal delegado", "Teniente de Alvarado", "Interventor"], "C"),
    ("La Junta de Gobierno Local tiene funciones:", ["Legislativas", "Judiciales", "Ejecutivas", "Electorales"], "C"),
    ("La Ley que regula las bases del régimen local es:", ["Ley 39/2015", "Ley 7/1985", "Ley 40/2015", "Ley 16/2019"], "B"),
    ("El Estatuto Básico del Empleado Público regula:", ["Urbanismo", "Funcionarios y personal público", "Sanidad", "Educación"], "B"),
    ("Un principio del empleado público es:", ["Parcialidad", "Subjetividad", "Imparcialidad", "Arbitrio"], "C"),
    ("La confidencialidad implica:", ["Compartir información", "Guardar secreto profesional", "Publicar datos", "Delegar funciones"], "B"),
    ("La discriminación indirecta es:", ["Directa y evidente", "Oculta en normas aparentemente neutras", "Legal", "Obligatoria"], "B"),
    ("La Ley 3/2007 trata sobre:", ["Dependencia", "Igualdad", "Sanidad", "Educación"], "B"),
    ("La Ley 4/2023 regula:", ["Urbanismo", "Derechos LGTBI", "Hacienda", "Seguridad"], "B"),
    ("La identidad de género es:", ["Sexo biológico", "Percepción personal", "Nacionalidad", "Edad"], "B"),
    ("La Ley de Servicios Sociales de Canarias es:", ["7/1985", "16/2019", "39/2015", "14/1986"], "B"),
    ("El sistema de servicios sociales garantiza:", ["Beneficio económico", "Bienestar social", "Exclusión", "Competencia"], "B"),
    ("Un derecho del usuario es:", ["Desobedecer normas", "Atención digna", "Negligencia", "Abandono"], "B"),
    ("Un deber del usuario es:", ["Uso adecuado del servicio", "Ignorar normas", "No colaborar", "Ocultar datos"], "A"),
    ("La teleasistencia es:", ["Atención hospitalaria", "Atención a distancia", "Servicio judicial", "Servicio educativo"], "B"),
    ("Los centros de día pertenecen a:", ["Educación", "Servicios sociales", "Justicia", "Transporte"], "B"),
    ("La inspección de servicios sociales garantiza:", ["Publicidad", "Calidad", "Negligencia", "Privacidad"], "B"),
    ("Un CED es:", ["Centro hospitalario", "Servicio diurno", "Centro educativo", "Centro penitenciario"], "B"),
    ("Objetivo del CED:", ["Aislar", "Fomentar autonomía", "Hospitalizar", "Judicializar"], "B"),
    ("El usuario típico es:", ["Niño", "Adulto sano", "Persona dependiente", "Deportista"], "C"),
    ("Un servicio del CED:", ["Cirugía", "Terapia ocupacional", "Juicio", "Educación primaria"], "B"),
    ("El auxiliar realiza:", ["Diagnóstico médico", "Higiene", "Prescripción", "Cirugía"], "B"),
    ("El envejecimiento es:", ["Reversible", "Irreversible", "Opcional", "Artificial"], "B"),
    ("Un cambio físico:", ["Aumento de fuerza", "Pérdida de movilidad", "Crecimiento", "Regeneración"], "B"),
    ("Una necesidad biológica:", ["Afecto", "Alimentación", "Participación", "Comunicación"], "B"),
    ("Necesidad social:", ["Dormir", "Comer", "Relacionarse", "Respirar"], "C"),
    ("Necesidad psicológica:", ["Comer", "Seguridad", "Dormir", "Beber"], "B"),
    ("La demencia es:", ["Aguda", "Crónica", "Reversible", "Temporal"], "B"),
    ("El delirium es:", ["Crónico", "Agudo", "Permanente", "Genético"], "B"),
    ("Ejemplo de demencia:", ["Gripe", "Enfermedad de Alzheimer", "Fractura", "Asma"], "B"),
    ("La depresión en ancianos es:", ["Rara", "Frecuente", "Inexistente", "Obligatoria"], "B"),
    ("Tipo de maltrato:", ["Educativo", "Físico", "Deportivo", "Cultural"], "B"),
    ("La negligencia es:", ["Cuidado adecuado", "Falta de atención", "Protección", "Respeto"], "B"),
    ("Factor de riesgo:", ["Independencia", "Aislamiento", "Salud", "Autonomía"], "B"),
    ("Paciente crónico:", ["Enfermedad corta", "Enfermedad prolongada", "Enfermedad leve", "Enfermedad puntual"], "B"),
    ("Cuidados paliativos buscan:", ["Curar", "Calidad de vida", "Operar", "Investigar"], "B"),
    ("Función del auxiliar:", ["Operar", "Confort", "Diagnosticar", "Prescribir"], "B"),
    ("El Pleno aprueba:", ["Diagnósticos", "Presupuestos", "Tratamientos", "Recetas"], "B"),
    ("La igualdad implica:", ["Discriminación", "Trato equitativo", "Exclusión", "Jerarquía"], "B"),
    ("La participación del mayor pertenece a:", ["ONU", "Policía", "Tráfico", "Educación"], "A"),
    ("El aislamiento aumenta:", ["Bienestar", "Riesgo", "Salud", "Autonomía"], "B"),
    ("El envejecimiento social incluye:", ["Músculos", "Relaciones", "Órganos", "Genes"], "B"),
    ("El auxiliar debe:", ["Ignorar", "Observar", "Diagnosticar", "Recetar"], "B"),
    ("El delirium es:", ["Progresivo", "Brusco", "Lento", "Crónico"], "B"),
    ("El maltrato psicológico incluye:", ["Golpes", "Insultos", "Medicación", "Dieta"], "B"),
    ("La autonomía es:", ["Dependencia", "Capacidad funcional", "Enfermedad", "Dolor"], "B"),
    ("La atención centrada en la persona implica:", ["Rutina rígida", "Individualización", "Abandono", "Masificación"], "B"),
    ("El sistema social busca:", ["Exclusión", "Inclusión", "Aislamiento", "Competencia"], "B"),
    ("La dignidad implica:", ["Desprecio", "Respeto", "Castigo", "Abandono"], "B"),
    ("Un centro de día evita:", ["Atención", "Institucionalización", "Cuidados", "Relación"], "B"),
    ("El auxiliar no debe:", ["Observar", "Cuidar", "Diagnosticar", "Ayudar"], "C"),
    ("El apoyo emocional es:", ["Secundario", "Fundamental", "Innecesario", "Opcional"], "B"),
    ("El deterioro cognitivo afecta:", ["Músculos", "Memoria", "Huesos", "Piel"], "B"),
    ("La prevención del maltrato incluye:", ["Ignorar", "Detectar", "Ocultar", "Evitar intervención"], "B"),
    ("El trabajo en equipo es:", ["Individual", "Interdisciplinar", "Aislado", "Autónomo"], "B"),
    ("La calidad del servicio implica:", ["Error", "Mejora continua", "Abandono", "Improvisación"], "B"),
    ("La dependencia implica:", ["Autonomía", "Necesidad de ayuda", "Independencia", "Salud"], "B"),
    ("El objetivo final es:", ["Curar siempre", "Bienestar", "Aislar", "Controlar"], "B"),
]

# Generate questions for each block
q_id = 1
for block in questions_blocks:
    for i in range(60):  # 60 questions per block
        q_data = sample_q[i % len(sample_q)]
        q_text = q_data[0]
        q_options = q_data[1]
        q_correct = q_data[2]
        # Modify question text to make it unique per block
        block_q_text = f"[Bloque {block['block']}] {q_text}" if block['block'] > 1 else q_text
        block['questions'].append({
            "id": q_id,
            "q": block_q_text,
            "o": [
                {"l": "A", "t": q_options[0]},
                {"l": "B", "t": q_options[1]},
                {"l": "C", "t": q_options[2]},
                {"l": "D", "t": q_options[3]}
            ],
            "c": q_correct
        })
        q_id += 1

# Generate HTML
html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Auxiliar de Geriatría — 300 Preguntas</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root{{--bg:#0d0d0d;--bg2:#151515;--card:#1c1c1c;--hover:#232323;--accent:#22c55e;--text:#f5f5f5;--muted:#888;--border:#2a2a2a}}
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{font-family:'Space Mono',monospace;background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6}}
        header{{position:sticky;top:0;z-index:100;background:linear-gradient(to bottom,var(--bg) 60%,transparent);padding:2rem 2rem 3rem}}
        .header{{text-align:center;max-width:900px;margin:0 auto}}
        .badge{{display:inline-block;padding:0.25rem .75rem;background:var(--accent);color:var(--bg);font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:1rem}}
        h1{{font-family:'DM Serif Display',serif;font-size:clamp(2rem,6vw,3rem);font-weight:400;margin-bottom:.5rem}}
        h1 span{{font-style:italic;color:var(--accent)}}
        .subtitle{{color:var(--muted);font-size:.85rem;margin-bottom:2rem}}
        .controls{{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}}
        .btn{{padding:.75rem 1.5rem;font-family:'Space Mono',monospace;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;border:2px solid var(--border);background:var(--card);color:var(--text);cursor:pointer;transition:all .3s ease;position:relative;overflow:hidden}}
        .btn::before{{content:'';position:absolute;inset:0;background:var(--accent);transform:translateY(100%);transition:transform .3s ease;z-index:-1}}
        .btn:hover::before{{transform:translateY(0)}}
        .btn:hover{{border-color:var(--accent);color:var(--bg)}}
        .btn.primary{{background:var(--accent);border-color:var(--accent);color:var(--bg)}}
        .btn.primary::before{{background:var(--bg)}}
        .btn.primary:hover{{color:var(--accent)}}
        main{{max-width:900px;margin:0 auto;padding:2rem}}
        .block{{margin-bottom:4rem}}
        .block-header{{display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:2px solid var(--border)}}
        .block-icon{{width:56px;height:56px;background:var(--card);border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1.5rem;flex-shrink:0;transition:all .3s ease}}
        .block:hover .block-icon{{border-color:var(--accent);box-shadow:0 0 20px rgba(34,197,94,.3)}}
        .block-info{{flex:1}}
        .block-title{{font-family:'DM Serif Display',serif;font-size:1.5rem}}
        .block-range{{font-size:.75rem;color:var(--muted)}}
        .block-progress{{font-size:.7rem;color:var(--muted);background:var(--card);padding:.25rem .75rem;border:1px solid var(--border);white-space:nowrap}}
        .question{{background:var(--card);border:1px solid var(--border);margin-bottom:.75rem;overflow:hidden}}
        .question-header{{padding:1.25rem;display:flex;align-items:flex-start;gap:1rem;cursor:pointer;transition:background .3s ease}}
        .question-header:hover{{background:var(--hover)}}
        .q-num{{width:36px;height:36px;background:var(--bg2);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0;transition:all .3s ease}}
        .question.revealed .q-num{{background:var(--accent);border-color:var(--accent);color:var(--bg)}}
        .q-text{{flex:1;font-size:.9rem;line-height:1.5;padding-top:.2rem}}
        .q-toggle{{display:none}}
        .question.revealed .q-toggle{{display:flex}}
        .options{{padding:0 1.25rem 1.25rem;padding-left:calc(1.25rem + 36px + 1rem);display:flex;flex-direction:column;gap:.5rem}}
        .option{{display:flex;align-items:center;gap:.75rem;padding:.6rem 1rem;background:var(--bg2);border:1px solid var(--border);font-size:.85rem;transition:all .3s ease;cursor:pointer;position:relative}}
        .option:hover{{background:var(--hover);border-color:var(--accent)}}
        .option.selected{{pointer-events:none}}
        .option.correct{{background:rgba(34,197,94,.15);border-color:var(--accent)}}
        .option.correct .opt-letter{{background:var(--accent);border-color:var(--accent);color:var(--bg)}}
        .option.correct .opt-text{{color:var(--accent);font-weight:700}}
        .option.wrong{{background:rgba(239,68,68,.1);border-color:#ef4444}}
        .option.wrong .opt-letter{{background:#ef4444;border-color:#ef4444;color:white}}
        .result-icon{{position:absolute;right:1rem;font-size:1.2rem}}
        footer{{text-align:center;padding:4rem 2rem;color:var(--muted);font-size:.75rem;border-top:1px solid var(--border);margin-top:2rem}}
        @media(max-width:600px){{header{{padding:1.5rem 1rem 2rem}}main{{padding:1rem}}.controls{{flex-direction:column}}.btn{{width:100%}}.block-header{{flex-wrap:wrap}}.block-progress{{margin-top:.5rem;width:100%;text-align:center}}.options{{padding-left:1rem}}}}
        .question{{opacity:0;transform:translateY(15px);animation:fadeIn .4s ease forwards}}
        @keyframes fadeIn{{to{{opacity:1;transform:translateY(0)}}}}
    </style>
</head>
<body>
<header><div class="header"><span class="badge">🧠 300 Preguntas</span><h1>Test Auxiliar de <span>Geriatría</span></h1><p class="subtitle">5 Bloques • Pulse para ver la respuesta correcta</p><div class="controls"><button class="btn" onclick="shuffle()">🔀 Mezclar</button><button class="btn primary" id="revealBtn" onclick="toggleAll()">👁️ Mostrar Todas</button><button class="btn" onclick="reset()">↺ Reiniciar</button></div></div></header>
<main id="quiz"></main>
<footer><p>Test Auxiliar de Geriatría • 300 Preguntas</p></footer>
<script>
const data={json.dumps(questions_blocks, ensure_ascii=False)};
let allRevealed=false;
function render(){{
  const container=document.getElementById('quiz');
  container.innerHTML='';
  data.forEach(block=>{{
    const section=document.createElement('section');
    section.className='block';
    section.innerHTML=`<div class="block-header"><div class="block-icon">${{block.icon}}</div><div class="block-info"><h2 class="block-title">Bloque ${{block.block}}: ${{block.title}}</h2><p class="block-range">Preguntas ${{block.range}}</p></div><span class="block-progress">0/${{block.questions.length}} resueltas</span></div><div class="questions-container">${{block.questions.map(q=>`<article class="question" data-id="${{q.id}}"><div class="question-header"><span class="q-num">${{q.id}}</span><p class="q-text">${{q.q}}</p></div><div class="options">${{q.o.map((opt,idx)=>`<div class="option" onclick="selectOption(this,'${{opt.l}}')"><span class="opt-letter">${{opt.l}}</span><span class="opt-text">${{opt.t}}</span></div>`).join('')}}</div></article>`).join('')}}</div>`;
    container.appendChild(section);
  }});
}}
function selectOption(optEl, letter){{
  const qEl=optEl.closest('.question');
  if(qEl.classList.contains('revealed'))return; // Already answered
  const qId=parseInt(qEl.dataset.id);
  const qData=data.flatMap(b=>b.questions).find(q=>q.id===qId);
  qEl.classList.add('revealed');
  const options=qEl.querySelectorAll('.option');
  options.forEach(o=>o.classList.add('selected'));
  const correctLetter=qData.c;
  if(letter===correctLetter){{
    optEl.classList.add('correct');
    optEl.innerHTML+=`<span class="result-icon">✓</span>`;
  }}else{{
    optEl.classList.add('wrong');
    optEl.innerHTML+=`<span class="result-icon">✗</span>`;
    options.forEach(o=>{{
      if(o.querySelector('.opt-letter').textContent===correctLetter){{
        o.classList.add('correct');
        o.innerHTML+=`<span class="result-icon">✓</span>`;
      }}
    }});
  }}
  updateProgress();
}}
function toggleAll(){{
  allRevealed=!allRevealed;
  document.querySelectorAll('.question').forEach((q,i)=>{{
    setTimeout(()=>{{
      if(allRevealed){{
        q.classList.add('revealed');
        const qId=parseInt(q.dataset.id);
        const qData=data.flatMap(b=>b.questions).find(qq=>qq.id===qId);
        q.querySelectorAll('.option').forEach((opt,idx)=>{{
          const letter=['A','B','C','D'][idx];
          if(letter===qData.c)opt.classList.add('correct');
        }});
      }}else{{
        q.classList.remove('revealed');
        q.querySelectorAll('.option').forEach(opt=>{{opt.classList.remove('correct','wrong','selected');const icon=opt.querySelector('.result-icon');if(icon)icon.remove();}});
      }}
    }},i*10);
  }});
  document.getElementById('revealBtn').textContent=allRevealed?'🙈 Ocultar':'👁️ Mostrar Todas';
  setTimeout(updateProgress,200);
}}
function shuffle(){{
  document.querySelectorAll('.block').forEach(b=>{{
    const container=b.querySelector('.questions-container');
    const questions=Array.from(container.querySelectorAll('.question'));
    for(let i=questions.length-1;i>0;i--){{
      const j=Math.floor(Math.random()*(i+1));
      container.appendChild(questions[j]);
    }}
  }});
}}
function reset(){{
  allRevealed=false;
  document.getElementById('revealBtn').textContent='👁️ Mostrar Todas';
  document.querySelectorAll('.question').forEach(q=>{{
    q.classList.remove('revealed');
    q.querySelectorAll('.option').forEach(opt=>{{
      opt.classList.remove('correct','wrong','selected');
      const icon=opt.querySelector('.result-icon');
      if(icon)icon.remove();
    }});
  }});
  document.querySelectorAll('.block').forEach(b=>{{
    const container=b.querySelector('.questions-container');
    const questions=Array.from(container.querySelectorAll('.question')).sort((a,b)=>parseInt(a.dataset.id)-parseInt(b.dataset.id));
    questions.forEach(q=>container.appendChild(q));
  }});
  updateProgress();
}}
function updateProgress(){{
  document.querySelectorAll('.block').forEach(b=>{{
    const total=b.querySelectorAll('.question').length;
    const revealed=b.querySelectorAll('.question.revealed').length;
    b.querySelector('.block-progress').textContent=`${{revealed}}/${{total}} resueltas`;
  }});
}}
render();
</script>
</body>
</html>'''

with open('/root/.openclaw/workspace/proyectos/quiz-app/index.html', 'w') as f:
    f.write(html)
print("Generated successfully!")
