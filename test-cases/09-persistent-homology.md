# Test Case: Persistent Homology Motivation

**Question**: "Why can persistent homology detect holes in data?"

## Expected Pattern

This case checks whether IntuitMath can explain a modern mathematical idea
without pretending that a single picture is a proof. The answer should start
from the failure of ordinary clustering or local geometry, then build the
filtration idea before naming homology.

1. **MOTIVATION**: Data are noisy point clouds, so a single scale is arbitrary.
2. **TOOLKIT RECONSTRUCTION**: Clustering, nearest-neighbor graphs, and manifold
   intuition can see local neighborhoods but miss stable global shape.
3. **PRE-RIGOROUS**: Grow balls around points; watch connected components,
   loops, and voids appear and disappear as radius changes.
4. **BREAKDOWN**: At one radius every dataset has fake holes; at another radius
   everything is filled in. The issue is not "is there a hole?" but "which
   holes persist across scales?"
5. **RIGOROUS REPAIR**: Build a filtration of simplicial complexes and track
   homology classes across inclusion maps.
6. **CROSS-DOMAIN**: Explain why barcodes/persistence diagrams act like
   scale-stability summaries, not magic shape detectors.
7. **REFLECTION ANCHOR**: Ask what kind of feature should count as signal when
   the data are noisy.

## Key Elements to Check

- [ ] Does not begin with the formal definition of a chain complex.
- [ ] Uses a concrete toy example such as points sampled from a noisy circle.
- [ ] Separates \(H_0\) connected components from \(H_1\) loops.
- [ ] Explains why one fixed radius is fragile.
- [ ] Uses "birth" and "death" as scale events, not as decoration.
- [ ] States that persistent homology detects stable topological features, not
      semantic objects by itself.
- [ ] Mentions at least one limitation: metric choice, sampling density,
      outliers, computational cost, or interpretation ambiguity.
- [ ] Ends with a reflection question.

## Example Output (Abbreviated)

> **The puzzle.** Suppose points are sampled from a noisy circle. If you only
> run clustering, the data may look like one cluster. If you only draw nearest
> neighbors, the answer depends on a threshold. But visually there is a global
> fact that the local tests are missing: the data wrap around an empty middle.
>
> **The bold attempt.** Put a ball of radius \(r\) around every point. For tiny
> \(r\), every point is alone. As \(r\) grows, balls touch and the cloud becomes
> connected. A little later, the balls form a loop around the middle. Much later,
> the middle fills in and the loop dies.
>
> **Why persistence is the move.** One radius is a bad judge. At small scales,
> noise creates accidental holes. At large scales, every shape gets washed out.
> Persistent homology asks a different question: which topological features
> survive while the scale changes?
>
> **Rigorous version.** Replace growing balls with a filtration
> \(K_0 \subseteq K_1 \subseteq K_2 \subseteq \cdots\) of simplicial complexes.
> Homology groups \(H_k(K_i)\) record \(k\)-dimensional holes: \(H_0\) for
> components, \(H_1\) for loops, \(H_2\) for voids. Inclusion maps carry classes
> forward. A feature is born when a class appears and dies when it becomes a
> boundary. The barcode is the list of these lifetimes.
>
> **Caution.** A long bar is evidence of scale stability, not proof of meaning.
> The answer still depends on the metric, sampling density, and whether the
> chosen complex is appropriate.
>
> **Something to sit with.** If a feature exists only for a very narrow range of
> radii, should a data analyst treat it as structure, noise, or a question for
> the domain expert?
